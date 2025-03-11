import pytest
import logging
import base64
from datetime import datetime

# Cấu hình logging
logging.basicConfig(
    filename="test_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

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

                # Thêm ảnh vào report.html
                if "pytest_html" in item.config.pluginmanager.list_name_plugin():
                    extra = getattr(report, "extra", [])
                    extra.append(pytest_html.extras.html(img_html))
                    report.extra = extra

            except Exception as e:
                logging.error(f"Error capturing screenshot for test {test_name}: {e}")