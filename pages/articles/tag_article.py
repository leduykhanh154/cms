import logging
from selenium.webdriver.common.by import By
from locators.locator_article import LocatorArticle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class TagArticle:
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorArticle

    def click_tag_dropdown(self):
        try:
            dropdown = self.wait.until(EC.element_to_be_clickable(self.locators.DROPDOWN_SELECT_TAG))
            dropdown.click()
            logging.info("Đã mở dropdown 'Tag'.")
        except TimeoutException:
            logging.error("Không thể mở dropdown 'Tag'.")
            raise

    def is_dropdown_open(self):
        dropdown_menu = self.driver.find_elements(self.locators.TAG_DROPDOWN_MENU)
        return len(dropdown_menu) > 0 

    def is_tag_dropdown_visible(self):
        try:
            dropdown = self.wait.until(EC.visibility_of_element_located(self.locators.TAG_DROPDOWN_MENU))
            return dropdown.is_displayed()
        except TimeoutException:
            logging.error("Dropdown 'Tag' không hiển thị.")
            return False
    
    def select_tag(self, tag_name):
        try:
            option_locator = (By.XPATH, f"//li[contains(@class, 'select2-results__option') and contains(text(), '{tag_name}')]")
            self.wait.until(EC.presence_of_element_located(option_locator))
            tags = self.driver.find_elements(By.XPATH, "//li[contains(@class, 'select2-results__option')]")
            logging.info(f"Danh sách tag tìm thấy: {[tag.text for tag in tags]}")
            option = self.wait.until(EC.element_to_be_clickable(option_locator))
            option.click()
            logging.info(f"Đã chọn tag: {tag_name}")

            # Chờ một chút để UI cập nhật
            self.wait.until(lambda driver: self.get_selected_tag() == tag_name)
        except TimeoutException:
            logging.error(f"Không tìm thấy tag: {tag_name}. Kiểm tra lại tên hoặc dropdown.")
            raise

    def is_selected_tag_correct(self, expected_tag):
        try:
            selected_tag_element = self.wait.until(
                EC.presence_of_element_located(self.locators.SELECTED_TAG_FIELD)
            )
            selected_tag_text = selected_tag_element.text.strip()
            logging.info(f"Tag hiển thị sau khi chọn: '{selected_tag_text}' (Expected: '{expected_tag}')")

            return selected_tag_text == expected_tag
        except TimeoutException:
            logging.error("Không thể lấy giá trị 'Tag' đã chọn.")
            return False

    def click_create_keyword_button(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.CREATE_KEYWORD_BUTTON)).click()
        
    def is_add_keyword_sidebar_visible(self):
        try:
            sidebar = self.wait.until(EC.visibility_of_element_located(self.locators.ADD_KEYWORD_SIDEBAR))
            return sidebar.is_displayed()
        except:
            logging.error("Sidebar 'Thêm từ khóa' không hiển thị!")
            return False

    def get_selected_tag(self):
        try:
            selected_tag_element = self.wait.until(
                EC.presence_of_element_located(self.locators.SELECTED_TAG_FIELD)
            )
            return selected_tag_element.text.strip()
        except TimeoutException:
            logging.error("Không thể lấy giá trị 'Tag' đã chọn.")
            return None

    