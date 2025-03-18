import time
import pytest
import logging
import datetime
from utils.login import Login
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
    article.click_content_menu()
    article.click_article_menu()
    result = article.click_all_article_menu()
    if result:
        print("Test Case 1 PASS: Hệ thống chuyển hướng thành công đến trang 'Tất cả bài viết'.")
        logging.info("Test Case 1 PASS: Hệ thống chuyển hướng thành công đến trang 'Tất cả bài viết'.")
    else:
        print("Test Case 1 FAIL: Hệ thống không chuyển hướng đến trang 'Tất cả bài viết'.")
        logging.error("Test Case 1 FAIL: Hệ thống không chuyển hướng đến trang 'Tất cả bài viết'.")
        assert False, "Lỗi: Trang 'Tất cả bài viết' không tải được!"
