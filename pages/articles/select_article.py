import time
import logging
from selenium.webdriver.common.by import By
from locators.locator_article import LocatorArticle
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SelectArticle:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorArticle 

    def click_select(self):
        try:
            select_element = self.wait.until(EC.element_to_be_clickable(self.locators.DROPDOWN_ARTICLE_TYPE))
            select_element.click()
            logging.info("Đã mở dropdown 'Loại bài viết'.")
        except TimeoutException:
            logging.error("Không thể mở dropdown 'Loại bài viết'.")
            raise

    def is_dropdown_visible(self):
        try:
            dropdown_element = self.wait.until(EC.visibility_of_element_located(self.locators.DROPDOWN_ARTICLE_TYPE))
            return dropdown_element.is_displayed()
        except TimeoutException:
            return False

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
    
    def is_selected_article_type_displayed(self, expected_article_type):
        try:
            selected_article_type = self.wait.until(
                EC.visibility_of_element_located(self.locators.DROPDOWN_ARTICLE_TYPE_DISPLAY)
            ).text.strip()
            return selected_article_type == expected_article_type
        except TimeoutException:
            logging.error("Không thể lấy loại bài viết đã chọn.")
            return False

    def click_status_dropdown(self):
        try:
            dropdown = self.wait.until(EC.element_to_be_clickable(self.locators.DROPDOWN_STATUS))
            dropdown.click()
            logging.info("Đã mở dropdown 'Trạng thái'.")
        except TimeoutException:
            logging.error("Không thể mở dropdown 'Trạng thái'.")
            raise

    def is_status_dropdown_visible(self):
        try:
            dropdown = self.wait.until(EC.visibility_of_element_located(self.locators.DROPDOWN_STATUS))
            return dropdown.is_displayed()
        except TimeoutException:
            return False

    def select_status(self, status_name):
        try:
            option_locator = (By.XPATH, f"//li[contains(@class, 'select2-results__option') and text()='{status_name}']")
            option = self.wait.until(EC.element_to_be_clickable(option_locator))
            option.click()
            logging.info(f"Đã chọn trạng thái: {status_name}")
        except TimeoutException:
            logging.error(f"Không thể chọn trạng thái: {status_name}")
            raise

    def is_selected_status_correct(self, expected_status):
        try:
            selected_text = self.wait.until(
                EC.visibility_of_element_located(self.locators.DROPDOWN_STATUS_SELECTED)
            ).text.strip()
            return selected_text == expected_status
        except TimeoutException:
            logging.error("Không thể lấy giá trị 'Trạng thái' đã chọn.")
            return False
    
    def close_dropdown_if_open(self):
        try:
            outside_element = self.wait.until(EC.element_to_be_clickable(self.locators.HEADER_SECTION))
            outside_element.click()
            time.sleep(1)
            if not self.is_dropdown_visible():
                logging.info("Dropdown 'Loại bài viết' đã đóng sau khi click bên ngoài.")
                return True
            else:
                logging.warning("Dropdown 'Loại bài viết' vẫn mở sau khi click bên ngoài.")
                return False
        except TimeoutException:
            logging.error("Không thể thực hiện thao tác đóng dropdown.")
            return False

    def is_status_selected(self, expected_status):
        selected_status = self.driver.find_element(self.locators.DROPDOWN_STATUS_SELECTED[0], self.locators.DROPDOWN_STATUS_SELECTED[1]).text.strip()
        return selected_status == expected_status

    def scroll_to_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        time.sleep(0.5)
        return element

    def click_related_article_dropdown(self):
        try:
            dropdown = self.wait.until(EC.element_to_be_clickable(LocatorArticle.RELATED_ARTICLE_DROPDOWN))
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", dropdown)
            time.sleep(0.5)
            dropdown.click()
            logging.info("Đã mở dropdown 'Bài viết liên quan'.")
        except TimeoutException:
            logging.error("Không thể mở dropdown 'Bài viết liên quan'.")
            raise

    def select_related_article(self, article_name):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'select2-results__option')]")))
            articles = self.driver.find_elements(By.XPATH, "//li[contains(@class, 'select2-results__option')]")
            logging.info(f"Danh sách bài viết trong dropdown: {[article.text for article in articles]}")
            for article in articles:
                if article_name.strip() in article.text.strip():
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", article)
                    time.sleep(1)
                    article.click()
                    logging.info(f"Đã chọn bài viết: {article_name}")
                    return
            logging.error(f"Không tìm thấy bài viết: {article_name}. Kiểm tra lại tên hoặc dropdown.")
            raise TimeoutException(f"Không tìm thấy bài viết: {article_name}")
        except TimeoutException:
            logging.error(f"Timeout khi tìm bài viết: {article_name}")
            raise

    def is_selected_related_article_correct(self, expected_article):
        try:
            selected_article_element = self.wait.until(
                EC.presence_of_element_located(LocatorArticle.SELECTED_RELATED_ARTICLE_FIELD)
            )
            selected_article_text = selected_article_element.text.strip()
            logging.info(f"Bài viết hiển thị sau khi chọn: '{selected_article_text}'")
            logging.info(f"Expected: '{expected_article}'")
            return selected_article_text.strip() == expected_article.strip()
        except TimeoutException:
            logging.error("Không thể lấy giá trị bài viết đã chọn.")
            return False

    def is_related_article_dropdown_visible(self):
        try:
            dropdown_element = self.wait.until(
                EC.visibility_of_element_located(LocatorArticle.RELATED_ARTICLE_DROPDOWN)
            )
            logging.info("Dropdown 'Bài viết liên quan' đã mở.")
            return True
        except TimeoutException:
            logging.error("Dropdown 'Bài viết liên quan' không hiển thị!")
            return False

    def print_related_articles_list(self):
        try:
            articles = self.driver.find_elements(By.XPATH, "//li[contains(@class, 'select2-results__option')]")
            logging.info(f"Danh sách bài viết trong dropdown: {[article.text for article in articles]}")
        except Exception as e:
            logging.error(f"Lỗi khi lấy danh sách bài viết: {str(e)}")

    def get_selected_related_article(self):
        try:
            selected_article_element = self.wait.until(
                EC.presence_of_element_located(LocatorArticle.SELECTED_RELATED_ARTICLE_FIELD)
            )
            selected_article_text = selected_article_element.text.strip()

            logging.info(f"Giá trị bài viết hiển thị: '{selected_article_text}'")
            return selected_article_text
        except TimeoutException:
            logging.error("Không thể lấy giá trị bài viết đã chọn.")
            return ""
    
    def wait_for_selected_related_article_to_update(self, expected_text, timeout=5):
        try:
            self.wait.until(lambda driver: self.get_selected_related_article() == expected_text, f"Không tìm thấy bài viết mong đợi: {expected_text}")
            logging.info("Bài viết đã chọn hiển thị đúng.")
        except TimeoutException:
            logging.error(f"Bài viết đã chọn không cập nhật đúng. Expected: '{expected_text}'")