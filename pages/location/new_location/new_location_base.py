import time
import logging
import selenium
from selenium.webdriver.common.by import By
from locators.locator_location.locator_new_location import LocatorNewLocation
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class NewLocatorBase:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorNewLocation 
        
    # Hàm nhấn vào một menu cụ thể trên giao diện
    def click_menu(self, locator, menu_name):
        try:
            menu = self.wait.until(EC.element_to_be_clickable(locator))
            menu.click()
            logging.info(f"Đã nhấn menu {menu_name}.")
            return self
        except TimeoutException as e:
            logging.error(f"Không thể nhấn menu {menu_name}: {e}", exc_info=True)
            raise
    
    # Hàm nhấn vào menu Nội dung
    def click_content_menu(self):
        return self.click_menu(self.locators.CONTENT_MENU, "Nội dung")
    
    # Hàm nhấn vào menu Địa điểm
    def click_location_menu(self):
        self.click_menu(self.locators.LOCATION_MENU, "Địa điểm")
        expected_url = "https://mpire-cms-demo.mpire.asia/cms/dealer?page=1"
        
        try:
            self.wait.until(EC.url_to_be(expected_url))
            logging.info("Trang 'Địa điểm' đã load thành công.")
            return True
        except TimeoutException:
            logging.error("Trang 'Địa điểm' không tải được!")
            return False    

    # Hàm thực hiện thao tác nhấn menu Nội dung -> Nhấn mục Địa điểm
    def perform_tag_operations(self):
        self.click_content_menu()
        self.click_location_menu()
    
    # Hàm nhấn vào nút "Tạo mới" và kiểm tra đường dẫn sau khi chuyển hướng
    def click_create_button(self):
        try:
            create_button = self.wait.until(
                EC.element_to_be_clickable(self.locators.CREATE_BUTTON)
            )

            try:
                create_button.click()
                logging.info("Đã nhấn vào nút 'Thêm loại bài viết mới'.")
            except Exception:
                self.driver.execute_script("arguments[0].click();", create_button)
                logging.info("Đã nhấn vào nút 'Thêm loại bài viết mới' bằng JavaScript.")

            expected_url = "https://mpire-cms-demo.mpire.asia/cms/dealer/create"
            self.wait.until(EC.url_to_be(expected_url))
            logging.info("Trang 'Thêm loại bài viết mới' đã load thành công.")
            return True

        except TimeoutException:
            logging.error("Trang 'Thêm loại bài viết mới' không tải được!")
            return False 