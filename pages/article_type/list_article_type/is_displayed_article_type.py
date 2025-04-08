import logging
from locators.locator_article_type.locator_type import LocatorArticleType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IsDisplayedArticleType:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorArticleType
        
    # Ham kiem tra canh bao 'Vui long chon trang de xoa' co xuat hien
    def is_warning_displayed(self):
        try:
            warning_element = self.wait.until(
                EC.visibility_of_element_located(self.locators.POPUP_WARNING)
            )
            logging.info("Hộp thoại cảnh báo đã xuất hiện.")
            return True
        except TimeoutException:
            logging.error("Không tìm thấy hộp thoại cảnh báo!")
            return False

    # Ham kiem tra canh bao 'Xac nhan xoa'
    def is_warning_text_correct(self, expected_text):
        try:
            warning_element = self.wait.until(
                EC.visibility_of_element_located(self.locators.WARNING_TEXT)
            )
            warning_text = warning_element.text.strip()

            logging.info(f"Nội dung cảnh báo hiển thị: '{warning_text}'")
            return warning_text == expected_text
        except TimeoutException:
            logging.error("Không tìm thấy hộp thoại cảnh báo!")
            return False

    # Ham kiem tra so hang duoc chon
    def is_selected_line_correct(self, expected_text):
        try:
            selected_line = self.wait.until(
                EC.visibility_of_element_located(self.locators.SELECTED_LINE)
            )
            actual_text = selected_line.text.strip()
            
            if actual_text == expected_text:
                logging.info(f"Dòng chọn hiển thị đúng: '{actual_text}'")
                return True
            else:
                logging.error(f"Dòng chọn hiển thị sai! Expected: '{expected_text}', Actual: '{actual_text}'")
                return False
        except TimeoutException:
            logging.error("Không tìm thấy phần tử hiển thị dòng đã chọn!")
            return False

    # Ham kiem tra text tren trang
    def is_text_displayed_on_page(self, expected_text):
        try:
            # Chờ phần tử chứa text xuất hiện trên trang
            page_source = self.driver.page_source

            # Kiểm tra xem text mong đợi có trong nguồn trang không
            if expected_text in page_source:
                logging.info(f"Text '{expected_text}' hiển thị đúng.")
                return True
            else:
                logging.error(f"Text '{expected_text}' Không hiển thị.")
                return False
        except Exception as e:
            logging.error(f"Lỗi khi kiểm tra trên trang: {str(e)}")
            return False

    # Ham kiểm tra xem cảnh báo có tồn tại không
    def is_warning_popup_closed(self, expected_text):
        try:
            # Kiểm tra xem cảnh báo có tồn tại không
            self.wait.until(
                EC.invisibility_of_element_located(self.locators.WARNING_TEXT)
            )
            logging.info(f"Hộp thoại cảnh báo '{expected_text}' đã đóng.")
            return True
        except TimeoutException:
            logging.error(f"Hộp thoại cảnh báo '{expected_text}' vẫn còn hiển thị!")
            return False

    # Hàm kiểm tra checkbox đầu tiên không hiển thị
    def is_first_checkbox_not_visible(self):
        try:
            self.wait.until_not(
                EC.visibility_of_element_located(self.locators.SELECT_FIRST)
            )
            logging.info("Checkbox 'Select First' không hiển thị (ẩn thành công).")
            return True
        except TimeoutException:
            logging.error("Checkbox 'Select First' vẫn đang hiển thị khi không mong đợi.")
            return False

    

