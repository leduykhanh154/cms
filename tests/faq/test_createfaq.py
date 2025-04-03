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
# def test_empty_faq_vi(setup_driver, createfaq, enter_field, validation):
#     createfaq.navigate_to_faq()
#     createfaq.click_create_new_button()
#     empty_data = ""
#     enter_field.enter_faq_vi(empty_data)
#     expected_result = "Hệ thống hiển thị validate 'Vui lòng nhập Câu hỏi'"
#     result = validation.is_faq_vi_error_displayed()
#     actual_result = expected_result if result else "Hệ thống không hiển thị validate Vui lòng nhập Câu hỏi"

#     if result:
#         test_logger.info(f"Test Case 5 PASS: test_empty_faq_vi | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 5 FAIL: test_empty_faq_vi | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 6: Verify khi nhập lại giá trị ở field 'Câu hỏi*' -> Hệ thống ẩn validate.
# def test_enter_faq_vi(setup_driver, createfaq, enter_field, validation):
#     createfaq.navigate_to_faq()
#     createfaq.click_create_new_button()
#     enter_data = "test-cauhoi"
#     enter_field.enter_faq_vi(enter_data)
#     expected_result = "Hệ thống ẩn validate"
#     result = validation.is_faq_vi_error_invisible()
#     actual_result = expected_result if result else "Hệ thống không ẩn validate"

#     if result:
#         test_logger.info(f"Test Case 6 PASS: test_enter_faq_vi | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 6 FAIL: test_enter_faq_vi | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 7: Verify 499 kí tự ở field Câu hỏi* -> Hệ thống hiển thị giá trị ở field
# def test_499_character_faq_vi(setup_driver, createfaq, enter_field, validation):
#     createfaq.navigate_to_faq()
#     createfaq.click_create_new_button()
#     character_data = "A" * 50
#     enter_field.enter_faq_vi(character_data)
#     expected_result = "Hệ thống hiển thị giá trị ở field"
#     result = validation.is_faq_vi_499_character()
#     actual_result = expected_result if result else "Hệ thống không hiển thị giá trị ở field"

#     if result:
#         test_logger.info(f"Test Case 7 PASS: test_499_character_faq_vi | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 7 FAIL: test_499_character_faq_vi | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 8: Verify 500 kí tự ở field Câu hỏi* -> Hệ thống hiển thị giá trị ở field
# def test_500_character_faq_vi(setup_driver, createfaq, enter_field, validation):
#     createfaq.navigate_to_faq()
#     createfaq.click_create_new_button()
#     character_data = "A" * 500
#     enter_field.enter_faq_vi(character_data)
#     expected_result = "Hệ thống hiển thị giá trị ở field"
#     result = validation.is_faq_vi_500_character()
#     actual_result = expected_result if result else "Hệ thống không hiển thị giá trị ở field"

#     if result:
#         test_logger.info(f"Test Case 8 PASS: test_500_character_faq_vi | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 8 FAIL: test_500_character_faq_vi | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 9: Verify 501 kí tự ở field Câu hỏi* -> Hệ thống hiển thị validate Vui lòng nhập Câu hỏi không quá 500 ký tự
# def test_501_character_faq_vi(setup_driver, createfaq, enter_field, validation):
#     createfaq.navigate_to_faq()
#     createfaq.click_create_new_button()
#     character_data = "A" * 501
#     enter_field.enter_faq_vi(character_data)
#     expected_result = "Hệ thống hiển thị validate Vui lòng nhập Câu hỏi không quá 500 ký tự"
#     result = validation.is_faq_vi_501_character()
#     actual_result = expected_result if result else "Hệ thống hiển thị không đúng validate Vui lòng nhập Câu hỏi không quá 500 ký tự"

#     if result:
#         test_logger.info(f"Test Case 9 PASS: test_501_character_faq_vi | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 9 FAIL: test_501_character_faq_vi | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 10: Verify khi bỏ trống giá trị ở field Câu trả lời* -> Hệ thống hiển thị validate Vui lòng nhập Câu trả lời
# def test_empty_answer_vi(setup_driver, createfaq, enter_field, validation):
#     createfaq.navigate_to_faq()
#     createfaq.click_create_new_button()
#     empty_data = ""
#     enter_field.enter_answer_vi(empty_data)
#     expected_result = "Hệ thống hiển thị validate 'Vui lòng nhập Câu trả lời'"
#     result = validation.is_answer_vi_error_displayed()
#     actual_result = expected_result if result else "Hệ thống không hiển thị đúng validate 'Vui lòng nhập Câu trả lời'"

#     if result:
#         test_logger.info(f"Test Case 10 PASS: test_empty_answer_vi | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 10 FAIL: test_empty_answer_vi | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 11: Verify khi nhập lại giá trị ở field Câu trả lời* -> Hệ thống ẩn validate.
# def test_enter_answer_vi(setup_driver, createfaq, enter_field, validation):
#     createfaq.navigate_to_faq()
#     createfaq.click_create_new_button()
#     enter_data = "test-cautraloi"
#     enter_field.enter_answer_vi(enter_data)
#     expected_result = "Hệ thống ẩn validate"
#     result = validation.is_answer_vi_error_invisible()
#     actual_result = expected_result if result else "Hệ thống không ẩn validate"

#     if result:
#         test_logger.info(f"Test Case 11 PASS: test_enter_answer_vi | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 11 FAIL: test_enter_answer_vi | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"
         