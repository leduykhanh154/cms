import time
import logging
from locators.faq.locator_editfaq import LocatorEditFAQ
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class ValidationEditFAQ:
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
            element = self.wait.until(EC.presence_of_element_located(locator))
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
    
    def is_edit_faq_vi_displayed(self):
        try:
            time.sleep(5)
            value_element = self.get_text(self.locators.CHECK_FAQ_INPUT_VI)
            expected_value = "test-cauhoi-dachinhsua"

            if value_element == expected_value:
                logging.info("Đã hiển thị giá trị đã chỉnh sửa ở field.")
                return True
            else:
                logging.error(f"Lỗi: Expected: '{expected_value}', nhưng nhận được: '{value_element}'")
                return False
        except TimeoutException:
            return False
    
    def is_answer_vi_error_displayed(self):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            return self.is_error_message_displayed(self.locators.ANSWER_ERROR_MESSAGE_VI, "Vui lòng nhập Câu trả lời")
        except TimeoutException:
            return False

    def is_answer_vi_error_invisible(self):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            answer_vi_error_invisible = self.wait.until(EC.invisibility_of_element_located(self.locators.ANSWER_ERROR_MESSAGE_VI))
            logging.info('Đã ẩn validate.')
            return answer_vi_error_invisible
        except TimeoutException:
            logging.error('Không ẩn validate.')
            return False
        
    def is_answer_vi_4999_character(self):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            character_element_invisible = self.wait.until(EC.invisibility_of_element_located(self.locators.ANSWER_ERROR_MESSAGE_VI))
            logging.info('Đã hiển thị giá trị ở field và không có thông báo lỗi.')
            return character_element_invisible
        except TimeoutException:
            logging.error('Đã có hiển thị thông báo lỗi.')
            return False
        
    def is_answer_vi_5000_character(self):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            character_element_invisible = self.wait.until(EC.invisibility_of_element_located(self.locators.ANSWER_ERROR_MESSAGE_VI))
            logging.info('Đã hiển thị giá trị ở field và không có thông báo lỗi.')
            return character_element_invisible
        except TimeoutException:
            logging.error('Đã có hiển thị thông báo lỗi.')
            return False
        
    def is_answer_vi_5001_character(self):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            return self.is_error_message_displayed(self.locators.ANSWER_ERROR_MESSAGE_VI, "Vui lòng nhập Câu trả lời không quá 5000 ký tự")
        except TimeoutException:
            return False
        
    def is_edit_sort_order_displayed(self, data):
        try:
            time.sleep(1)
            value_element = self.wait.until(
                EC.text_to_be_present_in_element_attribute(self.locators.SORT_ORDER_INPUT_VI, "value", data)
            )

            if value_element:
                logging.info(f"Đã hiển thị giá trị '{data}' vừa chỉnh sửa ở field.")
                return True
            else:
                logging.error(f"Lỗi: Expected: '{data}', nhưng nhận được: '{value_element}'")
                return False
        except TimeoutException:
            return False