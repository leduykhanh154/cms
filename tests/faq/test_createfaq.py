import time
import pytest
import logging
import datetime
from utils.login import Login
from utils.logger import LoggerConfig
from utils.driver_setup import get_driver
from pages.faq.createfaq.createfaq_base import CreateFAQBase
from pages.faq.createfaq.select import SelectCreateFAQ
from pages.faq.createfaq.enter_field import EnterFieldCreateFAQ
from pages.faq.createfaq.validation import ValidationCreateFAQ
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
def createfaq(setup_driver):
    return CreateFAQBase(setup_driver)

@pytest.fixture
def select(setup_driver):
    return SelectCreateFAQ(setup_driver)

@pytest.fixture
def enter_field(setup_driver):
    return EnterFieldCreateFAQ(setup_driver)

@pytest.fixture
def validation(setup_driver):
    return ValidationCreateFAQ(setup_driver)

# Test Case 1: Verify khi click select Hiển thị -> Hệ thống mở select 'Hiển thị'.
# def test_open_select_show(setup_driver, createfaq, select):
#     createfaq.navigate_to_faq()
#     createfaq.click_create_new_button()
#     select.click_select_show()
#     expected_result = "Hệ thống mở select 'Hiển thị'"
#     result = select.is_select_show_visible()
#     actual_result = expected_result if result else "Hệ thống không mở select 'Hiển thị'"

#     if result:
#         test_logger.info(f"Test Case 1 PASS: test_open_select_show | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 1 FAIL: test_open_select_show | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 2: Verify khi click lại select Hiển thị -> Hệ thống đóng select 'Hiển thị'.
# def test_close_select_show(setup_driver, createfaq, select):
#     createfaq.navigate_to_faq()
#     createfaq.click_create_new_button()
#     select.click_select_show()
#     select.click_again_select_show()
#     expected_result = "Hệ thống đóng select ' Hiển thị'"
#     result = select.is_select_show_invisible()
#     actual_result = expected_result if result else "Hệ thống không đóng select 'Hiển thị'"

#     if result:
#         test_logger.info(f"Test Case 2 PASS: test_close_select_show | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 2 FAIL: test_close_select_show | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 3: Verify khi chọn giá trị Không -> Hệ thống hiển thị giá trị Không ở field.
# def test_value_not_select_show(setup_driver, createfaq, select):
#     createfaq.navigate_to_faq()
#     createfaq.click_create_new_button()
#     select.click_select_show()
#     select.click_value_not_select_show()
#     expected_result = "Hệ thống hiển thị giá trị Không ở field"
#     result = select.is_value_not_visible()
#     actual_result = expected_result if result else "Hệ thống không hiển thị giá trị Không ở field"

#     if result:
#         test_logger.info(f"Test Case 3 PASS: test_value_not_select_show | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 3 FAIL: test_value_not_select_show | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 4: Verify khi chọn giá trị Có -> Hệ thống hiển thị giá trị Có ở field.
# def test_value_has_select_show(setup_driver, createfaq, select):
#     createfaq.navigate_to_faq()
#     createfaq.click_create_new_button()
#     select.click_select_show()
#     select.click_value_has_select_show()
#     expected_result = "Hệ thống hiển thị giá trị Có ở field"
#     result = select.is_value_has_visible()
#     actual_result = expected_result if result else "Hệ thống không hiển thị giá trị Có ở field"

#     if result:
#         test_logger.info(f"Test Case 4 PASS: test_value_has_select_show | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 4 FAIL: test_value_has_select_show | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# Test Case 5: Verify khi bỏ trống giá trị ở field 'Câu hỏi*' -> Hệ thống hiển thị validate: 'Vui lòng nhập Câu hỏi'.
def test_empty_faq_vi(setup_driver, createfaq, enter_field, validation, select):
    createfaq.navigate_to_faq()
    createfaq.click_create_new_button()
    data = "123"
    enter_field.enter_faq_vi(data)
    select.click_save_button()
    expected_result = "Hệ thống hiển thị validate: 'Vui lòng nhập Câu hỏi'"
    result = validation.is_faq_vi_error_displayed()
    actual_result = expected_result if result else "Hệ thống không hiển thị validate: 'Vui lòng nhập Câu hỏi'"

    if result:
        test_logger.info(f"Test Case 5 PASS: test_empty_faq_vi | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 5 FAIL: test_empty_faq_vi | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
