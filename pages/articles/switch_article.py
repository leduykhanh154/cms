import logging
from locators.locator_article import LocatorArticle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SwitchArticle: 
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorArticle

    # Nhấn vào switch để thay đổi trạng thái (ON/OFF)
    def click_switch(self, switch_label_locator):
        switch_label = self.wait.until(EC.element_to_be_clickable(switch_label_locator))
        switch_label.click()

    # Kiểm tra xem switch có đang bật (ON) không
    def is_switch_on(self, switch_locator):
        switch = self.wait.until(EC.presence_of_element_located(switch_locator))
        return switch.get_attribute("checked") is not None

    # Đặt switch về OFF nếu nó đang bật
    def reset_switch(self, switch_locator, switch_label_locator):
        try:
            if self.is_switch_on(switch_locator):
                logging.info("Switch đang bật (ON). Đang thay đổi sang OFF...")
                self.click_switch(switch_label_locator)  # Nhấn vào switch để đặt về OFF
            else:
                logging.info("Switch đã ở trạng thái OFF.")
        except Exception as e:
            logging.error(f"Lỗi khi đặt lại switch: {e}")
