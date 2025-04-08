import time
import pytest
import logging
import datetime
from utils.login import Login
from utils.logger import LoggerConfig
from utils.driver_setup import get_driver
from pages.faq.editfaq.editfaq_base import EditFAQBase
from pages.faq.editfaq.select import SelectEditFAQ
from pages.faq.editfaq.enter_field import EnterFieldEditFAQ
from pages.faq.editfaq.validation import ValidationEditFAQ
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
def editfaq(setup_driver):
    return EditFAQBase(setup_driver)

@pytest.fixture
def select(setup_driver):
    return SelectEditFAQ(setup_driver)

@pytest.fixture
def enter_field(setup_driver):
    return EnterFieldEditFAQ(setup_driver)

@pytest.fixture
def validation(setup_driver):
    return ValidationEditFAQ(setup_driver)

# Test Case 1: Verify khi chọn giá trị Không -> Hệ thống hiển thị giá trị Không ở field
# def test_value_not_select_show(setup_driver, editfaq, select):
#     editfaq.navigate_to_faq()
#     editfaq.click_edit_first_line()
#     select.click_select_show()
#     select.click_value_not_select_show()
#     expected_result = "Hệ thống hiển thị giá trị Không ở field"
#     result = select.is_value_not_visible()
#     actual_result = expected_result if result else "Hệ thống không hiển thị giá trị Không ở field"

#     if result:
#         test_logger.info(f"Test Case 1 PASS: test_value_not_select_show | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 1 FAIL: test_value_not_select_show | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 2: Verify khi chọn giá trị Có -> Hệ thống hiển thị giá trị Có ở field
# def test_value_has_select_show(setup_driver, editfaq, select):
#     editfaq.navigate_to_faq()
#     editfaq.click_edit_first_line()
#     select.click_select_show()
#     select.click_value_has_select_show()
#     expected_result = "Hệ thống hiển thị giá trị Có ở field"
#     result = select.is_value_has_visible()
#     actual_result = expected_result if result else "Hệ thống không hiển thị giá trị Có ở field"

#     if result:
#         test_logger.info(f"Test Case 2 PASS: test_value_has_select_show | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 2 FAIL: test_value_has_select_show | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 3: Verify khi chỉnh sửa giá trị ở field Câu hỏi* -> Hệ thống hiển thị giá trị đã chỉnh sửa
def test_edited_faq_vi(setup_driver, editfaq, enter_field, validation):
    editfaq.navigate_to_faq()
    editfaq.click_edit_first_line()
    edit_data = "test-cauhoi-dachinhsua"
    enter_field.edit_faq_vi(edit_data)
    editfaq.click_save_continue_button()
    expected_result = "Hệ thống hiển thị giá trị đã chỉnh sửa"
    result = validation.is_edit_faq_vi_displayed()
    actual_result = expected_result if result else "Hệ thống không hiển thị giá trị vừa chỉnh sửa"

    if result:
        test_logger.info(f"Test Case 3 PASS: test_edited_faq_vi | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 3 FAIL: test_edited_faq_vi | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"