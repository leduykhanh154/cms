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

# Test Case 1: Verify khi click menu 'Tất cả bài viết' -> Hệ thống chuyển hướng đến trang Danh sách bài viết 
def test_navigate_to_all_articles(article):
    test_logger.info("Bat dau Test Case 1: Verify khi click menu Tat ca bai viet -> He thong chuyen huong den trang Danh sach bai viet")
    article.click_content_menu()
    article.click_article_menu()
    expected_result = "He thong chuyen huong den trang Danh sach bai viet"
    result = article.click_all_article_menu()
    actual_result = expected_result if result else "He thong khong chuyen huong den trang Danh sach bai viet"
    if result:
        test_logger.info(f"Test Case 1 PASS: test_navigate_to_all_articles | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 1 FAIL: test_navigate_to_all_articles | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 2: Verify khi click nút 'Tạo mới' -> Hệ thống chuyển hướng đến trang Tạo mới bài viết 
def test_navigate_to_create_article(article):
    test_logger.info("Bat dau Test Case 2: Verify khi click nut Tao moi -> He thong chuyen huong den trang Tao moi bai viet")
    article.click_content_menu()
    article.click_article_menu()
    article.click_all_article_menu()
    expected_result = "He thong chuyen huong den trang Tao moi bai viet"
    result = article.click_create_new_button()
    actual_result = expected_result if result else "He thong khong chuyen huong den trang Tao moi bai viet"
    if result:
        test_logger.info(f"Test Case 2 PASS: test_navigate_to_create_article | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 2 FAIL: test_navigate_to_create_article | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 3: Verify khi không nhập Tiêu đề - Tiếng Việt -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Tiêu đề'
def test_empty_article_title_vi(article, enter_field, validation):
    test_logger.info("Bat dau Test Case 3: Verify khi khong nhap Tieu de - Tieng Viet -> He thong hien thi thong bao loi Vui long nhap Tieu de")
    article.perform_tag_operations()
    article.click_create_new_button()
    enter_field.enter_title_vi("")
    article.click_save_button()
    expected_result = "He thong hien thi thong bao loi Vui long nhap Tieu de"
    result = validation.is_title_vi_error_displayed()
    actual_result = expected_result if result else "He thong khong hien thi thong bao loi Vui long nhap Tieu de"
    if result:
        test_logger.info(f"Test Case 3 PASS: test_empty_article_title_vi | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 3 FAIL: test_empty_article_title_vi | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 4: Verify khi nhập Tiêu đề - Tiếng Việt -> Hệ thống ẩn đi thông báo lỗi 'Vui lòng nhập Tiêu đề'
def test_title_vi_error_disappears(article, enter_field, validation):
    test_logger.info("Bat dau Test Case 4: Verify khi nhap Tieu de - Tieng Viet -> He thong an di thong bao loi Vui long nhap Tieu de")
    article.perform_tag_operations()
    article.click_create_new_button()
    enter_field.enter_title_vi("")
    article.click_save_button()
    validation.is_title_vi_error_displayed()
    enter_field.enter_title_vi("Tiêu đề bài viết")
    expected_result = "He thong an di thong bao loi Vui long nhap Tieu de"
    result = not validation.is_title_vi_error_displayed()
    actual_result = expected_result if result else "He thong khong an di thong bao loi Vui long nhap Tieu de"
    if result:
        test_logger.info(f"Test Case 4 PASS: test_title_vi_error_disappears | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 4 FAIL: test_title_vi_error_disappears | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 5: Verify khi nhập Tiêu đề - Tiếng Việt hơn 250 ký tự -> Hệ thống hiển thị thông báo lỗi 'Tiêu đề không được vượt quá 250 ký tự'
def test_title_vi_max_length_error(article, enter_field, validation):
    test_logger.info("Bat dau Test Case 5: Verify khi nhap Tieu de - Tieng Viet hon 250 ky tu -> He thong hien thi thong bao loi Tieu de khong duoc vuot qua 250 ky tu")
    article.perform_tag_operations()
    article.click_create_new_button()
    long_title = "A" * 251
    enter_field.enter_title_vi(long_title)
    expected_result = "He thong hien thi thong bao loi Tieu de khong duoc vuot qua 250 ky tu"
    result = validation.is_title_vi_max_length_error_displayed()
    actual_result = expected_result if result else "He thong khong hien thi thong bao loi Tieu de khong duoc vuot qua 250 ky tu"
    if result:
        test_logger.info(f"Test Case 5 PASS: test_title_vi_max_length_error | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 5 FAIL: test_title_vi_max_length_error | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 6: Verify khi giảm số ký tự trong Tiêu đề - Tiếng Việt xuống <= 250 -> Hệ thống ẩn đi thông báo lỗi 'Tiêu đề không được vượt quá 250 ký tự'
def test_title_vi_max_length_error_disappears(article, enter_field, validation):
    test_logger.info("Bat dau Test Case 6: Verify khi giam so ky tu trong Tieu de - Tieng Viet xuong <= 250 -> He thong an thong bao loi Tieu de khong duoc vuot qua 250 ky tu")
    article.perform_tag_operations()
    article.click_create_new_button()
    long_title = "A" * 251
    enter_field.enter_title_vi(long_title)
    assert validation.is_title_vi_max_length_error_displayed(), "Error: Khong hien thi thong bao Tieu de khong duoc vuot qua 250 ky tu"
    short_title = "A" * 250
    enter_field.enter_title_vi(short_title)
    expected_result = "Thong bao loi bien mat sau khi giam so ky tu xuong <= 250"
    result = not validation.is_title_vi_max_length_error_displayed()
    actual_result = expected_result if result else "Thong bao loi van con du tieu de da giam xuong <= 250 ky tu"
    if result:
        test_logger.info(f"Test Case 6 PASS: test_title_vi_max_length_error_disappears | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 6 FAIL: test_title_vi_max_length_error_disappears | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 7: Verify khi nhập Mô tả ngắn - Tiếng Việt hơn 1000 ký tự -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Mô tả ngắn không quá 1000 ký tự'
def test_short_description_vi_max_length_error(article, enter_field, validation):
    test_logger.info("Bat dau Test Case 11: Verify khi nhap Mo ta ngan - Tieng Viet hon 1000 ky tu -> He thong hien thi thong bao loi Vui long nhap Mo ta ngan khong qua 1000 ky tu")
    article.perform_tag_operations()
    article.click_create_new_button()
    long_description = "A" * 1002
    enter_field.enter_short_description_vi(long_description)
    expected_result = "He thong hien thi thong bao loi Vui long nhap Mo ta ngan khong qua 1000 ky tu"
    result = validation.is_short_description_vi_max_length_error_displayed()
    actual_result = expected_result if result else "He thong khong hien thi thong bao loi khi Mo ta ngan qua 1000 ky tu"
    if result:
        test_logger.info(f"Test Case 7 PASS: test_short_description_vi_max_length_error | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 7 FAIL: test_short_description_vi_max_length_error | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 8: Verify khi nhập lại Mô tả ngắn - Tiếng Việt < 1000 ký tự -> Hệ thống ẩn đi thông báo lỗi 'Vui lòng nhập Mô tả ngắn không quá 1000 ký tự'
def test_short_description_vi_max_length_error_disappears(article, enter_field, validation):
    test_logger.info("Bat dau Test Case 12: Verify khi nhap lai Mo ta ngan - Tieng Viet < 1000 ky tu -> He thong an di thong bao loi 'Vui long nhap Mo ta ngan khong qua 1000 ky tu'")
    article.perform_tag_operations()
    article.click_create_new_button()
    long_description = "A" * 1002
    enter_field.enter_short_description_vi(long_description)
    assert validation.is_short_description_vi_max_length_error_displayed(), f"Lỗi: Không hiển thị thông báo khi mô tả ngắn vượt quá 1000 ký tự."
    valid_description = "A" * 999
    enter_field.enter_short_description_vi(valid_description)
    expected_result = "He thong an di thong bao loi 'Vui long nhap Mo ta ngan khong qua 1000 ky tu'"
    result = not validation.is_short_description_vi_max_length_error_displayed()
    actual_result = expected_result if result else "He thong van hien thi thong bao loi du da giam so ky tu"
    if result:
        test_logger.info(f"Test Case 8 PASS: test_short_description_vi_max_length_error_disappears | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 8 FAIL: test_short_description_vi_max_length_error_disappears | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
    
# Test Case 9: Verify khi không nhập Nội dung - Tiếng Việt -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Nội dung'
def test_empty_article_content_vi(article, enter_field, validation):
    test_logger.info("Bat dau Test Case 15: Verify khi khong nhap Noi dung - Tieng Viet -> He thong hien thi thong bao loi 'Vui long nhap Noi dung'")
    article.perform_tag_operations()
    article.click_create_new_button()
    enter_field.enter_title_vi("Tieu de bai viet")
    enter_field.enter_content_vi("")
    article.click_save_button()
    expected_result = "Vui long nhap Noi dung"
    result = validation.is_content_vi_error_displayed()
    actual_result = expected_result if result else "Khong hien thi thong bao loi"
    if result:
        test_logger.info(f"Test Case 9 PASS: test_empty_article_content_vi | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 9 FAIL: test_empty_article_content_vi | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 10: Verify khi nhập lại dữ liệu vào field Nội dung - Tiếng Việt -> Hệ thống ẩn đi thông báo lỗi 'Vui lòng nhập Nội dung'
def test_content_vi_error_disappears(article, enter_field, validation):
    test_logger.info("Bat dau Test Case 10: Verify khi nhap du lieu vao field Noi dung - Tieng Viet -> He thong an di thong bao loi 'Vui long nhap Noi dung'")
    article.perform_tag_operations()
    article.click_create_new_button()
    enter_field.enter_title_vi("Tieu de bai viet")
    enter_field.enter_content_vi("")
    article.click_save_button()
    validation.is_content_vi_error_displayed()
    enter_field.enter_content_vi("Noi dung bai viet")
    error_message_after_input = validation.is_content_vi_error_displayed()
    expected_result = "Thong bao loi Vui long nhap Noi dung bien mat"
    actual_result = expected_result if not error_message_after_input else "Thong bao loi Vui long nhap Noi dung van ton tai"
    if not error_message_after_input:
        test_logger.info(f"Test Case 10 PASS: test_content_vi_error_disappears | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 10 FAIL: test_content_vi_error_disappears | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 11: Verify khi không nhập Tiêu đề - Enlish -> Hệ thống hiển thị thống báo lỗi 'Vui lòng nhập Tiêu đề'
def test_empty_article_title_en(article, enter_field, validation):
    test_logger.info("Bat dau Test Case 11: Verify khi khong nhap Tieu de - English -> He thong hien thi thong bao loi 'Vui long nhap Tieu de'")
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_en_tab()
    article.click_translate_content_button()
    enter_field.enter_title_en("")
    article.click_save_button()
    expected_result = "Vui long nhap Tieu de"
    result = validation.is_title_en_error_displayed()
    actual_result = expected_result if result else "Khong hien thi thong bao loi"
    if result:
        test_logger.info(f"Test Case 11 PASS: test_empty_article_title_en | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 11 FAIL: test_empty_article_title_en | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 12: Verify khi nhập lại Tiêu đề - Enlish -> Hệ thống ẩn đi thông báo lỗi 'Vui lòng nhập Tiêu đề'
def test_title_en_error_disappears(article, enter_field, validation):
    test_logger.info("Bat dau Test Case 12: Verify khi nhap Tieu de - English -> He thong an di thong bao loi 'Vui long nhap Tieu de'")
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_en_tab()
    article.click_translate_content_button()
    enter_field.enter_title_en("")
    article.click_save_button()
    validation.is_title_en_error_displayed()
    enter_field.enter_title_en("Article Title")
    expected_result = "Thông báo lỗi biến mất"
    result = not validation.is_title_en_error_displayed()
    actual_result = expected_result if result else "Thông báo lỗi vẫn còn"
    if result:
        test_logger.info(f"Test Case 12 PASS: test_title_en_error_disappears | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 12 FAIL: test_title_en_error_disappears | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 13: Verify khi nhập Tiêu đề - Enlish hơn 250 ký tự -> Hệ thống hiển thị thông báo lỗi 'Tiêu đề không được vượt quá 250 ký tự'
def test_title_en_max_length_error(article, enter_field, validation):
    test_logger.info("Bat dau Test Case 12: Verify khi nhap Tieu de - English hon 250 ky tu -> He thong hien thi thong bao loi 'Tieu de khong duoc vuot qua 250 ky tu'")
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_en_tab()
    article.click_translate_content_button()
    long_title = "A" * 251
    enter_field.enter_title_en(long_title)
    article.click_save_button()
    expected_result = "Tiêu đề không được vượt quá 250 ký tự"
    result = validation.is_title_en_max_length_error_displayed()
    actual_result = expected_result if result else "Khong hien thi thong bao loi"
    if result:
        test_logger.info(f"Test Case 13 PASS: test_title_en_max_length_error | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 13 FAIL: test_title_en_max_length_error | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 14: Verify khi giảm số ký tự trong Tiêu đề - Enlish xuống <= 250 -> Hệ thống ẩn đi thông báo lỗi 'Vui lòng nhập Tiêu đề không quá 250 ký tự'
def test_title_en_max_length_error_disappears(article, enter_field, validation):
    test_logger.info("Bat dau Test Case 14: Verify khi giam so ky tu trong Tieu de - English xuong <= 250 -> He thong an di thong bao loi 'Vui long nhap Tieu de khong qua 250 ky tu'")
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_en_tab()
    article.click_translate_content_button()
    long_title = "A" * 251
    enter_field.enter_title_en(long_title)
    article.click_save_button()
    assert validation.is_title_en_max_length_error_displayed(), "Lỗi: Không hiển thị thông báo 'Vui lòng nhập Tiêu đề không quá 250 ký tự'"
    short_title = "A" * 250
    enter_field.enter_title_en(short_title)
    expected_result = "Thông báo lỗi biến mất"
    result = not validation.is_title_en_max_length_error_displayed()
    actual_result = expected_result if result else "Thông báo lỗi vẫn còn"
    if result:
        test_logger.info(f"Test Case 14 PASS: test_title_en_max_length_error_disappears | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 14 FAIL: test_title_en_max_length_error_disappears | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 15: Verify khi nhập Mô tả ngắn - English hơn 1000 ký tự -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Mô tả ngắn không quá 1000 ký tự' 
def test_short_description_en_max_length_error(article, enter_field, validation):
    test_logger.info("Bat dau Test Case 13: Verify khi nhap Mo ta ngan - English hon 1000 ky tu -> He thong hien thi thong bao loi 'Vui long nhap Mo ta ngan khong qua 1000 ky tu'")
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_en_tab()
    article.click_translate_content_button()
    long_description = "A" * 1002
    enter_field.enter_short_description_en(long_description)
    article.click_save_button()
    expected_result = "Vui lòng nhập Mô tả ngắn không quá 1000 ký tự"
    result = validation.is_short_description_en_max_lenght_error_displayed()
    actual_result = expected_result if result else "Khong hien thi thong bao loi"
    if result:
        test_logger.info(f"Test Case 15 PASS: test_short_description_en_max_length_error | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 15 FAIL: test_short_description_en_max_length_error | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 16: Verify khi nhập lại Mô tả ngắn - English < 1000 ký tự -> Hệ thống ẩn đi thông báo lỗi 'Vui lòng nhập Mô tả ngắn không quá 100 ký tự'
def test_short_description_en_max_length_error_disappears(article, enter_field, validation):
    test_logger.info("Bat dau Test Case 16: Verify khi giam so ky tu trong Mo ta ngan - English xuong <= 1000 -> He thong an di thong bao loi 'Vui long nhap Mo ta ngan khong qua 1000 ky tu'")
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_en_tab()
    article.click_translate_content_button()
    long_description = "A" * 1002
    enter_field.enter_short_description_en(long_description)
    article.click_save_button()
    assert validation.is_short_description_en_max_lenght_error_displayed(), "Lỗi: Không hiển thị thông báo 'Vui lòng nhập Mô tả ngắn không quá 1000 ký tự'"
    short_description = "A" * 999
    enter_field.enter_short_description_en(short_description)
    expected_result = "Thông báo lỗi biến mất"
    result = not validation.is_short_description_en_max_lenght_error_displayed()
    actual_result = expected_result if result else "Thông báo lỗi vẫn còn"
    if result:
        test_logger.info(f"Test Case 16 PASS: test_short_description_en_max_length_error_disappears | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 16 FAIL: test_short_description_en_max_length_error_disappears | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 17: Verify khi không nhập Nội dung - English -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Nội dung'
def test_empty_article_content_en(article, enter_field, validation):
    test_logger.info("Bat dau Test Case 14: Verify khi khong nhap Noi dung - English -> He thong hien thi thong bao loi 'Vui long nhap Noi dung'")
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_en_tab()
    article.click_translate_content_button()
    enter_field.enter_content_en("")
    article.click_save_button()
    expected_result = "Vui lòng nhập Nội dung"
    result = validation.is_content_en_error_displayed()
    actual_result = expected_result if result else "Không hiển thị thông báo lỗi"
    if result:
        test_logger.info(f"Test Case 17 PASS: test_empty_article_content_en | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 17 FAIL: test_empty_article_content_en | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 18: Verify nhập lại Nội dung - English -> Hệ thống ẩn đi thông báo lỗi Vui lòng nhập Nội dung
def test_content_vi_error_disappears(article, enter_field, validation):
    test_logger.info("Bat dau Test Case 18: Verify khi nhap du lieu vao field Noi dung - Tieng Viet -> He thong an di thong bao loi 'Vui long nhap Noi dung'")
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_en_tab()
    article.click_translate_content_button()
    enter_field.enter_title_en("Tieu de bai viet")
    enter_field.enter_content_en("")
    article.click_save_button()
    validation.is_content_en_error_displayed()
    enter_field.enter_content_en("Noi dung bai viet")
    error_message_after_input = validation.is_content_en_error_displayed()
    expected_result = "Thong bao loi Vui long nhap Noi dung bien mat"
    actual_result = expected_result if not error_message_after_input else "Thong bao loi Vui long nhap Noi dung van ton tai"
    if not error_message_after_input:
        test_logger.info(f"Test Case 18 PASS: test_content_vi_error_disappears | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 18 FAIL: test_content_vi_error_disappears | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 19: Verify khi không chọn 'Loại bài viết' -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Loại bài viết'
def test_article_type_error(article, enter_field, validation):
    test_logger.info("Bat dau Test Case 15: Verify khi khong chon 'Loai bai viet' -> He thong hien thi thong bao loi 'Vui long nhap Loai bai viet'")
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_save_button()
    article.click_tab_general_info()
    expected_result = "Vui long nhap Loai bai viet"
    result = validation.is_article_type_error_displayed()
    actual_result = expected_result if result else "Khong hien thi thong bao loi"
    if result:
        test_logger.info(f"Test Case 19 PASS: test_article_type_error | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 19 FAIL: test_article_type_error | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 20: Verify khi click vào dropdown 'Loại bài viết' -> Hệ thống mở dropdown 'Loại bài viết'
def test_open_article_type_dropdown(article, select):
    test_logger.info("Bat dau Test Case 20: Verify khi click vao dropdown 'Loai bai viet' -> He thong mo dropdown 'Loai bai viet'")
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_tab_general_info()
    select.click_select()
    expected_result = True
    result = select.is_dropdown_visible()
    actual_result = "Dropdown mở dropdown thành công" if result else "Hệ thống không mở dropdown"
    if result:
        test_logger.info(f"Test Case 20 PASS: test_open_article_type_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 20 FAIL: test_open_article_type_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 21: Verify khi chọn 'Loại bài viết' từ dropdown -> Hệ thống hiển thị đúng giá trị đã chọn và ẩn đi thông báo lỗi
def test_select_article_type_from_dropdown(article, select):
    test_logger.info("Bat dau Test Case 17: Verify khi chon 'Loai bai viet' tu dropdown -> He thong hien thi dung gia tri da chon va an di thong bao loi")
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_tab_general_info()
    select.click_select()
    select.select_article_type("Tin tức chuyên ngành")
    expected_result = "Tin tức chuyên ngành"
    result = select.is_selected_article_type_displayed(expected_result)
    actual_result = expected_result if result else "Loại bài viết không hiển thị đúng"
    if result:
        test_logger.info(f"Test Case 21 PASS: test_select_article_type_from_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 21 FAIL: test_select_article_type_from_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 22: Verify khi click vào dropdown 'Trạng thái' -> Hệ thống mở dropdown 'Trạng thái'
def test_open_status_dropdown(article, select):
    test_logger.info("Bắt đầu Test Case 22: Verify khi click dropdwon Trạng thái -> Hệ thống mở dropdown Trạng thái.")
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_tab_general_info()
    select.click_status_dropdown()
    expected_result = "Hệ thống mở dropdown Trạng thái"
    result = select.is_status_dropdown_visible()
    actual_result = expected_result if result else "Hệ thống không mở dropdown Trạng thái"
    if result:
        test_logger.info(f"Test Case 22 PASS: test_open_status_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 22 FAIL: test_open_status_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 23: Verify khi click chọn giá trị Chờ xử lý -> Hệ thống hiển thị giá trị chờ xử lý lên dropdown Trạng thái
def test_select_status_from_dropdown(article, select):
    test_logger.info("Bắt đầu Test Case 23: Verify khi click chọn giá trị 'Chờ xử lý' -> Hệ thống hiển thị giá trị 'Chờ xử lý' lên dropdown 'Trạng thái'")
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_tab_general_info()
    select.click_status_dropdown()
    select.select_status("Chờ xử lý")
    expected_result = "Chờ xử lý"
    result = select.is_status_selected("Chờ xử lý")
    actual_result = expected_result if result else "Trạng thái không hiển thị đúng"
    if result:
        test_logger.info(f"Test Case 23 PASS: test_select_status_from_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 23 FAIL: test_select_status_from_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 24: Verify khi click dropdown Tag -> Hệ thống mở dropdown và hiển thị Danh sách tag
def test_open_tag_dropdown(article, tag):
    test_logger.info("Bắt đầu Test Case 24: Verify khi click dropdown 'Tag' -> Hệ thống mở dropdown và hiển thị Danh sách tag")
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_tab_general_info()
    tag.click_tag_dropdown()
    result = tag.is_tag_dropdown_visible()
    expected_result = True
    actual_result = "Hệ thống mở dropdown và hiển thị danh sách tag" if result else "Hệ thống không mở dropdown và không hiển thị danh sách tag"
    if result:
        test_logger.info(f"Test Case 24 PASS: test_open_tag_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 24 FAIL: test_open_tag_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 25: Verify khi click nút Tạo mới -> Hệ thống hiển thị sidebar Thêm tag mới
def test_create_keyword_sidebar(article, tag):
    test_logger.info("Bắt đầu Test Case 25: Verify khi click nút 'Tạo mới' -> Hệ thống hiển thị sidebar 'Thêm tag mới'")
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_tab_general_info()
    tag.click_create_keyword_button()
    result = tag.is_add_keyword_sidebar_visible()
    expected_result = True
    actual_result = "Hệ thống hiển thị sidebar 'Thêm tag mới'" if result else "Hệ thống không hiển thị sidebar 'Thêm tag mới'"
    if result:
        test_logger.info(f"Test Case 25 PASS: test_create_keyword_sidebar | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 25 FAIL: test_create_keyword_sidebar | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 26: Verify khi không nhập Thứ tự sắp xếp -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Thứ tự sắp xếp'
def test_ordering_error_message(article, enter_field, validation, select):
    test_logger.info("Bắt đầu Test Case 27: Verify khi không nhập Thứ tự sắp xếp -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Thứ tự sắp xếp'")
    article.perform_tag_operations()
    article.click_create_new_button()
    enter_field.enter_title_vi("Tiêu đề bài viết")
    enter_field.enter_short_description_vi("Mô tả ngắn bài viết")
    enter_field.enter_content_vi("Nội dung bài viết")
    article.click_tab_general_info()
    select.click_select()
    select.select_article_type("Tin tức chuyên ngành")
    enter_field.ordering("")
    article.click_save_button()
    result = validation.is_ordering_error_displayed()
    expected_result = "Hệ thống hiển thị thông báo lỗi Vui lòng nhập Thứ tự sắp xếp"
    actual_result = "Hệ thống hiển thị lỗi 'Vui lòng nhập Thứ tự sắp xếp'" if result else "Hệ thống không hiển thị thông báo lỗi Vui lòng nhập Thứ tự sắp xếp"
    if result:
        test_logger.info(f"Test Case 26 PASS: test_ordering_error_message | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
        assert True
    else:
        test_logger.error(f"Test Case 26 FAIL: test_ordering_error_message | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 27: Verify khi nhập lại Thứ tự sắp xếp -> Hệ thống ẩn đi thông báo lỗi 'Vui lòng nhập Thứ tự sắp xếp'
def test_ordering_error_disappears(article, enter_field, validation, select):
    test_logger.info("Bắt đầu Test Case 27: Verify khi nhập lại Thứ tự sắp xếp -> Hệ thống ẩn đi thông báo lỗi 'Vui lòng nhập Thứ tự sắp xếp'")
    article.perform_tag_operations()
    article.click_create_new_button()
    enter_field.enter_title_vi("Tiêu đề bài viết")
    enter_field.enter_short_description_vi("Mô tả ngắn bài viết")
    enter_field.enter_content_vi("Nội dung bài viết")
    article.click_tab_general_info()
    select.click_select()
    select.select_article_type("Tin tức chuyên ngành")
    enter_field.ordering("")
    enter_field.ordering("2")
    result = validation.is_ordering_error_displayed()
    expected_result = "Thông báo lỗi bị ấn sau khi nhập lại Thứ tự sắp xếp"
    actual_result = "Thông báo lỗi bị ẩn sau khi nhập Thứ tự sắp xếp" if not result else "Thông báo lỗi vẫn còn sau khi nhập Thứ tự sắp xếp"
    if not result:
        test_logger.info(f"Test Case 27 PASS: test_ordering_error_disappears | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
        assert True
    else:
        test_logger.error(f"Test Case 27 FAIL: test_ordering_error_disappears | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 28: Verify khi nhập Thứ tự sắp xếp > 7 số -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập không quá 7 số'
def test_ordering_max_length_error_message(article, enter_field, validation, select):
    test_logger.info("Bắt đầu Test Case 28: Verify khi nhập Thứ tự sắp xếp > 7 số -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập không quá 7 số'")
    article.perform_tag_operations()
    article.click_create_new_button()
    enter_field.enter_title_vi("Tiêu đề bài viết")
    enter_field.enter_short_description_vi("Mô tả ngắn bài viết")
    enter_field.enter_content_vi("Nội dung bài viết")
    article.click_tab_general_info()
    select.click_select()
    select.select_article_type("Tin tức chuyên ngành")
    enter_field.ordering("123456789")
    result = validation.is_ordering_max_length_error_displayed()
    expected_result = "Hệ thống hiển thị thông báo lỗi Vui lòng không nhập quá 7 số"
    actual_result = "Hệ thống không hiển thị thông báo lỗi khi nhập quá 7 số" if result else "Hệ thống không hiển thị thông báo lỗi"
    if result:
        test_logger.info(f"Test Case 28 PASS: test_ordering_max_length_error_message | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
        assert True
    else:
        test_logger.error(f"Test Case 28 FAIL: test_ordering_max_length_error_message | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 29: Verify khi nhập chữ -> Hệ thống không chấp nhận
def test_ordering_specific(article, enter_field, validation, select):
    test_logger.info("Bắt đầu Test Case 29: Verify khi nhập chữ -> Hệ thống không chấp nhận ký tự chữ")
    article.perform_tag_operations()
    article.click_create_new_button()
    enter_field.enter_title_vi("Tiêu đề bài viết")
    enter_field.enter_short_description_vi("Mô tả ngắn bài viết")
    enter_field.enter_content_vi("Nội dung bài viết")
    article.click_tab_general_info()
    select.click_select()
    select.select_article_type("Tin tức chuyên ngành")
    enter_field.ordering("adcdfghtktgdadcdfght")
    error_message = validation.get_text(validation.locators.ORDERING_ERROR_MESSAGE)
    result = error_message is None or error_message == ""
    expected_result = "Hệ thống không chấp nhận ký tự chữ và không hiển thị thông báo lỗi"
    actual_result = "Thông báo lỗi vẫn còn" if not result else "Thông báo lỗi bị ẩn"
    if result:
        test_logger.info(f"Test Case 29 PASS: test_ordering_specific | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
        assert True
    else:
        test_logger.error(f"Test Case 29 FAIL: test_ordering_specific | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 30: Verify khi nhập số âm -> Hệ thống vẫn chấp nhận
def test_ordering_negative_number(article, enter_field, validation, select):
    test_logger.info("Bắt đầu Test Case 30: Verify khi nhập số âm -> Hệ thống vẫn chấp nhận")
    article.perform_tag_operations()
    article.click_create_new_button()
    enter_field.enter_title_vi("Tiêu đề bài viết")
    enter_field.enter_short_description_vi("Mô tả ngắn bài viết")
    enter_field.enter_content_vi("Nội dung bài viết")
    article.click_tab_general_info()
    select.click_select()
    select.select_article_type("Tin tức chuyên ngành")
    enter_field.ordering("-5")
    error_message = validation.get_text(validation.locators.ORDERING_ERROR_MESSAGE)
    result = error_message is None or error_message == ""
    expected_result = "Hệ thống chấp nhận số âm và không hiển thị thông báo lỗi"
    actual_result = "Thông báo lỗi hiển thị" if not result else "Không hiển thị thông báo lỗi"
    if result:
        test_logger.info(f"Test Case 30 PASS: test_ordering_negative_number | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
        assert True
    else:
        test_logger.error(f"Test Case 30 FAIL: test_ordering_negative_number | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 31: Verify giá trị mặc định của ngày đăng -> Hệ thống hiển thị đúng ngày hiện tại
def test_public_date_default_value(article, date):
    test_logger.info("Bắt đầu Test Case 31: Verify giá trị mặc định của ngày đăng -> Hệ thống hiển thị đúng ngày hiện tại")
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_tab_general_info()
    article.wait.until(EC.visibility_of_element_located(article.locators.PUBLIC_DATE)).click()
    displayed_date = date.get_public_date()
    expected_date = datetime.datetime.now().strftime("%Y-%m-%d")
    if displayed_date == expected_date:
        expected_result = "Ngày đăng hiển thị đúng ngày hiện tại"
        actual_result = "Ngày đăng hiển thị đúng ngày hiện tại"
        test_logger.info(f"Test Case 31 PASS: test_public_date_default_value | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
        assert True
    else:
        expected_result = f"Ngày đăng hiển thị đúng ngày hiện tại, mong đợi: {expected_date}"
        actual_result = f"Ngày hiển thị là {displayed_date}, mong đợi {expected_date}"
        test_logger.error(f"Test Case 31 FAIL: test_public_date_default_value | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 32: Verify khi nhập ngày quá khứ -> Hệ thống chấp nhận ngày đăng là ngày quá khứ
def test_enter_past_public_date(article, date):
    test_logger.info("Bắt đầu Test Case 32: Verify khi nhập ngày quá khứ -> Hệ thống chấp nhận ngày đăng là ngày quá khứ")
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_tab_general_info()
    past_date = (datetime.datetime.now() - datetime.timedelta(days=10)).strftime("%Y-%m-%d")
    date.set_public_date(past_date)
    displayed_date = date.get_public_date()
    if displayed_date == past_date:
        expected_result = "Ngày đăng hiển thị đúng ngày quá khứ"
        actual_result = "Ngày đăng hiển thị đúng ngày quá khứ"
        test_logger.info(f"Test Case 32 PASS: test_enter_past_public_date | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
        assert True
    else:
        expected_result = f"Ngày đăng hiển thị đúng ngày quá khứ, mong đợi: {past_date}"
        actual_result = f"Ngày hiển thị là {displayed_date}, mong đợi {past_date}"
        test_logger.error(f"Test Case 32 FAIL: test_enter_past_public_date | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 33: Verify khi nhập ngày tương lai -> Hệ thống chấp nhận ngày đăng là ngày tương lai
def test_enter_future_public_date(article, enter_field, date):
    test_logger.info("Bắt đầu Test Case 33: Verify khi nhập ngày tương lai -> Hệ thống chấp nhận ngày đăng là ngày tương lai")
    article.perform_tag_operations()
    article.click_create_new_button()
    enter_field.enter_title_vi("Tiêu đề bài viết")
    enter_field.enter_short_description_vi("Mô tả ngắn bài viết")
    enter_field.enter_content_vi("Nội dung bài viết")
    article.click_tab_general_info()
    future_date = (datetime.datetime.now() + datetime.timedelta(days=10)).strftime("%Y-%m-%d")
    date.set_public_date(future_date)
    displayed_date = date.get_public_date()
    if displayed_date == future_date:
        expected_result = "Ngày đăng hiển thị đúng ngày tương lai"
        actual_result = "Ngày đăng hiển thị đúng ngày tương lai"
        test_logger.info(f"Test Case 33 PASS: test_enter_future_public_date | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
        assert True
    else:
        expected_result = f"Ngày đăng hiển thị đúng ngày tương lai, mong đợi: {future_date}"
        actual_result = f"Ngày hiển thị là {displayed_date}, mong đợi {future_date}"
        test_logger.error(f"Test Case 33 FAIL: test_enter_future_public_date | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 34: Verify trạng thái mặc định nút switch Nổi bật là OFF
def test_featured_switch_initial_state(article, enter_field, switch):
    test_logger.info("Bắt đầu Test Case 34: Verify trạng thái mặc định nút switch Nổi bật là OFF")
    article.perform_tag_operations()
    article.click_create_new_button()
    enter_field.enter_title_vi("Tiêu đề bài viết")
    enter_field.enter_short_description_vi("Mô tả ngắn bài viết")
    enter_field.enter_content_vi("Nội dung bài viết")
    article.click_tab_general_info()
    switch.reset_switch(LocatorArticle.FEATURED_SWITCH, LocatorArticle.FEATURED_LABEL)
    result = switch.is_switch_on(LocatorArticle.FEATURED_SWITCH)
    expected_result = "Trạng thái ban đầu của switch là OFF"
    actual_result = "Trạng thái ban đầu của switch là OFF" if not result else "Trạng thái ban đầu của switch là ON"
    if not result:
        test_logger.info(f"Test Case 34 PASS: test_featured_switch_initial_state | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
        assert True
    else:
        test_logger.error(f"Test Case 34 FAIL: test_featured_switch_initial_state | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 35: Verify chuyển trạng thái nút switch Nổi bật từ OFF -> ON
def test_toggle_featured_switch_on(article, enter_field, switch):
    test_logger.info("Bắt đầu Test Case 35: Verify chuyển trạng thái nút switch Nổi bật từ OFF -> ON")
    article.perform_tag_operations()
    article.click_create_new_button()
    enter_field.enter_title_vi("Tiêu đề bài viết")
    enter_field.enter_short_description_vi("Mô tả ngắn bài viết")
    enter_field.enter_content_vi("Nội dung bài viết")
    article.click_tab_general_info()
    switch.reset_switch(LocatorArticle.FEATURED_SWITCH, LocatorArticle.FEATURED_LABEL)
    switch.click_switch(LocatorArticle.FEATURED_LABEL)
    result = switch.is_switch_on(LocatorArticle.FEATURED_SWITCH)
    expected_result = "Trạng thái switch Nổi bật đã chuyển từ OFF sang ON"
    actual_result = "Trạng thái switch Nổi bật vẫn là OFF" if not result else "Trạng thái switch Nổi bật đã chuyển sang ON"
    if result:
        test_logger.info(f"Test Case 35 PASS: test_toggle_featured_switch_on | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
        assert True
    else:
        test_logger.error(f"Test Case 35 FAIL: test_toggle_featured_switch_on | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 36: Verify chuyển trạng thái nút switch Nổi bật từ ON -> OFF
def test_toggle_featured_switch_off(article, enter_field, switch):
    test_logger.info("Bắt đầu Test Case 36: Verify chuyển trạng thái nút switch Nổi bật từ ON -> OFF")
    article.perform_tag_operations()
    article.click_create_new_button()
    enter_field.enter_title_vi("Tiêu đề bài viết")
    enter_field.enter_short_description_vi("Mô tả ngắn bài viết")
    enter_field.enter_content_vi("Nội dung bài viết")
    article.click_tab_general_info()
    switch.reset_switch(LocatorArticle.FEATURED_SWITCH, LocatorArticle.FEATURED_LABEL)
    switch.click_switch(LocatorArticle.FEATURED_LABEL)
    switch.click_switch(LocatorArticle.FEATURED_LABEL)
    result = switch.is_switch_on(LocatorArticle.FEATURED_SWITCH)
    expected_result = "Trạng thái switch Nổi bật đã chuyển từ ON về OFF"
    actual_result = "Trạng thái switch Nổi bật vẫn là ON" if result else "Trạng thái switch Nổi bật đã chuyển về OFF"
    if not result:
        test_logger.info(f"Test Case 36 PASS: test_toggle_featured_switch_off | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
        assert True
    else:
        test_logger.error(f"Test Case 36 FAIL: test_toggle_featured_switch_off | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 37: Verify khi chuyển trạng thái nút switch Đặt làm trang chủ từ OFF -> ON
def test_toggle_homepage_switch_on(article, enter_field, switch):
    test_logger.info("Bắt đầu Test Case 37: Verify khi chuyển trạng thái nút switch Đặt làm trang chủ từ OFF -> ON")
    article.perform_tag_operations()
    article.click_create_new_button()
    enter_field.enter_title_vi("Tiêu đề bài viết")
    enter_field.enter_short_description_vi("Mô tả ngắn bài viết")
    enter_field.enter_content_vi("Nội dung bài viết")
    article.click_tab_general_info()
    switch.reset_switch(LocatorArticle.HOMEPAGE_SWITCH, LocatorArticle.HOMEPAGE_LABEL)
    switch.click_switch(LocatorArticle.HOMEPAGE_LABEL)
    result = switch.is_switch_on(LocatorArticle.HOMEPAGE_SWITCH)
    expected_result = "Trạng thái switch Đặt làm trang chủ phải là ON"
    actual_result = "Trạng thái switch Đặt làm trang chủ không thay đổi thành ON" if not result else "Trạng thái switch Đặt làm trang chủ đã chuyển sang ON"
    if result:
        test_logger.info(f"Test Case 37 PASS: test_toggle_homepage_switch_on | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
        assert True
    else:
        test_logger.error(f"Test Case 37 FAIL: test_toggle_homepage_switch_on | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 38: Verify khi chuyển trạng thái nút switch Đặt làm trang chủ từ OFF -> ON
def test_toggle_homepage_switch_on(article, enter_field, switch):
    test_logger.info("Bắt đầu Test Case 38: Verify khi chuyển trạng thái nút switch Đặt làm trang chủ từ OFF -> ON")
    article.perform_tag_operations()
    article.click_create_new_button()
    enter_field.enter_title_vi("Tiêu đề bài viết")
    enter_field.enter_short_description_vi("Mô tả ngắn bài viết")
    enter_field.enter_content_vi("Nội dung bài viết")
    article.click_tab_general_info()
    switch.reset_switch(LocatorArticle.HOMEPAGE_SWITCH, LocatorArticle.HOMEPAGE_LABEL)
    switch.click_switch(LocatorArticle.HOMEPAGE_LABEL)
    result = switch.is_switch_on(LocatorArticle.HOMEPAGE_SWITCH)
    expected_result = "Trạng thái switch Đặt làm trang chủ phải là ON"
    actual_result = "Trạng thái switch Đặt làm trang chủ không thay đổi thành ON" if not result else "Trạng thái switch Đặt làm trang chủ đã chuyển sang ON"
    if result:
        test_logger.info(f"Test Case 38 PASS: test_toggle_homepage_switch_on | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
        assert True
    else:
        test_logger.error(f"Test Case 38 FAIL: test_toggle_homepage_switch_on | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 39: Verify khi chuyển trạng thái nút switch Đặt làm trang chủ từ OFF -> ON
def test_toggle_homepage_switch_on(article, enter_field, switch):
    test_logger.info("Bắt đầu Test Case 39: Verify khi chuyển trạng thái nút switch Đặt làm trang chủ từ OFF -> ON")
    article.perform_tag_operations()
    article.click_create_new_button()
    enter_field.enter_title_vi("Tiêu đề bài viết")
    enter_field.enter_short_description_vi("Mô tả ngắn bài viết")
    enter_field.enter_content_vi("Nội dung bài viết")
    article.click_tab_general_info()
    switch.reset_switch(LocatorArticle.HOMEPAGE_SWITCH, LocatorArticle.HOMEPAGE_LABEL)
    switch.click_switch(LocatorArticle.HOMEPAGE_LABEL)
    result = switch.is_switch_on(LocatorArticle.HOMEPAGE_SWITCH)
    expected_result = "Trạng thái switch Đặt làm trang chủ phải là ON"
    actual_result = "Trạng thái switch Đặt làm trang chủ không thay đổi thành ON" if not result else "Trạng thái switch Đặt làm trang chủ đã chuyển sang ON"
    if result:
        test_logger.info(f"Test Case 39 PASS: test_toggle_homepage_switch_on | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
        assert True
    else:
        test_logger.error(f"Test Case 39 FAIL: test_toggle_homepage_switch_on | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 40: Verify khi chuyển trạng thái nút switch Đặt làm trang chủ từ ON -> OFF
def test_toggle_homepage_switch_off(article, enter_field, switch):
    test_logger.info("Bắt đầu Test Case 40: Verify khi chuyển trạng thái nút switch Đặt làm trang chủ từ ON -> OFF")
    article.perform_tag_operations()
    article.click_create_new_button()
    enter_field.enter_title_vi("Tiêu đề bài viết")
    enter_field.enter_short_description_vi("Mô tả ngắn bài viết")
    enter_field.enter_content_vi("Nội dung bài viết")
    article.click_tab_general_info()
    switch.reset_switch(LocatorArticle.HOMEPAGE_SWITCH, LocatorArticle.HOMEPAGE_LABEL)
    switch.click_switch(LocatorArticle.HOMEPAGE_LABEL)
    switch.click_switch(LocatorArticle.HOMEPAGE_LABEL)
    result = switch.is_switch_on(LocatorArticle.HOMEPAGE_SWITCH)
    expected_result = "Trạng thái switch Đặt làm trang chủ phải là OFF"
    actual_result = "Trạng thái switch Đặt làm trang chủ không thay đổi thành OFF" if result else "Trạng thái switch Đặt làm trang chủ đã chuyển sang OFF"
    if not result:
        test_logger.info(f"Test Case 40 PASS: test_toggle_homepage_switch_off | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
        assert True
    else:
        test_logger.error(f"Test Case 40 FAIL: test_toggle_homepage_switch_off | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 32: Verify khi click field Hình ảnh thumbnail -> Hệ thống hiển thị pop-up Upload hình ảnh
def test_upload_thumbnail_image_field(article, image):
    test_logger.info("Bắt đầu Test Case 32: Verify khi click field Hình ảnh thumbnail -> Hệ thống hiển thị pop-up Upload hình ảnh")
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_tab_general_info()
    image.click_upload_thumbnail_image_field()
    result = image.is_upload_popup_displayed()
    expected_result = "Pop-up upload hình ảnh phải hiển thị sau khi click vào trường Hình ảnh thumbnail"
    actual_result = expected_result if not result else "Pop-up upload hình ảnh hiển thị thành công"
    if result:
        test_logger.info(f"Test Case 32 PASS: test_upload_thumbnail_image_field | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
        assert True
    else:
        test_logger.error(f"Test Case 32 FAIL: test_upload_thumbnail_image_field | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 42: Verify khi click nút Tải lên ở Hình ảnh thumbnail -> Hệ thống hiển thị pop-up Upload hình ảnh
def test_click_thumbnail_image_button(article, image):
    test_logger.info("Bắt đầu Test Case 42: Verify khi click nút Tải lên ở Hình ảnh thumbnail -> Hệ thống hiển thị pop-up Upload hình ảnh")
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_tab_general_info()
    image.click_upload_thumbnail_image_button()
    result = image.is_upload_popup_displayed()
    expected_result = "Pop-up upload hình ảnh phải hiển thị sau khi click nút Tải lên ở trường Hình ảnh thumbnail"
    actual_result = "Pop-up upload hình ảnh không hiển thị" if not result else "Pop-up upload hình ảnh hiển thị thành công"
    if result:
        test_logger.info(f"Test Case 42 PASS: test_click_thumbnail_image_button | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
        assert True
    else:
        test_logger.error(f"Test Case 42 FAIL: test_click_thumbnail_image_button | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"


# Test Case 46: Verify khi tải lên Hình ảnh Thumbnail -> Hệ thống hiển thị hình ảnh lên field Hình ảnh Thumbnail
def test_upload_thumbnail_image(article, image):
    test_logger.info("Bắt đầu Test Case 46: Verify khi tải lên Hình ảnh Thumbnail -> Hệ thống hiển thị hình ảnh lên field Hình ảnh Thumbnail")
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_tab_general_info()
    image.click_upload_thumbnail_image_field()
    image.click_tab_browser_by_href()
    image.wait_for_file_listing()
    image.select_first_image()
    image.click_choose_upload_button()
    result = image.is_thumbnail_image_uploaded()
    expected_result = "Hình ảnh phải được upload và hiển thị thành công trên field Hình ảnh Thumbnail"
    actual_result = "Hình ảnh không hiển thị trên field Hình ảnh Thumbnail" if not result else "Hình ảnh hiển thị thành công"
    if result:
        test_logger.info(f"Test Case 46 PASS: test_upload_thumbnail_image | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
        assert True
    else:
        test_logger.error(f"Test Case 46 FAIL: test_upload_thumbnail_image | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"


# Test Case 47: Verify khi click nút Xóa ảnh -> Hệ thống xóa ảnh ra khỏi field Hình ảnh Thumbnail
def test_delete_thumbnail_image(article, image):
    test_logger.info("Bắt đầu Test Case 47: Verify khi click nút Xóa ảnh -> Hệ thống xóa ảnh ra khỏi field Hình ảnh Thumbnail")
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_tab_general_info()
    image.click_upload_thumbnail_image_field()
    image.click_tab_browser_by_href()
    image.wait_for_file_listing()
    image.select_first_image()
    image.click_choose_upload_button()
    if not image.is_thumbnail_image_uploaded():
        test_logger.error("Test Case 47 FAIL: Hình ảnh không hiển thị sau khi tải lên.")
        assert False, "Test Case 47 FAIL: Hình ảnh không hiển thị sau khi tải lên."
    image.delete_thumbnail_image()
    result = image.is_thumbnail_image_deleted()
    expected_result = "Hình ảnh phải được xóa khỏi field Hình ảnh Thumbnail"
    actual_result = "Hình ảnh vẫn còn trong field Hình ảnh Thumbnail" if not result else "Hình ảnh đã bị xóa thành công"
    if result:
        test_logger.info(f"Test Case 47 PASS: test_delete_thumbnail_image | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
        assert True
    else:
        test_logger.error(f"Test Case 47 FAIL: test_delete_thumbnail_image | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

