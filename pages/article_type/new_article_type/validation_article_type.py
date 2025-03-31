import time
import logging
import selenium
from selenium.webdriver.common.by import By
from locators.locator_article_type.locator_new_article_type import LocatorNewArticleType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class ValidationArticleType:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorNewArticleType  
        
    # Hàm lấy nội dung văn bản của một phần tử trên giao diện
    def get_text(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.text.strip()
        except TimeoutException:
            logging.error(f"Lỗi: Không tìm thấy phần tử {locator}")
            return None
        
    # Ham kiem tra Loai bai viet khong vuot qua 255 ky tu
    def is_max_type_error_displayed(self):
        try:
            error_message = self.get_text(self.locators.VI_ERROR_PLEASE_FIELD_TYPE_ARTICLE)
            expected_message = "Vui lòng nhập Loại bài viết không quá 254 ký tự"

            if error_message == expected_message:
                logging.info("Thông báo lỗi hiển thị đúng.")
                return True
            elif error_message == "global.validation.required":
                logging.error("Lỗi: global.validation.required. Thông báo lỗi không đúng.")
                return False  # Khi hiển thị "global.validation.required",
            else:
                logging.error(f"Lỗi: Expected: '{expected_message}', nhưng nhận được: '{error_message}'")
                return False
        except Exception as e:
            logging.error(f"Lỗi: Không tìm thấy phần tử thông báo lỗi. Exception: {e}")
        return False

# Ham kiem tra Loai bai viet khong dien hoac dien va xoa Loai bai viet
    def is_field_error_displayed(self):
        try:
            error_message = self.get_text(self.locators.VI_ERROR_PLEASE_FIELD_TYPE_ARTICLE)
            expected_message = "Vui lòng nhập Loại bài viết"

            if error_message == expected_message:
                logging.info("Thông báo lỗi hiển thị đúng.")
                return True
            elif error_message == "global.validation.required":
                logging.error("Lỗi: global.validation.required. Thông báo lỗi không đúng.")
                return False  # Khi hiển thị "global.validation.required",
            else:
                logging.error(f"Lỗi: Expected: '{expected_message}', nhưng nhận được: '{error_message}'")
                return False
        except Exception as e:
            logging.error(f"Lỗi: Không tìm thấy phần tử thông báo lỗi. Exception: {e}")
        return False
    
    # Ham kiem tra duong dan khong vuot qua 255 ky tu
    def is_max_link_error_displayed(self):
        try:
            error_message = self.get_text(self.locators.VI_ERROR_LINK)
            expected_message = "Vui lòng nhập Đường dẫn không quá 254 ký tự"

            if error_message == expected_message:
                logging.info("Thông báo lỗi hiển thị đúng.")
                return True
            elif error_message == "global.validation.required":
                logging.error("Lỗi: global.validation.required. Thông báo lỗi không đúng.")
                return False  # Khi hiển thị "global.validation.required",
            else:
                logging.error(f"Lỗi: Expected: '{expected_message}', nhưng nhận được: '{error_message}'")
                return False
        except Exception as e:
            logging.error(f"Lỗi: Không tìm thấy phần tử thông báo lỗi. Exception: {e}")
        return False
    
    # Ham kiem tra Mo ta ngan khong vuot qua 200 ky tu
    def is_max_short_description_error_displayed(self):
        try:
            error_message = self.get_text(self.locators.VI_ERROR_SHORT_DESCRIPTION)
            expected_message = "Vui lòng nhập Mô tả ngắn không quá 200 ký tự"

            if error_message == expected_message:
                logging.info("Thông báo lỗi hiển thị đúng.")
                return True
            elif error_message == "global.validation.required":
                logging.error("Lỗi: global.validation.required. Thông báo lỗi không đúng.")
                return False  # Khi hiển thị "global.validation.required",
            else:
                logging.error(f"Lỗi: Expected: '{expected_message}', nhưng nhận được: '{error_message}'")
                return False
        except Exception as e:
            logging.error(f"Lỗi: Không tìm thấy phần tử thông báo lỗi. Exception: {e}")
        return False
    
    # Ham kiem tra Meta Keyword khong vuot qua 100 ky tu
    def is_meta_keyword_error_displayed(self):
        try:
            error_message = self.get_text(self.locators.VI_ERROR_META_KEYWORD)
            expected_message = "Vui lòng nhập Meta Keyword không quá 100 ký tự"

            if error_message == expected_message:
                logging.info("Thông báo lỗi hiển thị đúng.")
                return True
            elif error_message == "global.validation.required":
                logging.error("Lỗi: global.validation.required. Thông báo lỗi không đúng.")
                return False  # Khi hiển thị "global.validation.required",
            else:
                logging.error(f"Lỗi: Expected: '{expected_message}', nhưng nhận được: '{error_message}'")
                return False
        except Exception as e:
            logging.error(f"Lỗi: Không tìm thấy phần tử thông báo lỗi. Exception: {e}")
        return False
    
    # Ham kiem tra Meta Keyword khong vuot qua 100 ky tu
    def is_meta_description_error_displayed(self):
        try:
            error_message = self.get_text(self.locators.VI_ERROR_META_DESCRIPTION)
            expected_message = "Vui lòng nhập Meta Description không quá 500 ký tự"

            if error_message == expected_message:
                logging.info("Thông báo lỗi hiển thị đúng.")
                return True
            elif error_message == "global.validation.required":
                logging.error("Lỗi: global.validation.required. Thông báo lỗi không đúng.")
                return False  # Khi hiển thị "global.validation.required",
            else:
                logging.error(f"Lỗi: Expected: '{expected_message}', nhưng nhận được: '{error_message}'")
                return False
        except Exception as e:
            logging.error(f"Lỗi: Không tìm thấy phần tử thông báo lỗi. Exception: {e}")
        return False