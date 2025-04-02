import time
import logging
from locators.faq.locator_faq import LocatorFAQ
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class ValidationFAQ:
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
            logging.error(f"Lỗi: Hệ thống hiển thị key '{error_message}' thay vì nội dung dịch.")
        else:
            logging.error(f"Lỗi: Thông báo không đúng, nhận được: '{error_message}'")
        return False
    
    # Hàm kiểm tra xem 'Dữ liệu không hợp lệ' trong field 'Tìm kiếm' có hiển thị table hay không.
    def is_invalid_search_in_list(self, input):
        try:
            tag_list_wrapper = self.wait.until(
                EC.visibility_of_element_located(self.locators.PAGE_LIST_WRAPPER)
            )
            if not input in tag_list_wrapper.text:
                logging.info(f"Dữ liệu '{input}' vừa tìm kiếm không có trong table!")
                return True
            else:
                logging.info(f"Dữ liệu '{input}' vừa tìm kiếm có trong table.")
                return False
        except Exception as e:
            logging.error(f"Lỗi khi kiểm tra dữ liệu vừa tìm kiếm trong table: {e}", exc_info=True)
            return False
        
    # Hàm kiểm tra xem 'Dữ liệu hợp lệ' trong field 'Tìm kiếm' có hiển thị trong table hay không.
    def is_valid_search_in_list(self, input):
        try:
            tag_list_wrapper = self.wait.until(
                EC.visibility_of_element_located(self.locators.PAGE_LIST_WRAPPER)
            )
            if input in tag_list_wrapper.text:
                logging.info(f"Dữ liệu '{input}' vừa tìm kiếm có trong table.")
                return True
            else:
                logging.info(f"Dữ liệu '{input}' vừa tìm kiếm không có trong table!")
                return False
        except Exception as e:
            logging.error(f"Lỗi khi kiểm tra dữ liệu vừa tìm kiếm trong table: {e}", exc_info=True)
            return False