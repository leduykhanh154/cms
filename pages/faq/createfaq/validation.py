import time
import logging
from locators.faq.locator_faq import LocatorFAQ
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


class ValidationCreateFAQ:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorFAQ

    # Hàm lấy nội dung văn bản của một phần tử trên giao diện
    def get_text(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.text.strip()
        except TimeoutException:
            logging.error(f"Lỗi: Không tìm thấy phần tử {locator}")
            return None
    
    # Hàm hiển thị thông báo lỗi
    def is_error_message_displayed(self, locator, expected_message):
        error_message = self.get_text(locator)
        if error_message == expected_message:
            logging.info(f"Thông báo lỗi '{expected_message}' hiển thị đúng.")
            return True
        elif error_message in ["global.validation.maxlength", "global.validation.required"]:
            logging.error(f"Lỗi: Hệ thống hiển thị key '{expected_message}' thay vì nội dung dịch.")
        else:
            logging.error(f"Lỗi: Thông báo lỗi không đúng, nhận được: '{expected_message}'")
        return False
    
    def is_faq_vi_error_displayed(self):
        time.sleep(1)
        return self.is_error_message_displayed(self.locators.FAQ_ERROR_MESSAGE_VI, "Vui lòng nhập Câu hỏi")

    def is_faq_vi_error_invisible(self):
        try:
            error_element = self.wait.until(EC.invisibility_of_element_located(self.locators.FAQ_ERROR_MESSAGE_VI))
            return error_element
        except TimeoutException:
            return False
        
    def is_faq_vi_499_character(self):
        try:
            character_element = self.wait.until(EC.invisibility_of_element_located(self.locators.FAQ_ERROR_MESSAGE_VI))
            return character_element
        except TimeoutException:
            return False
    
    def is_faq_vi_500_character(self):
        try:
            character_element = self.wait.until(EC.invisibility_of_element_located(self.locators.FAQ_ERROR_MESSAGE_VI))
            return character_element
        except TimeoutException:
            return False
        
    def is_faq_vi_501_character(self):
        return self.is_error_message_displayed(self.locators.FAQ_ERROR_MESSAGE_VI, "Vui lòng nhập Câu hỏi không quá 500 ký tự")
    
    def is_answer_vi_error_displayed(self):
        try:
            answer_vi_error = self.wait.until(EC.presence_of_element_located(self.locators.ANSWER_ERROR_MESSAGE_VI))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", answer_vi_error)
            time.sleep(1)
            return self.is_error_message_displayed(self.locators.ANSWER_ERROR_MESSAGE_VI, "Vui lòng nhập Câu trả lời")
        except TimeoutException:
            return False

    def is_answer_vi_error_invisible(self):
        try:
            answer_vi_error = self.wait.until(EC.presence_of_element_located(self.locators.ANSWER_ERROR_MESSAGE_VI))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", answer_vi_error)
            answer_vi_error_invisible = self.wait.until(EC.invisibility_of_element_located(self.locators.ANSWER_ERROR_MESSAGE_VI))
            logging.info('Đã ẩn validate.')
            return answer_vi_error_invisible
        except TimeoutException:
            logging.error('Không ẩn validate.')
            return False