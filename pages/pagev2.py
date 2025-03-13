import time
import logging
from utils.login import Login
from utils.driver_setup import get_driver
from selenium.webdriver.common.by import By
from locators.locator_pagev2 import LocatorPageV2
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

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
        self.rename_text_input = LocatorPageV2.RENAME_TEXT_INPUT

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
    
    # Kiem tra popup Rename hien thi
    def is_rename_popup_displayed(self):
        try:
            popup = self.wait.until(EC.visibility_of_element_located(self.rename_section_popup))
            return popup.is_displayed()
        except TimeoutException:
            logging.error("Popup Rename không hiển thị!")
            return False

    # Kiem tra pop-up Rename dong hay chua
    def is_rename_popup_closed(self):
        try:
            # Kiểm tra nếu phần tử pop-up không còn hiển thị
            self.wait.until_not(EC.visibility_of_element_located(LocatorPageV2.RENAME_SECTION_POPUP))
            logging.info(" Pop-up Rename đã đóng.")
            return True
        except TimeoutException:
            logging.error(" Pop-up Rename vẫn hiển thị!")
            return False

    
    # Click icon Close popup Rename
    def click_icon_close_rename(self):
        try:
            icon_close = self.wait.until(EC.element_to_be_clickable(LocatorPageV2.ICON_CLOSE))
            icon_close.click()
            logging.info("Đã nhấn icon 'Close' trong popup Rename.")
            return True
        except Exception as e:
            logging.error(f"Lỗi khi nhấn icon 'Close' trong popup Rename: {e}", exc_info=True)
            return False

