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
# Test case failed: Chưa check được nội dung nhập vào CKE
# def test_edited_faq_vi(setup_driver, editfaq, enter_field, validation):
#     editfaq.navigate_to_faq()
#     editfaq.click_edit_first_line()
#     edit_data = "test-cauhoi-dachinhsua"
#     enter_field.edit_faq_vi(edit_data)
#     editfaq.click_save_continue_button()
#     expected_result = "Hệ thống hiển thị giá trị đã chỉnh sửa"
#     result = validation.is_edit_faq_vi_displayed()
#     actual_result = expected_result if result else "Hệ thống không hiển thị giá trị vừa chỉnh sửa"

#     if result:
#         test_logger.info(f"Test Case 3 PASS: test_edited_faq_vi | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 3 FAIL: test_edited_faq_vi | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# TCs 4: Chưa check được nội dung nhập vào CKE

# Test Case 5: Verify khi chọn giá trị Thủ tục, quy trình -> Hệ thống hiển thị giá trị Thủ tục, quy trình ở field
# def test_value_procedure_select_question_type(setup_driver, editfaq, select):
#     editfaq.navigate_to_faq()
#     editfaq.click_edit_first_line()
#     editfaq.click_general_info_tab()
#     select.click_select_question_type()
#     select.click_value_procedure_select_question_type()
#     editfaq.click_save_continue_button()
#     time.sleep(2)
#     editfaq.click_general_info_tab()
#     expected_result = "Hệ thống hiển thị giá trị Thủ tục, quy trình ở field"
#     result = select.is_value_procedure_visible()
#     actual_result = expected_result if result else "Hệ thống không hiển thị giá trị Thủ tục, quy trình ở field"

#     if result:
#         test_logger.info(f"Test Case 5 PASS: test_value_procedure_select_question_type | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 5 FAIL: test_value_procedure_select_question_type | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 6: Verify khi chọn giá trị Dịch vụ khác -> Hệ thống hiển thị giá trị Dịch vụ khác ở field
# def test_value_other_service_select_question_type(setup_driver, editfaq, select):
#     editfaq.navigate_to_faq()
#     editfaq.click_edit_first_line()
#     editfaq.click_general_info_tab()
#     select.click_select_question_type()
#     select.click_value_other_service_select_question_type()
#     editfaq.click_save_continue_button()
#     time.sleep(2)
#     editfaq.click_general_info_tab()
#     expected_result = "Hệ thống hiển thị giá trị Dịch vụ khác ở field"
#     result = select.is_value_other_service_visible()
#     actual_result = expected_result if result else "Hệ thống không hiển thị giá trị Dịch vụ khác ở field"

#     if result:
#         test_logger.info(f"Test Case 6 PASS: test_value_other_service_select_question_type | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 6 FAIL: test_value_other_service_select_question_type | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 7: Verify khi chọn giá trị Verify khi chọn giá trị Dịch vụ Hoa tiêu -> Hệ thống hiển thị giá trị Dịch vụ Hoa tiêu ở field
# def test_value_pilotage_service_select_question_type(setup_driver, editfaq, select):
#     editfaq.navigate_to_faq()
#     editfaq.click_edit_first_line()
#     editfaq.click_general_info_tab()
#     select.click_select_question_type()
#     select.click_value_pilotage_service_select_question_type()
#     editfaq.click_save_continue_button()
#     time.sleep(2)
#     editfaq.click_general_info_tab()
#     expected_result = "Hệ thống hiển thị giá trị Dịch vụ Hoa tiêu ở field"
#     result = select.is_value_pilotage_service_visible()
#     actual_result = expected_result if result else "Hệ thống không hiển thị giá trị Dịch vụ Hoa tiêu ở field"

#     if result:
#         test_logger.info(f"Test Case 7 PASS: test_value_pilotage_service_select_question_type | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 7 FAIL: test_value_pilotage_service_select_question_type | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 8: Verify khi chỉnh sửa giá trị ở field Thứ tự sắp xếp* -> Hệ thống hiển thị giá trị vừa chỉnh sửa
# def test_edited_sort_order(setup_driver, editfaq, validation, enter_field):
#     editfaq.navigate_to_faq()
#     editfaq.click_edit_first_line()
#     editfaq.click_general_info_tab()
#     edit_data = "55"
#     enter_field.edit_sort_order_vi(edit_data)
#     editfaq.click_save_continue_button()
#     time.sleep(2)
#     editfaq.click_general_info_tab()
#     expected_result = "Hệ thống hiển thị giá trị vừa chỉnh sửa"
#     result = validation.is_edit_sort_order_displayed(edit_data)
#     actual_result = expected_result if result else "Hệ thống không hiển thị giá trị vừa chỉnh sửa"

#     if result:
#         test_logger.info(f"Test Case 8 PASS: test_edited_sort_order | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 8 FAIL: test_edited_sort_order | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 9: Verify khi chỉnh sửa giá trị ở field Ngày đăng -> Hệ thống hiển thị giá trị vừa chỉnh sửa
# def test_value_14apr_select_posted_date(setup_driver, editfaq, select):
#     editfaq.navigate_to_faq()
#     editfaq.click_edit_first_line()
#     editfaq.click_general_info_tab()
#     date_data = "2025-04-14"
#     select.click_select_posted_date()
#     select.click_value_14apr_select_posted_date()
#     editfaq.click_save_continue_button()
#     time.sleep(2)
#     editfaq.click_general_info_tab()
#     expected_result = "Hệ thống hiển thị giá trị 14/04/2025 ở field"
#     result = select.is_value_14apr_visible(date_data)
#     actual_result = expected_result if result else "Hệ thống không hiển thị giá trị 14/04/2025 ở field"

#     if result:
#         test_logger.info(f"Test Case 9 PASS: test_value_14apr_select_posted_date | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 9 FAIL: test_value_14apr_select_posted_date | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 10: Verify khi chọn giá trị Chờ xử lý -> Hệ thống hiển thị giá trị Chờ xử lý ở field
# def test_value_pending_select_status(setup_driver, editfaq, select):
#     editfaq.navigate_to_faq()
#     editfaq.click_edit_first_line()
#     editfaq.click_general_info_tab()
#     select.click_select_status()
#     select.click_value_pending_select_status()
#     editfaq.click_save_continue_button()
#     time.sleep(2)
#     editfaq.click_general_info_tab()
#     expected_result = "Hệ thống hiển thị giá trị Chờ xử lý ở field"
#     result = select.is_value_pending_visible()
#     actual_result = expected_result if result else "Hệ thống không hiển thị giá trị Chờ xử lý ở field"

#     if result:
#         test_logger.info(f"Test Case 10 PASS: test_value_pending_select_status | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 10 FAIL: test_value_pending_select_status | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 11: Verify khi chọn giá trị Kích hoạt -> Hệ thống hiển thị giá trị Kích hoạt ở field
# def test_value_activate_select_status(setup_driver, editfaq, select):
#     editfaq.navigate_to_faq()
#     editfaq.click_edit_first_line()
#     editfaq.click_general_info_tab()
#     select.click_select_status()
#     select.click_value_activate_select_status()
#     editfaq.click_save_continue_button()
#     time.sleep(2)
#     editfaq.click_general_info_tab()
#     expected_result = "Hệ thống hiển thị giá trị Kích hoạt ở field"
#     result = select.is_value_activate_visible()
#     actual_result = expected_result if result else "Hệ thống không hiển thị giá trị Kích hoạt ở field"

#     if result:
#         test_logger.info(f"Test Case 11 PASS: test_value_activate_select_status | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 11 FAIL: test_value_activate_select_status | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"
