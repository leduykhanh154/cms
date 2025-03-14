import time
import logging
from utils.login import Login
from utils.driver_setup import get_driver
from selenium.webdriver.common.by import By
from locators.locator_pagev2 import LocatorPageV2
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class PageV2:
    # Khởi tạo instance của PageV2 với driver và các locator
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
    
        # Khởi tạo locators
        self.content_menu = LocatorPageV2.CONTENT_MENU
        self.page_v2_menu = LocatorPageV2.MENU_PAGE_V2
        self.page_v2_list_url = LocatorPageV2.PAGE_V2_LIST_URL
        self.page_v2_create_url = LocatorPageV2.PAGE_V2_CREATE_URL
        self.create_new_button = LocatorPageV2.CREATE_NEW_BUTTON
        self.page_title_input = LocatorPageV2.PAGE_TITLE_INPUT
        self.title_error_message = LocatorPageV2.TITLE_ERROR_MESSAGE
        self.add_section_button = LocatorPageV2.ADD_SECTION_BUTTON
        self.section_news = LocatorPageV2.SECTION_NEWS
        self.add_button = LocatorPageV2.ADD_BUTTON
        self.save_button = LocatorPageV2.SAVE_BUTTON
        self.save_and_continue_button = LocatorPageV2.SAVE_AND_CONTINUE_BUTTON
        self.add_section_popup = LocatorPageV2.ADD_SECTION_POPUP
        self.news_section_display = LocatorPageV2.NEWS_SECTION_DISPLAY
        self.section_list = LocatorPageV2.SECTION_LIST
        self.news_section_error = LocatorPageV2.NEWS_SECTION_ERROR
        self.page_list_wrapper = LocatorPageV2.PAGE_LIST_WRAPPER
        self.rename_section_button = LocatorPageV2.RENAME_SECTION_BUTTON
        self.rename_section_popup = LocatorPageV2.RENAME_SECTION_POPUP
        NUMBER_OF_ARTICLES_INPUT = (By.ID, "root_47mwegrft4_quantity-vi")

    # Hàm nhấn vào một menu cụ thể trong CMS
    def click_menu(self, locator, menu_name, timeout=10):
        try:
            menu = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            menu.click()
            logging.info(f"Đã nhấn menu {menu_name}.")
            return self
        except TimeoutException as e:
            logging.error(f"Không thể nhấn menu {menu_name}: {e}", exc_info=True)
            raise
    
    # Hàm nhấn vào menu 'Nội dung' trong CMS
    def click_content_menu(self):
        self.click_menu(self.content_menu, "Nội dung")
        return self
    
    # Hàm nhấn vào menu 'Page V2' và kiểm tra xem danh sách Page V2 có hiển thị không
    def click_page_v2_menu(self):
        self.click_menu(self.page_v2_menu, "Page V2")
        try:
            self.wait.until(EC.url_to_be(self.page_v2_list_url))
            logging.info("Chuyển hướng thành công đến trang tạo mới Page V2.")
        except Exception:
            logging.error("Không thể chuyển hướng đến trang tạo mới Page V2!")
            raise
        return self
    
    # Hàm nhấn vào nút 'Tạo mới' để tạo trang mới
    def click_create_new_button(self):
        try:
            create_new_button = self.wait.until(EC.element_to_be_clickable(self.create_new_button))
            self.driver.execute_script("arguments[0].click();", create_new_button)
            logging.info("Đã nhấn nút Tạo mới.")

            self.wait.until(EC.url_to_be(self.page_v2_create_url))

            if self.driver.current_url == self.page_v2_create_url:
                logging.info(f"Chuyển hướng thành công đến {self.page_v2_create_url}")
                return True
            else:
                logging.warning(f"Chuyển hướng không thành công. URL hiện tại: {self.driver.current_url}")
                return False
        except Exception as e:
            logging.error(f"Lỗi khi nhấn nút Tạo mới hoặc chuyển hướng: {e}", exc_info=True)
            return False
    
    # Hàm nhập tiêu đề trang
    def enter_page_title(self, title, timeout=10):
        try:
            title_input = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.page_title_input))
            title_input.clear()
            title_input.send_keys(title)
            logging.info(f"Đã nhập tiêu đề trang: {title}")
        except Exception as e:
            logging.error(f"Lỗi khi nhập tiêu đề trang: {e}", exc_info=True)
            raise

    # Hàm kiểm tra xem có thông báo lỗi nào xuất hiện khi nhập tiêu đề không
    def check_title_error_message(self):
        try:
            error_element = self.wait.until(
                EC.visibility_of_element_located(self.title_error_message)
            )
            return error_element.text
        except Exception as e:
            logging.warning(f"Không tìm thấy thông báo lỗi: {e}")
            return None

    # Hàm kiểm tra xem tiêu đề trang đã nhập có hiển thị trong danh sách hay không.
    def is_page_title_in_list(self, expected_title):
        try:
            page_list_wrapper = self.wait.until(
                EC.visibility_of_element_located(self.page_list_wrapper)
            )
            if expected_title in page_list_wrapper.text:
                logging.info(f"Tiêu đề trang '{expected_title}' đã xuất hiện trong danh sách!")
                return True
            else:
                logging.info(f"Tiêu đề trang '{expected_title}' không xuất hiện trong danh sách!")
                return False
        except Exception as e:
            logging.error(f"Lỗi khi kiểm tra tiêu đề trang trong danh sách: {e}", exc_info=True)
            return False
    
    # Hàm nhấn vào nút 'Thêm section' để mở popup thêm section
    def click_add_section_button(self):
        try:
            add_section_button = self.wait.until(EC.element_to_be_clickable(self.add_section_button))
            self.driver.execute_script("arguments[0].click();", add_section_button)
            logging.info("Đã nhấn nút 'Thêm section'.")
            return True
        except Exception as e:
            logging.error(f"Lỗi khi nhấn nút 'Thêm section': {e}", exc_info=True)
            return False
    
    # Hàm kiểm tra xem popup 'Thêm section' có hiển thị không
    def is_add_section_popup_displayed(self):
        try:
            popup_element = self.wait.until(EC.visibility_of_element_located(self.add_section_popup))
            return popup_element.is_displayed()
        except Exception as e:
            logging.error(f"Lỗi khi kiểm tra pop-up thêm section: {e}", exc_info=True)
            return False

    # Hàm chọn checkbox 'News' để thêm section Tin tức
    def click_section_news_checkbox(self):
        try:
            checkbox = self.wait.until(EC.element_to_be_clickable(LocatorPageV2.SECTION_NEWS))
            if not checkbox.is_selected():
                checkbox.click()
                logging.info("Checkbox 'News' đã được chọn.")
            else:
                logging.info("Checkbox 'News' đã được chọn từ trước.")
            return checkbox.is_selected()
        except Exception as e:
            logging.error(f"Lỗi khi nhấn checkbox 'News': {e}", exc_info=True)
            return False
        
    # Hàm nhấn nút 'ADD' để thêm section đã chọn vào trang
    def click_add_button(self):
        try:
            add_button = self.wait.until(EC.element_to_be_clickable(LocatorPageV2.ADD_BUTTON))
            add_button.click()
            logging.info("Đã nhấn nút 'ADD' sau khi thêm section.")
            return True
        except Exception as e:
            logging.error(f"Lỗi khi nhấn nút 'ADD': {e}", exc_info=True)
            return False
    
    # Hàm kiểm tra xem section 'News' có xuất hiện trên trang không
    def is_news_section_displayed(self):
        try:
            news_section_element = self.wait.until(EC.visibility_of_element_located(self.news_section_display))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", news_section_element)
            self.wait.until(EC.visibility_of(news_section_element))
            return news_section_element
        except TimeoutException:
            logging.error("Section 'News' không hiển thị!")
            return None
    
    # Hàm kiểm tra và lấy thông báo lỗi khi không nhập tiêu đề tin tức
    def get_news_section_error_message(self, news_section_element):
        try:
            error_message_element = WebDriverWait(news_section_element, 10).until(
                EC.presence_of_element_located(self.news_section_error)
            )
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", error_message_element)
            self.wait.until(EC.visibility_of(error_message_element))
            return error_message_element.text.strip()
        except TimeoutException:
            return None
        
    # Hàm nhấn vào nút 'Rename section' để đổi tên section
    def click_rename_section(self):
        try:
            rename_button = self.wait.until(EC.element_to_be_clickable(self.rename_section_button))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", rename_button)  
            time.sleep(1) 
            rename_button.click()
            logging.info("Đã nhấn nút Rename section.")
        except Exception as e:
            logging.error("Lỗi khi nhấn nút Rename section: %s", e, exc_info=True)
            raise

    # Hàm kiểm tra xem popup đổi tên section có hiển thị không
    def is_rename_popup_displayed(self):
        try:
            popup = self.wait.until(EC.visibility_of_element_located(self.rename_section_popup))
            return popup.is_displayed()
        except TimeoutException:
            logging.error("Popup Rename không hiển thị!")
            return False 
    
    def enter_number_of_articles(self, value):
        try:
            logging.info(f"🔎 Đang tìm input số lượng bài viết: {self.NUMBER_OF_ARTICLES_INPUT}")
            input_element = self.wait.until(
                EC.presence_of_element_located(self.NUMBER_OF_ARTICLES_INPUT)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", input_element)
            if not input_element.is_enabled():
                logging.error("Input số lượng bài viết bị vô hiệu hóa!")
                return False
            input_element.clear()
            time.sleep(0.5) 
            input_element.send_keys(str(value))
            time.sleep(1)
            actual_value = input_element.get_attribute("value").strip()
            logging.info(f"Giá trị nhập vào: '{actual_value}'")
            return actual_value == str(value)
        except Exception as e:
            logging.error(f"Lỗi khi nhập số vào input: {e}", exc_info=True)
            return False
    
    def get_number_of_articles_value(self):
        try:
            logging.info("Đang lấy giá trị từ input số lượng bài viết...")
            input_element = self.wait.until(
                EC.presence_of_element_located(self.NUMBER_OF_ARTICLES_INPUT)
            )
            actual_value = input_element.get_attribute("value").strip()
            logging.info(f"Giá trị hiện tại trong input: '{actual_value}'")
            return actual_value if actual_value else ""
        except Exception as e:
            logging.error(f"Lỗi khi lấy giá trị từ input: {e}", exc_info=True)
            return ""

    # Hàm nhấn vào nút 'Lưu' để lưu trang hiện tại
    def click_save_button(self):
        try:
            save_button = self.wait.until(EC.element_to_be_clickable(self.save_button))
            self.driver.execute_script("arguments[0].click();", save_button)
            logging.info("Đã nhấn nút Lưu.")
            return True
        except Exception as e:
            logging.error(f"Lỗi khi nhấn nút Lưu: {e}", exc_info=True)
            return False
    
    # Hàm nhấn vào nút 'Lưu và tiếp tục chỉnh sửa' để lưu mà không thoát trang
    def click_save_and_continue_button(self):
        try:
            save_and_continue_button = self.wait.until(EC.element_to_be_clickable(self.save_and_continue_button))
            self.driver.execute_script("arguments[0].click();", save_and_continue_button)
            logging.info("Đã nhấn nút Lưu.")
            return True
        except Exception as e:
            logging.error(f"Lỗi khi nhấn nút Lưu: {e}", exc_info=True)
            return False
    
    # Hàm thực hiện các bước mở menu 'Nội dung', vào 'Page V2' và tạo mới trang
    def perform_tag_operations(self):
        self.click_content_menu()
        self.click_page_v2_menu()
        self.click_create_new_button()

    # Hàm thực hiện các bước thêm section 'News' vào trang
    def add_news_section(self):
        self.click_add_section_button()
        self.is_add_section_popup_displayed()
        self.click_section_news_checkbox()
        self.click_add_button()