import logging
from locators.faq.locator_faq import LocatorFAQ
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EnterFieldCreateFAQ:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorFAQ

    # Hàm nhập Câu hỏi - VI
    def enter_faq_vi(self, expected):
        faq_input = self.wait.until(EC.visibility_of_element_located(self.locators.FAQ_INPUT))
        faq_input.clear()
        faq_input.send_keys(expected)
        logging.info(f"Đã nhập Câu hỏi: {expected}")