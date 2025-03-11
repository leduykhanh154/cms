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
        self.url_key_input = LocatorPageV2.URL_KEY_INPUT
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

    # Nhấn vào một mục menu bất kỳ trên giao diện
    def click_menu(self, locator, menu_name):
        try:
            menu = self.wait.until(EC.element_to_be_clickable(locator))
            menu.click()
            logging.info(f"Đã nhấn menu {menu_name}.")
            return self
        except Exception as e:
            logging.error(f"Lỗi khi nhấn menu {menu_name}: {e}", exc_info=True)
            raise
    
    # Nhấn vào menu "Nội dung" trong giao diện
    def click_content_menu(self):
        self.click_menu(self.content_menu, "Nội dung")
        return self
    
    # Nhấn vào menu "Page V2" trong giao diện
    def click_page_v2_menu(self):
        self.click_menu(self.page_v2_menu, "Page V2")
        try:
            self.wait.until(EC.url_to_be(self.page_v2_list_url))
            logging.info("Chuyển hướng thành công đến trang tạo mới Page V2.")
        except Exception:
            logging.error("Không thể chuyển hướng đến trang tạo mới Page V2!")
            raise
        return self
    
    # Nhấn nút "Tạo mới" để mở trang tạo PageV2
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
    
    # Nhập tiêu đề cho trang PageV2
    def enter_page_title(self, title):
        try:
            title_input = self.wait.until(EC.visibility_of_element_located(self.page_title_input))
            title_input.clear() 
            title_input.send_keys(title)
            logging.info(f"Đã nhập tiêu đề trang: {title}")
        except Exception as e:
            logging.error(f"Lỗi khi nhập tiêu đề trang: {e}", exc_info=True)
            raise

    # Kiểm tra và lấy thông báo lỗi của trường tiêu đề trang
    def check_title_error_message(self):
        try:
            error_element = self.wait.until(
                EC.visibility_of_element_located(self.title_error_message)
            )
            return error_element.text
        except Exception as e:
            logging.warning(f"Không tìm thấy thông báo lỗi: {e}")
            return None
    
    # Kiểm tra tiêu đề trang có xuất hiện trong danh sách PageV2 không
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
    
    # Nhập đường dẫn (URL key) cho trang PageV2
    def enter_url_key_vi(self, url_key):
        try:
            url_input = self.wait.until(EC.visibility_of_element_located(LocatorPageV2.URL_KEY_VI_INPUT))
            url_input.clear()
            url_input.send_keys(url_key)
            logging.info(f"Đã nhập đường dẫn: {url_key}")
            return True
        except Exception as e:
            logging.error(f"Lỗi khi nhập đường dẫn: {e}", exc_info=True)
            return False
    
    # Nhấn nút "Thêm section" để mở popup thêm section
    def click_add_section_button(self):
        try:
            add_section_button = self.wait.until(EC.element_to_be_clickable(self.add_section_button))
            self.driver.execute_script("arguments[0].click();", add_section_button)
            logging.info("Đã nhấn nút 'Thêm section'.")
            return True
        except Exception as e:
            logging.error(f"Lỗi khi nhấn nút 'Thêm section': {e}", exc_info=True)
            return False
    
    # Kiểm tra popup thêm section có hiển thị không
    def is_add_section_popup_displayed(self):
        try:
            popup_element = self.wait.until(EC.visibility_of_element_located(self.add_section_popup))
            return popup_element.is_displayed()
        except Exception as e:
            logging.error(f"Lỗi khi kiểm tra pop-up thêm section: {e}", exc_info=True)
            return False

    def is_section_news_present(self):
        try:
            # Chờ phần tử xuất hiện trên giao diện
            news_section = self.wait.until(
                EC.presence_of_element_located(LocatorPageV2.SECTION_NEWS)
            )
            
            if news_section.is_displayed():
                logging.info("Section 'News' đã xuất hiện trên giao diện.")
                return True
            else:
                logging.info("Section 'News' KHÔNG hiển thị trên giao diện.")
                return False
        except Exception as e:
            logging.error(f"Lỗi khi tìm section 'News': {e}", exc_info=True)
            return False


    # Nhấn checkbox "News" trong popup thêm section
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
    
    # Nhấn nút "ADD" trong popup để thêm section
    def click_add_button(self):
        try:
            add_button = self.wait.until(EC.element_to_be_clickable(LocatorPageV2.ADD_BUTTON))
            add_button.click()
            logging.info("Đã nhấn nút 'ADD' sau khi thêm section.")
            return True
        except Exception as e:
            logging.error(f"Lỗi khi nhấn nút 'ADD': {e}", exc_info=True)
            return False
    
    # Kiểm tra section "News" có hiển thị trong danh sách section không
    def is_news_section_displayed(self):
        try:
            news_section_element = self.wait.until(EC.visibility_of_element_located(self.news_section_display))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", news_section_element)
            self.wait.until(EC.visibility_of(news_section_element))
            return news_section_element
        except TimeoutException:
            logging.error("Section 'News' không hiển thị!")
            return None

    # Lấy thông báo lỗi của Tiêu đề tin tức
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
    
    # Nhấn nút "Lưu" để lưu trang PageV2
    def click_save_button(self):
        try:
            save_button = self.wait.until(EC.element_to_be_clickable(self.save_button))
            self.driver.execute_script("arguments[0].click();", save_button)
            logging.info("Đã nhấn nút Lưu.")
            return True
        except Exception as e:
            logging.error(f"Lỗi khi nhấn nút Lưu: {e}", exc_info=True)
            return False
    
    # Nhấn nút "Lưu và tiếp tục cập nhật" để lưu trang PageV2
    def click_save_and_continue_button(self):
        try:
            logging.info("Đang tìm nút Lưu và tiếp tục cập nhật...")
            save_and_continue_button = self.wait.until(
                EC.element_to_be_clickable(self.save_and_continue_button)
            )
            logging.info("Tìm thấy nút, thực hiện click bằng JavaScript...")
            
            self.driver.execute_script("arguments[0].click();", save_and_continue_button)
            logging.info("Đã nhấn nút Lưu và tiếp tục cập nhật.")
            return True
        except Exception as e:
            logging.error(f"Lỗi khi nhấn nút Lưu và tiếp tục cập nhật: {e}", exc_info=True)
            return False

    
    def perform_tag_operations(self):
        self.click_content_menu()
        self.click_page_v2_menu()
        self.click_create_new_button()
