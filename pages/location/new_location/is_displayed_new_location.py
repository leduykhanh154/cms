import time
import logging
import selenium
from selenium.webdriver.common.by import By
from locators.locator_location.locator_new_location import LocatorNewLocation
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class IsDisplayedNewLocation:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorNewLocation 
    
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

    # Hàm kiểm tra text không hiển thị trên trang
    def is_text_not_displayed_on_page(self, expected_text, timeout=3):
        try:
            # Chờ một khoảng thời gian để chắc chắn rằng text không xuất hiện
            WebDriverWait(self.driver, timeout).until_not(
                lambda d: expected_text in d.page_source
            )
            logging.info(f"'{expected_text}' Không hiển thị trên trang (như mong đợi).")
            return True

        except TimeoutException:
            logging.error(f"'{expected_text}' vẫn còn hiển thị trên trang sau {timeout} giây.")
            return False
        except Exception as e:
            logging.error(f"Lỗi khi kiểm tra không hiển thị trên trang: {str(e)}")
            return False

    # Hàm kiểm tra text hiển thị trong phần tử PROVINCE_DROPDOWN
    def is_text_displayed_in_province_dropdown(self, expected_text):
        try:
            # Chờ phần tử dropdown có mặt trên trang
            element = self.wait.until(
                EC.presence_of_element_located(self.locators.PROVINCE_DROPDOWN)
            )

            # Lấy text của phần tử dropdown đang hiển thị (có thể là text của tỉnh đã chọn)
            actual_text = element.text.strip()

            # Kiểm tra xem expected_text có chứa trong text của dropdown hiện tại không
            if expected_text.lower() in actual_text.lower():
                logging.info(f"Text '{expected_text}' có trong dropdown tỉnh/thành.")
                return True
            else:
                logging.error(f"Text '{expected_text}' KHÔNG có trong dropdown tỉnh/thành.")
                return False

        except Exception as e:
            logging.error(f"Lỗi khi kiểm tra text trong dropdown tỉnh/thành: {str(e)}")
            return False


    # Hàm kiểm tra text KHÔNG hiển thị trong phần tử PROVINCE_DROPDOWN
    def is_text_not_displayed_in_province_dropdown(self, expected_text):
        try:
            element = self.wait.until(
                EC.presence_of_element_located(self.locators.PROVINCE_DROPDOWN)
            )
            actual_text = element.text.strip()

            if expected_text.lower() not in actual_text.lower():
                logging.info(f"Text '{expected_text}' KHÔNG hiển thị trong dropdown tỉnh/thành (như mong đợi).")
                return True
            else:
                logging.error(f"Text '{expected_text}' vẫn còn hiển thị trong dropdown tỉnh/thành.")
                return False

        except Exception as e:
            logging.error(f"Lỗi khi kiểm tra text không hiển thị trong dropdown tỉnh/thành: {str(e)}")
            return False


    # Hàm kiểm tra text hiển thị trong dropdown quận/huyện
    def is_text_displayed_in_district_dropdown(self, expected_text):
        try:
            element = self.wait.until(
                EC.presence_of_element_located(self.locators.DISTRICT_DROPDOWN)
            )
            actual_text = element.text.strip()

            if expected_text.lower() in actual_text.lower():
                logging.info(f"Text '{expected_text}' hiển thị trong dropdown quận/huyện.")
                return True
            else:
                logging.error(f"Text '{expected_text}' KHÔNG hiển thị trong dropdown quận/huyện.")
                return False

        except Exception as e:
            logging.error(f"Lỗi khi kiểm tra text trong dropdown quận/huyện: {str(e)}")
            return False
    
    # Hàm kiểm tra text KHÔNG hiển thị trong dropdown quận/huyện
    def is_text_not_displayed_in_district_dropdown(self, expected_text):
        try:
            element = self.wait.until(
                EC.presence_of_element_located(self.locators.DISTRICT_DROPDOWN)
            )
            actual_text = element.text.strip()

            if expected_text.lower() not in actual_text.lower():
                logging.info(f"Text '{expected_text}' KHÔNG hiển thị trong dropdown quận/huyện (như mong đợi).")
                return True
            else:
                logging.error(f"Text '{expected_text}' vẫn đang hiển thị trong dropdown quận/huyện.")
                return False

        except Exception as e:
            logging.error(f"Lỗi khi kiểm tra text không hiển thị trong dropdown quận/huyện: {str(e)}")
            return False

    # Hàm kiểm tra text hiển thị tại item đầu tiên trong danh sách quận/huyện
    def is_text_displayed_in_first_district_item(self, expected_text):
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(self.locators.FIRST_DISTRICT_ITEM)
            )
            actual_text = element.text.strip()

            if expected_text in actual_text:
                logging.info(f"Text '{expected_text}' hiển thị trong item đầu tiên của danh sách quận/huyện.")
                return True
            else:
                logging.error(f"Text '{expected_text}' KHÔNG hiển thị trong item đầu tiên của danh sách quận/huyện.")
                return False

        except Exception as e:
            logging.error(f"Lỗi khi kiểm tra text trong item đầu tiên của danh sách quận/huyện: {str(e)}")
            return False
    
    # Hàm kiểm tra không hiển thị tại item đầu tiên trong danh sách quận/huyện
    def is_first_district_item_not_present(self):
        try:
            self.driver.find_element(*self.locators.FIRST_DISTRICT_ITEM)
            logging.warning("Phần tử FIRST_ITEM_DISTRICT vẫn đang tồn tại trong DOM.")
            return False
        except:
            logging.info("Phần tử FIRST_ITEM_DISTRICT KHÔNG tồn tại trong DOM (như mong đợi).")
            return True

    # Hàm kiểm tra text hiển thị trong dropdown trạng thái
    def is_text_displayed_in_status_dropdown(self, expected_text):
        try:
            element = self.wait.until(
                EC.presence_of_element_located(self.locators.STATUS_DROPDOWN)
            )
            actual_text = element.text.strip()

            if expected_text.lower() in actual_text.lower():
                logging.info(f"Text '{expected_text}' hiển thị trong dropdown trạng thái.")
                return True
            else:
                logging.error(f"Text '{expected_text}' KHÔNG hiển thị trong dropdown trạng thái.")
                return False

        except Exception as e:
            logging.error(f"Lỗi khi kiểm tra text trong dropdown trạng thái: {str(e)}")
            return False
    
    # Hàm kiểm tra popup Upload Image có xuất hiện không
    def is_upload_image_popup_displayed(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.locators.UPLOAD_IMAGE_POPUP)
            )
            logging.info("Popup Upload Image đã hiển thị.")
            return True
        except TimeoutException:
            logging.error("Popup Upload Image không hiển thị.")
            return False
    
    # Hàm kiểm tra nút Delete Image có hiển thị không
    def is_delete_image_button_displayed(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.locators.DELETE_IMAGE_BUTTON)
            )
            logging.info("Nút Delete Image đã hiển thị.")
            return True
        except TimeoutException:
            logging.error("Nút Delete Image không hiển thị.")
            return False
    
    # Hàm kiểm tra nút Delete Image không hiển thị
    def is_delete_image_button_not_displayed(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.locators.DELETE_IMAGE_BUTTON)
            )
            logging.error("Nút Delete Image vẫn đang hiển thị.")
            return False
        except TimeoutException:
            logging.info("Nút Delete Image không hiển thị như mong đợi.")
            return True

    # Ham verify mot phan cua duong dan    
    def verify_path_of_current_url(self, expected_partial_url):
        try:
            current_url = self.driver.current_url
            if expected_partial_url in current_url:
                logging.info(f"URL hiện tại chứa phần mong đợi: {expected_partial_url}")
                return True
            else:
                logging.error(f"URL không chứa phần mong đợi! Expected to contain: {expected_partial_url}, Actual: {current_url}")
                return False
        except Exception as e:
            logging.error(f"Lỗi khi kiểm tra URL: {str(e)}")
            return False
    
    # Hàm kiểm tra ảnh có hiển thị không
    def is_image_displayed(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.locators.IMAGE_FIELD)
            )
            logging.info("Ảnh đã hiển thị.")
            return True
        except TimeoutException:
            logging.error("Ảnh không hiển thị.")
            return False
    
    # Hàm kiểm tra ảnh không hiển thị
    def is_image_not_displayed(self):
        try:
            element = self.wait.until(
                EC.presence_of_element_located(self.locators.IMAGE_FIELD)
            )
            content = element.text.strip()
            if content == "":
                logging.info("không có ảnh hiển thị.")
                return True
            else:
                logging.error(f"Ảnh vẫn đang hiển thị")
                return False
        except TimeoutException:
            logging.error("Không tìm thấy phần tử ảnh.")
            return False

    