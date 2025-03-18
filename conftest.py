import glob
import os
import pytest
import base64
import logging
import pytest_html
from selenium import webdriver

logging.basicConfig(level=logging.INFO)

def normalize_test_name(test_name):
    """Chuẩn hóa tên test để khớp giữa pytest và log"""
    return test_name.split(".")[-1]  # Bỏ prefix module/class nếu có

def get_latest_log_file():
    """Tìm log file mới nhất"""
    log_files = glob.glob("logs/test_results_*.log")
    if not log_files:
        logging.error("❌ Không tìm thấy file log nào trong thư mục logs/")
        return None
    latest_log = max(log_files, key=os.path.getctime)
    logging.info(f"📌 Đọc file log mới nhất: {latest_log}")
    return latest_log

def read_test_log():
    """Đọc dữ liệu test từ log file mới nhất"""
    test_data = {}
    latest_log = get_latest_log_file()
    if not latest_log:
        return test_data

    try:
        with open(latest_log, "r", encoding="utf-8") as file:
            logging.info("📌 Nội dung file log:")
            for line in file.readlines():
                logging.info(line.strip())
                if "Test Case" in line:  # Chỉ lấy dòng chứa kết quả test
                    parts = line.strip().split("|")
                    if len(parts) < 4:
                        logging.warning(f"⚠️ Dòng log sai định dạng: {line.strip()}")
                        continue
                    raw_test_name = parts[0].split(": ")[1].strip()
                    test_name = normalize_test_name(raw_test_name)  # Chuẩn hóa tên test
                    expected = parts[1].split(": ")[1].strip()
                    actual = parts[2].split(": ")[1].strip()
                    status = parts[3].split(": ")[1].strip()
                    test_data[test_name] = {"expected": expected, "actual": actual, "status": status}
    except FileNotFoundError:
        logging.error(f"❌ Không tìm thấy file {latest_log}")
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
        driver = item.funcargs.get("setup_driver")  # Lấy driver từ fixture
        test_name = normalize_test_name(item.name)  # Chuẩn hóa test name
        expected_result = test_data.get(test_name, {}).get("expected", "N/A")
        actual_result = test_data.get(test_name, {}).get("actual", "N/A")
        test_status = test_data.get(test_name, {}).get("status", "N/A")

        logging.info(f"📌 DEBUG HOOK: {test_name} | Expected = {expected_result} | Actual = {actual_result} | Status = {test_status}")

        # ✅ Hiển thị kết quả test trong báo cáo HTML
        result_html = f"""
        <div>
            <strong>Test Name:</strong> {test_name}<br>
            <strong>Expected Result:</strong> {expected_result}<br>
            <strong>Actual Result:</strong> {actual_result}<br>
            <strong>Status:</strong> {test_status}
        </div>
        """
        extra.append(pytest_html.extras.html(result_html))

        # Chụp ảnh màn hình nếu test fail
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
