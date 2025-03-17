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

# Test Case 16: Verify khi không nhập Thứ tự sắp xếp -> Hệ thống hiển thị thông báo lỗi 
def test_ordering_error_message(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    enter_field.enter_title_vi("Tiêu đề bài viết")
    enter_field.enter_short_description_vi("Mô tả ngắn bài viết")
    enter_field.enter_content_vi("Nội dung bài viết")
    article.click_tab_general_info()
    article.click_select()
    article.select_article_type("Tin tức chuyên ngành")
    article.ordering("")
    article.click_save_button()
    if article.is_ordering_error_displayed():
        logging.info("Test Case 16 PASS: Hệ thống hiển thị lỗi đúng khi không nhập Thứ tự sắp xếp!")
    else:
        logging.error("Test Case 16 FAIL: Hệ thống không hiển thị lỗi khi Thứ tự sắp xếp trống!")
        assert False, "Lỗi: Không hiển thị thông báo 'Vui lòng nhập Thứ tự sắp xếp'."



    def test_save_article(article, enter_field, select):
        article.perform_tag_operations()
        article.click_create_new_button()
        enter_field.enter_title_vi("Tiêu đề bài viết")
        enter_field.enter_short_description_vi("Mô tả ngắn bài viết")
        enter_field.enter_content_vi("Nội dung bài viết")
        article.click_en_tab()
        article.click_translate_content_button()
        enter_field.enter_title_en("Article Title")
        enter_field.enter_short_description_en("Article Short Description")
        enter_field.enter_content_en("Article Content")
        article.click_tab_general_info()
        select.click_select()
        select.select_article_type("Tin tức chuyên ngành")
        article.click_save_and_continue_button()
        if article.wait_for_article_to_appear_in_list("Tiêu đề bài viết"):
            logging.info("Test Case 23 PASS: Bài viết hiển thị đúng tên trong danh sách bài viết.")
        else:
            logging.error("Test Case 23 FAIL: Tên bài viết không xuất hiện trong danh sách bài viết.")