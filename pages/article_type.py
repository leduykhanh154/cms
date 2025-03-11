import logging
from utils.login import Login
from utils.driver_setup import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class ArticleTypePage:
    CONTENT_MENU = (By.XPATH, "//*[@id='left-menu']/ul/li[1]/a")
    POSTS_MENU = (By.XPATH, "//*[@id='left-menu']/ul/li[1]/ul/li[2]/a")
    ARTICLETYPE_MENU = (By.XPATH, "//*[@id='left-menu']/ul/li[1]/ul/li[2]/ul/li[3]/a")
    CREATE_NEW_BUTTON = (By.XPATH, "//*[@id='app-container']/main/div/div[2]/div[2]/div/a")

    VI_TITLE_INPUT = (By.XPATH, "//*[@id='languages[vi][title]']")
    VI_ERROR_MESSAGE_REQUIRED_NAME = (By.XPATH, "//*[@id='vi-content']/div[1]/div[2]/div/div")
    VI_ERROR_MESSAGE_MAX_LENGTH = (By.XPATH, "//*[@id='vi-content']/div[1]/div[2]/div/div/div")

    ENGLISH_TAB = (By.XPATH, '//*[@id="en-tab"]')
    TRANSLATE_BUTTON = (By.XPATH, '//*[@id="en-content"]/button')

    EN_TITLE_INPUT = (By.XPATH, '//*[@id="languages[en][title]"]')
    EN_ERROR_MESSAGE_REQUIRED_NAME = (By.XPATH, '//*[@id="en-content"]/div[1]/div[2]/div/div/div')
    EN_ERROR_MESSAGE_MAX_LENGTH = (By.XPATH, '//*[@id="en-content"]/div[1]/div[2]/div/div/div')

    MAIN_TAB = (By.XPATH, '//*[@id="MainTab"]')

    DROPDOWN = (By.XPATH, '//*[@id="showSettingTab"]/div/div[2]/div')
    ACTIVATE_OPTION = (By.XPATH, '//*[@id="select2-status-result-07ki-1"]')
    PENDING_OPTION = (By.XPATH, '//*[@id="select2-status-result-v9hr-2"]')

    SAVE_BUTTON = (By.XPATH, '//*[@id="save-button"]')
    SAVE_AND_CONTINUE_BUTTON = (By.XPATH, '//*[@id="save-category"]/div[1]/div[2]/div/div/button[2]')

    def __init__(self, driver, timeout=None):
        self.driver = driver
        self.timeout = timeout if timeout else 10
        self.wait = WebDriverWait(self.driver, self.timeout)
    
    def click_menu(self, locator, menu_name):
        try:
            menu = self.wait.until(EC.element_to_be_clickable(locator))
            menu.click()
            logging.info(f"Đã nhấn menu {menu_name}.")
        except Exception as e:
            logging.error(f"Lỗi khi nhấn menu {menu_name}: {e}", exc_info=True)
            raise

    def click_content_menu(self):
        self.click_menu(self.CONTENT_MENU, "Nội dung")

    def click_posts_menu(self):
        self.click_menu(self.POSTS_MENU, "Bài viết")

    def click_article_type_menu(self):
        self.click_menu(self.ARTICLETYPE_MENU, "Loại bài viết")

    def click_create_new_button(self):
        try:
            create_new_button = self.wait.until(EC.element_to_be_clickable(self.CREATE_NEW_BUTTON))
            self.driver.execute_script("arguments[0].click();", create_new_button)
            logging.info("Đã nhấn nút Tạo mới.")

            expected_url = "https://mpire-cms-demo.mpire.asia/cms/category/create"
            if self.wait.until(EC.url_to_be(expected_url)):
                logging.info(f"Chuyển hướng thành công đến {expected_url}")
                return True
            else:
                logging.warning(f"Chuyển hướng không thành công. URL hiện tại: {self.driver.current_url}")
                return False
        except Exception as e:
            logging.error(f"Lỗi khi nhấn nút Tạo mới hoặc chuyển hướng: {e}", exc_info=True)
            return False

    def vi_input_article_type_name(self, name):
        try:
            name_input = self.wait.until(EC.presence_of_element_located(self.VI_TITLE_INPUT))
            name_input.clear()
            name_input.send_keys(name)
            logging.info(f"Đã nhập tên loại bài viết (VI): {name}")
        except Exception as e:
            logging.error(f"Lỗi khi nhập tên loại bài viết (VI): {e}", exc_info=True)
            raise

    def vi_check_error_message_for_empty_name(self):
        try:
            error_message = self.wait.until(
                EC.presence_of_element_located(self.VI_ERROR_MESSAGE_REQUIRED_NAME)
            )
            logging.info(f"Thông báo lỗi khi không nhập tên (VI): {error_message.text}")
            return error_message.text
        except Exception as e:
            logging.error(f"Lỗi khi kiểm tra thông báo lỗi (VI): {e}", exc_info=True)
            raise

    def vi_check_error_message_for_max_length(self):
        try:
            error_message = self.wait.until(
                EC.presence_of_element_located(self.VI_ERROR_MESSAGE_MAX_LENGTH)
            )
            logging.info(f"Thông báo lỗi khi nhập quá 254 ký tự (VI): {error_message.text}")
            return error_message.text
        except Exception as e:
            logging.error(f"Lỗi khi kiểm tra thông báo lỗi (VI): {e}", exc_info=True)
            raise

    def click_english_tab(self):
        try:
            english_tab = self.wait.until(EC.element_to_be_clickable(self.ENGLISH_TAB))
            english_tab.click()
            logging.info("Đã nhấn vào tab Tiếng Anh.")
        except Exception as e:
            logging.error(f"Lỗi khi nhấn vào tab Tiếng Anh: {e}", exc_info=True)
            raise

    def click_translate_button(self):
        try:
            translate_button = self.wait.until(EC.element_to_be_clickable(self.TRANSLATE_BUTTON))
            translate_button.click()
            logging.info("Đã nhấn vào nút Dịch (Translate).")
        except Exception as e:
            logging.error(f"Lỗi khi nhấn vào nút Dịch: {e}", exc_info=True)
            raise
    
    def en_input_article_type_name(self, name):
        try:
            name_input = self.wait.until(EC.presence_of_element_located(self.EN_TITLE_INPUT))
            name_input.clear()
            name_input.send_keys(name)
            logging.info(f"Đã nhập tên loại bài viết (EN): {name}")
        except Exception as e:
            logging.error(f"Lỗi khi nhập tên loại bài viết (EN): {e}", exc_info=True)
            raise

    def en_check_error_message_for_empty_name(self):
        try:
            error_message = self.wait.until(
                EC.presence_of_element_located(self.EN_ERROR_MESSAGE_REQUIRED_NAME)
            )
            logging.info(f"Thông báo lỗi khi không nhập tên (EN): {error_message.text}")
            return error_message.text
        except Exception as e:
            logging.error(f"Lỗi khi kiểm tra thông báo lỗi (EN): {e}", exc_info=True)
            raise

    def en_check_error_message_for_max_length(self):
        try:
            error_message = self.wait.until(
                EC.presence_of_element_located(self.EN_ERROR_MESSAGE_MAX_LENGTH)
            )
            logging.info(f"Thông báo lỗi khi nhập quá 254 ký tự (EN): {error_message.text}")
            return error_message.text
        except Exception as e:
            logging.error(f"Lỗi khi kiểm tra thông báo lỗi (EN): {e}", exc_info=True)
            raise

    def click_main_tab(self):
        try:
            main_tab = self.wait.until(EC.element_to_be_clickable(self.MAIN_TAB))
            main_tab.click()
            logging.info("Đã nhấn vào tab Chính (Main).")
        except Exception as e:
            logging.error(f"Lỗi khi nhấn vào tab Chính (Main): {e}", exc_info=True)
            raise

    def click_dropdown(self):
        try:
            dropdown = self.wait.until(EC.element_to_be_clickable(self.DROPDOWN))
            dropdown.click()
            self.wait.until(EC.visibility_of_element_located(self.DROPDOWN_MENU))
            logging.info("Đã nhấn vào dropdown trạng thái hiển thị.")
        except Exception as e:
            logging.error(f"Lỗi khi nhấn vào dropdown: {e}", exc_info=True)
            raise

    def select_pending_status(self):
        try:
            self.click_dropdown()
            pending_option = self.wait.until(EC.presence_of_element_located(self.PENDING_OPTION))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", pending_option)
            self.wait.until(EC.element_to_be_clickable(self.PENDING_OPTION)).click()
            logging.info("Đã chọn trạng thái 'Chờ xử lý'.")
        except Exception as e:
            logging.error(f"Lỗi khi chọn 'Chờ xử lý': {e}", exc_info=True)
            raise

    def get_selected_status(self):
        try:
            self.click_dropdown()
            pending_option = self.wait.until(EC.element_to_be_clickable(self.PENDING_OPTION))
            pending_option.click()
            logging.info("Đã chọn trạng thái 'Chờ xử lý'.")
        except Exception as e:
            logging.error(f"Lỗi khi chọn 'Chờ xử lý': {e}", exc_info=True)
            raise
    
    def click_save_button(self):
        try:
            save_button = self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON))
            self.driver.execute_script("arguments[0].click();", save_button)
            logging.info("Đã nhấn nút Lưu.")
        except Exception as e:
            logging.error(f"Lỗi khi nhấn nút Lưu: {e}", exc_info=True)
            raise

    def perform_tag_operations(self):
        self.click_content_menu()
        self.click_posts_menu()
        self.click_article_type_menu()
