
import time
import pytest
import logging
import datetime
from utils.login import Login
from utils.logger import LoggerConfig
from utils.driver_setup import get_driver
from pages.tag.tag import Tag
from locators.locator_tag import LocatorTag
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def setup_driver():
    driver = get_driver()
    login_page = Login(driver)
    login_success = login_page.login()
    if not login_success:
        pytest.fail("Không thể đăng nhập!")
    yield driver
    driver.quit()

@pytest.fixture
def tag(setup_driver):
    return Tag(setup_driver)

def log_success(message):
    print(f"{message}")
    logging.info(message)

# Test Case 1: Verify breadcrumb 'Trang chủ -> Tag'. Hệ thống chuyển hướng sang trang chủ
def test_home_action(tag, setup_driver):
    try:
        tag.perform_tag_operations()
        tag.click_home_page()
        print('Test Case 1 PASS: Chuyển hướng lại: Trang chủ')
    except Exception as e:
        print(f"Test Case 1 FAIL: Không chuyển hướng lại Trang chủ! Lỗi: {str(e)}")
        assert False

