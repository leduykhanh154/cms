import logging
import keyword
import time
from locators.faq.locator_faq import LocatorFAQ
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class EnterFieldCreateFAQ:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorFAQ

    # Hàm nhập Câu hỏi - VI
    def enter_faq_vi(self, data):
        try:
            faq_input = self.wait.until(EC.visibility_of_element_located(self.locators.FAQ_INPUT))
            faq_input.send_keys(Keys.CONTROL + "a")
            faq_input.send_keys(Keys.DELETE)
            time.sleep(1)
            faq_input.send_keys(data)
            logging.info(f"Đã nhập Câu hỏi: {data}")
        except Exception as e:
            logging.error(f"Lỗi exception {e}")
 