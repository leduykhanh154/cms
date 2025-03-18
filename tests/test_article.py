import time
import pytest
import logging
import datetime
from utils.login import Login
from utils.driver_setup import get_driver
from pages.articles.article import Article
from pages.articles.date import DateArticle
from pages.articles.select import SelectArticle
from locators.locator_article import LocatorArticle
from pages.articles.switch import SwitchArticle
from pages.articles.enterfield import EnterFieldArticle
from pages.articles.tag_article import TagArticle
from pages.articles.validation import ArticleValidation
from pages.articles.image_article import ImageArticle
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

def test_upload_thumbnail_image_popup(article, enter_field, image):
    article.perform_tag_operations()
    article.click_create_new_button()
    enter_field.enter_title_vi("Bài viết kiểm thử")
    enter_field.enter_content_vi("Đây là nội dung bài viết test")
    article.click_tab_general_info()
    image.click_upload_thumbnail_image_field()
    assert image.is_upload_popup_displayed(), "Test Case FAIL: Pop-up upload hình ảnh không hiển thị"
    logging.info("Test Case PASS: Pop-up upload hình ảnh hiển thị thành công")


