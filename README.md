# cms

import pytest
import pytest_html
import logging
import base64
import os
from selenium import webdriver

LOG_FILE = "reports/test_results.log"

def setup_logger():
    """Thiết lập logger để ghi kết quả test vào file"""
    os.makedirs("reports", exist_ok=True)
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.INFO)
    if logger.hasHandlers():
        logger.handlers.clear()
    file_handler = logging.FileHandler(LOG_FILE, mode="a", encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

test_logger = setup_logger()

def log_test_result(test_name, expected, actual, status):
    """Ghi kết quả test vào file log"""
    log_entry = f"Test: {test_name} | Expected: {expected} | Actual: {actual} | Status: {status}"
    test_logger.info(log_entry)
    print(log_entry)  # Thêm log ra console

@pytest.fixture(scope="function")
def setup_driver():
    """Khởi tạo trình duyệt"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Ghi log kết quả test vào file và chụp ảnh màn hình"""
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    test_name = item.name
    expected_result = "Expected result here"  # Có thể lấy từ test case
    actual_result = "Actual result here"  # Lấy từ logic test thực tế
    status = "FAILED" if report.failed else "PASSED"

    # ✅ Ghi log kết quả vào test_results.log
    log_test_result(test_name, expected_result, actual_result, status)

    result_html = f"""
    <div>
        <strong>Test Name:</strong> {test_name}<br>
        <strong>Expected Result:</strong> {expected_result}<br>
        <strong>Actual Result:</strong> {actual_result}<br>
        <strong>Status:</strong> {status}
    </div>
    """
    extra.append(pytest_html.extras.html(result_html))

    driver = item.funcargs.get("setup_driver", None)
    if driver and report.failed:
        try:
            screenshot = driver.get_screenshot_as_png()
            screenshot_base64 = base64.b64encode(screenshot).decode('utf-8')
            img_html = f'<div><strong>{test_name} - FAILED</strong><br><img src="data:image/png;base64,{screenshot_base64}" width="400px"/></div>'
            if item.config.pluginmanager.hasplugin("html"):
                extra.append(pytest_html.extras.html(img_html))
        except Exception as e:
            logging.error(f"Error capturing screenshot for test {test_name}: {e}", exc_info=True)

    report.extra = extra