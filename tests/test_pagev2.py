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
    pagev2.click_add_section_button()
    pagev2.is_add_section_popup_displayed()
    pagev2.click_section_news_checkbox()
    pagev2.click_add_button()
    news_section_element = WebDriverWait(setup_driver, 5).until(
        EC.presence_of_element_located(LocatorPageV2.NEWS_SECTION)
    )

    if news_section_element and news_section_element.is_displayed():
        logging.info("Test Case 4 PASS: Section 'News' đã được thêm thành công và hiển thị trong danh sách.")
    else:
        logging.error("Test Case 4 PASS: Section 'News' không hiển thị trong danh sách.")
        assert False, "Section 'News' không hiển thị sau khi thêm!"

# Test Case 5: Verify khi không nhập Tiêu đề tin tức -> Hệ thống hiển thị thông báo lỗi Vui lòng nhập tiêu đề tin tức
def test_news_section_title_validation(setup_driver, pagev2):
    pagev2.click_content_menu()
    pagev2.click_page_v2_menu()
    assert pagev2.click_create_new_button()
    assert pagev2.click_add_section_button()
    assert pagev2.is_add_section_popup_displayed()
    assert pagev2.click_section_news_checkbox()
    assert pagev2.click_add_button()
    news_section_element = pagev2.is_news_section_displayed()
    assert news_section_element is not None
    assert pagev2.click_save_button()
    error_message = pagev2.get_news_section_error_message(news_section_element)
    if error_message == "Vui lòng nhập tiêu đề tin tức":
        logging.info("PASS: Hiển thị đúng thông báo lỗi: Vui lòng nhập tiêu đề tin tức.")
    else:
        logging.error(f"FAILED: Không hiển thị hoặc hiển thị sai thông báo lỗi: {error_message}")
        assert False, "Không tìm thấy hoặc thông báo lỗi không đúng."
