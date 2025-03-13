import pytest
import pytest_html
import logging
import base64
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Cấu hình logging
logging.basicConfig(
    filename="reports/test_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w"  # Ghi đè log file mỗi lần chạy
)

@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """ Chụp ảnh màn hình và nhúng trực tiếp vào report.html """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        driver = item.funcargs.get("setup_driver", None)  # Lấy driver từ fixture
        test_name = item.name

        if driver:
            try:
                status = "FAILED" if report.failed else "PASSED"
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

                # Chụp ảnh màn hình và chuyển thành base64
                screenshot = driver.get_screenshot_as_png()
                screenshot_base64 = base64.b64encode(screenshot).decode('utf-8')
                img_html = f'<div><strong>{test_name} - {status}</strong><br><img src="data:image/png;base64,{screenshot_base64}" width="400px"/></div>'

                # Ghi log kết quả test
                logging.info(f"Test: {test_name} - {status}")

                # Thêm ảnh vào report.html
                if item.config.pluginmanager.hasplugin("html"):
                    extra = getattr(report, "extra", [])
                    extra.append(pytest_html.extras.html(img_html))
                    report.extra = extra

            except Exception as e:
                logging.error(f"Error capturing screenshot for test {test_name}: {e}", exc_info=True)