import pytest
import logging
from utils.login import Login
from pages.pagev2.pagev2 import PageV2
from utils.driver_setup import get_driver
from locators.locator_pagev2 import LocatorPageV2
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Cấu hình logging
test_logger = logging.getLogger("test_logger")
test_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("reports/test_results.log", mode="w")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
test_logger.addHandler(file_handler)

@pytest.fixture(scope="function")
def setup_driver():
    """Khởi tạo trình duyệt và đăng nhập vào hệ thống"""
    driver = get_driver()
    login_page = Login(driver)
    if not login_page.login():
        pytest.fail("Không thể đăng nhập!")
    yield driver
    driver.quit()

@pytest.fixture
def pagev2(setup_driver):
    """Khởi tạo đối tượng trang PageV2"""
    return PageV2(setup_driver)

def test_empty_page_title(pagev2, setup_driver, request):
    """
    Kiểm tra khi nhập Tiêu đề rỗng -> Hệ thống hiển thị thông báo lỗi.
    """
    pagev2.perform_tag_operations()
    pagev2.click_create_new_button()
    pagev2.enter_page_title("")  # Nhập tiêu đề rỗng
    pagev2.click_save_button()

    # ✅ Lấy thông báo lỗi từ hệ thống
    actual_result = pagev2.check_title_error_message()
    expected_result = "Vui lòng nhập tiêu đề trang"

    # ✅ Lưu Expected & Actual vào request.config.cache
    request.config.cache.set(f"expected_result_{request.node.name}", expected_result)
    request.config.cache.set(f"actual_result_{request.node.name}", actual_result)

    # ✅ Ghi log vào file `test_results.log`
    test_status = "PASSED" if actual_result == expected_result else "FAILED"
    test_logger.info(f"Test: {request.node.name} | Expected: {expected_result} | Actual: {actual_result} | Status: {test_status}")

    # ✅ Kiểm tra giá trị
    assert actual_result == expected_result, f"Test FAIL: Expected '{expected_result}', but got '{actual_result}'"

# Test Case 1: Verify khi không nhập Tiêu đề trang -> Hệ thống hiển thị thông báo lỗi Vui lòng nhập tiêu đề trang
def test_empty_page_title(pagev2, setup_driver):
    pagev2.perform_tag_operations()
    pagev2.click_create_new_button()
    pagev2.enter_page_title("")
    pagev2.click_save_button()
    error_message = pagev2.check_title_error_message()
    assert error_message == "Vui lòng nhập tiêu đề trang", f"Lỗi: {error_message}"
    logging.info("Test Case 1 PASS: Hiển thị đúng thông báo lỗi.")

# Test Case 2: Verify khi nhập Tiêu đề trang -> Hệ thống lưu thành công và chuyển hướng về trang danh sách
def test_save_page_and_check_in_list(pagev2, setup_driver):
    pagev2.perform_tag_operations()
    valid_title = "Trang kiểm thử"
    pagev2.enter_page_title(valid_title)
    pagev2.click_save_button()
    expected_url = "https://mpire-cms-demo.mpire.asia/cms/admin-page-v2?page=1"
    WebDriverWait(setup_driver, 10).until(EC.url_to_be(expected_url))
    assert pagev2.is_page_title_in_list(valid_title), "Tiêu đề trang không xuất hiện trong danh sách!"
    logging.info("Test Case 2 PASS: Lưu trang thành công.")

# Test Case 3: Verify khi nhấn nút Thêm section -> Hệ thống hiển thị pop-up Thêm section
def test_add_section_popup_displayed(setup_driver, pagev2):
    pagev2.perform_tag_operations()
    pagev2.click_add_section_button()   
    popup_element = WebDriverWait(setup_driver, 5).until(
        EC.visibility_of_element_located(LocatorPageV2.ADD_SECTION_POPUP)
    )
    assert popup_element.is_displayed(), "Pop-up không hiển thị sau khi nhấn 'Thêm section'."
    logging.info("Test Case 3 PASS: Pop-up hiển thị thành công.")

# Test Case 4: Verify sau khi thêm section News -> Hệ thống hiển thị section News bên ngoài Danh sách section
def test_add_news_section_and_verify_display(setup_driver, pagev2):
    pagev2.perform_tag_operations()
    pagev2.add_news_section()
    news_section_element = WebDriverWait(setup_driver, 10).until(
        EC.visibility_of_element_located(LocatorPageV2.NEWS_SECTION)
    )
    assert news_section_element.is_displayed(), "Section 'News' không hiển thị sau khi thêm!"
    logging.info("Test Case 4 PASS: Section 'News' hiển thị thành công.")

# Test Case 5: Verify khi không nhập Tiêu đề tin tức -> Hệ thống hiển thị thông báo lỗi Vui lòng nhập tiêu đề tin tức
def test_news_section_title_validation(setup_driver, pagev2):
    pagev2.perform_tag_operations()
    pagev2.add_news_section()
    news_section_element = pagev2.is_news_section_displayed()
    assert news_section_element is not None
    assert pagev2.click_save_button()
    error_message = pagev2.get_news_section_error_message(news_section_element)
    assert error_message == "Vui lòng nhập tiêu đề tin tức", f"Lỗi: {error_message}"
    logging.info("Test Case 5 PASS: Hiển thị đúng thông báo lỗi.")

# Test Case 6: Verify khi click icon rename -> Hệ thống hiển thị pop-up Chỉnh sửa tên section
def test_rename_section_popup_display(setup_driver, pagev2):
    pagev2.perform_tag_operations()
    pagev2.add_news_section()
    news_section_element = pagev2.is_news_section_displayed()
    assert news_section_element is not None
    pagev2.click_rename_section() 
    assert pagev2.is_rename_popup_displayed(), "Pop-up Rename không hiển thị."
    logging.info("Test Case 6 PASS: Pop-up Rename hiển thị thành công.")

