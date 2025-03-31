import time
import logging
import selenium
from selenium.webdriver.common.by import By
from locators.locator_article_type.locator_new_article_type import LocatorNewArticleType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class EnterFieldNewArticleType:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorNewArticleType 
    
    # Ham nhap loai bai viet ( tab Tieng Viet)
    def enter_vi_article_type(self, text):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(self.locators.VI_TEXT_INPUT_ARTICLE_TYPE))
            input_field.clear()
            input_field.send_keys(text)
            logging.info(f"Đã nhập '{text}' vào ô 'Loại bài viết' tiếng Việt.")
        except TimeoutException:
            logging.error("Không thể tìm thấy hoặc nhập dữ liệu vào ô 'Loại bài viết' tiếng Việt.") 
    
    # Ham dien duong dan ( tab Tieng Viet )
    def enter_vi_article_link(self, text):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(self.locators.VI_TEXT_INPUT_LINK))
            input_field.clear()
            input_field.send_keys(text)
            logging.info(f"Đã nhập '{text}' vào ô 'Đường dẫn' tiếng Việt.")
        except TimeoutException:
            logging.error("Không thể tìm thấy hoặc nhập dữ liệu vào ô 'Đường dẫn' tiếng Việt.")
    
    # Ham dien meta keywords ( tab Tieng Viet )
    def enter_vi_meta_keyword(self, text):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(self.locators.VI_TEXT_INPUT_META_KEYWORD))
            input_field.clear()
            input_field.send_keys(text)
            logging.info(f"Đã nhập '{text}' vào ô 'Từ khóa meta' tiếng Việt.")
        except TimeoutException:
            logging.error("Không thể tìm thấy hoặc nhập dữ liệu vào ô 'Từ khóa meta' tiếng Việt.")

    # Ham dien mo ta ( tab Tieng Viet )
    def enter_vi_description(self, text):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(self.locators.VI_TEXT_AREA_DESCRIPTION))
            input_field.clear()
            input_field.send_keys(text)
            logging.info(f"Đã nhập '{text}' vào ô 'Mô tả' tiếng Việt.")
        except TimeoutException:
            logging.error("Không thể tìm thấy hoặc nhập dữ liệu vào ô 'Mô tả' tiếng Việt.")

    # Ham dien mo ta Meta ( tab Tieng Viet )
    def enter_vi_meta_description(self, text):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(self.locators.VI_TEXT_AREA_META_DESCRIPTION))
            input_field.clear()
            input_field.send_keys(text)
            logging.info(f"Đã nhập '{text}' vào ô 'Meta Description' tiếng Việt.")
        except TimeoutException:
            logging.error("Không thể tìm thấy hoặc nhập dữ liệu vào ô 'Meta Description' tiếng Việt.")
            
    # Ham xoa loai bai viet 
    def clear_vi_article_type(self):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(self.locators.VI_TEXT_INPUT_ARTICLE_TYPE))

            # Lấy độ dài văn bản hiện tại
            text_length = len(input_field.get_attribute("value"))

            # Nhấn phím Backspace tương ứng với độ dài văn bản
            for _ in range(text_length):
                input_field.send_keys(Keys.BACKSPACE)

            logging.info("Đã xóa nội dung trong ô 'Loại bài viết' tiếng Việt bằng phím Backspace.")
        except TimeoutException:
            logging.error("Không thể tìm thấy hoặc xóa dữ liệu trong ô 'Loại bài viết' tiếng Việt.")

    