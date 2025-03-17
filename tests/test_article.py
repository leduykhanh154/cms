import time
import pytest
import logging
import datetime
from utils.login import Login
from utils.driver_setup import get_driver
from pages.articles.article import Article
from pages.articles.select import SelectArticle
from pages.articles.enterfield import EnterFieldArticle
from pages.articles.validation import ArticleValidation
from selenium.webdriver.support import expected_conditions as EC

test_logger = logging.getLogger("test_logger")
test_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("reports/test_results.log", mode="w")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
test_logger.addHandler(file_handler)

@pytest.fixture(scope="function")
def setup_driver():
    driver = get_driver()
    try:
        login_page = Login(driver)
        if not login_page.login():
            pytest.fail("Không thể đăng nhập!")
        yield driver
    finally:
        time.sleep(5)
        driver.quit()

@pytest.fixture
def article(setup_driver):
    return Article(setup_driver)

@pytest.fixture
def validation(setup_driver):
    return ArticleValidation(setup_driver)

@pytest.fixture
def enter_field(setup_driver):
    return EnterFieldArticle(setup_driver)

@pytest.fixture
def select(setup_driver):
    return SelectArticle(setup_driver)



# Test Case 28: Verify khi nhập Thứ tự sắp xếp > 7 số -> Hệ thống hiển thị thông báo lỗi Vui lòng nhập không quá 7 số
def test_ordering_max_lenght_error_message(article, enter_field, validation, select):
    article.perform_tag_operations()
    article.click_create_new_button()
    enter_field.enter_title_vi("Tiêu đề bài viết")
    enter_field.enter_short_description_vi("Mô tả ngắn bài viết")
    enter_field.enter_content_vi("Nội dung bài viết")
    article.click_tab_general_info()
    select.click_select()
    select.select_article_type("Tin tức chuyên ngành")
    enter_field.ordering("123456789")
    if validation.is_ordering_max_lenght_error_displayed():
        logging.info("Test Case 17 PASS: Hệ thống hiển thị thông báo lỗi ")
    else:
        logging.error("Test Case 17 FAIL: Hệ thống KHÔNG hiển thị lỗi khi Thứ tự sắp xếp trống!")
        assert False, "Lỗi: Không hiển thị thông báo 'Vui lòng nhập Thứ tự sắp xếp'."

# Test Case 18: Verify khi nhập chữ -> Hệ thống không chấp nhận
def test_ordering_specific(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.enter_title("Bài viết kiểm thử")
    article.enter_content("Đây là nội dung bài viết test")
    article.click_tab_general_info()
    article.click_select()
    article.select_article_type("Tin tức chuyên ngành")
    article.ordering("adcdfghtktgdadcdfght")
    error_message = article.get_text(article.locators.ORDERING_ERROR_MESSAGE)
    assert error_message is None or error_message == "", "Test Case FAIL: Hệ thống chấp nhận ký tự chữ!"
    logging.info("Test Case PASS: Hệ thống không chấp nhận ký tự chữ!")