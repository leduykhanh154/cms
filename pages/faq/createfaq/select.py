import logging
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.faq.locator_faq import LocatorFAQ

class SelectCreateFAQ:
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

    # Hàm click select Hiển thị
    def click_select_show(self):
        try:
            select_element = self.wait.until(EC.element_to_be_clickable(self.locators.SELECT_SHOW))
            select_element.click()
            logging.info("Đã click select Hiển thị.")
        except TimeoutException:
            logging.error("Không thể click select Hiển thị.")
            raise

    # Hàm click lại select Hiển thị
    def click_again_select_show(self):
        try:
            select_element = self.wait.until(EC.element_to_be_clickable(self.locators.SELECT_SHOW))
            select_element.click()
            logging.info("Đã click lại select Hiển thị.")
        except TimeoutException:
            logging.error("Không thể click lại select Hiển thị.")
            raise

    # Hàm kiểm tra select Hiển thị đã mở
    def is_select_show_visible(self):
        try:
            dropdown_element = self.wait.until(EC.visibility_of_element_located(self.locators.DROPDOWN_SHOW_VISIBLE))
            return dropdown_element.is_displayed()
        except TimeoutException:
            return False

    # Hàm kiểm tra select Hiển thị đã đóng
    def is_select_show_invisible(self):
        try:
            dropdown_element = self.wait.until(EC.invisibility_of_element_located(self.locators.DROPDOWN_SHOW_VISIBLE))
            return dropdown_element
        except TimeoutException:
            return False
        
    # Hàm click chọn giá trị Không
    def click_value_not_select_show(self):
        try:
            value = self.wait.until(EC.element_to_be_clickable(self.locators.SELECT_VALUE_NOT))
            value.click()
            logging.info("Đã click chọn giá trị Không.")
        except TimeoutException:
            logging.error("Không thể click chọn giá trị Không.")
            raise

    # Hàm kiểm tra xem giá trị Có hiển thị
    def is_value_not_visible(self):
        try:
            value_element = self.get_text(self.locators.SELECT_VALUE_VISIBLE)
            expected_value = "Không"

            if value_element == expected_value:
                logging.info("Hiển thị giá trị Không ở field.")
                return True
            else:
                logging.error(f"Lỗi: Expected: '{expected_value}', nhưng nhận được: '{value_element}'")
                return False
        except TimeoutException:
            return False
        
    # Hàm click chọn giá trị Có
    def click_value_has_select_show(self):
        try:
            value = self.wait.until(EC.element_to_be_clickable(self.locators.SELECT_VALUE_HAS))
            value.click()
            logging.info("Đã click chọn giá trị Có.")
        except TimeoutException:
            logging.error("Không thể click chọn giá trị Có.")
            raise

    # Hàm kiểm tra xem giá trị Có hiển thị
    def is_value_has_visible(self):
        try:
            value_element = self.get_text(self.locators.SELECT_VALUE_VISIBLE)
            expected_value = "Có"

            if value_element == expected_value:
                logging.info("Hiển thị giá trị Có ở field.")
                return True
            else:
                logging.error(f"Lỗi: Expected: '{expected_value}', nhưng nhận được: '{value_element}'")
                return False
        except TimeoutException:
            return False
        