import pytest
import base64
import logging
import pytest_html
from selenium import webdriver

LOG_FILE = "reports/test_results.log"

# Đọc dữ liệu từ test_results.log
def read_test_log():
    test_data = {}
    try:
        with open("reports/test_results.log", "r") as file:
            for line in file.readlines():
                if "Test:" in line:
                    parts = line.strip().split("|")
                    test_name = parts[0].split(": ")[1].strip()
                    expected = parts[1].split(": ")[1].strip()
                    actual = parts[2].split(": ")[1].strip()
                    status = parts[3].split(": ")[1].strip()
                    test_data[test_name] = {"expected": expected, "actual": actual, "status": status}
    except FileNotFoundError:
        logging.error("Không tìm thấy file test_results.log")
    return test_data

@pytest.fixture(scope="function")
def setup_driver():
    """Khởi tạo trình duyệt"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Chụp ảnh màn hình và nhúng vào báo cáo pytest-html"""
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    test_data = read_test_log()  # Đọc kết quả từ log

    if report.when == "call":
        driver = item.funcargs.get("setup_driver", None)  # Lấy driver từ fixture
        test_name = item.name
        expected_result = test_data.get(test_name, {}).get("expected", "N/A")
        actual_result = test_data.get(test_name, {}).get("actual", "N/A")
        test_status = test_data.get(test_name, {}).get("status", "N/A")

        print(f"DEBUG HOOK: {test_name} | Expected = {expected_result} | Actual = {actual_result}")

        # ✅ Thêm vào báo cáo pytest HTML
        result_html = f"""
        <div>
            <strong>Test Name:</strong> {test_name}<br>
            <strong>Expected Result:</strong> {expected_result}<br>
            <strong>Actual Result:</strong> {actual_result}<br>
            <strong>Status:</strong> {test_status}
        </div>
        """
        extra.append(pytest_html.extras.html(result_html))

        if driver:
            try:
                status_text = "FAILED" if report.failed else "PASSED"

                # Chụp ảnh màn hình & convert sang base64
                screenshot = driver.get_screenshot_as_png()
                screenshot_base64 = base64.b64encode(screenshot).decode('utf-8')
                img_html = f'<div><strong>{test_name} - {status_text}</strong><br><img src="data:image/png;base64,{screenshot_base64}" width="400px"/></div>'

                # ✅ Thêm ảnh chụp màn hình vào report
                if item.config.pluginmanager.hasplugin("html"):
                    extra.append(pytest_html.extras.html(img_html))

            except Exception as e:
                logging.error(f"Error capturing screenshot for test {test_name}: {e}", exc_info=True)

    report.extra = extra
