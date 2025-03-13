import time
import pytest
import logging
from utils.login import Login
from pages.pagev2 import PageV2
from utils.driver_setup import get_driver
from selenium.webdriver.common.by import By
from locators.locator_pagev2 import LocatorPageV2
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
        logging.info("Test Case 1 PASS: Hiển thị đúng thông báo lỗi khi không nhập tiêu đề trang.")
    else:
        logging.error(f"Test Case 1 FAILED: Không hiển thị hoặc hiển thị sai thông báo lỗi: {error_message}")
        assert False, "Thông báo lỗi không đúng hoặc không xuất hiện!"

# Test Case 2: Verify khi nhập Tiêu đề trang -> Hệ thống lưu thành công và chuyển hướng về trang danh sách
def test_save_page_and_check_in_list(pagev2, setup_driver):
    pagev2.perform_tag_operations()
    valid_title = "Trang kiểm thử"
    pagev2.enter_page_title(valid_title)
    pagev2.click_save_button()
    expected_url = "https://mpire-cms-demo.mpire.asia/cms/admin-page-v2?page=1"
    WebDriverWait(setup_driver, 5).until(EC.url_to_be(expected_url))
    if pagev2.is_page_title_in_list(valid_title):
        logging.info("Test Case 2 PASS: Lưu trang thành công và hiển thị trong danh sách.")
    else:
        logging.error("Test Case 2 FAILED: Tiêu đề trang không xuất hiện trong danh sách sau khi lưu!")
        assert False, "Tiêu đề trang không xuất hiện trong danh sách!"

# Test Case 3: Verify khi nhấn nút Thêm section -> Hệ thống hiển thị pop-up Thêm section
def test_add_section_popup_displayed(setup_driver, pagev2):
    pagev2.perform_tag_operations()
    pagev2.click_add_section_button()   
    popup_element = None
    try:
        popup_element = WebDriverWait(setup_driver, 5).until(
            EC.visibility_of_element_located(LocatorPageV2.ADD_SECTION_POPUP)
        )
    except Exception as e:
        logging.error(f"ERROR: Pop-up không xuất hiện! {e}", exc_info=True)
    if popup_element and popup_element.is_displayed():
        logging.info("Test Case 3 PASS: Pop-up thêm section hiển thị thành công.")
    else:
        logging.error("Test Case 3 FAILED: Pop-up không hiển thị sau khi nhấn 'Thêm section'.")
        assert False, "Pop-up không hiển thị sau khi nhấn 'Thêm section'."

# Test Case 4: Verify sau khi thêm section News -> Hệ thống hiển thị section News bên ngoài Danh sách section
def test_add_news_section_and_verify_display(setup_driver, pagev2):
    pagev2.perform_tag_operations()
    pagev2.add_news_section()
    news_section_element = WebDriverWait(setup_driver, 10).until(
        EC.visibility_of_element_located(LocatorPageV2.NEWS_SECTION)
    )

    if news_section_element and news_section_element.is_displayed():
        logging.info("Test Case 4 PASS: Section 'News' đã được thêm thành công và hiển thị trong danh sách.")
    else:
        logging.error("Test Case 4 FAILED: Section 'News' không hiển thị trong danh sách.")
        assert False, "Section 'News' không hiển thị sau khi thêm!"

# Test Case 5: Verify khi không nhập Tiêu đề tin tức -> Hệ thống hiển thị thông báo lỗi Vui lòng nhập tiêu đề tin tức
def test_news_section_title_validation(setup_driver, pagev2):
    pagev2.perform_tag_operations()
    pagev2.add_news_section()
    news_section_element = pagev2.is_news_section_displayed()
    assert news_section_element is not None
    assert pagev2.click_save_button()
    error_message = pagev2.get_news_section_error_message(news_section_element)
    if error_message == "Vui lòng nhập tiêu đề tin tức":
        logging.info("Test Case 5 PASS: Hiển thị đúng thông báo lỗi: Vui lòng nhập tiêu đề tin tức.")
    else:
        logging.error(f"Test Case 5 FAILED: Không hiển thị hoặc hiển thị sai thông báo lỗi: {error_message}")
        assert False, "Không tìm thấy hoặc thông báo lỗi không đúng."

