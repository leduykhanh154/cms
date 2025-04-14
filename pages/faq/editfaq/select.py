import logging
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.faq.locator_editfaq import LocatorEditFAQ

class SelectEditFAQ:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorEditFAQ 


    # Hàm lấy nội dung văn bản của một phần tử trên giao diện
    def get_text(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.text.strip()
        except TimeoutException:
            logging.error(f"Lỗi: Không tìm thấy phần tử {locator}")
            return None

    # Hàm click select Hiển thị
    def click_select_show(self):
        try:
            select_element = self.wait.until(EC.element_to_be_clickable(self.locators.SELECT_SHOW))
            select_element.click()
            logging.info("Đã click select Hiển thị.")
        except TimeoutException:
            logging.error("Không thể click select Hiển thị.")
            raise
        
    # Hàm click chọn giá trị Không
    def click_value_not_select_show(self):
        try:
            value = self.wait.until(EC.element_to_be_clickable(self.locators.SELECT_VALUE_NOT))
            value.click()
            logging.info("Đã click chọn giá trị Không.")
        except TimeoutException:
            logging.error("Không thể click chọn giá trị Không.")
            raise

    # Hàm kiểm tra xem giá trị Không hiển thị
    def is_value_not_visible(self):
        try:
            value_element = self.get_text(self.locators.SELECT_SHOW)
            expected_value = "Không"

            if value_element == expected_value:
                logging.info("Đã hiển thị giá trị Không ở field.")
                return True
            else:
                logging.error(f"Lỗi: Expected: '{expected_value}', nhưng nhận được: '{value_element}'")
                return False
        except TimeoutException:
            return False
        
    # Hàm click chọn giá trị Có
    def click_value_has_select_show(self):
        try:
            value = self.wait.until(EC.element_to_be_clickable(self.locators.SELECT_VALUE_HAS))
            value.click()
            logging.info("Đã click chọn giá trị Có.")
        except TimeoutException:
            logging.error("Không thể click chọn giá trị Có.")
            raise

    # Hàm kiểm tra xem giá trị Có hiển thị
    def is_value_has_visible(self):
        try:
            value_element = self.get_text(self.locators.SELECT_SHOW)
            expected_value = "Có"

            if value_element == expected_value:
                logging.info("Đã hiển thị giá trị Có ở field.")
                return True
            else:
                logging.error(f"Lỗi: Expected: '{expected_value}', nhưng nhận được: '{value_element}'")
                return False
        except TimeoutException:
            return False
        
    # Hàm click select Loại câu hỏi*
    def click_select_question_type(self):
        try:
            select_element = self.wait.until(EC.element_to_be_clickable(self.locators.SELECT_QUESTION_TYPE))
            select_element.click()
            logging.info("Đã click select Loại câu hỏi*.")
        except TimeoutException:
            logging.error("Không thể click select Loại câu hỏi*.")
            raise
        
    # Hàm click chọn giá trị Thủ tục, quy trình
    def click_value_procedure_select_question_type(self):
        try:
            value = self.wait.until(EC.element_to_be_clickable(self.locators.SELECT_VALUE_PROCEDURE))
            value.click()
            logging.info("Đã click chọn giá trị Thủ tục, quy trình.")
        except TimeoutException:
            logging.error("Không thể click chọn giá trị Thủ tục, quy trình.")
            raise

    # Hàm kiểm tra xem giá trị Thủ tục, quy trình hiển thị
    def is_value_procedure_visible(self):
        try:
            value_element = self.get_text(self.locators.SELECT_QUESTION_TYPE)
            expected_value = "Thủ tục, quy trình"

            if value_element == expected_value:
                logging.info("Đã hiển thị giá trị Thủ tục, quy trình ở field.")
                return True
            else:
                logging.error(f"Lỗi: Expected: '{expected_value}', nhưng nhận được: '{value_element}'")
                return False
        except TimeoutException:
            return False
        
    # Hàm click chọn giá trị Dịch vụ khác
    def click_value_other_service_select_question_type(self):
        try:
            value = self.wait.until(EC.element_to_be_clickable(self.locators.SELECT_VALUE_OTHER_SERVICE))
            value.click()
            logging.info("Đã click chọn giá trị Dịch vụ khác.")
        except TimeoutException:
            logging.error("Không thể click chọn giá trị Dịch vụ khác.")
            raise

    # Hàm kiểm tra xem giá trị Dịch vụ khác hiển thị
    def is_value_other_service_visible(self):
        try:
            value_element = self.get_text(self.locators.SELECT_QUESTION_TYPE)
            expected_value = "Dịch vụ khác"

            if value_element == expected_value:
                logging.info("Đã hiển thị giá trị Dịch vụ khác ở field.")
                return True
            else:
                logging.error(f"Lỗi: Expected: '{expected_value}', nhưng nhận được: '{value_element}'")
                return False
        except TimeoutException:
            return False
        
    # Hàm click chọn giá trị Dịch vụ Hoa tiêu
    def click_value_pilotage_service_select_question_type(self):
        try:
            value = self.wait.until(EC.element_to_be_clickable(self.locators.SELECT_VALUE_PILOTAGE_SERVICE))
            value.click()
            logging.info("Đã click chọn giá trị Dịch vụ Hoa tiêu.")
        except TimeoutException:
            logging.error("Không thể click chọn giá trị Dịch vụ Hoa tiêu.")
            raise

    # Hàm kiểm tra xem giá trị Dịch vụ Hoa tiêu hiển thị
    def is_value_pilotage_service_visible(self):
        try:
            value_element = self.get_text(self.locators.SELECT_QUESTION_TYPE)
            expected_value = "Dịch vụ Hoa tiêu"

            if value_element == expected_value:
                logging.info("Đã hiển thị giá trị Dịch vụ Hoa tiêu ở field.")
                return True
            else:
                logging.error(f"Lỗi: Expected: '{expected_value}', nhưng nhận được: '{value_element}'")
                return False
        except TimeoutException:
            return False
        
    # Hàm click select Trạng thái
    def click_select_status(self):
        try:
            select = self.wait.until(EC.element_to_be_clickable(self.locators.SELECT_STATUS))
            select.click()
            logging.info("Đã click select Trạng thái.")
        except TimeoutException:
            logging.error("Không thể click select Trạng thái.")
            raise

    # Hàm click chọn giá trị Chờ xử lý
    def click_value_pending_select_status(self):
        try:
            value = self.wait.until(EC.element_to_be_clickable(self.locators.SELECT_VALUE_PENDING))
            value.click()
            logging.info("Đã click chọn giá trị Chờ xử lý.")
        except TimeoutException:
            logging.error("Không thể click chọn giá trị Chờ xử lý.")
            raise

    # Hàm kiểm tra xem giá trị Chờ xử lý hiển thị
    def is_value_pending_visible(self):
        try:
            value_element = self.get_text(self.locators.SELECT_STATUS)
            expected_value = "Chờ xử lý"

            if value_element == expected_value:
                logging.info("Đã hiển thị giá trị Chờ xử lý ở field.")
                return True
            else:
                logging.error(f"Lỗi: Expected: '{expected_value}', nhưng nhận được: '{value_element}'")
                return False
        except TimeoutException:
            return False
        
    # Hàm click chọn giá trị Kích hoạt
    def click_value_activate_select_status(self):
        try:
            value = self.wait.until(EC.element_to_be_clickable(self.locators.SELECT_VALUE_ACTIVATE))
            value.click()
            logging.info("Đã click chọn giá trị Kích hoạt.")
        except TimeoutException:
            logging.error("Không thể click chọn giá trị Kích hoạt.")
            raise

    # Hàm kiểm tra xem giá trị Kích hoạt hiển thị
    def is_value_activate_visible(self):
        try:
            value_element = self.get_text(self.locators.SELECT_STATUS)
            expected_value = "Kích hoạt"

            if value_element == expected_value:
                logging.info("Đã hiển thị giá trị Kích hoạt ở field.")
                return True
            else:
                logging.error(f"Lỗi: Expected: '{expected_value}', nhưng nhận được: '{value_element}'")
                return False
        except TimeoutException:
            return False
        
    # Hàm click select Ngày đăng
    def click_select_posted_date(self):
        try:
            select = self.wait.until(EC.element_to_be_clickable(self.locators.SELECT_POSTED_DATE))
            select.click()
            logging.info("Đã click select Ngày đăng.")
        except TimeoutException:
            logging.error("Không thể click select Ngày đăng.")
            raise

    # Hàm click chọn giá trị ngày 14/04/2025 ở field Ngày đăng
    def click_value_14apr_select_posted_date(self):
        try:
            value = self.wait.until(EC.element_to_be_clickable(self.locators.SELECT_14APR))
            value.click()
            logging.info("Đã click chọn giá trị 14/04/2025.")
        except TimeoutException:
            logging.error("Không thể click chọn giá trị 14/04/2025.")
            raise

    # Hàm kiểm tra xem giá trị 14/04/2025 hiển thị
    def is_value_14apr_visible(self, data):
        try:
            time.sleep(1)
            value_element = self.wait.until(
                EC.text_to_be_present_in_element_attribute(self.locators.SELECT_POSTED_DATE, "value", data)
            )

            if value_element:
                logging.info(f"Đã hiển thị giá trị {data} vừa chỉnh sửa ở field.")
                return True
            else:
                logging.error(f"Lỗi: Expected: '{data}', nhưng nhận được: '{value_element}'")
                return False
        except TimeoutException:
            return False