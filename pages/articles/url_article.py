import logging
import unicodedata
import re
from locators.locator_article import LocatorArticle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class URLArticle:
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorArticle

    def get_url_key_value(self):
        try:
            url_input = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='languages[vi][url_key]']"))
            )
            return url_input.get_attribute("value")
        except TimeoutException:
            logging.error("Không tìm thấy trường URL Key sau 5 giây.")
            return None  

    def check_url_key_generated(self):
        title_input = self.driver.find_element(self.locators.TITLE_INPUT).get_attribute("value")
        url_input = self.get_url_key_value()
        expected_url_key = self.generate_expected_url_key(title_input)
        return expected_url_key in url_input

    def generate_expected_url_key(self, title):
        title = title.strip().lower()
        title = title.replace("đ", "d").replace("Đ", "d")
        title = unicodedata.normalize("NFKD", title)
        title = "".join([c for c in title if not unicodedata.combining(c)])
        title = re.sub(r"\s+", "-", title)
        title = re.sub(r"[^a-z0-9-]", "", title)
        title = re.sub(r"-+", "-", title)
        return title

