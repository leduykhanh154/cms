import pytest
import pytest_html
import base64
from datetime import datetime
from selenium import webdriver
import logging

@pytest.fixture
def setup_driver():
    """Khởi tạo WebDriver và trả về instance."""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook Pytest để lưu kết quả test vào report (bao gồm log và ảnh chụp màn hình)."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":  # Chỉ chụp ảnh sau khi test case chạy xong
        driver = item.funcargs.get("setup_driver", None)
        test_name = item.name
        log_output = getattr(report, "longrepr", "")

        if driver:
            try:
                status = "FAILED" if report.failed else "PASSED"
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

                # Chụp ảnh màn hình
                screenshot = driver.get_screenshot_as_png()
                screenshot_base64 = base64.b64encode(screenshot).decode('utf-8')

                # Thêm log vào report
                log_html = f"<pre style='color: black; background: #f4f4f4; padding: 10px;'>{log_output}</pre>"

                # HTML hiển thị trong report
                img_html = f"""
                <div style="border: 2px solid {'red' if report.failed else 'green'}; padding: 10px; margin: 10px;">
                    <img src="data:image/png;base64,{screenshot_base64}" width="400px"/><br>
                    {log_html}  <!-- Thêm log vào HTML -->
                </div>
                """

                # Thêm vào report pytest-html
                if item.config.pluginmanager.hasplugin("html"):
                    extra = getattr(report, "extra", [])
                    extra.append(pytest_html.extras.html(img_html))
                    report.extra = extra

            except Exception as e:
                print(f"⚠ Lỗi khi chụp màn hình cho test {test_name}: {e}")
