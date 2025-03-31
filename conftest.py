import glob
import os
import pytest
import base64
import logging
import pytest_html
from selenium import webdriver

logging.basicConfig(level=logging.INFO)

def normalize_test_name(test_name):
    return test_name.split(".")[-1]

def get_latest_log_file():
    log_files = glob.glob("logs/test_results_*.log")
    if not log_files:
        logging.error("Không tìm thấy file log nào trong thư mục logs/")
        return None
    latest_log = max(log_files, key=os.path.getctime)
    logging.info(f"Đọc file log mới nhất: {latest_log}")
    return latest_log

def read_test_log():
    test_data = {}
    latest_log = get_latest_log_file()
    if not latest_log:
        return test_data
    try:
        with open(latest_log, "r", encoding="utf-8") as file:
            logging.info("Nội dung file log:")
            for line in file.readlines():
                logging.info(line.strip())
                if "Test Case" in line:
                    parts = line.strip().split("|")
                    if len(parts) < 4:
                        logging.warning(f"Dòng log sai định dạng: {line.strip()}")
                        continue
                    
                    # Kiểm tra và trích xuất raw_test_name an toàn
                    test_name_part = parts[0].split(": ")
                    if len(test_name_part) < 2:
                        logging.warning(f"Lỗi tách tên test case: {parts[0]}")
                        continue
                    raw_test_name = test_name_part[1].strip()
                    test_name = normalize_test_name(raw_test_name)

                    expected = parts[1].split(": ")[1].strip() if ": " in parts[1] else "N/A"
                    actual = parts[2].split(": ")[1].strip() if ": " in parts[2] else "N/A"
                    status = parts[3].split(": ")[1].strip() if ": " in parts[3] else "N/A"

                    test_data[test_name] = {"expected": expected, "actual": actual, "status": status}
    except FileNotFoundError:
        logging.error(f"Không tìm thấy file {latest_log}")
    return test_data


@pytest.fixture(scope="function")
def setup_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    test_data = read_test_log()
    
    if report.when == "call":
        driver = item.funcargs.get("setup_driver") 
        test_name = normalize_test_name(item.name)
        expected_result = test_data.get(test_name, {}).get("expected", "N/A")
        actual_result = test_data.get(test_name, {}).get("actual", "N/A")
        test_status = test_data.get(test_name, {}).get("status", "N/A")
        
        logging.info(f"DEBUG HOOK: {test_name} | Expected = {expected_result} | Actual = {actual_result} | Status = {test_status}")

        # Bảng kết quả
        result_html = f"""
            <table border="1" style="border-collapse: collapse; width: 100%; text-align: left;">
                <tr>
                    <th style="padding: 8px; background-color: #f2f2f2;">Test Name</th>
                    <td style="padding: 8px;">{test_name}</td>
                </tr>
                <tr>
                    <th style="padding: 8px; background-color: #f2f2f2;">Expected Result</th>
                    <td style="padding: 8px;">{expected_result}</td>
                </tr>
                <tr>
                    <th style="padding: 8px; background-color: #f2f2f2;">Actual Result</th>
                    <td style="padding: 8px;">{actual_result}</td>
                </tr>
                <tr>
                    <th style="padding: 8px; background-color: #f2f2f2;">Status</th>
                    <td style="padding: 8px; font-weight: bold; color: {'green' if test_status == 'PASS' else 'red'};">
                        {test_status}
                    </td>
                </tr>
            </table>
        """
        extra.append(pytest_html.extras.html(result_html))

        # Chụp ảnh màn hình nếu test FAIL
        if driver:
            try:
                if report.failed:
                    status_text = "FAILED"
                else:
                    status_text = "PASSED"

                screenshot = driver.get_screenshot_as_png()
                screenshot_base64 = base64.b64encode(screenshot).decode('utf-8')
                img_html = f'<div><strong>{test_name} - {status_text}</strong><br><img src="data:image/png;base64,{screenshot_base64}" width="400px"/></div>'

                if item.config.pluginmanager.hasplugin("html"):
                    extra.append(pytest_html.extras.html(img_html))

            except Exception as e:
                logging.error(f"Error capturing screenshot for test {test_name}: {e}", exc_info=True)

    report.extra = extra

# Ẩn dòng PASSED trong output pytest
def pytest_report_teststatus(report, config):
    if report.when == "call" and report.outcome == "passed":
        return "", "", ""  # Ẩn dòng "PASSED"
