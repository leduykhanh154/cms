import time
import pytest
import logging
import datetime
from utils.login import Login
from utils.logger import LoggerConfig
from utils.driver_setup import get_driver
from pages.articles.tag_article import TagArticle
from pages.articles.url_article import URLArticle
from pages.articles.article_base import ArticleBase
from pages.articles.date_article import DateArticle
from locators.locator_article import LocatorArticle
from pages.articles.image_article import ImageArticle
from pages.articles.select_article import SelectArticle
from pages.articles.switch_article import SwitchArticle
from selenium.common.exceptions import TimeoutException
from pages.articles.validation_article import ArticleValidation
from pages.articles.enter_field_article import EnterFieldArticle
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
        time.sleep(3)
        driver.quit()

@pytest.fixture
def article(setup_driver):
    return ArticleBase(setup_driver)

@pytest.fixture
def validation(setup_driver):
    return ArticleValidation(setup_driver)

@pytest.fixture
def enter_field(setup_driver):
    return EnterFieldArticle(setup_driver)

@pytest.fixture
def select(setup_driver):
    return SelectArticle(setup_driver)

@pytest.fixture
def date(setup_driver):
    return DateArticle(setup_driver)

@pytest.fixture
def switch(setup_driver):
    return SwitchArticle(setup_driver)

@pytest.fixture
def tag(setup_driver):
    return TagArticle(setup_driver)

@pytest.fixture
def image(setup_driver):
    return ImageArticle(setup_driver)

@pytest.fixture
def url(setup_driver):
    return URLArticle(setup_driver)

# # Test Case 1: Verify khi click menu 'Tất cả bài viết' -> Hệ thống chuyển hướng đến trang Danh sách bài viết 
# def test_navigate_to_all_articles(article):
#     article.click_content_menu()
#     article.click_article_menu()
#     result = article.click_all_article_menu()
#     if result:
#         logging.info("Test Case 1 PASS: Hệ thống chuyển hướng thành công đến trang 'Tất cả bài viết'")
#     else:
#         logging.error("Test Case 1 FAIL: Hệ thống không chuyển hướng đến trang 'Tất cả bài viết'")
#         assert False, "Lỗi: Trang 'Tất cả bài viết' không tải được!"

# # Test Case 2: Verify khi click nút 'Tạo mới' -> Hệ thống chuyển hướng đến trang Tạo mới bài viết 
# def test_navigate_to_create_article(article):
#     article.click_content_menu()
#     article.click_article_menu()
#     article.click_all_article_menu()
#     result = article.click_create_new_button()
#     if result:
#         logging.info("Test Case 2 PASS: Hệ thống chuyển hướng thành công đến trang 'Tạo mới bài viết'")
#     else:
#         logging.error("Test Case 2 FAIL: Hệ thống không chuyển đến trang 'Tạo mới bài viết")
#         assert False, "Lỗi: Trang 'Tạo mới bài viết' không tải được!"

