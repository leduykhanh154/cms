import time
import logging
import selenium
from selenium.webdriver.common.by import By
from locators.locator_article_type.locator_new_article_type import LocatorNewArticleType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class MetaImageNewArticleType:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorNewArticleType 
    
    # Ham click field 'Upload image'
    def click_meta_image(self):
        meta_image_element = self.wait.until(
            EC.element_to_be_clickable(self.locators.FIELD_IMAGE)
        )
        self.driver.execute_script("arguments[0].click();", meta_image_element)
        logging.info("Đã click vào hình ảnh để mở popup tải lên.")

    # Ham click nut 'Tai len'
    def click_button_upload_image(self):
        try:
            button = self.wait.until(EC.element_to_be_clickable(self.locators.BUTTON_UPLOAD_IMAGE))
            button.click()
            logging.info("Đã click vào nút 'Upload image'.")
        except TimeoutException:
            logging.error("Không tìm thấy hoặc không thể click vào nút 'Upload image'!")
            raise

    # Ham click tab Browser
    def click_tab_browser(self):
        try:
            tab_browser = self.wait.until(EC.element_to_be_clickable(self.locators.TAB_BROWSER))
            tab_browser.click()
            logging.info("Đã click vào tab 'Browser'.")
        except TimeoutException:
            logging.error("Không tìm thấy hoặc không thể click vào tab 'Browser'!")
            raise

    # Ham click anh dau tien 
    def click_first_image(self):
        try:
            first_image = self.wait.until(EC.element_to_be_clickable(self.locators.FIRST_IMAGE))
            first_image.click()
            logging.info("Đã click vào ảnh đầu tiên trong danh sách file.")
        except TimeoutException:
            logging.error("Không tìm thấy hoặc không thể click vào ảnh đầu tiên!")
            raise
    
    # Ham click nut 'Upload'
    def click_button_upload(self):
        try:
            button_upload = self.wait.until(EC.element_to_be_clickable(self.locators.BUTTON_UPLOAD))
            button_upload.click()
            logging.info("Đã click vào nút Upload.")
        except TimeoutException:
            logging.error("Không tìm thấy hoặc không thể click vào nút Upload!")
            raise

    # Ham click nut 'Xoa anh'
    def click_button_delete_image(self):
        try:
            delete_button = self.wait.until(
                EC.element_to_be_clickable(self.locators.BUTTON_DELETE_IMAGE)
            )
            delete_button.click()
            logging.info("Đã click vào nút 'Xóa ảnh'.")
        except TimeoutException:
            logging.error("Không thể click vào nút 'Xóa ảnh' vì không tìm thấy!")
        except Exception as e:
            logging.error(f"Lỗi xảy ra khi click vào nút 'Xóa ảnh': {str(e)}")
