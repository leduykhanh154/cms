import time
import pytest
import logging
import datetime
from utils.login import Login
from utils.logger import LoggerConfig
from utils.driver_setup import get_driver
from pages.faq.faq_base import FAQBase
from pages.faq.url_faq import UrlFAQ
from locators.faq.locator_faq import LocatorFAQ
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
        time.sleep(2)
        driver.quit()

@pytest.fixture
def faq(setup_driver):
    return FAQBase(setup_driver)

@pytest.fixture
def url(setup_driver):
    return UrlFAQ(setup_driver)

# Test Case 1: Verify breadcrumb 'Trang chủ -> Danh sách câu hỏi' -> Hệ thống chuyển hướng đến 'Trang chủ'.
def test_home_action(faq, setup_driver, url):
    test_logger.info("Bắt đầu Test Case 1: Verify breadcrumb 'Trang chủ -> Danh sách câu hỏi' -> Hệ thống chuyển hướng đến 'Trang chủ'.")
    faq.navigate_to_faq()
    faq.click_home_page()
    expected_result = "Hệ thống chuyển hướng đến 'Trang chủ'."
    result = url.check_url_home_page()
    
    actual_result = expected_result if result else "Hệ thống không chuyển hướng đến 'Trang chủ'."

    if result:
        test_logger.info(f"Test Case 1 PASS: test_home_action | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 1 FAIL: test_home_action | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert result, f"Expected: {expected_result} | Actual: {actual_result}"

