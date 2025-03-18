import pytest
import logging
from utils.login import Login
from pages.tag import Tag
from utils.driver_setup import get_driver
from locators.locator_tag import LocatorTag
from selenium.webdriver.support.ui import WebDriverWait
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

# # Test Case 1: Verify breadcrumb 'Trang chủ -> Tag'. Hệ thống chuyển hướng sang trang chủ
# def test_home_action(tag, setup_driver):
#     try:
#         tag.perform_tag_operations()
#         tag.click_home_page()
#         print('Test Case 1 PASS: Chuyển hướng lại: Trang chủ')
#     except Exception as e:
#         print(f"Test Case 1 FAIL: Không chuyển hướng lại Trang chủ! Lỗi: {str(e)}")
#         assert False

# # Test Case 2: Verify button 'Thêm từ khóa'. Hệ thống hiển thị pop-up
# def test_add_keyword_popup_display(tag, setup_driver):
#     tag.perform_tag_operations()
#     try:
#         tag.click_add_keyword_button()
#         assert tag.is_add_keyword_popup_displayed(), "Pop-up Thêm từ khóa không hiển thị!"
#         print("Test Case 2 PASS: Pop-up Thêm từ khóa được hiển thị")
#     except Exception as e:
#         print(f"Test Case 2 FAIL: Pop-up Thêm từ khóa không hiển thị! Lỗi: {str(e)}")
#         assert False

# # Test Case 3: Verify bỏ trống 'Tên tag*' và nhấn button 'Lưu' -> Hệ thống hiển thị thông báo lỗi: 'Vui lòng nhập Tên tag'
# def test_empty_tag_name(tag, setup_driver):
#     tag.perform_tag_operations()
#     tag.click_add_keyword_button()
#     tag.is_add_keyword_popup_displayed()
#     tag.enter_tag_name("")
#     tag.click_save_button()
#     error_message = tag.check_tag_name_error_message()
    
#     if error_message == "Vui lòng nhập Tên tag":
#         print("Test Case 3 PASS: Thông báo lỗi: 'Vui lòng nhập Tên tag' được hiển thị")
#     else:
#         print(f"Test Case 3 FAIL: Không hiển thị thông báo lỗi đúng! Lỗi: {error_message}")
#         assert False

# # Test Case 4: Verify nhập thông tin bắt buộc và nhấn button 'Lưu' -> Hệ thống chuyển hướng sang trang 'Danh sách Tag' và hiển thị dữ liệu 'test-nh' trong table
# def test_save_tagname_and_check_in_list(tag, setup_driver):
#     tag.perform_tag_operations()
#     tag.click_add_keyword_button()
#     tag.is_add_keyword_popup_displayed()
#     valid_tagname = 'test-nhan'
#     tag.enter_tag_name(valid_tagname)
#     tag.click_save_button()
#     expected_url = LocatorTag.TAG_LIST_URL
#     WebDriverWait(setup_driver, 10).until(EC.url_to_be(expected_url))
#     if tag.is_tag_name_in_list(valid_tagname):
#         print(f"Test Case 4 PASS: Tên tag '{valid_tagname}' đã hiển thị bên ngoài trang 'Danh sách Tag'")
#     else:
#         print(f"Test Case 4 FAIL: Tên tag '{valid_tagname}' không hiển thị bên ngoài trang 'Danh sách Tag'!")
#         assert False

    