import logging
import time
from selenium.webdriver.common.by import By
from locators.faq.locator_createfaq import LocatorCreateFAQ
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CreateFAQBase:
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorCreateFAQ

    def click_menu(self, locator, menu_name):
        try:
            menu = self.wait.until(EC.element_to_be_clickable(locator))
            menu.click()
            logging.info(f"Đã nhấn menu {menu_name}.")
            return self
        except TimeoutException as e:
            logging.error(f"Không thể nhấn menu {menu_name}: {e}", exc_info=True)
            raise

    # Hàm nhấn menu 'Nội dung'
    def click_content_menu(self):
        return self.click_menu(self.locators.CONTENT_MENU, "Nội dung")

    # Hàm nhấn menu 'FAQ'
    def click_faq_menu(self):
        return self.click_menu(self.locators.FAQ_MENU, "FAQ")

    # Hàm nhấn vào button Tạo mới
    def click_create_new_button(self):
        try:
            create_new_button = self.wait.until(EC.element_to_be_clickable(self.locators.CREATE_NEW_BUTTON))
            create_new_button.click()
            logging.info("Đã nhấn vào button Tạo mới.")
        except TimeoutException:
            logging.error("Không thể nhấn vào button Tạo mới.")
            raise
    
    # Hàm nhấn vào button Lưu
    def click_save_button(self):
        try:
            save_button = self.wait.until(EC.element_to_be_clickable(self.locators.CREATE_NEW_BUTTON))
            save_button.click()
            logging.info("Đã nhấn vào button Lưu.")
        except TimeoutException:
            logging.error("Không thể nhấn vào button Lưu.")
            raise

    # Hàm nhấn vào tab Thông tin chung
    def click_general_info_tab(self):
        try:
            general_info_tab = self.wait.until(EC.element_to_be_clickable(self.locators.GENERAL_INFO_TAB))
            general_info_tab.click()
            logging.info("Đã nhấn tab Thông tin chung.")
        except TimeoutException:
            logging.error("Không thể nhấn vào tab Thông tin chung.")
            raise

    # Hàm thực hiện thao tác nhấn menu Nội dung -> menu FAQ
    def navigate_to_faq(self):
        self.click_content_menu()
        self.click_faq_menu()
