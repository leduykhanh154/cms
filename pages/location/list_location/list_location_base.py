import time
import logging
import selenium
from selenium.webdriver.common.by import By
from locators.locator_location.locator_list_location import LocatorListLocation
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class ListLocationBase:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorListLocation  
        
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
    
    # Hàm nhấn vào Trang chủ trên breadcrumb
    def click_breadcrumb_home(self):
        try:
            breadcrumb_home = self.wait.until(EC.element_to_be_clickable(self.locators.HOME_BREADCRUMB))
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
    def click_create_button(self):
        try:
            create_button = self.wait.until(
                EC.element_to_be_clickable(self.locators.CREATE_BUTTON)
            )

            try:
                create_button.click()
                logging.info("Đã nhấn vào nút 'Tạo mới'.")
            except Exception:
                self.driver.execute_script("arguments[0].click();", create_button)
                logging.info("Đã nhấn vào nút 'Tạo mới' bằng JavaScript.")

            expected_url = "https://mpire-cms-demo.mpire.asia/cms/dealer/create"
            self.wait.until(EC.url_to_be(expected_url))
            logging.info("Trang 'Tạo mới' đã load thành công.")
            return True

        except TimeoutException:
            logging.error("Trang 'Tạo mới chi nhánh' không tải được!")
            return False

    # Ham click dropdown 'Tỉnh/Thành phố'
    def click_province_dropdown(self):
        try:
            dropdown_province = self.wait.until(
                EC.element_to_be_clickable(self.locators.PROVINCE_DROPDOWN)
            )
            try:
                dropdown_province.click()
                logging.info("Đã nhấn vào dropdown 'Tỉnh/Thành phố'.")
            except Exception:
                self.driver.execute_script("arguments[0].click();", dropdown_province)
                logging.info("Đã nhấn vào dropdown 'Tỉnh/Thành phố' bằng JavaScript.")

            return True

        except TimeoutException:
            logging.error("Không thể nhấn vào dropdown 'Tỉnh/Thành phố' do Timeout!")
            return False

    # Hàm click chọn Tỉnh/Thành phố đầu tiên
    def click_first_item_province(self):
        try:
            first_item_province = self.wait.until(
                EC.element_to_be_clickable(self.locators.FIRST_ITEM_PROVINCE)
            )
            try:
                first_item_province.click()
                logging.info("Đã nhấn vào Tỉnh/Thành phố đầu tiên.")
            except Exception:
                self.driver.execute_script("arguments[0].click();", first_item_province)
                logging.info("Đã nhấn vào Tỉnh/Thành phố đầu tiên bằng JavaScript.")

            return True

        except TimeoutException:
            logging.error("Không thể nhấn vào Tỉnh/Thành phố do Timeout!")
            return False

    # Ham click dropdown 'Huyện/Quận'
    def click_district_dropdown(self):
        try:
            dropdown_district = self.wait.until(
                EC.element_to_be_clickable(self.locators.DISTRICT_DROPDOWN)
            )
            try:
                dropdown_district.click()
                logging.info("Đã nhấn vào dropdown 'Huyện/Quận'.")
            except Exception:
                self.driver.execute_script("arguments[0].click();", dropdown_district)
                logging.info("Đã nhấn vào dropdown 'Huyện/Quận' bằng JavaScript.")

            return True

        except TimeoutException:
            logging.error("Không thể nhấn vào dropdown 'Huyện/Quận' do Timeout!")
            return False

    # Hàm click chọn Huyện/Quận đầu tiên
    def click_first_item_district(self):
        try:
            first_item_district = self.wait.until(
                EC.element_to_be_clickable(self.locators.FIRST_ITEM_DISTRICT)
            )
            first_item_district.click()
            logging.info("Đã nhấn vào Datepicker 'Từ ngày'.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào Datepicker 'Từ ngày'.")
            return False

    # Hàm click datepicker 'Từ ngày'
    def click_from_date_datepicker(self):
        try:
            from_date_datepicker = self.wait.until(
                EC.element_to_be_clickable(self.locators.FROM_DATE_DATEPICKER)
            )
            from_date_datepicker.click()
            logging.info("Đã nhấn vào Datepicker 'Từ ngày'.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào Datepicker 'Từ ngày'.")
            return False
    
    # Ham click datepicker 'Đến ngày'
    def click_to_date_datepicker(self):
        try:
            _to_date_datepicker = self.wait.until(
                EC.element_to_be_clickable(self.locators.TO_DATE_DAYEPICKER)
            )
            _to_date_datepicker.click()
            logging.info("Đã nhấn vào Datepicker 'Đến ngày'.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào Datepicker 'Đến ngày'.")
            return False

    # Ham click dropdown 'Trạng thái'
    def click_status_dropdown(self):
        try:
            status_dropdown = self.wait.until(
                EC.element_to_be_clickable(self.locators.STATUS_DROPDOWN)
            )
            try:
                status_dropdown.click()
                logging.info("Đã nhấn vào dropdown 'Trạng thái'.")
            except Exception:
                self.driver.execute_script("arguments[0].click();", status_dropdown)
                logging.info("Đã nhấn vào dropdown 'Trạng thái' bằng JavaScript.")

            return True

        except TimeoutException:
            logging.error("Không thể nhấn vào dropdown 'Trạng thái' do Timeout!")
            return False

    # Hàm chọn trạng thái 'Kích hoạt'
    def click_active_status(self):
        try:
            active_status = self.wait.until(
                EC.element_to_be_clickable(self.locators.ACTIVE_STATUS)
            )
            try:
                active_status.click()
                logging.info("Đã nhấn vào trạng thái 'Kích hoạt'.")
            except Exception:
                self.driver.execute_script("arguments[0].click();", active_status)
                logging.info("Đã nhấn vào trạng thái 'Kích hoạt' bằng JavaScript.")

            return True

        except TimeoutException:
            logging.error("Không thể nhấn vào trạng thái 'Kích hoạt' do Timeout!")
            return False
    
    # Hàm chọn trạng thái 'Chờ xử lý'
    def click_processing_status(self):
        try:
            dropdown_district = self.wait.until(
                EC.element_to_be_clickable(self.locators.PROCESSING_STATUS)
            )
            try:
                dropdown_district.click()
                logging.info("Đã nhấn vào trạng thái 'Chờ xử lý'.")
            except Exception:
                self.driver.execute_script("arguments[0].click();", dropdown_district)
                logging.info("Đã nhấn vào trạng thái 'Chờ xử lý' bằng JavaScript.")

            return True

        except TimeoutException:
            logging.error("Không thể nhấn vào trạng thái 'Chờ xử lý' do Timeout!")
            return False
   
    # Hàm click nút Tải lại
    def click_reload_button(self):
        try:
            reload_button = self.wait.until(
                EC.element_to_be_clickable(self.locators.RELOAD_BUTTON)
            )
            reload_button.click()
            logging.info("Đã nhấn vào nút 'Tải lại'.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào nút 'Tải lại'.")
            return False
    
    # Hàm click dropdown 'Phân trang'
    def click_pagination_dropdown(self):
        try:
            pagination_dropdown = self.wait.until(
                EC.element_to_be_clickable(self.locators.PAGINATION_DROPDOWN)
            )
            try:
                pagination_dropdown.click()
                logging.info("Đã nhấn vào dropdown 'Phân trang'.")
            except Exception:
                self.driver.execute_script("arguments[0].click();", pagination_dropdown)
                logging.info("Đã nhấn vào dropdown 'Phân trang' bằng JavaScript.")

            return True

        except TimeoutException:
            logging.error("Không thể nhấn vào dropdown 'Phân trang' do Timeout!")
            return False
    
    # Hàm click nút Số trang đầu tiên
    def click_first_pagination_item(self):
        try:
            first_pagination_item = self.wait.until(
                EC.element_to_be_clickable(self.locators.FIRST_PAGINATION_ITEM)
            )
            first_pagination_item.click()
            logging.info("Đã nhấn vào nút 'Số trang đầu tiên'.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào nút 'Số trang đầu tiên'.")
            return False
    
    # Hàm click nút Thao tác
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

    # Hàm click nút Xóa
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

    # Ham nhap tu khoa tim kiem
    def enter_search_keyword(self, keyword):
        try:
            search_bar = self.wait.until(
                EC.visibility_of_element_located(self.locators.LOCATION_SEARCHBAR)
            )
            search_bar.clear()  # Xóa nội dung hiện tại nếu có
            search_bar.send_keys(keyword)
            logging.info(f"Đã nhập '{keyword}' vào ô tìm kiếm và thực hiện tìm kiếm.")
            return True
        except TimeoutException:
            logging.error("Không thể nhập dữ liệu vào ô tìm kiếm.")
            return False
    
    # Hàm click checkbox "Chọn tất cả"
    def click_select_all_checkbox(self):
        try:
            select_all_checkbox = self.wait.until(
                EC.element_to_be_clickable(self.locators.SELECT_ALL_CHECKBOX)
            )
            select_all_checkbox.click()
            logging.info("Đã nhấn vào checkbox 'Chọn tất cả'.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào checkbox 'Chọn tất cả'!")
            return False

    # Ham click Ten chi nhanh dau tien
    def click_first_name(self):
        try:
            # Chờ tên của chi nhánh đầu tiên xuất hiện
            first_name = self.wait.until(
                EC.element_to_be_clickable(self.locators.FIRST_LOCATION_NAME)
            )

            # Lấy nội dung text của tên của chi nhánh
            name_text = first_name.text.strip()
            logging.info(f"Lấy text của tên của chi nhánh đầu tiên: '{name_text}'")

            # Click vào tên của chi nhánh
            first_name.click()
            logging.info("Đã nhấn vào tên của chi nhánh đầu tiên.")

            return name_text  # Trả về text để sử dụng trong test case
        except TimeoutException:
            logging.error("Không tìm thấy tên của chi nhánh đầu tiên để nhấn.")
            return None
        
    # Hàm click button '...' đầu tiên
    def click_first_menu_button(self):
        try:
            first_menu_button = self.wait.until(
                EC.element_to_be_clickable(self.locators.FIRST_MENU_BUTTON)
            )
            first_menu_button.click()
            logging.info("Đã nhấn vào button '...' đầu tiên.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào button '...' đầu tiên!")
            return False
        
    # Hàm click menu-item 'Chi tiết' của chi nhánh đầu tiên
    def click_first_detail_menu_item(self):
        try:
            first_detail_menu_item = self.wait.until(
                EC.element_to_be_clickable(self.locators.FIRST_DETAIL_MENU_ITEM)
            )
            first_detail_menu_item.click()
            logging.info("Đã nhấn vào menu-item 'Chi tiết' của chi nhánh đầu tiên.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào menu-item 'Chi tiết' của chi nhánh đầu tiên!")
            return False 
        
    # Hàm click menu-item 'Xóa' của chi nhánh đầu tiên
    def click_first_delete_menu_item(self):
        try:
            first_delete_menu_item = self.wait.until(
                EC.element_to_be_clickable(self.locators.FIRST_DELETE_MENU_ITEM)
            )
            first_delete_menu_item.click()
            logging.info("Đã nhấn vào menu-item 'Xóa' của chi nhánh đầu tiên.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào menu-item 'Xóa' của chi nhánh đầu tiên!")
            return False 
    
    # Hàm click chọn Có trong popup 'Xác nhận'
    def click_button_yes_in_popup(self):
        try:
            button_yes = self.wait.until(
                EC.element_to_be_clickable(self.locators.YES_BUTTON)
            )
            button_yes.click()
            logging.info("Đã nhấn chọn Có trong popup 'Xác nhận'.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn chọn Có trong popup 'Xác nhận'!")
            return False     
        
    # Hàm click chọn Không trong popup 'Xác nhận'
    def click_button_no_in_popup(self):
        try:
            button_no = self.wait.until(
                EC.element_to_be_clickable(self.locators.NO_BUTTON)
            )
            button_no.click()
            logging.info("Đã nhấn chọn Không trong popup 'Xác nhận'.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn chọn Không trong popup 'Xác nhận'!")
            return False     