# Test Case 1.2: Verify khi không nhập Tiêu đề trang -> Hệ thống hiển thị thông báo lỗi Vui lòng nhập tiêu đề trang
def test_empty_page_title_2(pagev2, setup_driver):
    pagev2.perform_tag_operations()
    pagev2.click_create_new_button()
    pagev2.enter_page_title("")
    pagev2.click_save_and_continue_button()
    error_message = pagev2.check_title_error_message()
    if error_message == "Vui lòng nhập tiêu đề trang":
        logging.info("Test Case 1.2 PASS: Hiển thị đúng thông báo lỗi khi không nhập tiêu đề trang.")
    else:
        logging.error(f"Test Case 1.2 FAILED: Không hiển thị hoặc hiển thị sai thông báo lỗi: {error_message}")
        assert False, "Thông báo lỗi không đúng hoặc không xuất hiện!"

# Test Case 2.2: Verify khi nhập Tiêu đề trang -> Hệ thống lưu thành công và chuyển hướng về trang danh sách
def test_save_page_and_check_in_list_2(pagev2, setup_driver):
    pagev2.perform_tag_operations()
    valid_title = "Trang kiểm thử"
    pagev2.enter_page_title(valid_title)
    pagev2.click_save_and_continue_button()
    try:
        # Chờ tối đa 5 giây để tìm kiếm 'Chỉnh sửa trang' trên toàn bộ trang
        WebDriverWait(setup_driver, 5).until(
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div/nav/ol/li[3]'), "Chỉnh sửa trang")
        )
        logging.info("Test Case 2.2 PASS: 'Chỉnh sửa trang' xuất hiện trên trang sau khi lưu.")
    except TimeoutException:
        logging.error("Test Case 2.2 FAILED: 'Chỉnh sửa trang' không xuất hiện trên trang sau khi lưu!")
        assert False, "'Chỉnh sửa trang' không xuất hiện trên trang!"

# Test Case 3.2: Verify Add_button is disable
def test_add_button_disable(setup_driver, pagev2):
    pagev2.perform_tag_operations()
    pagev2.click_add_section_button()
    pagev2.is_add_section_popup_displayed()
    assert pagev2.is_section_news_present()

# Test Case 3.3: Verify Add_button is disable
def test_add_button_disable(setup_driver, pagev2):
    pagev2.perform_tag_operations()
    pagev2.click_add_section_button()
    pagev2.is_add_section_popup_displayed()

    # Lấy phần tử nút "Add"
    add_button = WebDriverWait(setup_driver, 10).until(
        EC.presence_of_element_located(LocatorPageV2.ADD_BUTTON)
    )

    # Kiểm tra trạng thái của nút
    if add_button.is_enabled():
        logging.error("Test Case 3.3 FAIL: Nút 'Add' có thể click, đáng lẽ phải bị vô hiệu hóa.")
        assert False, "Nút 'Add' có thể click, testcase failed."
    else:
        logging.info("Test Case 3.3 PASS: Nút 'Add' bị vô hiệu hóa như mong đợi.")
        assert True

# Test Case 3.4: Verify Add_button is enable
def test_add_button_enable(setup_driver, pagev2):
    pagev2.perform_tag_operations()
    pagev2.click_add_section_button()
    pagev2.is_add_section_popup_displayed()
    pagev2.click_section_news_checkbox()
    
    # Lấy phần tử nút "Add"
    add_button = WebDriverWait(setup_driver, 10).until(
        EC.presence_of_element_located(LocatorPageV2.ADD_BUTTON)
    )

    # Kiểm tra trạng thái của nút
    if add_button.is_enabled():
        logging.info("Test Case 3.4 PASS: Nút 'Add' bị vô hiệu hóa như mong đợi.")
        assert True
    else:
        logging.error("Test Case 3.4 FAIL: Nút 'Add' có thể click, đáng lẽ phải bị vô hiệu hóa.")
        assert False, "Nút 'Add' có thể click, testcase failed."
    
# Test Case 6: Verify khi click icon rename -> Hệ thống hiển thị pop-up Chỉnh sửa tên section
def test_rename_section_popup_display(setup_driver, pagev2):
    pagev2.perform_tag_operations()
    pagev2.add_news_section()
    news_section_element = pagev2.is_news_section_displayed()
    assert news_section_element is not None
    pagev2.click_rename_section()
    popup_displayed = pagev2.is_rename_popup_displayed()
    if popup_displayed:
        logging.info("Test Case 6 PASS: Pop-up Rename hiển thị thành công.")
    else:
        logging.error("Test Case 6 FAILED: Pop-up Rename không hiển thị.")
        assert False, "Pop-up Rename không hiển thị."
    
