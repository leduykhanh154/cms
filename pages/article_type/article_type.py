import time
import logging
import selenium
from selenium.webdriver.common.by import By
from locators.locator_article_type.locator_type import LocatorArticleType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class ArticleTypeBase:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorArticleType  
    
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

    # Hàm nhấn vào menu Bài viết
    def click_article_menu(self):
        return self.click_menu(self.locators.ARTICLE_MENU, "Bài viết")

    # Hàm nhấn vào menu Loai bai viet
    def click_article_type_menu(self):
        self.click_menu(self.locators.ARTICLE_TYPE_MENU, "Loại bài viết")
        expected_url = "https://mpire-cms-demo.mpire.asia/cms/category?page=1"
        
        try:
            self.wait.until(EC.url_to_be(expected_url))
            logging.info("Trang 'Loại bài viết' đã load thành công.")
            return True
        except TimeoutException:
            logging.error("Trang 'Loại bài viết' không tải được!")
            return False
    
    # Hàm nhấn vào Trang chủ trên breadcrumb
    def click_breadcrumb_home(self):
        try:
            breadcrumb_home = self.wait.until(EC.element_to_be_clickable(self.locators.BREADCRUMB_HOME))
            breadcrumb_home.click()
            logging.info("Đã nhấn vào breadcrumb 'Trang chủ'.")

            expected_url = "https://mpire-cms-demo.mpire.asia/cms/dashboard"
            self.wait.until(EC.url_to_be(expected_url))
            logging.info("Trang 'Trang chủ' đã load thành công.")
            return True

        except TimeoutException:
            logging.error("Trang 'Trang chủ' không tải được!")
            return False

    # Hàm nhấn vào nút "Tạo mới" và kiểm tra đường dẫn sau khi chuyển hướng
    def click_new_article_type_button(self):
        try:
            new_article_type_button = self.wait.until(
                EC.element_to_be_clickable(self.locators.NEW_TYPE_BUTTON)
            )

            try:
                new_article_type_button.click()
                logging.info("Đã nhấn vào nút 'Thêm loại bài viết mới'.")
            except Exception:
                self.driver.execute_script("arguments[0].click();", new_article_type_button)
                logging.info("Đã nhấn vào nút 'Thêm loại bài viết mới' bằng JavaScript.")

            expected_url = "https://mpire-cms-demo.mpire.asia/cms/category/create"
            self.wait.until(EC.url_to_be(expected_url))
            logging.info("Trang 'Thêm loại bài viết mới' đã load thành công.")
            return True

        except TimeoutException:
            logging.error("Trang 'Thêm loại bài viết mới' không tải được!")
            return False
    
    # Ham click dropdown status
    def click_dropdown_status(self):
        try:
            dropdown_status = self.wait.until(
                EC.element_to_be_clickable(self.locators.DROPDOWN_STATUS)
            )
            try:
                dropdown_status.click()
                logging.info("Đã nhấn vào dropdown 'Trạng thái'.")
            except Exception:
                self.driver.execute_script("arguments[0].click();", dropdown_status)
                logging.info("Đã nhấn vào dropdown 'Trạng thái' bằng JavaScript.")

            return True

        except TimeoutException:
            logging.error("Không thể nhấn vào dropdown 'Trạng thái' do Timeout!")
            return False
    
    # # Ham click chon status kich hoat
    # def click_item_active(self):
    #     try:
    #         item_active = self.wait.until(
    #             EC.element_to_be_clickable(self.locators.ITEM_ACTIVE)
    #         )

    #         try:
    #             item_active.click()
    #             logging.info("Đã chọn trạng thái 'Kích hoạt'.")
    #         except Exception:
    #             self.driver.execute_script("arguments[0].click();", item_active)
    #             logging.info("Đã chọn trạng thái 'Kích hoạt' bằng JavaScript.")

    #         return True

    #     except TimeoutException:
    #         logging.error("Không thể chọn trạng thái 'Kích hoạt' do Timeout!")
    #         return False
    
    # Ham click datepicker Tu ngay
    def click_datepicker_from(self):
        try:
            datepicker_from = self.wait.until(
                EC.element_to_be_clickable(self.locators.DATEPICKER_FROM)
            )
            datepicker_from.click()
            logging.info("Đã nhấn vào Datepicker 'Từ ngày'.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào Datepicker 'Từ ngày'.")
            return False
    
    # Ham click datepicker 'Den ngay'
    def click_datepicker_to(self):
        try:
            datepicker_to = self.wait.until(
                EC.element_to_be_clickable(self.locators.DATEPICKER_TO)
            )
            datepicker_to.click()
            logging.info("Đã nhấn vào Datepicker 'Đến ngày'.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào Datepicker 'Đến ngày'.")
            return False

    # Ham click dropdown 'Loai bai viet cap cha'
    def click_dropdown_father_type(self):
        try:
            dropdown_father_type = self.wait.until(
                EC.element_to_be_clickable(self.locators.DROPDOWN_FATHER_TYPE)
            )
            dropdown_father_type.click()
            logging.info("Đã nhấn vào Dropdown 'Loại cha'.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào Dropdown 'Loại cha'.")
            return False

    # Ham click nut Tai lai
    def click_reset_button(self):
        try:
            reset_button = self.wait.until(
                EC.element_to_be_clickable(self.locators.RESET_BUTTON)
            )
            reset_button.click()
            logging.info("Đã nhấn vào nút 'Tai lai'.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào nút 'Tai lai'.")
            return False
    
    # Ham click dropdown 'Phan trang'
    def click_pagination_dropdown(self):
        try:
            pagination_dropdown = self.wait.until(
                EC.element_to_be_clickable(self.locators.DROPDOWN_SPLIT)
            )
            pagination_dropdown.click()
            logging.info("Đã nhấn vào dropdown phân trang 'Split'.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào dropdown phân trang 'Split'.")
            return False
    
    # Ham click nut 'Thao tac'
    def click_operate_button(self):
        try:
            operate_button = self.wait.until(
                EC.element_to_be_clickable(self.locators.OPERATE_BUTTON)
            )
            operate_button.click()
            logging.info("Đã nhấn vào nút 'Thao tác'.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào nút 'Thao tác'.")
            return False

    # Ham click nut xoa
    def click_delete_button(self):
        try:
            delete_button = self.wait.until(
                EC.element_to_be_clickable(self.locators.DELETE_BUTTON)
            )
            delete_button.click()
            logging.info("Đã nhấn vào nút 'Xóa'.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào nút 'Xóa'!")
            return False

    # Ham click checkbox 'Select all'
    def click_select_all_checkbox(self):
        try:
            select_all_checkbox = self.wait.until(
                EC.element_to_be_clickable(self.locators.SELECT_ALL)
            )
            select_all_checkbox.click()
            logging.info("Đã nhấn vào checkbox 'Select All'.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào checkbox 'Select All'.")
            return False
        
    # Ham click checkbox dau tien
    def click_select_first_checkbox(self):
        try:
            select_first_checkbox = self.wait.until(
                EC.element_to_be_clickable(self.locators.SELECT_FIRST)
            )
            select_first_checkbox.click()
            logging.info("Đã nhấn vào checkbox 'Select First'.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào checkbox 'Select First'.")
            return False
    
    # Ham click Ten loai bai viet dau tien
    def click_first_link(self):
        try:
            # Chờ liên kết đầu tiên xuất hiện
            first_link = self.wait.until(
                EC.element_to_be_clickable(self.locators.FIRST_LINK)
            )

            # Lấy nội dung text của liên kết
            link_text = first_link.text.strip()
            logging.info(f"Lấy text của liên kết đầu tiên: '{link_text}'")

            # Click vào liên kết
            first_link.click()
            logging.info("Đã nhấn vào liên kết đầu tiên.")

            return link_text  # Trả về text để sử dụng trong test case
        except TimeoutException:
            logging.error("Không tìm thấy liên kết đầu tiên để nhấn.")
            return None
    
    # Lay text cua hang dau tien
    def get_first_link_text(self):
        try:
            first_link = self.wait.until(
                EC.element_to_be_clickable(self.locators.FIRST_LINK)
            )

            # Thử lấy text theo cách thông thường
            first_link_text = first_link.text.strip()

            # Nếu text rỗng, thử lấy bằng JavaScript
            if not first_link_text:
                first_link_text = self.driver.execute_script("return arguments[0].textContent;", first_link).strip()

            if first_link_text:
                logging.info(f"Đã lấy được text của liên kết đầu tiên: '{first_link_text}'")
                return first_link_text
            else:
                logging.error("Không lấy được text của liên kết đầu tiên (text rỗng).")
                return None

        except TimeoutException:
            logging.error("Không tìm thấy liên kết đầu tiên trong thời gian chờ!")
            return None

    # Ham click icon '...' doc cua hang dau tien
    def click_first_menu_button(self):
        try:
            first_menu_button = self.wait.until(
                EC.element_to_be_clickable(self.locators.FIRST_MENU_BUTTON)
            )
            first_menu_button.click()
            logging.info("Đã nhấn vào nút menu đầu tiên.")

            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào nút menu đầu tiên!")
            return False
        
    # Ham click nut 'Chi tiet'
    def click_detail_button(self):
        try:
            detail_button = self.wait.until(
                EC.element_to_be_clickable(self.locators.DETAIL_BUTTON)
            )
            detail_button.click()
            logging.info("Đã nhấn vào menu-item 'Chi tiết' thành công.")
            return True
        except TimeoutException:
            logging.error("Không tìm thấy hoặc không thể nhấn vào menu-item 'Chi tiết'.")
            return False

    # Click menu-item 'Xoa'
    def click_item_delete_button(self):
        try:
            delete_button = self.wait.until(
                EC.element_to_be_clickable(self.locators.DELETE2_BUTTON)
            )
            delete_button.click()
            logging.info("Đã nhấn vào nút 'Xóa' trong menu thả xuống.")

            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào nút 'Xóa' hoặc trang không phản hồi!")
            return False
    
    # Kiem tra xem loai bai viet dau con khong
    def is_first_article_text_changed(self, old_text):
        try:
            # Lấy lại text của liên kết đầu tiên sau khi thực hiện xóa
            new_text = self.get_first_link_text()

            if new_text is None:
                logging.error("Không thể lấy text của liên kết đầu tiên sau khi xóa. Có thể danh sách đã trống hoặc gặp lỗi.")
                return False

            if new_text != old_text:
                logging.info(f"Text của liên kết đầu tiên đã thay đổi: '{old_text}' -> '{new_text}'")
                return True
            else:
                logging.info("Text của liên kết đầu tiên không thay đổi sau khi thực hiện xóa.")
                return False
        except Exception as e:
            logging.error(f"Lỗi khi kiểm tra text của liên kết đầu tiên: {str(e)}")
            return False

    # Ham verify duong dan 
    def verify_current_url(self, expected_url):
        try:
            current_url = self.driver.current_url
            if current_url == expected_url:
                logging.info(f"URL hiện tại khớp với mong đợi: {expected_url}")
                return True
            else:
                logging.error(f"URL không đúng! Expected: {expected_url}, Actual: {current_url}")
                return False
        except Exception as e:
            logging.error(f"Lỗi khi kiểm tra URL: {str(e)}")
            return False

    # Hàm thực hiện thao tác nhấn menu Nội dung -> menu Bài viết
    def navigate_to_article(self):
        self.click_content_menu()
        self.click_article_menu()

    # Hàm thực hiện thao tác nhấn menu Nội dung 
    def perform_tag_operations(self):
        self.navigate_to_article()
        self.click_article_type_menu()