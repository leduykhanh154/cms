import time
import logging
import selenium
from selenium.webdriver.common.by import By
from locators.locator_article_type.locator_new_article_type import LocatorNewArticleType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class GetFieldNewArticleType:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorNewArticleType 

    # Ham lay gia tri loai bai viet ( tab Tieng Viet )
    def get_vi_article_type_value(self):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(self.locators.VI_TEXT_INPUT_ARTICLE_TYPE))
            value = input_field.get_attribute("value")
            logging.info(f"Giá trị lấy được từ ô 'Loại bài viết' tiếng Việt: {value}")
            return value
        except TimeoutException:
            logging.error("Không thể lấy giá trị từ ô 'Loại bài viết' tiếng Việt.")
            return None
        
    # Ham lay gia tri duong dan ( tab Tieng Viet )
    def get_vi_article_link_value(self):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(self.locators.VI_TEXT_INPUT_LINK))
            value = input_field.get_attribute("value")
            logging.info(f"Giá trị lấy được từ ô 'Đường dẫn' tiếng Việt: {value}")
            return value
        except TimeoutException:
            logging.error("Không thể lấy giá trị từ ô 'Đường dẫn' tiếng Việt.")
            return None
        
    # Ham lay gia tri metakeywords ( tab Tieng Viet )
    def get_vi_meta_keyword_value(self):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(self.locators.VI_TEXT_INPUT_META_KEYWORD))
            value = input_field.get_attribute("value")
            logging.info(f"Giá trị lấy được từ ô 'Từ khóa meta' tiếng Việt: {value}")
            return value
        except TimeoutException:
            logging.error("Không thể lấy giá trị từ ô 'Từ khóa meta' tiếng Việt.")
            return None

    # Ham lay gia tri mo ta ( tab Tieng Viet )
    def get_vi_description_value(self):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(self.locators.VI_TEXT_AREA_DESCRIPTION))
            value = input_field.get_attribute("value")
            logging.info(f"Giá trị lấy được từ ô 'Mô tả' tiếng Việt: {value}")
            return value
        except TimeoutException:
            logging.error("Không thể lấy giá trị từ ô 'Mô tả' tiếng Việt.")
            return None

    # Ham lay gia tri mo ta Meta ( tab Tieng Viet )
    def get_vi_meta_description_value(self):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(self.locators.VI_TEXT_AREA_META_DESCRIPTION))
            value = input_field.get_attribute("value")
            logging.info(f"Giá trị lấy được từ ô 'Meta Description' tiếng Việt: {value}")
            return value
        except TimeoutException:
            logging.error("Không thể lấy giá trị từ ô 'Meta Description' tiếng Việt.")
            return None
