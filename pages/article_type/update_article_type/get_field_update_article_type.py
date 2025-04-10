import time
import logging
import selenium
from selenium.webdriver.common.by import By
from locators.locator_article_type.locator_update_article_type import LocatorUpdateArticleType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class GetFieldUpdateArticleType:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorUpdateArticleType 

    # Tab Tieng Viet
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

    # Tab English
    # Ham lay gia tri loai bai viet ( Tab English )
    def get_en_article_type_value(self):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(self.locators.EN_TEXT_INPUT_ARTICLE_TYPE))
            value = input_field.get_attribute("value")
            logging.info(f"Giá trị lấy được từ ô 'Loại bài viết' English: {value}")
            return value
        except TimeoutException:
            logging.error("Không thể lấy giá trị từ ô 'Loại bài viết' English.")
            return None
        
    # Ham lay gia tri duong dan ( Tab English )
    def get_en_article_link_value(self):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(self.locators.EN_TEXT_INPUT_LINK))
            value = input_field.get_attribute("value")
            logging.info(f"Giá trị lấy được từ ô 'Đường dẫn' English: {value}")
            return value
        except TimeoutException:
            logging.error("Không thể lấy giá trị từ ô 'Đường dẫn' English.")
            return None
        
    # Ham lay gia tri metakeywords ( Tab English )
    def get_en_meta_keyword_value(self):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(self.locators.EN_TEXT_INPUT_META_KEYWORD))
            value = input_field.get_attribute("value")
            logging.info(f"Giá trị lấy được từ ô 'Từ khóa meta' English: {value}")
            return value
        except TimeoutException:
            logging.error("Không thể lấy giá trị từ ô 'Từ khóa meta' English.")
            return None

    # Ham lay gia tri mo ta ( Tab English )
    def get_en_description_value(self):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(self.locators.EN_TEXT_AREA_DESCRIPTION))
            value = input_field.get_attribute("value")
            logging.info(f"Giá trị lấy được từ ô 'Mô tả' English: {value}")
            return value
        except TimeoutException:
            logging.error("Không thể lấy giá trị từ ô 'Mô tả' English.")
            return None

    # Ham lay gia tri mo ta Meta ( Tab English )
    def get_en_meta_description_value(self):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(self.locators.EN_TEXT_AREA_META_DESCRIPTION))
            value = input_field.get_attribute("value")
            logging.info(f"Giá trị lấy được từ ô 'Meta Description' English: {value}")
            return value
        except TimeoutException:
            logging.error("Không thể lấy giá trị từ ô 'Meta Description' English.")
            return None
        
    # Ham lay gia tri mo ta Meta ( Tab English )
    def get_en_meta_description_value(self):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(self.locators.EN_TEXT_AREA_META_DESCRIPTION))
            value = input_field.get_attribute("value")
            logging.info(f"Giá trị lấy được từ ô 'Meta Description' English: {value}")
            return value
        except TimeoutException:
            logging.error("Không thể lấy giá trị từ ô 'Meta Description' English.")
            return None
        
     # Ham lay gia tri Thu tu sap xep
    def get_sort_order_value(self):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(self.locators.TEXT_INPUT_SORT_ORDER))
            value = input_field.get_attribute("value")
            logging.info(f"Giá trị lấy được từ ô 'Thu tu sap xep': {value}")
            return value
        except TimeoutException:
            logging.error("Không thể lấy giá trị từ ô 'Thu tu sap xep'.")
            return None