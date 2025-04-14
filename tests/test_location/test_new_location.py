import time
import pytest
from utils.login import Login
from utils.logger import LoggerConfig
from utils.driver_setup import get_driver
from pages.location.new_location.new_location_base import NewLocatorBase
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

# Khởi tạo logger
test_logger = LoggerConfig.get_logger()

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    global test_logger
    test_logger = LoggerConfig.get_logger()

@pytest.fixture(scope="function")
def setup_driver():
    driver = get_driver()
    try:
        login_page = Login(driver)
        if not login_page.login():
            pytest.fail("Không thể đăng nhập!")
        yield driver
    finally:
        time.sleep(3)
        driver.quit()

@pytest.fixture
def new_location_base(setup_driver):
    return NewLocatorBase(setup_driver)

# Test Case 1: Verify khi nhấn nút 'Tạo mới' -> Hệ thống điều hướng đến trang 'Tạo mới chi nhánh'.
def test_click_create_button(new_location_base):
    test_logger.info("Bắt đầu Test Case 1: Verify khi nhấn nút 'Tạo mới'.")
    new_location_base.perform_tag_operations()
    result = new_location_base.click_create_button()
    expected_result = "Hệ thống điều hướng đến trang 'Tạo mới chi nhánh'."
    actual_result = expected_result if result else "Hệ thống không điều hướng đến trang 'Tạo mới chi nhánh'."
    if result:
        test_logger.info(f"Test Case 1 PASS: test_click_create_button | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 1 FAIL: test_click_create_button | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
