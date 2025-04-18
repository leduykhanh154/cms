import logging
from locators.locator_article_type.locator_type import LocatorArticleType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PopupArticleType:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorArticleType
    
    # Ham click nut 'Co'
    def click_yes_button(self):
        try:
            yes_button = self.wait.until(
                EC.element_to_be_clickable(self.locators.YES_BUTTON)
            )

            try:
                yes_button.click()
                logging.info("Đã nhấn vào nút 'Yes'.")
            except Exception:
                self.driver.execute_script("arguments[0].click();", yes_button)
                logging.info("Đã nhấn vào nút 'Yes' bằng JavaScript.")

            return True
        except TimeoutException:
            logging.error("Không tìm thấy hoặc không thể nhấn vào nút 'Yes'!")
            return False
    
    # Ham click nut 'Khong'
    def click_no_button(self):
        try:
            no_button = self.wait.until(
                EC.element_to_be_clickable(self.locators.NO_BUTTON)
            )

            try:
                no_button.click()
                logging.info("Đã nhấn vào nút 'No'.")
            except Exception:
                self.driver.execute_script("arguments[0].click();", no_button)
                logging.info("Đã nhấn vào nút 'No' bằng JavaScript.")

            return True
        except TimeoutException:
            logging.error("Không tìm thấy hoặc không thể nhấn vào nút 'No'!")
            return False
