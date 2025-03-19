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

# Test Case 2: Verify button 'Thêm từ khóa'. Hệ thống hiển thị pop-up
def test_add_keyword_popup_display(tag, setup_driver):
    tag.perform_tag_operations()
    try:
        tag.click_add_keyword_button()
        assert tag.is_add_keyword_popup_displayed(), "Pop-up Thêm từ khóa không hiển thị!"
        print("Test Case 2 PASS: Pop-up Thêm từ khóa được hiển thị")
    except Exception as e:
        print(f"Test Case 2 FAIL: Pop-up Thêm từ khóa không hiển thị! Lỗi: {str(e)}")
        assert False

# Test Case 3: Verify bỏ trống 'Tên tag*' và nhấn button 'Lưu' -> Hệ thống hiển thị thông báo lỗi: 'Vui lòng nhập Tên tag'
def test_empty_tag_name(tag, setup_driver):
    tag.perform_tag_operations()
    tag.click_add_keyword_button()
    tag.is_add_keyword_popup_displayed()
    tag.enter_tag_name("")
    tag.click_save_button()
    error_message = tag.check_tag_name_error_message()
    
    if error_message == "Vui lòng nhập Tên tag":
        print("Test Case 3 PASS: Thông báo lỗi: 'Vui lòng nhập Tên tag' được hiển thị")
    else:
        print(f"Test Case 3 FAIL: Không hiển thị thông báo lỗi đúng! Lỗi: {error_message}")
        assert False

# Test Case 4: Verify nhập thông tin bắt buộc và nhấn button 'Lưu' -> Hệ thống chuyển hướng sang trang 'Danh sách Tag' và hiển thị dữ liệu 'test-nhan' trong table
def test_save_tagname_and_check_in_list(tag, setup_driver):
    tag.perform_tag_operations()
    tag.click_add_keyword_button()
    tag.is_add_keyword_popup_displayed()
    valid_tagname = 'test-nhan'
    tag.enter_tag_name(valid_tagname)
    tag.click_save_button()
    expected_url = LocatorTag.TAG_LIST_URL
    WebDriverWait(setup_driver, 10).until(EC.url_to_be(expected_url))
    if tag.is_tag_name_in_list(valid_tagname):
        print(f"Test Case 4 PASS: Tên tag '{valid_tagname}' đã hiển thị bên ngoài trang 'Danh sách Tag'")
    else:
        print(f"Test Case 4 FAIL: Tên tag '{valid_tagname}' không hiển thị bên ngoài trang 'Danh sách Tag'!")
        assert False

# Test Case 5: Verify khi click vào dropdown 'Trạng thái' -> Hệ thống mở dropdown 'Trạng thái'
def test_open_status_dropdown(tag):
    tag.perform_tag_operations()
    tag.click_status_dropdown()
    if tag.is_status_dropdown_visible():
        logging.info("Test Case 5 PASS: Hệ thống mở dropdown 'Trạng thái' thành công!")
    else:
        logging.error("Test Case 5 FAIL: Hệ thống không mở dropdown 'Trạng thái'!")
        assert False, "Lỗi: Dropdown không mở."

# Test Case 6: Verify khi click vào dropdown 'Trang' -> Hệ thống mở dropdown 'Trang'
# FAIL không select được dropdown

# Test Case 7: Verify khi click số lượng trong dropdown 'Trang' -> Hệ thống hiển thị 2 trường thông tin trong table
# FAIL không select được khi hiển thị 2 trường thông tin

# Test Case 8: Verify button 'Thao tác' -> Hệ thống hiển thị dropdown của button 'Thao tác'
def test_operation_button(tag):
    tag.perform_tag_operations()
    tag.click_operation_button()
    if tag.is_operation_button_dropdown_visible():
        logging.info("Test Case 8 PASS: Hệ thống mở dropdown của button 'Thao tác' thành công!")
    else:
        logging.error("Test Case 8 FAIL: Hệ thống không mở dropdown của button 'Thao tác'!")
        assert False, "Lỗi: Dropdown không mở."

# Test Case 9: Verify click dropdown 'Xóa' trong button 'Thao tác' -> Hệ thống hiển thị toggle

# Test Case 10: Verify chọn checkbox và click dropdown 'Xóa' trong button 'Thao tác' -> Hệ thống hiển thị pop-up
def test_delete_popup_display(tag, setup_driver):
    tag.perform_tag_operations()
    try:
        tag.click_checkbox_first()
        tag.click_operation_button()
        tag.click_delete_dropdown()
        assert tag.is_delete_popup_displayed(), "Pop-up không hiển thị!"
        print("Test Case 10 PASS: Pop-up được hiển thị")
    except Exception as e:
        print(f"Test Case 10 FAIL: Pop-up không hiển thị! Lỗi: {str(e)}")
        assert False

# Test Case 11: Verify chọn checkbox và click dropdown 'Xóa', chọn button 'Có' trong button 'Thao tác' -> Hệ thống quay lại trang 'Danh sách Tag' và dữ liệu được xóa
def test_button_yes_and_verify_display(tag, setup_driver):
    tag.perform_tag_operations()
    try:
        tag.click_checkbox_first()
        tag.click_operation_button()
        tag.click_delete_dropdown()
        tag.is_delete_popup_displayed()
        tag.click_yes_button()
        valid_tagname = 'test-nhan'
        if tag.is_delete_tag_name_in_list(valid_tagname):
            print(f"Test Case 11 PASS: Tên tag '{valid_tagname}' không hiển thị bên ngoài trang 'Danh sách Tag'")
        else:
            print(f"Test Case 11 FAILED: Tên tag '{valid_tagname}' có hiển thị bên ngoài trang 'Danh sách Tag'!")
            assert False
    except Exception as e:
        print(f"Test Case 11 FAILED: Lỗi không hiển thị! Lỗi: {str(e)}")
        assert False

