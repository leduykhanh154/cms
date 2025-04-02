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

class DeleteLastCharNewArticleType:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorNewArticleType 

# Hàm chung để xóa 1 ký tự cuối cùng trong một ô nhập liệu bất kỳ
    def delete_last_character(self, input_locator):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(input_locator))
            input_field.send_keys(Keys.BACKSPACE)  # Nhấn phím Backspace để xóa ký tự cuối
            logging.info(f"Đã xóa 1 ký tự cuối trong ô nhập liệu {input_locator}.")
        except TimeoutException:
            logging.error(f"Không thể tìm thấy ô nhập liệu {input_locator} để xóa ký tự.")

    # Hàm xóa 1 ký tự cuối trong ô 'Loại bài viết' (Tiếng Việt)
    def delete_vi_article_type_character(self):
        self.delete_last_character(self.locators.VI_TEXT_INPUT_ARTICLE_TYPE)

    # Hàm xóa 1 ký tự cuối trong ô 'Đường dẫn' (Tiếng Việt)
    def delete_vi_article_link_character(self):
        self.delete_last_character(self.locators.VI_TEXT_INPUT_LINK)

    # Hàm xóa 1 ký tự cuối trong ô 'Từ khóa meta' (Tiếng Việt)
    def delete_vi_meta_keyword_character(self):
        self.delete_last_character(self.locators.VI_TEXT_INPUT_META_KEYWORD)

    # Hàm xóa 1 ký tự cuối trong ô 'Mô tả' (Tiếng Việt)
    def delete_vi_description_character(self):
        self.delete_last_character(self.locators.VI_TEXT_AREA_DESCRIPTION)

    # Hàm xóa 1 ký tự cuối trong ô 'Meta Description' (Tiếng Việt)
    def delete_vi_meta_description_character(self):
        self.delete_last_character(self.locators.VI_TEXT_AREA_META_DESCRIPTION)
        
    # Tab English
    # Hàm xóa 1 ký tự cuối trong ô 'Loại bài viết' (English)
    def delete_en_article_type_character(self):
        self.delete_last_character(self.locators.EN_TEXT_INPUT_ARTICLE_TYPE)

    # Hàm xóa 1 ký tự cuối trong ô 'Đường dẫn' (English)
    def delete_en_article_link_character(self):
        self.delete_last_character(self.locators.EN_TEXT_INPUT_LINK)

    # Hàm xóa 1 ký tự cuối trong ô 'Từ khóa meta' (English)
    def delete_en_meta_keyword_character(self):
        self.delete_last_character(self.locators.EN_TEXT_INPUT_META_KEYWORD)

    # Hàm xóa 1 ký tự cuối trong ô 'Mô tả' (English)
    def delete_en_description_character(self):
        self.delete_last_character(self.locators.EN_TEXT_AREA_DESCRIPTION)

    # Hàm xóa 1 ký tự cuối trong ô 'Meta Description' (English)
    def delete_en_meta_description_character(self):
        self.delete_last_character(self.locators.EN_TEXT_AREA_META_DESCRIPTION)
        
    # Hàm xóa 1 ký tự cuối trong ô 'Thứ Tự Sắp Xếp'
    def delete_last_character_in_sort_order(self):
        self.delete_last_character(self.locators.TEXT_INPUT_SORT_ORDER)
