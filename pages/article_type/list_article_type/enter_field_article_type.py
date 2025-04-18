import logging
from locators.locator_article_type.locator_type import LocatorArticleType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EnterFieldArticleType:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorArticleType
    
    # Ham nhap tu khoa tim kiem
    def enter_search_keyword(self, keyword):
        try:
            search_bar = self.wait.until(
                EC.visibility_of_element_located(self.locators.SEARCHBAR)
            )
            search_bar.clear()  # Xóa nội dung hiện tại nếu có
            search_bar.send_keys(keyword)
            logging.info(f"Đã nhập '{keyword}' vào ô tìm kiếm và thực hiện tìm kiếm.")
            return True
        except TimeoutException:
            logging.error("Không thể nhập dữ liệu vào ô tìm kiếm.")
            return False
