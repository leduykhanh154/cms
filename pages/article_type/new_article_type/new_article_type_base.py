import time
import logging
import selenium
from selenium.webdriver.common.by import By
from locators.locator_article_type.locator_new_article_type import LocatorNewArticleType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class NewArticleTypeBase:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorNewArticleType  
        
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

    # Ham click breadcrumb Danh sach loai bai viet
    def click_breadcrumb_type_list(self):
        try:
            breadcrumb = self.wait.until(
                EC.element_to_be_clickable(self.locators.BREADCRUMB_TYPE_LIST)
            )
            breadcrumb.click()
            logging.info("Đã nhấn vào 'Danh sách loại bài viết' trên breadcrumb.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào 'Danh sách loại bài viết' trên breadcrumb!")
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
    def click_tab_general_information(self):
        try:
            tab = self.wait.until(
                EC.element_to_be_clickable(self.locators.TAB_GENERAL_INFORMATION)
            )
            tab.click()
            logging.info("Đã nhấn vào tab 'General Information'.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào tab 'General Information'!")
            return False
    
    # Ham click tab 'Noi dung chinh'
    def click_tab_main_content(self):
        try:
            tab_main_content = self.wait.until(
                EC.element_to_be_clickable(self.locators.TAB_MAIN_CONTENT)
            )
            tab_main_content.click()
            logging.info("Đã nhấn vào tab 'Nội dung chính'.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào tab 'Nội dung chính'!")
            return False

    # Ham click tab 'English'
    def click_tab_english(self):
        try:
            tab_english = self.wait.until(
                EC.element_to_be_clickable(self.locators.TAB_ENGLISH)
            )
            tab_english.click()
            logging.info("Đã nhấn vào tab 'English'.")
            return True
        except TimeoutException:
            logging.error("Không thể nhấn vào tab 'English'!")
            return False

    # Ham click tab 'Tieng Viet'
    def click_tab_tieng_viet(self):
        try:
            tab_tieng_viet = self.wait.until(
                EC.element_to_be_clickable(self.locators.TAB_TIENG_VIET)
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

    # Ham click dropdown 'Status'
    def click_dropdown_status(self):
        try:
            dropdown = self.wait.until(EC.element_to_be_clickable(self.locators.DROPDOWN_STATUS))
            dropdown.click()
            print("Đã click vào dropdown 'Status'.")
        except Exception as e:
            print(f"Lỗi khi click vào dropdown 'Status': {e}")
    
    # Ham click dropdown Loai bai viet cap cha
    def click_dropdown_father_type(self):
        try:
            dropdown = self.wait.until(EC.element_to_be_clickable(self.locators.DROPDOWN_FATHER_TYPE))
            dropdown.click()
            print("Đã click vào dropdown 'Father Type'.")
        except Exception as e:
            print(f"Lỗi khi click vào dropdown 'Father Type': {e}")
            
    # Ham click dropdown Bo Banner
    def click_dropdown_banner_set(self):
        try:
            dropdown = self.wait.until(EC.element_to_be_clickable(self.locators.DROPDOWN_BANNER_SET))
            dropdown.click()
            print("Đã click vào dropdown 'Banner Set'.")
        except Exception as e:
            print(f"Lỗi khi click vào dropdown 'Banner Set': {e}")
        
    # Hàm thực hiện thao tác nhấn menu Nội dung -> menu Bài viết
    def navigate_to_article(self):
        self.click_content_menu()
        self.click_article_menu()

    # Hàm thực hiện thao tác nhấn menu Nội dung 
    def perform_tag_operations(self):
        self.navigate_to_article()
        self.click_article_type_menu()