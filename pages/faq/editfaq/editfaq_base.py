import logging
import time
from selenium.webdriver.common.by import By
from locators.faq.locator_editfaq import LocatorEditFAQ
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EditFAQBase:
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorEditFAQ

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
    
    # Hàm nhấn vào button Lưu và Tiếp tục cập nhật
    def click_save_continue_button(self):
        try:
            save_continue_button = self.wait.until(EC.element_to_be_clickable(self.locators.SAVE_CONTINUE_BUTTON))
            save_continue_button.click()
            logging.info("Đã nhấn vào button Lưu và Tiếp tục cập nhật.")
        except TimeoutException:
            logging.error("Không thể nhấn vào button Lưu và Tiếp tục cập nhật.")
            raise
    
    # Hàm nhấn vào dòng 'đầu tiên' ở cột 'Câu hỏi'
    def click_edit_first_line(self):
        try:
            edit_first_line = self.wait.until(EC.element_to_be_clickable(self.locators.EDIT_FIRST_LINE))
            edit_first_line.click()
            logging.info("Đã nhấn vào dòng 'đầu tiên' ở cột 'Câu hỏi'.")
        except TimeoutException:
            logging.error("Không thể nhấn vào dòng 'đầu tiên' ở cột 'Câu hỏi'.")
            raise


    
    # Hàm thực hiện thao tác nhấn menu Nội dung -> menu FAQ
    def navigate_to_faq(self):
        self.click_content_menu()
        self.click_faq_menu()