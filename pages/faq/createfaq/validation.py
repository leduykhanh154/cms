import time
import logging
from locators.faq.locator_faq import LocatorFAQ
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

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
        return self.is_error_message_displayed(self.locators.FAQ_ERROR_MESSAGE, "Vui lòng nhập Câu hỏi")

    def is_faq_vi_not_invisible(self):
        try:
            error_element = self.wait.until(EC.invisibility_of_element_located(self.locators.FAQ_ERROR_MESSAGE))
            return error_element
        except TimeoutException:
            return False
        
    def is_faq_vi_499_character(self):
        try:
            character_element = self.wait.until(EC.visibility_of_element_located(self.locators.FAQ_INPUT))
            return character_element.is_displayed()
        except TimeoutException:
            return False