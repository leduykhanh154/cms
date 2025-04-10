import logging
import keyword
import time
from locators.faq.locator_editfaq import LocatorEditFAQ
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class EnterFieldEditFAQ:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorEditFAQ

    # Hàm chỉnh sửa Câu hỏi - VI
    def edit_faq_vi(self, data):
        try:
            edit_faq_vi_input = self.wait.until(EC.presence_of_element_located(self.locators.FAQ_INPUT_VI))
            edit_faq_vi_input.send_keys(Keys.CONTROL + "a")
            edit_faq_vi_input.send_keys(Keys.BACKSPACE)
            time.sleep(1)
            edit_faq_vi_input.send_keys(data)
            logging.info(f"Đã chỉnh sửa Câu hỏi*: {data}")
        except Exception as e:
            logging.error(f"Lỗi exception {e}")

    # Hàm nhập Câu trả lời - VI
    def enter_answer_vi(self, data):
        try:
            answer_vi_input = self.wait.until(EC.presence_of_element_located(self.locators.ANSWER_INPUT_VI))
            answer_vi_input.send_keys(Keys.CONTROL + "a")
            answer_vi_input.send_keys(Keys.BACKSPACE)
            time.sleep(1)
            answer_vi_input.send_keys(data)
            logging.info(f"Đã nhập Câu trả lời*: {data}")
        except Exception as e:
            logging.error(f"Lỗi exception {e}")

    # Hàm chỉnh sửa Thứ tự sắp xếp - VI
    def edit_sort_order_vi(self, data):
        try:
            input = self.wait.until(EC.presence_of_element_located(self.locators.SORT_ORDER_INPUT_VI))
            input.clear()
            input.send_keys(data)
            logging.info(f"Đã chỉnh sửa Thứ tự sắp xếp*: {data}")
        except Exception as e:
            logging.error(f"Lỗi exception {e}")
 