import time
import logging
import selenium
from selenium.webdriver.common.by import By
from locators.locator_location.locator_update_location import LocatorUpdateLocation
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class EnterUpdateLocation:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorUpdateLocation 

    # Hàm nhập tên chi nhánh
    def enter_name(self, name):
        try:
            name_input = self.wait.until(
                EC.visibility_of_element_located(self.locators.NAME_TEXT_INPUT)
            )
            name_input.clear()
            name_input.send_keys(name)
            logging.info(f"Đã nhập tên chi nhánh: {name}")
            return True
        except TimeoutException:
            logging.error("Không tìm thấy ô nhập tên chi nhánh!")
            return False
        except Exception as e:
            logging.error(f"Lỗi khi nhập tên chi nhánh: {str(e)}")
            return False

    # Hàm nhập địa chỉ chi nhánh
    def enter_address(self, address):
        try:
            address_input = self.wait.until(
                EC.visibility_of_element_located(self.locators.ADDRESS_TEXT_INPUT)
            )
            address_input.clear()
            address_input.send_keys(address)
            logging.info(f"Đã nhập địa chỉ chi nhánh: {address}")
            return True
        except TimeoutException:
            logging.error("Không tìm thấy ô nhập địa chỉ chi nhánh!")
            return False
        except Exception as e:
            logging.error(f"Lỗi khi nhập địa chỉ chi nhánh: {str(e)}")
            return False

    # Hàm nhập tên chi nhánh
    def enter_en_name(self, name):
        try:
            name_input = self.wait.until(
                EC.visibility_of_element_located(self.locators.EN_NAME_TEXT_INPUT)
            )
            name_input.clear()
            name_input.send_keys(name)
            logging.info(f"Đã nhập tên chi nhánh: {name}")
            return True
        except TimeoutException:
            logging.error("Không tìm thấy ô nhập tên chi nhánh!")
            return False
        except Exception as e:
            logging.error(f"Lỗi khi nhập tên chi nhánh: {str(e)}")
            return False

    # Hàm nhập địa chỉ chi nhánh
    def enter_en_address(self, address):
        try:
            address_input = self.wait.until(
                EC.visibility_of_element_located(self.locators.EN_ADDRESS_TEXT_INPUT)
            )
            address_input.clear()
            address_input.send_keys(address)
            logging.info(f"Đã nhập địa chỉ chi nhánh: {address}")
            return True
        except TimeoutException:
            logging.error("Không tìm thấy ô nhập địa chỉ chi nhánh!")
            return False
        except Exception as e:
            logging.error(f"Lỗi khi nhập địa chỉ chi nhánh: {str(e)}")
            return False

    # Hàm nhập nội dung vào khung soạn thảo (CKEditor)
    def enter_content(self, content):
        try:
            # Chờ và chuyển vào iframe của CKEditor
            iframe = self.wait.until(
                EC.presence_of_element_located(self.locators.CONTENT_TEXT_AREA)
            )
            self.driver.switch_to.frame(iframe)

            # Chờ vùng soạn thảo trong iframe, sau đó nhập nội dung
            editable_area = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//body"))
            )
            editable_area.clear()
            editable_area.send_keys(content)
            logging.info(f"Đã nhập nội dung chi nhánh: {content}")

            # Thoát khỏi iframe
            self.driver.switch_to.default_content()
            return True

        except TimeoutException:
            logging.error("Không tìm thấy iframe hoặc vùng soạn thảo CKEditor!")
            return False
        except Exception as e:
            logging.error(f"Lỗi khi nhập nội dung chi nhánh: {str(e)}")
            return False

    # Hàm nhập nội dung vào khung soạn thảo (CKEditor)
    def enter_en_content(self, content):
        try:
            # Chờ và chuyển vào iframe của CKEditor
            iframe = self.wait.until(
                EC.presence_of_element_located(self.locators.EN_CONTENT_TEXT_AREA)
            )
            self.driver.switch_to.frame(iframe)

            # Chờ vùng soạn thảo trong iframe, sau đó nhập nội dung
            editable_area = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//body"))
            )
            editable_area.clear()
            editable_area.send_keys(content)
            logging.info(f"Đã nhập nội dung chi nhánh: {content}")

            # Thoát khỏi iframe
            self.driver.switch_to.default_content()
            return True

        except TimeoutException:
            logging.error("Không tìm thấy iframe hoặc vùng soạn thảo CKEditor!")
            return False
        except Exception as e:
            logging.error(f"Lỗi khi nhập nội dung chi nhánh: {str(e)}")
            return False

     # Hàm nhập số điện thoại chi nhánh
    def enter_phone(self, phone_number):
        try:
            phone_input = self.wait.until(
                EC.visibility_of_element_located(self.locators.PHONE_TEXT_INPUT)
            )
            phone_input.clear()
            phone_input.send_keys(phone_number)
            logging.info(f"Đã nhập số điện thoại: {phone_number}")
            return True
        except TimeoutException:
            logging.error("Không tìm thấy ô nhập số điện thoại!")
            return False
        except Exception as e:
            logging.error(f"Lỗi khi nhập số điện thoại: {str(e)}")
            return False
        
    # Hàm nhập số fax chi nhánh
    def enter_fax(self, fax_number):
        try:
            fax_input = self.wait.until(
                EC.visibility_of_element_located(self.locators.FAX_TEXT_INPUT)
            )
            fax_input.clear()
            fax_input.send_keys(fax_number)
            logging.info(f"Đã nhập số fax: {fax_number}")
            return True
        except TimeoutException:
            logging.error("Không tìm thấy ô nhập số fax!")
            return False
        except Exception as e:
            logging.error(f"Lỗi khi nhập số fax: {str(e)}")
            return False
    
    # Hàm nhập kinh độ chi nhánh
    def enter_longitude(self, longitude_value):
        try:
            longitude_input = self.wait.until(
                EC.visibility_of_element_located(self.locators.LONGITUDE_TEXT_INPUT)
            )
            longitude_input.clear()
            longitude_input.send_keys(longitude_value)
            logging.info(f"Đã nhập kinh độ: {longitude_value}")
            return True
        except TimeoutException:
            logging.error("Không tìm thấy ô nhập kinh độ!")
            return False
        except Exception as e:
            logging.error(f"Lỗi khi nhập kinh độ: {str(e)}")
            return False

    # Hàm nhập vĩ độ chi nhánh
    def enter_latitude(self, latitude_value):
        try:
            latitude_input = self.wait.until(
                EC.visibility_of_element_located(self.locators.LATITUDE_TEXT_INPUT)
            )
            latitude_input.clear()
            latitude_input.send_keys(latitude_value)
            logging.info(f"Đã nhập vĩ độ: {latitude_value}")
            return True
        except TimeoutException:
            logging.error("Không tìm thấy ô nhập vĩ độ!")
            return False
        except Exception as e:
            logging.error(f"Lỗi khi nhập vĩ độ: {str(e)}")
            return False

    # Hàm nhập email chi nhánh
    def enter_email(self, email_value):
        try:
            email_input = self.wait.until(
                EC.visibility_of_element_located(self.locators.EMAIL_TEXT_INPUT)
            )
            email_input.clear()
            email_input.send_keys(email_value)
            logging.info(f"Đã nhập email: {email_value}")
            return True
        except TimeoutException:
            logging.error("Không tìm thấy ô nhập email!")
            return False
        except Exception as e:
            logging.error(f"Lỗi khi nhập email: {str(e)}")
            return False

    # Hàm nhập giá trị sắp xếp
    def enter_sort_order(self, sort_value):
        try:
            sort_input = self.wait.until(
                EC.visibility_of_element_located(self.locators.SORT_ORDER_TEXT_INPUT)
            )
            sort_input.clear()
            sort_input.send_keys(sort_value)
            logging.info(f"Đã nhập giá trị sắp xếp: {sort_value}")
            return True
        except TimeoutException:
            logging.error("Không tìm thấy ô nhập giá trị sắp xếp!")
            return False
        except Exception as e:
            logging.error(f"Lỗi khi nhập giá trị sắp xếp: {str(e)}")
            return False