# Test Case 12: Verify chọn checkbox và click dropdown 'Xóa', chọn button 'Không' trong button 'Thao tác' -> Hệ thống quay lại trang 'Danh sách Tag' và dữ liệu không được xóa
def test_button_no_and_verify_display(tag, setup_driver):
    tag.perform_tag_operations()
    try:
        tag.click_checkbox_first()
        tag.click_operation_button()
        tag.click_delete_dropdown()
        tag.is_delete_popup_displayed()
        tag.click_no_button()
        valid_tagname = 'test-nhan'
        if tag.is_tag_name_in_list(valid_tagname):
            print(f"Test Case 12 PASS: Tên tag '{valid_tagname}' vẫn hiển thị bên ngoài trang 'Danh sách Tag'")
        else:
            print(f"Test Case 12 FAILED: Tên tag '{valid_tagname}' không hiển thị bên ngoài trang 'Danh sách Tag'!")
            assert False
    except Exception as e:
        print(f"Test Case 12 FAILED: Lỗi không hiển thị! Lỗi: {str(e)}")
        assert False

# Test Case 13: Verify nhập sai thông tin trong field 'Tìm kiếm' -> Hệ thống hiển thị text 'Không tìm thấy kết quả tương ứng' trong table
def test_invalid_in_search(tag, setup_driver):
    tag.perform_tag_operations()
    invalid_in_search = '123456'
    tag.enter_in_search(invalid_in_search)
    if tag.is_invalid_search_in_list(invalid_in_search):
        print(f"Test Case 13 PASS: Hệ thống hiển thị thông báo lỗi: 'Không tìm thấy kết quả tương ứng'! ")
    else:
        print(f"Test Case 13 FAILED: Giá trị '{invalid_in_search}' có hiển thị bên ngoài trang 'Danh sách Tag'!")
        assert False

# Test Case 14:

# Test Case 15: Verify nhập đúng thông tin trong field 'Tìm kiếm' -> Hệ thống hiển thị thông tin đã nhập trong table
def test_valid_in_search(tag, setup_driver):
    tag.perform_tag_operations()
    valid_in_search = 'test-nhan'
    tag.enter_in_search(valid_in_search)
    if tag.is_valid_search_in_list(valid_in_search):
        print(f"Test Case 15 PASS: Giá trị '{valid_in_search}' có hiển thị bên ngoài trang 'Danh sách Tag'! ")
    else:
        print(f"Test Case 15 FAILED:  Hệ thống hiển thị thông báo lỗi: 'Không tìm thấy kết quả tương ứng'!")
        assert False

# Test Case 16: Verify edit tag -> Hệ thống hiển thị pop-up
def test_edit_tag_popup_display(tag, setup_driver):
    tag.perform_tag_operations()
    try:
        tag.click_edit_tag_first()
        assert tag.is_edit_tag_popup_displayed(), "Pop-up không hiển thị!"
        print("Test Case 16 PASS: Pop-up 'Sửa từ khóa' được hiển thị")
    except Exception as e:
        print(f"Test Case 10 FAIL: Pop-up 'Sửa từ khóa' không hiển thị! Lỗi: {str(e)}")
        assert False

# Test Case 17: Verify edit tag và xóa thông tin -> Hệ thống hiển thị validate "Vui lòng nhập Tên tag"
def test_edit_tag_and_empty_tag_name(tag, setup_driver):
    tag.perform_tag_operations()
    tag.click_edit_tag_first()
    tag.is_edit_tag_popup_displayed()
    empty_tagname = ''
    tag.enter_tag_name(empty_tagname)
    tag.click_save_button()
    error_message = tag.check_tag_name_error_message()
    
    if error_message == "Vui lòng nhập Tên tag":
        print("Test Case 17 PASS: Thông báo lỗi: 'Vui lòng nhập Tên tag' được hiển thị")
    else:
        print(f"Test Case 17 FAIL: Không hiển thị thông báo lỗi đúng! Lỗi: {error_message}")
        assert False

# Test Case 18: Verify edit tag và sửa thông tin -> Hệ thống chuyển hướng sang trang 'Danh sách Tag' và hiển thị dữ liệu đã cập nhật trong table
def test_edit_tag_and_edit_tag_name(tag, setup_driver):
    tag.perform_tag_operations()
    tag.click_edit_tag_first()
    tag.is_edit_tag_popup_displayed()
    edit_tagname = 'test-nhan-edit'
    tag.edit_tag_name(edit_tagname)
    tag.click_save_button()
    if tag.is_edit_tag_name_in_list(edit_tagname):
        print(f"Test Case 18 PASS: Dữ liệu '{edit_tagname}' có hiển thị bên ngoài trang 'Danh sách Tag'! ")
    else:
        print(f"Test Case 18 FAILED:  Dữ liệu '{edit_tagname}' không có hiển thị bên ngoài trang 'Danh sách Tag'!")
        assert False

# Test Case 19: Verify edit tag và nhấn button 'Lưu'  -> Hệ thống chuyển hướng sang trang 'Danh sách Tag' và hiển thị dữ liệu ban đầu trong table
# FAILED không được text trong list wrapper

