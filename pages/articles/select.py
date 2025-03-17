import logging
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locator_article import LocatorArticle

class SelectArticle:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorArticle  # Định vị phần tử

    # Hàm nhấn vào dropdown Loại bài viết
    def click_select(self):
        try:
            select_element = self.wait.until(EC.element_to_be_clickable(self.locators.DROPDOWN_ARTICLE_TYPE))
            select_element.click()
            logging.info("Đã mở dropdown 'Loại bài viết'.")
        except TimeoutException:
            logging.error("Không thể mở dropdown 'Loại bài viết'.")
            raise

    # Hàm kiểm tra dropdown Loại bài viết có hiển thị không
    def is_dropdown_visible(self):
        try:
            dropdown_element = self.wait.until(EC.visibility_of_element_located(self.locators.DROPDOWN_ARTICLE_TYPE))
            return dropdown_element.is_displayed()
        except TimeoutException:
            return False

    # Hàm chọn một Loại bài viết trong dropdown
    def select_article_type(self, article_type):
        try:
            article_type_element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(), '{article_type}')]"))
            )
            article_type_element.click()
            logging.info(f"Đã chọn loại bài viết: {article_type}")
        except TimeoutException:
            logging.error(f"Không thể chọn loại bài viết: {article_type}")
            raise

    # Hàm kiểm tra Loại bài viết đã chọn có đúng không
    def is_selected_article_type_displayed(self, expected_article_type):
        try:
            selected_article_type = self.wait.until(
                EC.visibility_of_element_located(self.locators.DROPDOWN_ARTICLE_TYPE_DISPLAY)
            ).text.strip()
            return selected_article_type == expected_article_type
        except TimeoutException:
            logging.error("Không thể lấy loại bài viết đã chọn.")
            return False

    # Hàm nhấn vào dropdown Trạng thái
    def click_status_dropdown(self):
        try:
            dropdown = self.wait.until(EC.element_to_be_clickable(self.locators.DROPDOWN_STATUS))
            dropdown.click()
            logging.info("Đã mở dropdown 'Trạng thái'.")
        except TimeoutException:
            logging.error("Không thể mở dropdown 'Trạng thái'.")
            raise

    # Hàm kiểm tra dropdown Trạng thái có hiển thị không
    def is_status_dropdown_visible(self):
        try:
            dropdown = self.wait.until(EC.visibility_of_element_located(self.locators.DROPDOWN_STATUS))
            return dropdown.is_displayed()
        except TimeoutException:
            return False

    # Hàm chọn Trạng thái trong dropdown
    def select_status(self, status_name):
        try:
            option_locator = (By.XPATH, f"//li[contains(@class, 'select2-results__option') and text()='{status_name}']")
            option = self.wait.until(EC.element_to_be_clickable(option_locator))
            option.click()
            logging.info(f"Đã chọn trạng thái: {status_name}")
        except TimeoutException:
            logging.error(f"Không thể chọn trạng thái: {status_name}")
            raise

    # Hàm kiểm tra Trạng thái đã chọn có đúng không
    def is_selected_status_correct(self, expected_status):
        try:
            selected_text = self.wait.until(
                EC.visibility_of_element_located(self.locators.DROPDOWN_STATUS_SELECTED)
            ).text.strip()
            return selected_text == expected_status
        except TimeoutException:
            logging.error("Không thể lấy giá trị 'Trạng thái' đã chọn.")
            return False

    def is_status_selected(self, expected_status):
        selected_status = self.driver.find_element(self.locators.DROPDOWN_STATUS_SELECTED[0], self.locators.DROPDOWN_STATUS_SELECTED[1]).text.strip()
        return selected_status == expected_status
