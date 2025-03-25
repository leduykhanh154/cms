import logging
from selenium.webdriver.common.by import By
from locators.faq.locator_faq import LocatorFAQ
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FAQBase:
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorFAQ

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
    
    # Hàm nhấn vào breadcrumb 'Trang chủ'
    def click_home_page(self):
        return self.click_menu(self.locators.HOME_PAGE, "Trang chủ")
        
    


    # Hàm thực hiện thao tác nhấn menu Nội dung -> menu FAQ
    def navigate_to_faq(self):
        self.click_content_menu()
        self.click_faq_menu()
