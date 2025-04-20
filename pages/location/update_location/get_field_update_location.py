import time
import logging
import selenium
from selenium.webdriver.common.by import By
from locators.locator_location.locator_update_location import LocatorUpdateLocation
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class GetFieldUpdateLocation:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorUpdateLocation 

    # Hàm lấy giá trị ô 'Tên chi nhánh'
    def get_name(self):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(self.locators.NAME_TEXT_INPUT))
            value = input_field.get_attribute("value")
            logging.info(f"Giá trị lấy được từ ô 'Tên chi nhánh': {value}")
            return value
        except TimeoutException:
            logging.error("Không thể lấy giá trị từ ô 'Tên chi nhánh'.")
            return None        
    
    # Hàm lấy giá trị ô 'Địa chỉ chi nhánh'
    def get_address(self):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(self.locators.ADDRESS_TEXT_INPUT))
            value = input_field.get_attribute("value")
            logging.info(f"Giá trị lấy được từ ô địa chỉ chi nhánh: {value}")
            return value
        except TimeoutException:
            logging.error("Không thể lấy giá trị từ ô địa chỉ chi nhánh.")
            return None

    # Hàm lấy giá trị ô 'Tên chi nhánh'
    def get_en_name(self):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(self.locators.EN_NAME_TEXT_INPUT))
            value = input_field.get_attribute("value")
            logging.info(f"Giá trị lấy được từ ô 'Tên chi nhánh': {value}")
            return value
        except TimeoutException:
            logging.error("Không thể lấy giá trị từ ô 'Tên chi nhánh'.")
            return None        
    
    # Hàm lấy giá trị ô 'Địa chỉ chi nhánh'
    def get_en_address(self):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(self.locators.EN_ADDRESS_TEXT_INPUT))
            value = input_field.get_attribute("value")
            logging.info(f"Giá trị lấy được từ ô địa chỉ chi nhánh: {value}")
            return value
        except TimeoutException:
            logging.error("Không thể lấy giá trị từ ô địa chỉ chi nhánh.")
            return None

    # Hàm lấy nội dung từ khung soạn thảo CKEditor
    def get_content(self):
        try:
            iframe = self.wait.until(EC.presence_of_element_located(self.locators.CONTENT_TEXT_AREA))
            self.driver.switch_to.frame(iframe)

            editable_area = self.wait.until(EC.presence_of_element_located((By.XPATH, "//body")))
            content = editable_area.get_attribute("innerHTML")

            self.driver.switch_to.default_content()
            logging.info(f"Nội dung CKEditor lấy được: {content}")
            return content
        except TimeoutException:
            logging.error("Không thể lấy nội dung từ CKEditor.")
            return None

    # Hàm lấy nội dung từ khung soạn thảo CKEditor
    def get_en_content(self):
        try:
            iframe = self.wait.until(EC.presence_of_element_located(self.locators.EN_CONTENT_TEXT_AREA))
            self.driver.switch_to.frame(iframe)

            editable_area = self.wait.until(EC.presence_of_element_located((By.XPATH, "//body")))
            content = editable_area.get_attribute("innerHTML")

            self.driver.switch_to.default_content()
            logging.info(f"Nội dung CKEditor lấy được: {content}")
            return content
        except TimeoutException:
            logging.error("Không thể lấy nội dung từ CKEditor.")
            return None

    # Hàm lấy giá trị ô 'Số điện thoại'
    def get_phone(self):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(self.locators.PHONE_TEXT_INPUT))
            value = input_field.get_attribute("value")
            logging.info(f"Giá trị lấy được từ ô số điện thoại: {value}")
            return value
        except TimeoutException:
            logging.error("Không thể lấy giá trị từ ô số điện thoại.")
            return None

    # Hàm lấy giá trị ô 'Fax'
    def get_fax(self):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(self.locators.FAX_TEXT_INPUT))
            value = input_field.get_attribute("value")
            logging.info(f"Giá trị lấy được từ ô số fax: {value}")
            return value
        except TimeoutException:
            logging.error("Không thể lấy giá trị từ ô số fax.")
            return None

    # Hàm lấy giá trị ô 'Kinh độ'
    def get_longitude(self):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(self.locators.LONGITUDE_TEXT_INPUT))
            value = input_field.get_attribute("value")
            logging.info(f"Giá trị lấy được từ ô kinh độ: {value}")
            return value
        except TimeoutException:
            logging.error("Không thể lấy giá trị từ ô kinh độ.")
            return None

    # Hàm lấy giá trị ô 'Vĩ độ'
    def get_latitude(self):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(self.locators.LATITUDE_TEXT_INPUT))
            value = input_field.get_attribute("value")
            logging.info(f"Giá trị lấy được từ ô vĩ độ: {value}")
            return value
        except TimeoutException:
            logging.error("Không thể lấy giá trị từ ô vĩ độ.")
            return None

    # Hàm lấy giá trị ô 'Email'
    def get_email(self):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(self.locators.EMAIL_TEXT_INPUT))
            value = input_field.get_attribute("value")
            logging.info(f"Giá trị lấy được từ ô email: {value}")
            return value
        except TimeoutException:
            logging.error("Không thể lấy giá trị từ ô email.")
            return None

    # Hàm lấy giá trị ô 'Giá trị sắp xếp'
    def get_sort_order(self):
        try:
            input_field = self.wait.until(EC.element_to_be_clickable(self.locators.SORT_ORDER_TEXT_INPUT))
            value = input_field.get_attribute("value")
            logging.info(f"Giá trị lấy được từ ô sắp xếp: {value}")
            return value
        except TimeoutException:
            logging.error("Không thể lấy giá trị từ ô sắp xếp.")
            return None
        
    # Hàm lấy nội dung text của ô 'Giá trị sắp xếp' và so sánh với expected_name
    def is_first_location_name_matched(self, expected_name):
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.locators.FIRST_LOCATION_NAME))
            text = element.text.strip()
            if text == expected_name:
                logging.info(f"Giá trị đúng: '{text}' khớp với expected_name: '{expected_name}'")
                return True
            else:
                logging.error(f"Giá trị không khớp. Lấy được: '{text}', kỳ vọng: '{expected_name}'")
                return False
        except TimeoutException:
            logging.error("Không thể lấy nội dung từ ô sắp xếp.")
            return False

