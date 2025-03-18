import time
import pytest
import logging
import datetime
from utils.login import Login
from utils.logger import LoggerConfig
from utils.driver_setup import get_driver
from pages.articles.article import Article
from pages.articles.date import DateArticle
from pages.articles.select import SelectArticle
from pages.articles.switch import SwitchArticle
from pages.articles.tag_article import TagArticle
from pages.articles.url_article import URLArticle
from locators.locator_article import LocatorArticle
from pages.articles.image_article import ImageArticle
from pages.articles.enterfield import EnterFieldArticle
from pages.articles.validation import ArticleValidation
from selenium.common.exceptions import TimeoutException
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
    test_logger.info("Bat dau Test Case 1 : Verify khi click menu Tat ca bai viet -> He thong chuyen huong den trang Danh sach bai viet")
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





