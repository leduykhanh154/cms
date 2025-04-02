import time
import pytest
import logging
import datetime
from utils.login import Login
from utils.logger import LoggerConfig
from utils.driver_setup import get_driver
from pages.faq.listfaq.faq_base import FAQBase
from pages.faq.listfaq.url_faq import UrlFAQ
from pages.faq.listfaq.select_faq import SelectFAQ
from pages.faq.listfaq.enter_field_faq import EnterFieldFAQ
from pages.faq.listfaq.validation_faq import ValidationFAQ 
from pages.faq.listfaq.popup_faq import PopupFAQ 
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

@pytest.fixture
def select(setup_driver):
    return SelectFAQ(setup_driver)

@pytest.fixture
def enter_field(setup_driver):
    return EnterFieldFAQ(setup_driver)

@pytest.fixture
def validation(setup_driver):
    return ValidationFAQ(setup_driver)

@pytest.fixture
def popup(setup_driver):
    return PopupFAQ(setup_driver)

# Test Case 1: Verify breadcrumb 'Trang chủ -> Danh sách câu hỏi' -> Hệ thống chuyển hướng đến 'Trang chủ'.
# def test_home_action(faq, url, setup_driver):
#     test_logger.info("Bắt đầu Test Case 1: Verify breadcrumb 'Trang chủ' -> Danh sách câu hỏi' -> Hệ thống chuyển hướng đến 'Trang chủ'.")
#     faq.navigate_to_faq()
#     faq.click_home_page()
#     expected_result = "Hệ thống chuyển hướng đến 'Trang chủ'."
#     result = url.check_url_home_page()
    
#     actual_result = expected_result if result else "Hệ thống không chuyển hướng đến 'Trang chủ'."

#     if result:
#         test_logger.info(f"Test Case 1 PASS: test_home_action | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 1 FAIL: test_home_action | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert result, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 2: Verify button 'Tạo mới' -> Hệ thống chuyển hướng đến trang 'Tạo mới'.
# def test_create_new_button(faq, url, setup_driver):
#     test_logger.info("Bắt đầu Test Case 2: Verify button 'Tạo mới' -> Hệ thống chuyển hướng đến trang 'Tạo mới'.")
#     faq.navigate_to_faq()
#     faq.click_create_new_button()
#     expected_result = "Hệ thống chuyển hướng đến trang 'Tạo mới'."
#     result = url.check_url_create_page()
#     actual_result = expected_result if result else "Hệ thống không chuyển hướng đến trang 'Tạo mới'."

#     if result:
#         test_logger.info(f"Test Case 2 PASS: test_create_new_button | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 2 FAIL: test_create_new_button | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert result, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 3: Verify dropdown 'Trạng thái' -> Hệ thống hiển thị dropdown 'Trạng thái'.
# def test_open_status_dropdown(faq, select, setup_driver):
#     test_logger.info("Bắt đầu Test Case 3: Verify dropdown 'Trạng thái' -> Hệ thống hiển thị dropdown 'Trạng thái'.")
#     faq.navigate_to_faq()
#     select.click_status_dropdown()
#     expected_result = "Hệ thống hiển thị dropdown 'Trạng thái'."
#     result = select.is_status_dropdown_visible()
#     actual_result = expected_result if result else "Hệ thống không hiển thị dropdown 'Trạng thái'."

#     if result:
#         test_logger.info(f"Test Case 3 PASS: test_open_status_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 3 FAIL: test_open_status_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 4: Verify dropdown 'Loại câu hỏi' -> Hệ thống hiển thị dropdown 'Loại câu hỏi'.
# def test_open_question_type_dropdown(faq, select, setup_driver):
#     test_logger.info("Bắt đầu Test Case 4: Verify dropdown 'Loại câu hỏi' -> Hệ thống hiển thị dropdown 'Loại câu hỏi'.")
#     faq.navigate_to_faq()
#     select.click_question_type_dropdown()
#     expected_result = "Hệ thống hiển thị dropdown 'Loại câu hỏi'."
#     result = select.is_question_type_dropdown_visible()
#     actual_result = expected_result if result else "Hệ thống không hiển thị dropdown 'Loại câu hỏi'."

#     if result:
#         test_logger.info(f"Test Case 4 PASS: test_open_question_type_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 4 FAIL: test_open_question_type_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 5: Verify dropdown 'Dòng hiển thị trên trang' -> Hệ thống hiển thị dropdown.

