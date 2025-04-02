import logging
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.faq.locator_faq import LocatorFAQ

class SelectFAQ:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorFAQ    

    # Hàm nhấn vào dropdown 'Trạng thái'
    def click_status_dropdown(self):
        try:
            select_element = self.wait.until(EC.element_to_be_clickable(self.locators.DROPDOWN_STATUS))
            select_element.click()
            logging.info("Đã nhấn dropdown 'Trạng thái'.")
        except TimeoutException:
            logging.error("Không thể nhấn dropdown 'Trạng thái'.")
            raise

    # Hàm kiểm tra dropdown 'Trạng thái' có hiển thị không
    def is_status_dropdown_visible(self):
        try:
            dropdown_element = self.wait.until(EC.visibility_of_element_located(self.locators.DROPDOWN_STATUS_VISIBLE))
            return dropdown_element.is_displayed()
        except TimeoutException:
            return False
        
    # Hàm nhấn vào dropdown 'Loại câu hỏi'
    def click_question_type_dropdown(self):
        try:
            select_element = self.wait.until(EC.element_to_be_clickable(self.locators.DROPDOWN_QUESTION_TYPE))
            select_element.click()
            logging.info("Đã nhấn dropdown 'Loại câu hỏi'.")
        except TimeoutException:
            logging.error("Không thể nhấn dropdown 'Loại câu hỏi'.")
            raise

    # Hàm kiểm tra dropdown 'Loại câu hỏi' có hiển thị không
    def is_question_type_dropdown_visible(self):
        try:
            dropdown_element = self.wait.until(EC.visibility_of_element_located(self.locators.DROPDOWN_QUESTION_TYPE_VISIBLE))
            return dropdown_element.is_displayed()
        except TimeoutException:
            return False
        
    # Hàm nhấn vào select 'Xóa'
    def click_delete_select(self):
        try:
            select_element = self.wait.until(EC.element_to_be_clickable(self.locators.SELECT_DELETE))
            select_element.click()
            logging.info("Đã nhấn select 'Xóa'.")
        except TimeoutException:
            logging.error("Không thể nhấn select 'Xóa'.")
            raise