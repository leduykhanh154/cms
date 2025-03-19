import logging
from locators.locator_article import LocatorArticle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class ArticleValidation:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorArticle
    
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

    def is_title_vi_error_displayed(self):
        return self.is_error_message_displayed(self.locators.TITLE_ERROR_MESSAGE, "Vui lòng nhập Tiêu đề")
    
    def is_title_vi_max_length_error_displayed(self):
        return self.is_error_message_displayed(self.locators.TITLE_MAX_LENGTH_ERROR_MESSAGE, "Vui lòng nhập Tiêu đề không quá 250 ký tự")
    
    def is_title_en_error_displayed(self):
        return self.is_error_message_displayed(self.locators.TITLE_EN_ERROR_MESSAGE, "Vui lòng nhập Tiêu đề")
    
    def is_title_en_max_length_error_displayed(self):
        return self.is_error_message_displayed(self.locators.TITLE_EN_MAX_LENGTH_ERROR_LOCATOR, "Vui lòng nhập Tiêu đề không quá 250 ký tự")
    
    def is_short_description_vi_max_length_error_displayed(self):
        return self.is_error_message_displayed(self.locators.SHORT_DESCRIPTION_VI_ERROR_MESSAGE, "Vui lòng nhập Mô tả ngắn không quá 1000 ký tự")
    
    def is_short_description_en_max_lenght_error_displayed(self):
        return self.is_error_message_displayed(self.locators.SHORT_DESCRIPTION_EN_ERROR_MESSAGE, "Vui lòng nhập Mô tả ngắn không quá 1000 ký tự")
    
    def is_content_vi_error_displayed(self):
        return self.is_error_message_displayed(self.locators.CONTENT_VI_ERROR_MESSAGE, "Vui lòng nhập Nội dung")
    
    def is_content_en_error_displayed(self):
        return self.is_error_message_displayed(self.locators.CONTENT_EN_ERROR_MESSAGE, "Vui lòng nhập Nội dung")
    
    def is_article_type_error_displayed(self):
        return self.is_error_message_displayed(self.locators.ARTICLE_TYPE_ERROR_MESSAGE, "Vui lòng nhập Loại bài viết")
    
    def is_ordering_error_displayed(self):
        try:
            error_message = self.get_text(self.locators.ORDERING_ERROR_MESSAGE)
            expected_message = "Vui lòng nhập Thứ tự sắp xếp"

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

    def is_ordering_max_length_error_displayed(self):
        try:
            error_message = self.get_text(self.locators.ORDERING_MAX_LENGTH_ERROR_MESSAGE)
            expected_message = "Vui lòng nhập không quá 7 số"
            if error_message == expected_message:
                logging.info("Thông báo lỗi hiển thị đúng.")
                return True
            elif error_message == "global.validation.max_length":
                logging.error("Lỗi: global.validation.max_length. Thông báo lỗi không đúng.")
                return False
            else:
                logging.error(f"Lỗi: Expected: '{expected_message}', nhưng nhận được: '{error_message}'")
                return False
        except Exception as e:
            logging.error(f"Lỗi: Không tìm thấy phần tử thông báo lỗi. Exception: {e}")
        return False
        
    