# Test Case 6: Verify nhập sai thông tin ở field 'Tìm kiếm' -> Hệ thống hiển thị text 'Không tìm thấy kết quả tương ứng' trong table.
def test_invalid_in_search(faq, enter_field, validation, setup_driver):
    test_logger.info("Bắt đầu Test Case 6: Verify nhập sai thông tin ở field 'Tìm kiếm' -> Hệ thống hiển thị text 'Không tìm thấy kết quả tương ứng' trong table.")
    faq.navigate_to_faq()
    invalid_in_search = '123456'
    enter_field.enter_data_in_search(invalid_in_search)
    expected_result = "Hệ thống hiển thị text 'Không tìm thấy kết quả tương ứng' trong table"
    result = validation.is_invalid_search_in_list(invalid_in_search)
    actual_result = expected_result if result else "Hệ thống không hiển thị text 'Không tìm thấy kết quả tương ứng' trong table"

    if result:
        test_logger.info(f"Test Case 6 PASS: test_invalid_in_search | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 6 FAIL: test_invalid_in_search | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 7

# Test Case 8: Verify nhập đúng thông tin ở field 'Tìm kiếm' -> Hệ thống hiển thị dữ liệu liên quan đến 'Để Order tàu vào' trong table.
# def test_valid_in_search(faq, enter_field, validation, setup_driver):
#     test_logger.info("Bắt đầu Test Case 8: Verify nhập đúng thông tin ở field 'Tìm kiếm' -> Hệ thống hiển thị dữ liệu liên quan đến 'Để Order tàu vào' trong table.")
#     faq.navigate_to_faq()
#     valid_in_search = 'Để Order tàu vào'
#     enter_field.enter_data_in_search(valid_in_search)
#     expected_result = "Hệ thống hiển thị dữ liệu liên quan đến 'Để Order tàu vào' trong table"
#     result = validation.is_valid_search_in_list(valid_in_search)
#     actual_result = expected_result if result else "Hệ thống không hiển thị dữ liệu liên quan đến 'Để Order tàu vào' trong table"

#     if result:
#         test_logger.info(f"Test Case 8 PASS: test_valid_in_search | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 8 FAIL: test_valid_in_search | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 9: Verify edit FAQ -> Hệ thống chuyển hướng đến trang 'Chỉnh sửa câu hỏi'.
# def test_edit_tag_and_redirect(faq, url, setup_driver):
#     test_logger.info("Bắt đầu Test Case 9: Verify edit FAQ -> Hệ thống chuyển hướng đến trang 'Chỉnh sửa câu hỏi'.")
#     faq.navigate_to_faq()
#     faq.click_edit_tag_first()
#     expected_result = "Hệ thống chuyển hướng đến trang 'Chỉnh sửa câu hỏi' đầu tiên."
#     result = url.check_url_question_edit_page()
#     actual_result = expected_result if result else "Hệ thống không chuyển hướng đến trang 'Chỉnh sửa câu hỏi' đầu tiên."

#     if result:
#         test_logger.info(f"Test Case 9 PASS: test_edit_tag_and_redirect | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 9 FAIL: test_edit_tag_and_redirect | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert result, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 10: Verify button 'Thao tác' -> Hệ thống hiển thị popup 'Vui lòng chọn Câu hỏi để xóa.'.
# def test_operation_button(faq, popup, select, setup_driver):
#     test_logger.info("Bắt đầu Test Case 10: Verify button 'Thao tác' -> Hệ thống hiển thị popup 'Vui lòng chọn Câu hỏi để xóa.'")
#     faq.navigate_to_faq()
#     faq.click_operation_button()
#     select.click_delete_select()
#     expected_result = "Hệ thống hiển thị popup 'Vui lòng chọn Câu hỏi để xóa.'"
#     result = popup.is_select_question_to_delete_popup_displayed()
#     actual_result = expected_result if result else "Hệ thống không hiển thị popup 'Vui lòng chọn Câu hỏi để xóa.'"

#     if result:
#         test_logger.info(f"Test Case 10 PASS: test_operation_button | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 10 FAIL: test_operation_button | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert result, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 11: Verify button 'Thao tác' và chọn dữ liệu -> Hệ thống hiển thị popup 'Bạn có chắc chắn ?'.
def test_checkbox_and_operation_button(faq, popup, select, setup_driver):
    test_logger.info("Bắt đầu Test Case 11: Verify button 'Thao tác' và chọn dữ liệu -> Hệ thống hiển thị popup 'Bạn có chắc chắn ?'.")
    faq.navigate_to_faq()
    faq.click_checkbox_first()
    faq.click_operation_button()
    select.click_delete_select()
    expected_result = "Hệ thống hiển thị popup 'Bạn có chắc chắn ?'"
    result = popup.is_secure_popup_displayed()
    actual_result = expected_result if result else "Hệ thống không hiển thị popup 'Bạn có chắc chắn ?'"

    if result:
        test_logger.info(f"Test Case 11 PASS: test_checkbox_and_operation_button | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 11 FAIL: test_checkbox_and_operation_button | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert result, f"Expected: {expected_result} | Actual: {actual_result}"







