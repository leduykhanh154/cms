import pytest
import logging
from utils.login import Login
from pages.pagev2 import PageV2
from utils.driver_setup import get_driver
from locators.locator_pagev2 import LocatorPageV2
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
def pagev2(setup_driver):
    return PageV2(setup_driver)

def log_success(message):
    print(f"{message}")
    logging.info(message)

# Test Case 1: Verify khi không nhập Tiêu đề trang -> Hệ thống hiển thị thông báo lỗi Vui lòng nhập tiêu đề trang
def test_empty_page_title(pagev2, setup_driver):
    pagev2.perform_tag_operations()
    pagev2.click_create_new_button()
    pagev2.enter_page_title("")
    pagev2.click_save_button()
    error_message = pagev2.check_title_error_message()
    
    if error_message == "Vui lòng nhập tiêu đề trang":
        print("Test Case 1 PASS: Thông báo lỗi Vui lòng nhập tiêu đề trang được hiển thị")
    else:
        print(f"Test Case 1 FAIL: Nhận được '{error_message}'")
        assert False

# Test Case 2: Verify khi nhập Tiêu đề trang -> Hệ thống lưu thành công và chuyển hướng về trang danh sách
def test_save_page_and_check_in_list(pagev2, setup_driver):
    pagev2.perform_tag_operations()
    valid_title = "Trang kiểm thử"
    pagev2.enter_page_title(valid_title)
    pagev2.click_save_button()
    expected_url = "https://mpire-cms-demo.mpire.asia/cms/admin-page-v2?page=1"
    WebDriverWait(setup_driver, 10).until(EC.url_to_be(expected_url))
    if pagev2.is_page_title_in_list(valid_title):
        print("Test Case 2 PASS: Tiêu đề trang hiển thị bên ngoài trang danh sách")
    else:
        print(f"Test Case 2 FAIL: Tiêu đề '{valid_title}' không hiển thị bên ngoài trang danh sách!")
        assert False

# Test Case 3: Verify khi nhấn nút Thêm section -> Hệ thống hiển thị pop-up Thêm section
def test_add_section_popup_displayed(setup_driver, pagev2):
    pagev2.perform_tag_operations()
    pagev2.click_add_section_button()   
    try:
        popup_element = WebDriverWait(setup_driver, 5).until(
            EC.visibility_of_element_located(LocatorPageV2.ADD_SECTION_POPUP)
        )
        assert popup_element.is_displayed(), "Pop-up Thêm section không hiển thị sau khi nhấn nút Thêm section"
        print("Test Case 3 PASS: Pop-up Thêm section hiển thị")
    except Exception as e:
        print(f"Test Case 3 FAIL: Pop-up Thêm section không hiển thị! Lỗi: {str(e)}")
        assert False

# Test Case 4: Verify sau khi thêm section News -> Hệ thống hiển thị section News bên ngoài Danh sách section
def test_add_news_section_and_verify_display(setup_driver, pagev2):
    pagev2.perform_tag_operations()
    pagev2.add_news_section()
    try:
        news_section_element = WebDriverWait(setup_driver, 10).until(
            EC.visibility_of_element_located(LocatorPageV2.NEWS_SECTION)
        )
        assert news_section_element.is_displayed(), "Section News không hiển thị bên ngoài danh sách section sau khi thêm!"
        print("Test Case 4 PASS: Section News hiển thị bên ngoài danh sách section")
    except Exception as e:
        print(f"Test Case 4 FAIL: Section News không hiển thị! Lỗi: {str(e)}")
        assert False

# Test Case 5: Verify khi không nhập Tiêu đề tin tức -> Hệ thống hiển thị thông báo lỗi Vui lòng nhập tiêu đề tin tức
def test_news_section_title_validation(setup_driver, pagev2):
    pagev2.perform_tag_operations()
    pagev2.add_news_section()
    try:
        news_section_element = pagev2.is_news_section_displayed()
        assert news_section_element
        pagev2.click_save_button()
        error_message = pagev2.get_news_section_error_message(news_section_element)
        assert error_message == "Vui lòng nhập tiêu đề tin tức", f"Lỗi: {error_message}"
        print("Test Case 5 PASS: Thông báo lỗi 'Vui lòng nhập tiêu đề tin tức' được hiển thị")
    except Exception as e:
        print(f"Test Case 5 FAIL: Không hiển thị thông báo lỗi đúng! Lỗi: {str(e)}")
        assert False

# Test Case 6: Verify khi click icon rename -> Hệ thống hiển thị pop-up Chỉnh sửa tên section
def test_rename_section_popup_display(setup_driver, pagev2):
    pagev2.perform_tag_operations()
    pagev2.add_news_section()
    try:
        pagev2.is_news_section_displayed()
        pagev2.click_rename_section()
        assert pagev2.is_rename_popup_displayed(), "Pop-up Rename không hiển thị!"
        print("Test Case 6 PASS: Pop-up Rename được hiển thị")
    except Exception as e:
        print(f"Test Case 6 FAIL: Pop-up Rename không hiển thị! Lỗi: {str(e)}")
        assert False

# Test Case 7: Verify khi nhập chữ vào field nhập số lượng slide -> Hệ thống không nhập dữ liệu chữ
def test_number_of_articles_rejects_text(setup_driver, pagev2):
    pagev2.perform_tag_operations()
    pagev2.add_news_section()
    try:
        assert pagev2.is_news_section_displayed(), "Section News không hiển thị!" 
        invalid_input = "abc"
        pagev2.enter_number_of_articles(invalid_input)
        actual_value = pagev2.get_number_of_articles_value()
        assert actual_value == "" or actual_value.isnumeric(), f"Input không hợp lệ nhưng vẫn giữ giá trị: '{actual_value}'"
        print("Test Case 7 PASS: Nhập chữ vào field số lượng slide không thành công (đúng mong đợi)")
    except Exception as e:
        print(f"Test Case 7 FAIL: Hệ thống vẫn chấp nhận chữ! Lỗi: {str(e)}")
        assert False

