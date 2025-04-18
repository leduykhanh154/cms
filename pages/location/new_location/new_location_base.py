import time
import logging
import selenium
from selenium.webdriver.common.by import By
from locators.locator_location.locator_new_location import LocatorNewLocation
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class NewLocationBase:
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

    # Ham click tab 'Thong tin chung'
    def click_general_information_tab(self):
        try:
            tab = self.wait.until(
                EC.element_to_be_clickable(self.locators.GENERAL_INFORMATION_TAB)
            )
            tab.click()
            logging.info("Đã nhấn vào tab 'General Information'.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào tab 'General Information'!")
            return False
    
    # Ham click tab 'Noi dung chinh'
    def click_main_content_tab(self):
        try:
            tab_main_content = self.wait.until(
                EC.element_to_be_clickable(self.locators.MAIN_CONTENT_TAB)
            )
            tab_main_content.click()
            logging.info("Đã nhấn vào tab 'Nội dung chính'.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào tab 'Nội dung chính'!")
            return False

    # Ham click tab 'English'
    def click_english_tab(self):
        try:
            tab_english = self.wait.until(
                EC.element_to_be_clickable(self.locators.ENGLISH_TAB)
            )
            tab_english.click()
            logging.info("Đã nhấn vào tab 'English'.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào tab 'English'!")
            return False

    # Ham click tab 'Tieng Viet'
    def click_tieng_viet_tab(self):
        try:
            tab_tieng_viet = self.wait.until(
                EC.element_to_be_clickable(self.locators.TIENG_VIET_TAB)
            )
            tab_tieng_viet.click()
            logging.info("Đã nhấn vào tab 'Tiếng Việt'.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào tab 'Tiếng Việt'!")
            return False
    
    # Hàm click nút 'Lưu'
    def click_save_button(self):
        try:
            save_button = self.wait.until(
                EC.element_to_be_clickable(self.locators.SAVE_BUTTON)
            )

            try:
                save_button.click()
                logging.info("Đã nhấn vào nút 'Lưu'.")
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();", save_button)
                logging.info("Đã nhấn vào nút 'Lưu' bằng JavaScript.")

            return True

        except TimeoutException:
            logging.error("Không thể nhấn vào nút 'Lưu'. Hết thời gian chờ.")
            return False

    # Ham click nut 'Luu va tiep tuc cap nhat'
    def click_save_and_continue_button(self):
        try:
            save_and_continue_button = self.wait.until(
                EC.element_to_be_clickable(self.locators.SAVE_AND_CONTINUE_BUTTON)
            )

            try:
                save_and_continue_button.click()
                logging.info("Đã nhấn vào nút 'Lưu và Tiếp tục cập nhật'.")
            except Exception:
                self.driver.execute_script("arguments[0].click();", save_and_continue_button)
                logging.info("Đã nhấn vào nút 'Lưu và Tiếp tục cập nhật' bằng JavaScript.")

            return True

        except TimeoutException:
            logging.error("Không thể nhấn vào nút 'Lưu và Tiếp tục cập nhật'. Hết thời gian chờ.")
            return False

    # Click nut 'Dich noi dung'
    def click_translate_button(self):
        try:
            translate_button = self.wait.until(
                EC.element_to_be_clickable(self.locators.TRANSLATE_BUTTON)
            )

            try:
                translate_button.click()
                logging.info("Đã nhấn vào nút 'Dịch nội dung'.")
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();", translate_button)
                logging.info("Đã nhấn vào nút 'Dịch nội dung' bằng JavaScript.")

            return True

        except TimeoutException:
            logging.error("Không thể nhấn vào nút 'Dịch nội dung'. Hết thời gian chờ.")
            return False    
        
    # Hàm click dropdown 'Tỉnh/Thành phố'
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
                EC.element_to_be_clickable(self.locators.FIRST_PROVINCE_ITEM)
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
                EC.element_to_be_clickable(self.locators.FIRST_DISTRICT_ITEM)
            )
            first_item_district.click()
            logging.info("Đã nhấn vào Datepicker 'Từ ngày'.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào Datepicker 'Từ ngày'.")
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
