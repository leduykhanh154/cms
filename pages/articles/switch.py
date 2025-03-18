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

    def click_switch(self, switch_label_locator):
        switch_label = self.wait.until(EC.element_to_be_clickable(switch_label_locator))
        switch_label.click()

    def is_switch_on(self, switch_locator):
        switch = self.wait.until(EC.presence_of_element_located(switch_locator))
        return switch.get_attribute("checked") is not None

    def reset_switch(self, switch_locator, switch_label_locator):
        if self.is_switch_on(switch_locator):
            self.click_switch(switch_label_locator) 
    
    