import logging
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.faq.locator_editfaq import LocatorEditFAQ

class SelectEditFAQ:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorEditFAQ 

    # Hàm lấy nội dung văn bản của một phần tử trên giao diện
    def get_text(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.text.strip()
        except TimeoutException:
            logging.error(f"Lỗi: Không tìm thấy phần tử {locator}")
            return None

    # Hàm click select Hiển thị
    def click_select_show(self):
        try:
            select_element = self.wait.until(EC.element_to_be_clickable(self.locators.SELECT_SHOW))
            select_element.click()
            logging.info("Đã click select Hiển thị.")
        except TimeoutException:
            logging.error("Không thể click select Hiển thị.")
            raise
        
    # Hàm click chọn giá trị Không
    def click_value_not_select_show(self):
        try:
            value = self.wait.until(EC.element_to_be_clickable(self.locators.SELECT_VALUE_NOT))
            value.click()
            logging.info("Đã click chọn giá trị Không.")
        except TimeoutException:
            logging.error("Không thể click chọn giá trị Không.")
            raise

    # Hàm kiểm tra xem giá trị Không hiển thị
    def is_value_not_visible(self):
        try:
            value_element = self.get_text(self.locators.SELECT_SHOW)
            expected_value = "Không"

            if value_element == expected_value:
                logging.info("Đã hiển thị giá trị Không ở field.")
                return True
            else:
                logging.error(f"Lỗi: Expected: '{expected_value}', nhưng nhận được: '{value_element}'")
                return False
        except TimeoutException:
            return False
        
    # Hàm click chọn giá trị Có
    def click_value_has_select_show(self):
        try:
            value = self.wait.until(EC.element_to_be_clickable(self.locators.SELECT_VALUE_HAS))
            value.click()
            logging.info("Đã click chọn giá trị Có.")
        except TimeoutException:
            logging.error("Không thể click chọn giá trị Có.")
            raise

    # Hàm kiểm tra xem giá trị Có hiển thị
    def is_value_has_visible(self):
        try:
            value_element = self.get_text(self.locators.SELECT_SHOW)
            expected_value = "Có"

            if value_element == expected_value:
                logging.info("Đã hiển thị giá trị Có ở field.")
                return True
            else:
                logging.error(f"Lỗi: Expected: '{expected_value}', nhưng nhận được: '{value_element}'")
                return False
        except TimeoutException:
            return False
        
    # Hàm kiểm tra tab Thông tin chung hiển thị
    def is_general_info_tab_displayed(self):
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.locators.GENERAL_INFO_TAB_DISPLAYED))
            logging.info('Tất cả field của tab Thông tin chung đã hiển thị.')
            return element.is_displayed()
        except TimeoutException: 
            logging.error('Lỗi: Không tìm thấy được các field')
            return False
        
    # Hàm click select Loại câu hỏi*
    def click_select_question_type(self):
        try:
            select_element = self.wait.until(EC.element_to_be_clickable(self.locators.SELECT_QUESTION_TYPE))
            select_element.click()
            logging.info("Đã click select Loại câu hỏi*.")
        except TimeoutException:
            logging.error("Không thể click select Loại câu hỏi*.")
            raise

    # Hàm click lại select Loại câu hỏi*
    def click_again_select_question_type(self):
        try:
            select_element = self.wait.until(EC.element_to_be_clickable(self.locators.SELECT_QUESTION_TYPE))
            select_element.click()
            logging.info("Đã click lại select Loại câu hỏi*.")
        except TimeoutException:
            logging.error("Không thể click lại select Loại câu hỏi*.")
            raise

    # Hàm kiểm tra select Loại câu hỏi* đã mở chưa
    def is_select_question_type_visible(self):
        try:
            dropdown_element = self.wait.until(EC.visibility_of_element_located(self.locators.DROPDOWN_VISIBLE))
            logging.info('Select Loại câu hỏi* đã mở.')
            return dropdown_element.is_displayed()
        except TimeoutException:
            return False
        
    # Hàm kiểm tra select Loại câu hỏi* đã đóng chưa
    def is_select_question_type_invisible(self):
        try:
            dropdown_element = self.wait.until(EC.invisibility_of_element_located(self.locators.DROPDOWN_VISIBLE))
            logging.info('Select Loại câu hỏi* đã đóng.')
            return dropdown_element
        except TimeoutException:
            return False
        
    # Hàm click chọn giá trị Thủ tục, quy trình
    def click_value_procedure_select_question_type(self):
        try:
            value = self.wait.until(EC.element_to_be_clickable(self.locators.SELECT_VALUE_PROCEDURE))
            value.click()
            logging.info("Đã click chọn giá trị 'Thủ tục, quy trình'.")
        except TimeoutException:
            logging.error("Không thể click chọn giá trị 'Thủ tục, quy trình'.")
            raise

    # Hàm kiểm tra xem giá trị Thủ tục, quy trình hiển thị
    def is_value_procedure_visible(self):
        try:
            value_element = self.get_text(self.locators.SELECT_QUESTION_TYPE)
            expected_value = "Thủ tục, quy trình"

            if value_element == expected_value:
                logging.info("Hiển thị giá trị 'Thủ tục, quy trình' ở field.")
                return True
            else:
                logging.error(f"Lỗi: Expected: '{expected_value}', nhưng nhận được: '{value_element}'")
                return False
        except TimeoutException:
            return False