# Test Case 3: Verify khi không nhập Tiêu đề - Tiếng Việt -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Tiêu đề'.
def test_empty_article_title_vi(article, enter_field, validation):
    test_logger.info("Bắt đầu Test Case 3: Verify khi không nhập Tiêu đề - Tiếng Việt -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Tiêu đề'.")
    article.perform_tag_operations()
    article.click_create_new_button()
    enter_field.enter_title_vi("")
    article.click_save_button()
    expected_result = "Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Tiêu đề'."
    result = validation.is_title_vi_error_displayed()
    actual_result = expected_result if result else "Hệ thống không hiển thị thông báo lỗi 'Vui lòng nhập Tiêu đề'."
    if result:
        test_logger.info(f"Test Case 3 PASS: test_empty_article_title_vi | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 3 FAIL: test_empty_article_title_vi | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 4: Verify khi nhập Tiêu đề - Tiếng Việt -> Hệ thống ẩn đi thông báo lỗi 'Vui lòng nhập Tiêu đề'.
# def test_title_vi_error_disappears(article, enter_field, validation):
#     test_logger.info("Bắt đầu Test Case 4: Verify khi nhập lại Tiêu đề - Tiếng Việt -> Hệ thống ẩn đi thông báo lỗi 'Vui lòng nhập Tiêu đề'.")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     enter_field.enter_title_vi("")
#     article.click_save_button()
#     validation.is_title_vi_error_displayed()
#     enter_field.enter_title_vi("Tiêu đề bài viết")
#     expected_result = "Hệ thống ẩn đi thông báo lỗi 'Vui lòng nhập Tiêu đề'."
#     result = not validation.is_title_vi_error_displayed()
#     actual_result = expected_result if result else "Hệ thống không ẩn đi thông báo lỗi 'Vui lòng nhập Tiêu đề'."
#     if result:
#         test_logger.info(f"Test Case 4 PASS: test_title_vi_error_disappears | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 4 FAIL: test_title_vi_error_disappears | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 5: Verify khi nhập Tiêu đề - Tiếng Việt hơn 250 ký tự -> Hệ thống hiển thị thông báo lỗi 'Tiêu đề không được vượt quá 250 ký tự'.
# def test_title_vi_max_length_error(article, enter_field, validation):
#     test_logger.info("Bắt đầu Test Case 5: Verify khi nhập Tiêu đề - Tiếng Việt hơn 250 ký tự -> Hệ thống hiển thị thông báo lỗi 'Tiêu đề không được vượt quá 250 ký tự'.")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     long_title = "A" * 251
#     enter_field.enter_title_vi(long_title)
#     expected_result = "Hệ thống hiển thị thông báo lỗi 'Tiêu đề không được vượt quá 250 ký tự'."
#     result = validation.is_title_vi_max_length_error_displayed()
#     actual_result = expected_result if result else "Hệ thống không hiển thị thông báo lỗi 'Tiêu đề không được vượt quá 250 ký tự'."
#     if result:
#         test_logger.info(f"Test Case 5 PASS: test_title_vi_max_length_error | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 5 FAIL: test_title_vi_max_length_error | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 6: Verify khi giảm số ký tự trong Tiêu đề - Tiếng Việt xuống < 250 -> Hệ thống ẩn đi thông báo lỗi 'Tiêu đề không được vượt quá 250 ký tự'.
# def test_title_vi_max_length_error_disappears(article, enter_field, validation):
#     test_logger.info("Bắt đầu Test Case 6: erify khi giảm số ký tự trong Tiêu đề - Tiếng Việt xuống < 250 -> Hệ thống ẩn đi thông báo lỗi 'Tiêu đề không được vượt quá 250 ký tự'.")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     long_title = "A" * 251
#     enter_field.enter_title_vi(long_title)
#     assert validation.is_title_vi_max_length_error_displayed(), "Lỗi: Hệ thống không hiển thị thông báo lỗi 'Tiêu đề không được vượt quá 250 ký tự'."
#     short_title = "A" * 250
#     enter_field.enter_title_vi(short_title)
#     expected_result = "Hệ thống ẩn đi thông báo lỗi 'Tiêu đề không được vượt quá 250 ký tự'."
#     result = not validation.is_title_vi_max_length_error_displayed()
#     actual_result = expected_result if result else "Hệ thống không ẩn đi thông báo lỗi 'Tiêu đề không được vượt quá 250 ký tự'."
#     if result:
#         test_logger.info(f"Test Case 6 PASS: test_title_vi_max_length_error_disappears | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 6 FAIL: test_title_vi_max_length_error_disappears | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 7: Verify khi nhập Mô tả ngắn - Tiếng Việt hơn 1000 ký tự -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Mô tả ngắn không quá 1000 ký tự'.
# def test_short_description_vi_max_length_error(article, enter_field, validation):
#     test_logger.info("Bắt đầu Test Case 11: Verify khi nhập Mô tả ngắn - Tiếng Việt hơn 1000 ký tự -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Mô tả ngắn không quá 1000 ký tự'.")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     long_description = "A" * 1002
#     enter_field.enter_short_description_vi(long_description)
#     expected_result = "Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Mô tả ngắn không quá 1000 ký tự'."
#     result = validation.is_short_description_vi_max_length_error_displayed()
#     actual_result = expected_result if result else "Hệ thống không hiển thị thông báo lỗi 'Vui lòng nhập Mô tả ngắn không quá 1000 ký tự'."
#     if result:
#         test_logger.info(f"Test Case 7 PASS: test_short_description_vi_max_length_error | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 7 FAIL: test_short_description_vi_max_length_error | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 8: Verify khi nhập lại Mô tả ngắn - Tiếng Việt < 1000 ký tự -> Hệ thống ẩn đi thông báo lỗi 'Vui lòng nhập Mô tả ngắn không quá 1000 ký tự'.
# def test_short_description_vi_max_length_error_disappears(article, enter_field, validation):
#     test_logger.info("Bắt đầu Test Case 12: Verify khi nhập lại Mô tả ngắn - Tiếng Việt < 1000 ký tự -> Hệ thống ẩn đi thông báo lỗi 'Vui lòng nhập Mô tả ngắn không quá 1000 ký tự'.")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     long_description = "A" * 1002
#     enter_field.enter_short_description_vi(long_description)
#     assert validation.is_short_description_vi_max_length_error_displayed(), f"Lỗi: Hệ thống không hiển thị thông báo lỗi 'Vui lòng nhập Mô tả ngắn không quá 1000 ký tự'."
#     valid_description = "A" * 999
#     enter_field.enter_short_description_vi(valid_description)
#     expected_result = "Hệ thống ẩn đi thông báo lỗi 'Vui lòng nhập Mô tả ngắn không quá 1000 ký tự'."
#     result = not validation.is_short_description_vi_max_length_error_displayed()
#     actual_result = expected_result if result else "Hệ thống không ẩn đi thông báo lỗi 'Vui lòng nhập Mô tả ngắn không quá 1000 ký tự'."
#     if result:
#         test_logger.info(f"Test Case 8 PASS: test_short_description_vi_max_length_error_disappears | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 8 FAIL: test_short_description_vi_max_length_error_disappears | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 9: Verify khi không nhập Nội dung - Tiếng Việt -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Nội dung'.
# def test_empty_article_content_vi(article, enter_field, validation):
#     test_logger.info("Bắt đầu Test Case 15: Verify khi không nhập Nội dung - Tiếng Việt -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Nội dung'.")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     enter_field.enter_content_vi("")
#     article.click_save_button()
#     expected_result = "Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Nội dung'."
#     result = validation.is_content_vi_error_displayed()
#     actual_result = expected_result if result else "Hệ thống không hiển thị thông báo lỗi 'Vui lòng nhập Nội dung'."
#     if result:
#         test_logger.info(f"Test Case 9 PASS: test_empty_article_content_vi | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 9 FAIL: test_empty_article_content_vi | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 10: Verify khi nhập lại dữ liệu vào field Nội dung - Tiếng Việt -> Hệ thống ẩn đi thông báo lỗi 'Vui lòng nhập Nội dung'.
# def test_content_vi_error_disappears(article, enter_field, validation):
#     test_logger.info("Bắt đầu Test Case 10: Verify khi nhập lại dữ liệu vào field Nội dung - Tiếng Việt -> Hệ thống ẩn đi thông báo lỗi 'Vui lòng nhập Nội dung'.")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     enter_field.enter_content_vi("")
#     article.click_save_button()
#     validation.is_content_vi_error_displayed()
#     enter_field.enter_content_vi("Nội dung bài viết")
#     error_message_after_input = validation.is_content_vi_error_displayed()
#     expected_result = "Hệ thống ẩn đi thông báo lỗi 'Vui lòng nhập Nội dung'."
#     actual_result = expected_result if not error_message_after_input else "Hệ thống không ẩn đi thông báo lỗi 'Vui lòng nhập Nội dung'."
#     if not error_message_after_input:
#         test_logger.info(f"Test Case 10 PASS: test_content_vi_error_disappears | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 10 FAIL: test_content_vi_error_disappears | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 11: Verify khi không nhập Tiêu đề - Enlish -> Hệ thống hiển thị thống báo lỗi 'Vui lòng nhập Tiêu đề'.
# def test_empty_article_title_en(article, enter_field, validation):
#     test_logger.info("Bắt đầu Test Case 11: Verify khi không nhập Tiêu đề - Enlish -> Hệ thống hiển thị thống báo lỗi 'Vui lòng nhập Tiêu đề'.")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     article.click_en_tab()
#     article.click_translate_content_button()
#     enter_field.enter_title_en("")
#     article.click_save_button()
#     expected_result = "Hệ thống hiển thị thống báo lỗi 'Vui lòng nhập Tiêu đề'."
#     result = validation.is_title_en_error_displayed()
#     actual_result = expected_result if result else "Hệ thống không hiển thị thống báo lỗi 'Vui lòng nhập Tiêu đề'."
#     if result:
#         test_logger.info(f"Test Case 11 PASS: test_empty_article_title_en | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 11 FAIL: test_empty_article_title_en | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 12: Verify khi nhập Tiêu đề - Enlish hơn 250 ký tự -> Hệ thống hiển thị thông báo lỗi 'Tiêu đề không được vượt quá 250 ký tự'.
# def test_title_en_max_length_error(article, enter_field, validation):
#     test_logger.info("Bắt đầu Test Case 12: Verify khi nhập Tiêu đề - Enlish hơn 250 ký tự -> Hệ thống hiển thị thông báo lỗi 'Tiêu đề không được vượt quá 250 ký tự'.")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     article.click_en_tab()
#     article.click_translate_content_button()
#     long_title = "A" * 251
#     enter_field.enter_title_en(long_title)
#     article.click_save_button()
#     expected_result = "Hệ thống hiển thị thông báo lỗi 'Tiêu đề không được vượt quá 250 ký tự'."
#     result = validation.is_title_en_max_length_error_displayed()
#     actual_result = expected_result if result else "Hệ thống không hiển thị thông báo lỗi 'Tiêu đề không được vượt quá 250 ký tự'."
#     if result:
#         test_logger.info(f"Test Case 12 PASS: test_title_en_max_length_error | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 12 FAIL: test_title_en_max_length_error | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 13: Verify khi nhập Mô tả ngắn - English hơn 1000 ký tự -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Mô tả ngắn không quá 1000 ký tự'.
# def test_short_description_en_max_length_error(article, enter_field, validation):
#     test_logger.info("Bắt đầu Test Case 13: Verify khi nhập Mô tả ngắn - English hơn 1000 ký tự -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Mô tả ngắn không quá 1000 ký tự'.")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     article.click_en_tab()
#     article.click_translate_content_button()
#     long_description = "A" * 1002
#     enter_field.enter_short_description_en(long_description)
#     article.click_save_button()
#     expected_result = "Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Mô tả ngắn không quá 1000 ký tự'."
#     result = validation.is_short_description_en_max_lenght_error_displayed()
#     actual_result = expected_result if result else "Hệ thống không hiển thị thông báo lỗi 'Vui lòng nhập Mô tả ngắn không quá 1000 ký tự'."
#     if result:
#         test_logger.info(f"Test Case 13 PASS: test_short_description_en_max_length_error | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 13 FAIL: test_short_description_en_max_length_error | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 14: Verify khi không nhập Nội dung - English -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Nội dung'.
# def test_empty_article_content_en(article, enter_field, validation):
#     test_logger.info("Bắt đầu Test Case 14: Verify khi không nhập Nội dung - English -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Nội dung'.")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     article.click_en_tab()
#     article.click_translate_content_button()
#     enter_field.enter_content_en("")
#     article.click_save_button()
#     expected_result = "Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Nội dung'."
#     result = validation.is_content_en_error_displayed()
#     actual_result = expected_result if result else "Hệ thống không hiển thị thông báo lỗi 'Vui lòng nhập Nội dung'."
#     if result:
#         test_logger.info(f"Test Case 14 PASS: test_empty_article_content_en | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 14 FAIL: test_empty_article_content_en | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 15: Verify khi không chọn 'Loại bài viết' -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Loại bài viết'.
# def test_article_type_error(article, validation):
#     test_logger.info("Bắt đầu Test Case 15: Verify khi không chọn 'Loại bài viết' -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Loại bài viết'.")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     article.click_save_button()
#     article.click_tab_general_info()
#     expected_result = "Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Loại bài viết'."
#     result = validation.is_article_type_error_displayed()
#     actual_result = expected_result if result else "Hệ thống không hiển thị thông báo lỗi 'Vui lòng nhập Loại bài viết'."
#     if result:
#         test_logger.info(f"Test Case 15 PASS: test_article_type_error | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 15 FAIL: test_article_type_error | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 16: Verify khi click vào dropdown 'Loại bài viết' -> Hệ thống mở dropdown 'Loại bài viết'.
# def test_open_article_type_dropdown(article, select):
#     test_logger.info("Bắt đầu Test Case 16: Verify khi click vào dropdown 'Loại bài viết' -> Hệ thống mở dropdown 'Loại bài viết'.")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     article.click_tab_general_info()
#     select.click_select()
#     expected_result = True
#     result = select.is_dropdown_visible()
#     actual_result = "Hệ thống mở dropdown 'Loại bài viết'." if result else "Hệ thống không mở dropdown 'Loại bài viết'."
#     if result:
#         test_logger.info(f"Test Case 16 PASS: test_open_article_type_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 16 FAIL: test_open_article_type_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 17: Verify khi chọn lại 'Loại bài viết' từ dropdown -> Hệ thống ẩn đi thông báo lỗi.
# def test_select_article_type_from_dropdown(article, select):
#     test_logger.info("Bắt đầu Test Case 17: Verify khi chọn lại 'Loại bài viết' từ dropdown -> Hệ thống ẩn đi thông báo lỗi.")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     article.click_save_and_continue_button()
#     article.click_tab_general_info()
#     select.click_select()
#     select.select_article_type("Tin tức chuyên ngành")
#     expected_result = "Tin tức chuyên ngành"
#     result = select.is_selected_article_type_displayed(expected_result)
#     actual_result = expected_result if result else "Hệ thống không ẩn đi thông báo lỗi."
#     if result:
#         test_logger.info(f"Test Case 17 PASS: test_select_article_type_from_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 17 FAIL: test_select_article_type_from_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 18: Verify khi click vào dropdown 'Trạng thái' -> Hệ thống mở dropdown 'Trạng thái'.
# def test_open_status_dropdown(article, select):
#     test_logger.info("Bắt đầu Test Case 18: Verify khi click vào dropdown 'Trạng thái' -> Hệ thống mở dropdown 'Trạng thái'.")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     article.click_tab_general_info()
#     select.click_status_dropdown()
#     expected_result = "Hệ thống mở dropdown 'Trạng thái'."
#     result = select.is_status_dropdown_visible()
#     actual_result = expected_result if result else "Hệ thống không mở dropdown 'Trạng thái'."
#     if result:
#         test_logger.info(f"Test Case 18 PASS: test_open_status_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 18 FAIL: test_open_status_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 19: Verify khi click chọn giá trị 'Chờ xử lý' -> Hệ thống hiển thị giá trị 'Chờ xử lý' lên dropdown Trạng thái.
# def test_select_status_from_dropdown(article, select):
#     test_logger.info("Bắt đầu Test Case 19: Verify khi click chọn giá trị 'Chờ xử lý' -> Hệ thống hiển thị giá trị 'Chờ xử lý' lên dropdown Trạng thái.")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     article.click_tab_general_info()
#     select.click_status_dropdown()
#     select.select_status("Chờ xử lý")
#     expected_result = "Chờ xử lý"
#     result = select.is_status_selected("Chờ xử lý")
#     actual_result = expected_result if result else "Hệ thống không hiển thị giá trị 'Chờ xử lý' lên dropdown Trạng thái."
#     if result:
#         test_logger.info(f"Test Case 19 PASS: test_select_status_from_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 19 FAIL: test_select_status_from_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 20: Verify khi click dropdown Tag -> Hệ thống mở dropdown và hiển thị Danh sách tag.
# def test_open_tag_dropdown(article, tag):
#     test_logger.info("Bắt đầu Test Case 20: Verify khi click dropdown Tag -> Hệ thống mở dropdown và hiển thị Danh sách tag.")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     article.click_tab_general_info()
#     tag.click_tag_dropdown()
#     expected_result = "Hệ thống mở dropdown và hiển thị Danh sách tag."
#     result = tag.is_tag_dropdown_visible()
#     actual_result = expected_result if result else "Hệ thống không mở dropdown tag."
#     if result:
#         test_logger.info(f"Test Case 20 PASS: test_open_tag_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 20 FAIL: test_open_tag_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 21: Verify khi click nút Tạo mới -> Hệ thống hiển thị sidebar 'Thêm tag mới'.
# def test_create_keyword_sidebar(article, tag):
#     test_logger.info("Bắt đầu Test Case 21: Verify khi click nút Tạo mới -> Hệ thống hiển thị sidebar 'Thêm tag mới'.")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     article.click_tab_general_info()
#     tag.click_create_keyword_button()
#     expected_result = "Hệ thống hiển thị sidebar 'Thêm tag mới'."
#     result = tag.is_add_keyword_sidebar_visible()
#     actual_result = expected_result if result else "Hệ thống không hiển thị sidebar 'Thêm tag mới'."
#     if result:
#         test_logger.info(f"Test Case 21 PASS: test_create_keyword_sidebar | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 21 FAIL: test_create_keyword_sidebar | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 22: Verify khi không nhập Thứ tự sắp xếp -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Thứ tự sắp xếp'.
# def test_ordering_error_message(article, enter_field, validation):
#     test_logger.info("Bắt đầu Test Case 22: Verify khi không nhập Thứ tự sắp xếp -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Thứ tự sắp xếp'.")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     article.click_tab_general_info()
#     enter_field.ordering("")
#     article.click_save_button()
#     result = validation.is_ordering_error_displayed()
#     expected_result = "Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Thứ tự sắp xếp'."
#     actual_result = expected_result if result else "Hệ thống không hiển thị thông báo lỗi Vui lòng nhập Thứ tự sắp xếp"
#     if result:
#         test_logger.info(f"Test Case 22 PASS: test_ordering_error_message | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#         assert True
#     else:
#         test_logger.error(f"Test Case 22 FAIL: test_ordering_error_message | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 23: Verify khi nhập lại Thứ tự sắp xếp -> Hệ thống ẩn đi thông báo lỗi 'Vui lòng nhập Thứ tự sắp xếp'
# def test_ordering_error_disappears(article, enter_field, validation, select):
#     test_logger.info("Bắt đầu Test Case 23: Verify khi nhập lại Thứ tự sắp xếp -> Hệ thống ẩn đi thông báo lỗi 'Vui lòng nhập Thứ tự sắp xếp'.")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     article.click_tab_general_info()
#     enter_field.ordering("")
#     enter_field.ordering("2")
#     result = validation.is_ordering_error_displayed()
#     expected_result = "Hệ thống ẩn đi thông báo lỗi 'Vui lòng nhập Thứ tự sắp xếp'."
#     actual_result = expected_result if not result else "Hệ thống không ẩn đi thông báo lỗi 'Vui lòng nhập Thứ tự sắp xếp'."
#     if not result:
#         test_logger.info(f"Test Case 23 PASS: test_ordering_error_disappears | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#         assert True
#     else:
#         test_logger.error(f"Test Case 23 FAIL: test_ordering_error_disappears | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 24: Verify khi nhập Thứ tự sắp xếp > 7 số -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập không quá 7 số'.
# def test_ordering_max_length_error_message(article, enter_field, validation):
#     test_logger.info("Bắt đầu Test Case 24: Verify khi nhập Thứ tự sắp xếp > 7 số -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập không quá 7 số'.")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     article.click_tab_general_info()
#     enter_field.ordering("123456789")
#     result = validation.is_ordering_max_length_error_displayed()
#     expected_result = "Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập không quá 7 số'."
#     actual_result = expected_result if result else "Hệ thống không hiển thị thông báo lỗi 'Vui lòng nhập không quá 7 số'."
#     if result:
#         test_logger.info(f"Test Case 24 PASS: test_ordering_max_length_error_message | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#         assert True
#     else:
#         test_logger.error(f"Test Case 24 FAIL: test_ordering_max_length_error_message | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 25: Verify khi nhập số âm -> Hệ thống chấp nhận số âm và không hiển thị thông báo lỗi.
# def test_ordering_negative_number(article, enter_field, validation):
#     test_logger.info("Bắt đầu Test Case 25: Verify khi nhập số âm -> Hệ thống chấp nhận số âm và không hiển thị thông báo lỗi.")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     article.click_tab_general_info()
#     enter_field.ordering("-5")
#     error_message = validation.get_text(validation.locators.ORDERING_ERROR_MESSAGE)
#     result = error_message is None or error_message == ""
#     expected_result = "Hệ thống chấp nhận số âm và không hiển thị thông báo lỗi"
#     actual_result = expected_result if not result else "Hệ thống không chấp nhận số âm và không hiển thị thông báo lỗi"
#     if result:
#         test_logger.info(f"Test Case 25 PASS: test_ordering_negative_number | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#         assert True
#     else:
#         test_logger.error(f"Test Case 25 FAIL: test_ordering_negative_number | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 26: Verify khi nhập chữ -> Hệ thống không chấp nhận.
# def test_ordering_specific(article, enter_field, validation):
#     test_logger.info("Bắt đầu Test Case 26: Verify khi nhập chữ -> Hệ thống không chấp nhận ký tự chữ")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     article.click_tab_general_info()
#     enter_field.ordering("adcdfghtktgdadcdfght")
#     error_message = validation.get_text(validation.locators.ORDERING_ERROR_MESSAGE)
#     result = error_message is None or error_message == ""
#     expected_result = "Hệ thống không chấp nhận."
#     actual_result = expected_result if not result else "Hệ thống chấp nhận."
#     if result:
#         test_logger.info(f"Test Case 26 PASS: test_ordering_specific | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#         assert True
#     else:
#         test_logger.error(f"Test Case 26 FAIL: test_ordering_specific | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 27: Verify khi nhập ký tự đặc biệt -> Hệ thống không chấp nhận.
# def test_ordering_special_characters(article, enter_field, validation):
#     test_logger.info("Bắt đầu Test Case 27: Verify khi nhập ký tự đặc biệt -> Hệ thống không chấp nhận ký tự đặc biệt")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     article.click_tab_general_info()
#     enter_field.ordering("!@#$%^&*()")
#     error_message = validation.get_text(validation.locators.ORDERING_ERROR_MESSAGE)
#     result = error_message is None or error_message == ""
#     expected_result = "Hệ thống không chấp nhận."
#     actual_result = expected_result if not result else "Hệ thống chấp nhận."
#     if result:
#         test_logger.info(f"Test Case 27 PASS: test_ordering_special_characters | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#         assert True
#     else:
#         test_logger.error(f"Test Case 27 FAIL: test_ordering_special_characters | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 28: Verify khi click vào Ngày đăng -> Hệ thống hiển thị đúng ngày hiện tại.
# def test_public_date_default_value(article, date):
#     test_logger.info("Bắt đầu Test Case 28: Verify khi click vào Ngày đăng -> Hệ thống hiển thị đúng ngày hiện tại.")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     article.click_tab_general_info()
#     article.wait.until(EC.visibility_of_element_located(article.locators.PUBLIC_DATE)).click()
#     displayed_date = date.get_public_date()
#     expected_date = datetime.datetime.now().strftime("%Y-%m-%d")
#     if displayed_date == expected_date:
#         expected_result = "Ngày đăng hiển thị đúng ngày hiện tại"
#         actual_result = "Ngày đăng hiển thị đúng ngày hiện tại"
#         test_logger.info(f"Test Case 28 PASS: test_public_date_default_value | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#         assert True
#     else:
#         expected_result = f"Ngày đăng hiển thị đúng ngày hiện tại, mong đợi: {expected_date}"
#         actual_result = f"Ngày hiển thị là {displayed_date}, mong đợi {expected_date}"
#         test_logger.error(f"Test Case 28 FAIL: test_public_date_default_value | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 29: Verify khi nhập Ngày đăng -> Hệ thống chấp nhận và hiển thị Ngày đăng.
# def test_enter_past_public_date(article, date):
#     test_logger.info("Bắt đầu Test Case 29: Verify khi nhập Ngày đăng -> Hệ thống chấp nhận và hiển thị Ngày đăng.")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     article.click_tab_general_info()
#     past_date = (datetime.datetime.now() - datetime.timedelta(days=10)).strftime("%Y-%m-%d")
#     date.set_public_date(past_date)
#     displayed_date = date.get_public_date()
#     if displayed_date == past_date:
#         expected_result = "Hệ thống chấp nhận và hiển thị Ngày đăng."
#         actual_result = "Hệ thống chấp nhận và hiển thị Ngày đăng."
#         test_logger.info(f"Test Case 29 PASS: test_enter_past_public_date | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#         assert True
#     else:
#         expected_result = f"Hệ thống chấp nhận và hiển thị Ngày đăng. mong đợi: {past_date}"
#         actual_result = f"Ngày hiển thị là {displayed_date}, mong đợi {past_date}"
#         test_logger.error(f"Test Case 29 FAIL: test_enter_past_public_date | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 30: Verify trạng thái mặc định nút switch Nổi bật -> Hệ thống hiển thị trạng thái mặc định của nút switch Nổi bật là OFF.
# def test_featured_switch_initial_state(article, switch):
#     test_logger.info("Bắt đầu Test Case 30: Verify trạng thái mặc định nút switch Nổi bật -> Hệ thống hiển thị trạng thái mặc định của nút switch Nổi bật là OFF.")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     article.click_tab_general_info()
#     switch.reset_switch(LocatorArticle.FEATURED_SWITCH, LocatorArticle.FEATURED_LABEL)
#     result = switch.is_switch_on(LocatorArticle.FEATURED_SWITCH)
#     expected_result = "Hệ thống hiển thị trạng thái mặc định của nút switch Nổi bật là OFF"
#     actual_result = expected_result if not result else "Hệ thống hiển thị trạng thái mặc định của nút switch Nổi bật không phải là OFF"
#     if not result:
#         test_logger.info(f"Test Case 30 PASS: test_featured_switch_initial_state | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#         assert True
#     else:
#         test_logger.error(f"Test Case 30 FAIL: test_featured_switch_initial_state | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 31: Verify chuyển trạng thái nút switch Nổi bật từ OFF -> ON -> Hệ thống cập nhật đúng trạng thái
# def test_toggle_featured_switch_on(article, switch):
#     test_logger.info("Bắt đầu Test Case 31: Verify chuyển trạng thái nút switch Nổi bật từ OFF -> ON.")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     article.click_tab_general_info()
#     switch.reset_switch(LocatorArticle.FEATURED_SWITCH, LocatorArticle.FEATURED_LABEL)
#     switch.click_switch(LocatorArticle.FEATURED_LABEL)
#     result = switch.is_switch_on(LocatorArticle.FEATURED_SWITCH)
#     expected_result = "Trạng thái switch Nổi bật đã chuyển từ OFF sang ON"
#     actual_result = expected_result if not result else "Trạng thái switch Nổi bật đã chuyển sang ON"
#     if result:
#         test_logger.info(f"Test Case 31 PASS: test_toggle_featured_switch_on | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#         assert True
#     else:
#         test_logger.error(f"Test Case 31 FAIL: test_toggle_featured_switch_on | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 32: Verify chuyển trạng thái nút switch Nổi bật từ ON -> OFF -> Hệ thống cập nhật đúng trạng thái
# def test_toggle_featured_switch_off(article, switch):
#     test_logger.info("Bắt đầu Test Case 32: Verify chuyển trạng thái nút switch Nổi bật từ ON -> OFF")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     article.click_tab_general_info()
#     switch.reset_switch(LocatorArticle.FEATURED_SWITCH, LocatorArticle.FEATURED_LABEL)
#     switch.click_switch(LocatorArticle.FEATURED_LABEL)
#     switch.click_switch(LocatorArticle.FEATURED_LABEL)
#     result = switch.is_switch_on(LocatorArticle.FEATURED_SWITCH)
#     expected_result = "Trạng thái switch Nổi bật đã chuyển từ ON về OFF"
#     actual_result = expected_result if result else "Trạng thái switch Nổi bật đã chuyển về OFF"
#     if not result:
#         test_logger.info(f"Test Case 32 PASS: test_toggle_featured_switch_off | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#         assert True
#     else:
#         test_logger.error(f"Test Case 32 FAIL: test_toggle_featured_switch_off | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 33: Verify khi click field Hình ảnh thumbnail -> Hệ thống hiển thị pop-up Upload hình ảnh
# def test_upload_thumbnail_image_field(article, image):
#     test_logger.info("Bắt đầu Test Case 33: Verify khi click field Hình ảnh thumbnail -> Hệ thống hiển thị pop-up Upload hình ảnh")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     article.click_tab_general_info()
#     image.click_upload_thumbnail_image_field()
#     result = image.is_upload_popup_displayed()
#     expected_result = "Pop-up upload hình ảnh phải hiển thị sau khi click vào trường Hình ảnh thumbnail"
#     actual_result = expected_result if not result else "Pop-up upload hình ảnh hiển thị thành công"
#     if result:
#         test_logger.info(f"Test Case 33 PASS: test_upload_thumbnail_image_field | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#         assert True
#     else:
#         test_logger.error(f"Test Case 33 FAIL: test_upload_thumbnail_image_field | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 34: Verify khi click nút Tải lên ở Hình ảnh thumbnail -> Hệ thống hiển thị pop-up Upload hình ảnh
# def test_click_thumbnail_image_button(article, image):
#     test_logger.info("Bắt đầu Test Case 34: Verify khi click nút Tải lên ở Hình ảnh thumbnail -> Hệ thống hiển thị pop-up Upload hình ảnh")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     article.click_tab_general_info()
#     image.click_upload_thumbnail_image_button()
#     result = image.is_upload_popup_displayed()
#     expected_result = "Pop-up upload hình ảnh phải hiển thị sau khi click nút Tải lên ở trường Hình ảnh thumbnail"
#     actual_result = expected_result if not result else "Pop-up upload hình ảnh hiển thị thành công"
#     if result:
#         test_logger.info(f"Test Case 34 PASS: test_click_thumbnail_image_button | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#         assert True
#     else:
#         test_logger.error(f"Test Case 34 FAIL: test_click_thumbnail_image_button | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 35: Verify khi tải lên Hình ảnh Thumbnail -> Hệ thống hiển thị hình ảnh lên field Hình ảnh Thumbnail.
# def test_upload_thumbnail_image(article, image):
#     test_logger.info("Bắt đầu Test Case 35: Verify khi tải lên Hình ảnh Thumbnail -> Hệ thống hiển thị hình ảnh lên field Hình ảnh Thumbnail.")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     article.click_tab_general_info()
#     image.click_upload_thumbnail_image_field()
#     image.click_tab_browser_by_href()
#     image.wait_for_file_listing()
#     image.select_first_image()
#     image.click_choose_upload_button()
#     result = image.is_thumbnail_image_uploaded()
#     expected_result = "Hình ảnh phải được upload và hiển thị thành công trên field Hình ảnh Thumbnail."
#     actual_result = expected_result if not result else "Hình ảnh hiển thị thành công"
#     if result:
#         test_logger.info(f"Test Case 35 PASS: test_upload_thumbnail_image | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#         assert True
#     else:
#         test_logger.error(f"Test Case 35 FAIL: test_upload_thumbnail_image | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 36: Verify khi click nút Xóa ảnh -> Hệ thống xóa ảnh ra khỏi field Hình ảnh Thumbnail
# def test_delete_thumbnail_image(article, image):
#     test_logger.info("Bắt đầu Test Case 36: Verify khi click nút Xóa ảnh -> Hệ thống xóa ảnh ra khỏi field Hình ảnh Thumbnail")
#     article.perform_tag_operations()
#     article.click_create_new_button()
#     article.click_tab_general_info()
#     image.click_upload_thumbnail_image_field()
#     image.click_tab_browser_by_href()
#     image.wait_for_file_listing()
#     image.select_first_image()
#     image.click_choose_upload_button()
#     image.is_thumbnail_image_uploaded()
#     image.delete_thumbnail_image()
#     result = image.is_thumbnail_image_deleted()
#     expected_result = "Hình ảnh phải được xóa khỏi field Hình ảnh Thumbnail"
#     actual_result = expected_result if not result else "Hình ảnh đã bị xóa thành công"
#     if result:
#         test_logger.info(f"Test Case 36 PASS: test_delete_thumbnail_image | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#         assert True
#     else:
#         test_logger.error(f"Test Case 36 FAIL: test_delete_thumbnail_image | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

