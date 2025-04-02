import logging
from selenium.webdriver.common.by import By
from locators.faq.locator_faq import LocatorFAQ
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrlFAQ:
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorFAQ

    # Hàm check url có đang ở trang 'Trang chủ' không
    def check_url_home_page(self):
        expected_url = 'https://mpire-cms-demo.mpire.asia/cms/dashboard'
        
        try:
            self.wait.until(EC.url_to_be(expected_url))
            logging.info("Chuyển hướng thành công đến Trang Chủ.")
            return True
        except Exception:
            logging.error("Không thể chuyển hướng đến Trang Chủ!")
            return False
        
    # Hàm check url có đang ở trang 'Tạo mới' không
    def check_url_create_page(self):
        expected_url = 'https://mpire-cms-demo.mpire.asia/cms/faq/create'

        try:
            self.wait.until(EC.url_to_be(expected_url))
            logging.info("Chuyển hướng thành công đến trang 'Tạo mới'.")
            return True
        except Exception:
            logging.error("Chuyển hướng không thành công đến trang 'Tạo mới'!")
            return False

    # Hàm check url có đang ở trang 'Chỉnh sửa câu hỏi' đầu tiên hay không
    def check_url_question_edit_page(self):
        expected_url = 'https://mpire-cms-demo.mpire.asia/cms/faq/edit/66c04598ca70a'

        try:
            self.wait.until(EC.url_to_be(expected_url))
            logging.info("Chuyển hướng thành công đến trang 'Chỉnh sửa câu hỏi' đầu tiên.")
            return True
        except Exception:
            logging.error("Chuyển hướng không thành công đến trang 'Chỉnh sửa câu hỏi' đầu tiên!")
            return False