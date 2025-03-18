import time
import logging
from utils.login import Login
from utils.driver_setup import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from locators.locator_tag import LocatorTag
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Tag:
    # Khởi tạo instance của Tag với driver và các locator
    def __init__(self, driver, timeout=5):
        if not driver: 
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

        # Khởi tạo locators
        self.content_menu = LocatorTag.CONTENT_MENU
        self.article_menu = LocatorTag.ARTICLE_MENU
        self.tag_menu = LocatorTag.TAG_MENU
        self.home_page = LocatorTag.HOME_PAGE
        self.tag_list_url = LocatorTag.TAG_LIST_URL
        self.home_page_url = LocatorTag.HOME_PAGE_URL
        self.page_v2_create_url = LocatorTag.PAGE_V2_CREATE_URL
        self.page_list_wrapper = LocatorTag.PAGE_LIST_WRAPPER
        self.tag_list_wrapper = LocatorTag.TAG_LIST_WRAPPER
        self.dropdown_status = LocatorTag.DROPDOWN_STATUS
        self.dropdown_status_display = LocatorTag.DROPDOWN_STATUS_DISPLAY
        self.dropdown_page = LocatorTag.DROPDOWN_PAGE

        self.operation_button = LocatorTag.OPERATION_BUTTON
        self.yes_button = LocatorTag.YES_BUTTON
        self.dropdown_operation_display = LocatorTag.DROPDOWN_OPERATION_DISPLAY
        
        self.add_keyword_button = LocatorTag.ADD_KEYWORD_BUTTON
        self.add_keyword_popup = LocatorTag.ADD_KEYWORD_POPUP
        self.delete_popup = LocatorTag.DELETE_POPUP
        self.tag_name_input = LocatorTag.TAG_NAME_INPUT
        self.save_button = LocatorTag.SAVE_BUTTON
        self.tag_name_error_message = LocatorTag.TAG_NAME_ERROR_MESSAGE
        self.tag_name_valid = LocatorTag.TAG_NAME_VALID

        self.checkbox_first = LocatorTag.CHECKBOX_FIRST

    
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
        time.sleep(1) 
        self.click_menu(self.content_menu, 'Nội dung')
        return self
    
    # Hàm nhấn vào menu 'Bài viết -> Tag' và kiểm tra xem Danh Sách Tag có hiển thị không
    def click_tag_menu(self):
        time.sleep(1)
        self.click_menu(self.article_menu, "Bài viết")
        time.sleep(1)
        self.click_menu(self.tag_menu, 'Tag')
        try:
            self.wait.until(EC.url_to_be(self.tag_list_url))
            logging.info("Chuyển hướng thành công đến trang Danh sách Tag.")
        except Exception:
            logging.error("Không thể chuyển hướng đến trang Danh sách Tag!")
            raise
        return self
    
    # Hàm nhấn vào breadcrumb 'Trang chủ' và kiểm tra hệ thống có chuyển hướng sang 'Trang chủ' hay không
    def click_home_page(self):
        self.click_menu(self.home_page, "Trang chủ")
        try:
            self.wait.until(EC.url_to_be(self.home_page_url))
            logging.info("Chuyển hướng thành công đến Trang chủ.")
        except Exception:
            logging.error("Không thể chuyển hướng đến Trang chủ!")
            raise
        return self
    
    # Hàm nhấn vào button 'Thêm từ khóa'
    def click_add_keyword_button(self):
        try:
            add_keyword_button = self.wait.until(EC.element_to_be_clickable(self.add_keyword_button))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_keyword_button)  
            time.sleep(1) 
            add_keyword_button.click()
            logging.info("Đã nhấn nút 'Thêm từ khóa'.")
        except Exception as e:
            logging.error("Lỗi khi nhấn nút 'Thêm từ khóa': %s", e, exc_info=True)
            raise
    
    # Hàm kiểm tra xem pop-up 'Thêm từ khóa' có hiển thị không
    def is_add_keyword_popup_displayed(self):
        try:
            time.sleep(1)
            popup_element = self.wait.until(EC.visibility_of_element_located(self.add_keyword_popup))
            return popup_element.is_displayed()
        except TimeoutException:
            logging.error("Pop-up 'Thêm từ khóa' không hiển thị!")
            return False
        
    # Hàm nhập Tên tag*
    def enter_tag_name(self, title, timeout=10):
        try:
            tag_name_input = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.tag_name_input))
            tag_name_input.clear()
            tag_name_input.send_keys(title)
            logging.info(f"Đã nhập tiêu đề trang: {title}")
        except Exception as e:
            logging.error(f"Lỗi khi nhập tiêu đề trang: {e}", exc_info=True)
            raise

    # Hàm nhấn vào nút 'Lưu' để lưu trong pop-up 'Thêm từ khóa'
    def click_save_button(self):
        try:
            save_button = self.wait.until(EC.element_to_be_clickable(self.save_button))
            self.driver.execute_script("arguments[0].click();", save_button)
            logging.info("Đã nhấn nút Lưu.")
            time.sleep(2)
            return True
        except Exception as e:
            logging.error(f"Lỗi khi nhấn nút Lưu: {e}", exc_info=True)
            return False
        
    # Hàm kiểm tra xem có thông báo lỗi nào xuất hiện khi nhập 'Tên tag' không
    def check_tag_name_error_message(self):
        try:
            error_element = self.wait.until(
                EC.visibility_of_element_located(self.tag_name_error_message)
            )
            return error_element.text
        except Exception as e:
            logging.warning(f"Không tìm thấy thông báo lỗi: {e}")
            return None
        
    # Hàm kiểm tra xem 'Tên tag' đã nhập có hiển thị trong 'Danh sách Tag' hay không.
    def is_tag_name_in_list(self, expected_tagname):
        try:
            tag_list_wrapper = self.wait.until(
                EC.visibility_of_element_located(self.tag_list_wrapper)
            )
            if expected_tagname in tag_list_wrapper.text:
                logging.info(f"Tên tag '{expected_tagname}' đã xuất hiện trong danh sách!")
                return True
            else:
                logging.info(f"Tên tag '{expected_tagname}' không xuất hiện trong danh sách!")
                return False
        except Exception as e:
            logging.error(f"Lỗi khi kiểm tra tên tag trong danh sách: {e}", exc_info=True)
            return False
        
    # Hàm kiểm tra xem 'Tên tag' có xóa trong 'Danh sách Tag' hay không.
    def is_delete_tag_name_in_list(self, expected_tagname):
        try:
            tag_list_wrapper = self.wait.until(
                EC.visibility_of_element_located(self.tag_list_wrapper)
            )
            if not expected_tagname in tag_list_wrapper.text:
                logging.info(f"Tên tag '{expected_tagname}' không xuất hiện trong danh sách!")
                return True
            else:
                logging.info(f"Tên tag '{expected_tagname}' xuất hiện trong danh sách!")
                return False
        except Exception as e:
            logging.error(f"Lỗi khi kiểm tra tên tag trong danh sách: {e}", exc_info=True)
            return False
        
    # Hàm nhấn vào dropdown 'Trạng thái'
    def click_status_dropdown(self):
        try:
            select_element = self.wait.until(EC.element_to_be_clickable(self.dropdown_status))
            select_element.click()
            logging.info("Đã mở dropdown 'Trạng thái'.")
        except TimeoutException:
            logging.error("Không thể mở dropdown 'Trạng thái'.")
            raise

    # Hàm kiểm tra dropdown 'Trạng thái' có hiển thị không
    def is_status_dropdown_visible(self):
        try:
            dropdown_element = self.wait.until(EC.visibility_of_element_located(self.dropdown_status_display))
            return dropdown_element.is_displayed()
        except TimeoutException:
            return False
        
    # Hàm nhấn vào dropdown 'Trang'
    def click_quantity_page(self):
        try:
            select_element = self.wait.until(EC.element_to_be_clickable(self.dropdown_page))
            select_element.click()
            logging.info("Đã mở dropdown 'Trang'.")
            time.sleep(1)
            select_quantityPage = Select(select_element)
            select_quantityPage.select_by_value('2')
            logging.info("Đã select '2/TRANG' trong dropdown 'Trang'.")
        except TimeoutException:
            logging.error("Không thể mở dropdown 'Trang'.")
            raise

    # Hàm nhấn vào button 'Thao tác'
    def click_operation_button(self):
        try:
            operation_button = self.wait.until(EC.element_to_be_clickable(self.operation_button))
            operation_button.click()
            logging.info("Đã nhấn vào button 'Thao tác'.")
        except TimeoutException:
            logging.error("Không thể nhấn vào 'Thao tác'.")
            raise

    # Hàm kiểm tra dropdown của button 'Thao tác' có hiển thị không
    def is_operation_button_dropdown_visible(self):
        try:
            dropdown_element = self.wait.until(EC.visibility_of_element_located(self.dropdown_operation_display))
            return dropdown_element.is_displayed()
        except TimeoutException:
            return False 
        
        
    # Hàm chọn checkbox 'đầu tiên'
    def click_checkbox_first(self):
        try:
            checkbox = self.wait.until(EC.element_to_be_clickable(self.checkbox_first))
            if not checkbox.is_selected():
                checkbox.click()
                logging.info("Checkbox 'đầu tiên' đã được chọn.")
            else:
                logging.info("Checkbox 'đầu tiên' đã được chọn từ trước.")
            return checkbox.is_selected()
        except Exception as e:
            logging.error(f"Lỗi khi nhấn checkbox 'đầu tiên': {e}", exc_info=True)
            return False
        
    # Hàm select dropdown 'Xóa' trong button 'Thao tác'
    def click_delete_dropdown(self):
        try:
            delete_dropdown = self.wait.until(EC.element_to_be_clickable(self.dropdown_operation_display))
            delete_dropdown.click()
            logging.info("Đã nhấn vào dropdown 'Xóa'.")
        except TimeoutException:
            logging.error("Không thể nhấn vào dropdown 'Xóa'.")
            raise
     
    # Hàm kiểm tra xem popup 'Xóa' có hiển thị không
    def is_delete_popup_displayed(self):
        try:
            time.sleep(1)
            popup_element = self.wait.until(EC.visibility_of_element_located(self.delete_popup))
            return popup_element.is_displayed()
        except Exception as e:
            logging.error(f"Lỗi khi kiểm tra pop-up 'Xóa': {e}", exc_info=True)
            return False
    
    # Hàm nhấn vào button 'Có' trong popup 'Xóa'
    def click_yes_button(self):
        try:
            yes_button = self.wait.until(EC.element_to_be_clickable(self.yes_button))
            yes_button.click()
            time.sleep(1)
            logging.info("Đã nhấn vào button 'Có'.")
        except TimeoutException:
            logging.error("Không thể nhấn vào button'Có'.")
            raise
        



    # Hàm thực hiện các bước mở menu 'Nội dung', vào menu 'Bài viết -> Tag'
    def perform_tag_operations(self):
        self.click_content_menu()
        self.click_tag_menu()