# Click button Close popup Rename
    def click_button_close_rename(self):
        try:
            button_close = self.wait.until(EC.element_to_be_clickable(LocatorPageV2.BUTTON_CLOSE))
            button_close.click()
            logging.info("Đã nhấn button 'Dong' trong popup Rename.")
            return True
        except Exception as e:
            logging.error(f"Lỗi khi nhấn Button 'Dong' trong popup Rename: {e}", exc_info=True)
            return False

    # Click nut Luu
    def click_save_button(self):
        try:
            save_button = self.wait.until(EC.element_to_be_clickable(self.save_button))
            self.driver.execute_script("arguments[0].click();", save_button)
            logging.info("Đã nhấn nút Lưu.")
            return True
        except Exception as e:
            logging.error(f"Lỗi khi nhấn nút Lưu: {e}", exc_info=True)
            return False
    
    # Click nut Luu va tiep tuc cap nhat
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

    # Dien thong tin vao text-input Rename
    def enter_and_verify_rename_text(self, new_name):
        try:
            # Tìm phần tử input và nhập dữ liệu
            rename_input = self.wait.until(EC.presence_of_element_located(LocatorPageV2.RENAME_TEXT_INPUT))
            rename_input.clear()  # Xóa nội dung cũ (nếu có)
            rename_input.send_keys(new_name)
            logging.info(f"Đã nhập '{new_name}' vào ô Rename.")

            # Kiểm tra lại giá trị đã nhập
            entered_text = rename_input.get_attribute("value")
            assert entered_text == new_name, f" Giá trị nhập vào bị sai! Dự kiến: '{new_name}', Thực tế: '{entered_text}'"

            logging.info(" Xác nhận giá trị nhập vào đúng.")

        except Exception as e:
            logging.error(" Lỗi khi nhập hoặc kiểm tra text input Rename: %s", e, exc_info=True)
            raise
    
    # Lay ten section
    def get_section_name(self):
        try:
            section_name_element = self.wait.until(EC.presence_of_element_located(LocatorPageV2.NAME_SECTION))
            section_name = section_name_element.text.strip()
            logging.info(f"Tên section hiện tại: {section_name}")
            return section_name
        except Exception as e:
            logging.error("Lỗi khi lấy tên section: %s", e, exc_info=True)
            return None

    # tim kiem tren trang
    def search_text_on_page(self, keyword, timeout=5):
        try:
            self.wait.until(lambda driver: keyword in driver.page_source, timeout)
            logging.info(f"Tìm thấy từ khóa '{keyword}' trên trang.")
            return True
        except Exception as e:
            logging.error(f"Không tìm thấy từ khóa '{keyword}' trên trang: {e}")
            return False

    # Click nut Luu ten section
    def click_save_rename(self):
        try:
            save_button = self.wait.until(EC.element_to_be_clickable(LocatorPageV2.BUTTON_SAVE_RENAME))
            save_button.click()
            logging.info("Đã nhấn nút Lưu trên pop-up Rename.")
            time.sleep(2)  # Đợi UI cập nhật (tùy vào tốc độ hệ thống, có thể thay bằng WebDriverWait)
        except Exception as e:
            logging.error("Lỗi khi nhấn nút Lưu: %s", e, exc_info=True)
            raise

    # Click icon Collapse section
    def click_collapse_section(self):
        try:
            collapse_icon = self.wait.until(EC.element_to_be_clickable(LocatorPageV2.COLLAPSE_SECTION))
            collapse_icon.click()
            logging.info("Đã nhấn vào icon collapse để thu gọn section.")
            
        except Exception as e:
            logging.error("Lỗi khi nhấn icon collapse: %s", e, exc_info=True)
            raise

    # kiem tra section co duoc thu gon khong
    def is_section_collapsed(self):
        try:
            section_element = self.driver.find_element(*LocatorPageV2.NAME_SECTION)
            return not section_element.is_displayed()  # Nếu bị ẩn thì trả về True
        except Exception:
            return True  # Nếu không tìm thấy element thì có thể nó đã bị ẩn/collapse

    def click_expand_section(self):
        try:
            expand_icon = self.wait.until(EC.element_to_be_clickable(LocatorPageV2.COLLAPSE_SECTION))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", expand_icon)
            time.sleep(1)  # Đợi UI cập nhật
            expand_icon.click()
            logging.info("Đã nhấn vào icon expand để mở rộng section.")
        except Exception as e:
            logging.error("Lỗi khi mở rộng section: %s", e, exc_info=True)
            raise

    # Click vào icon '...' để mở menu
    def click_menu_icon(self):
        try:
            menu_icon = self.wait.until(EC.element_to_be_clickable(LocatorPageV2.MENU_SECTION))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", menu_icon)  
            time.sleep(1)  # Đợi UI ổn định trước khi click
            menu_icon.click()
            logging.info("Đã nhấn vào icon '...' để mở menu.")
        except Exception as e:
            logging.error("Lỗi khi nhấn vào icon menu: %s", e, exc_info=True)
            raise

    # Kiểm tra nút Delete có hiển thị không
    def is_delete_button_displayed(self):
        try:
            delete_button = self.wait.until(EC.presence_of_element_located(LocatorPageV2.DELETE_BUTTON))
            is_displayed = delete_button.is_displayed()
            logging.info(f"Nút Xóa hiển thị: {is_displayed}")
            return is_displayed
        except Exception as e:
            logging.error("Lỗi khi kiểm tra nút Xóa: %s", e, exc_info=True)
            return False

    # Kiểm tra nút Duplicate có hiển thị không
    def is_duplicate_button_displayed(self):
        try:
            duplicate_button = self.wait.until(EC.presence_of_element_located(LocatorPageV2.DUPLICATE_BUTTON))
            is_displayed = duplicate_button.is_displayed()
            logging.info(f"Nút Sao chép hiển thị: {is_displayed}")
            return is_displayed
        except Exception as e:
            logging.error("Lỗi khi kiểm tra nút Sao chép: %s", e, exc_info=True)
            return False

    # Click vào nút Delete trong menu
    def click_delete_button(self):
        try:
            delete_button = self.wait.until(EC.element_to_be_clickable(LocatorPageV2.DELETE_BUTTON))
            delete_button.click()
            logging.info("Đã nhấn vào nút Xóa trong menu.")
        except Exception as e:
            logging.error("Lỗi khi nhấn vào nút Xóa: %s", e, exc_info=True)
            raise

    # Click vào nút Duplicate trong menu
    def click_duplicate_button(self):
        try:
            duplicate_button = self.wait.until(EC.element_to_be_clickable(LocatorPageV2.DUPLICATE_BUTTON))
            duplicate_button.click()
            logging.info("Đã nhấn vào nút Sao chép trong menu.")
        except Exception as e:
            logging.error("Lỗi khi nhấn vào nút Sao chép: %s", e, exc_info=True)
            raise

    # Kiem tra pop-up Confirm delete co hien thi        
    def is_delete_confirmation_popup_displayed(self):
        try:
            popup = self.wait.until(EC.visibility_of_element_located(LocatorPageV2.POPUP_CONFIRM))
            return popup.is_displayed()
        except:
            return False
    
    # Click icon Dong popup Confirm
    def click_close_confirm_popup(self):
        try:
            close_icon = self.wait.until(EC.element_to_be_clickable(LocatorPageV2.ICON_CLOSE_CONFIRM))
            close_icon.click()
            logging.info("Đã nhấn icon 'X' để đóng pop-up xác nhận.")
            time.sleep(1)  # Đợi pop-up đóng
        except Exception as e:
            logging.error("Lỗi khi đóng pop-up xác nhận: %s", e, exc_info=True)
            raise

    
    # Xac nhan xoa
    def confirm_delete_section(self):
        try:
            yes_button = self.wait.until(EC.element_to_be_clickable(LocatorPageV2.BUTTON_YES))
            yes_button.click()
            logging.info("Đã nhấn nút 'Yes' để xác nhận xóa section.")
            time.sleep(2)  # Đợi UI cập nhật sau khi xóa
        except Exception as e:
            logging.error("Lỗi khi xác nhận xóa section: %s", e, exc_info=True)
            raise
    
    # Khong xoa
    def cancel_delete_section(self):
        try:
            no_button = self.wait.until(EC.element_to_be_clickable(LocatorPageV2.BUTTON_NO))
            no_button.click()
            logging.info("Đã nhấn nút 'No' để hủy xóa section.")
            time.sleep(1)  # Đợi pop-up đóng
        except Exception as e:
            logging.error("Lỗi khi hủy xóa section: %s", e, exc_info=True)
            raise

    # Kiem tra section bi xoa chua
    def is_section_news_deleted(self):
        try:
            # Kiểm tra xem phần tử có còn tồn tại hay không
            self.driver.find_element(*LocatorPageV2.SECTION_NEWS)
            logging.info("Section 'News' vẫn còn tồn tại trên giao diện.")
            return False  # Nếu tìm thấy phần tử, tức là chưa bị xóa
        except NoSuchElementException:
            logging.info("Section 'News' đã bị xóa thành công.")
            return True  # Nếu không tìm thấy phần tử, tức là đã bị xóa

    # Click nut Duplicate
    def click_duplicate_button(self):
        try:
            duplicate_button = self.wait.until(EC.element_to_be_clickable(LocatorPageV2.DUPLICATE_BUTTON))
            duplicate_button.click()
            logging.info("Đã nhấn nút 'Duplicate' để sao chép Section News.")
            time.sleep(1)  # Đợi hệ thống xử lý sao chép
        except Exception as e:
            logging.error("Lỗi khi nhấn nút 'Duplicate': %s", e, exc_info=True)
            raise
    
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