
import logging
import time
from locators.faq.locator_faq import LocatorFAQ
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EnterFieldFAQ:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorFAQ

    # Hàm nhập dữ liệu trong thanh tìm kiếm
    def enter_data_in_search(self, data):
        data_input = self.wait.until(EC.visibility_of_element_located(self.locators.SEARCH_INPUT))
        data_input.clear()
        data_input.send_keys(data)
        logging.info(f"Đã nhập dữ liệu '{data}' vào thanh tìm kiếm")
        time.sleep(1)