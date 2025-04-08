import time
import logging
import selenium
from selenium.webdriver.common.by import By
from locators.locator_article_type.locator_new_article_type import LocatorNewArticleType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class IsDisplayedNewArticleType:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorNewArticleType  
    
    # Ham kiem tra noi dung label 'Trang thai'
    def is_label_status_displayed(self):
        try:
            label = self.wait.until(
                EC.visibility_of_element_located(self.locators.LABEL_STATUS)
            )
            if label.text.strip() == "Hiển thị":
                logging.info("LABEL_STATUS hiển thị đúng: 'Hiển thị'.")
                return True
            else:
                logging.warning(f"LABEL_STATUS không đúng! Giá trị hiện tại: '{label.text.strip()}'.")
                return False
        except TimeoutException:
            logging.error("Không tìm thấy LABEL_STATUS!")
            return False
        
    # Ham kiem tra noi dung label 'Loai bai viet'
    def is_label_article_type_correct(self):
        try:
            label = self.wait.until(
                EC.visibility_of_element_located(self.locators.LABEL_ARTICLE_TYPE)
            )
            actual_text = label.text.strip()
            expected_text = "Loại bài viết*"
            if actual_text == expected_text:
                logging.info(f"Giá trị LABEL_ARTICLE_TYPE đúng: '{actual_text}'.")
                return True
            else:
                logging.warning(f"Giá trị LABEL_ARTICLE_TYPE không đúng: '{actual_text}' (mong đợi: '{expected_text}').")
                return False
        except TimeoutException:
            logging.error("Không thể tìm thấy LABEL_ARTICLE_TYPE trên giao diện!")
            return False
        
    # Ham kiem tra nut dich noi dung 
    def is_translate_button_displayed(self):
        try:
            translate_button = self.wait.until(
                EC.visibility_of_element_located(self.locators.TRANSLATE_BUTTON)
            )
            logging.info("Nút 'Dịch nội dung' xuất hiện.")
            return True
        except TimeoutException:
            logging.warning("Nút 'Dịch nội dung' không xuất hiện!")
            return False

    # Ham kiem tra error message 'Vui long nhap loai bai viet'
    def is_please_field_type_article_displayed(self):
        try:
            element = self.wait.until(
                EC.presence_of_element_located(self.locators.VI_ERROR_PLEASE_FIELD_TYPE_ARTICLE)
            )
            logging.info("Thông báo 'Vui lòng nhập loại bài viết' đã xuất hiện.")
            return True
        except TimeoutException:
            logging.error("Thông báo 'Vui lòng nhập loại bài viết' không xuất hiện!")
            return False
     
    # Ham kiem tra co duoc dua toi trang chinh sua loai bai viet chua    
    def is_edit_text_present(self):
        try:
            text_edit_element = self.wait.until(
                EC.presence_of_element_located(self.locators.TEXT_EDIT)
            )
            text_content = text_edit_element.text.strip()

            if "Chỉnh sửa" in text_content:
                logging.info("He thong chuyen huong den trang chinh sua loai bai viet.")
                return True
            else:
                logging.warning("He thong khong chuyen huong den trang chinh sua loai bai viet.")
                return False
        except TimeoutException:
            logging.error("Phần tử 'TEXT_EDIT' không xuất hiện.")
            return False

    # Kiểm tra xem popup 'Upload image' có xuat hien khong
    def is_popup_upload_image_displayed(self):
        try:
            # Lấy toàn bộ nội dung văn bản của trang
            page_text = self.driver.page_source

            # Kiểm tra xem chuỗi "Upload image" có trong nội dung trang không
            if "upload image" in page_text:
                logging.info("Popup tải lên ảnh đã xuất hiện với nội dung 'Upload image'.")
                return True
            else:
                logging.error("Không tìm thấy chữ 'Upload image' trên toàn bộ trang!")
                return False
        except Exception as e:
            logging.error(f"Lỗi khi kiểm tra popup: {e}")
            return False

    # Tab Tieng Viet
    # Ham kiem tra nut 'Xoa anh' co hien thi khong
    def is_delete_image_button_displayed(self):
        try:
            delete_button = self.wait.until(
                EC.visibility_of_element_located(self.locators.BUTTON_DELETE_IMAGE)
            )
            logging.info("Nút 'Xóa ảnh' đã xuất hiện.")
            return True
        except TimeoutException:
            logging.error("Nút 'Xóa ảnh' không xuất hiện!")
            return False

    # Ham kiem tra anh co xuat hien khong
    def is_uploaded_image_displayed(self):
        try:
            uploaded_image = self.wait.until(
                EC.visibility_of_element_located(self.locators.FIELD_IMAGE)
            )
            logging.info("Ảnh đã hiển thị trên giao diện sau khi tải lên.")
            return True
        except TimeoutException:
            logging.error("Ảnh không hiển thị sau khi tải lên!")
            return False

    # Tab English
    # Ham kiem tra nut 'Xoa anh' co hien thi khong
    def is_en_delete_image_button_displayed(self):
        try:
            delete_button = self.wait.until(
                EC.visibility_of_element_located(self.locators.EN_BUTTON_DELETE_IMAGE)
            )
            logging.info("Nút 'Xóa ảnh' đã xuất hiện.")
            return True
        except TimeoutException:
            logging.error("Nút 'Xóa ảnh' không xuất hiện!")
            return False

    # Ham kiem tra anh co xuat hien khong
    def is_en_uploaded_image_displayed(self):
        try:
            uploaded_image = self.wait.until(
                EC.visibility_of_element_located(self.locators.EN_FIELD_IMAGE)
            )
            logging.info("Ảnh đã hiển thị trên giao diện sau khi tải lên.")
            return True
        except TimeoutException:
            logging.error("Ảnh không hiển thị sau khi tải lên!")
            return False

    # Tab Thong tin chung
    # Ham kiem tra dropdown status co duoc mo khong
    def is_dropdown_opened(self):
        if self.is_text_present_on_page("Chờ xử lý"):
            print("Dropdown đã mở (tìm thấy 'Chờ xử lý').")
            return True
        else:
            print("Dropdown chưa mở hoặc không tìm thấy 'Chờ xử lý'.")
            return False
    
    # Ham kiem tra dropdown Loai bai viet cap cha co mo chua
    def is_father_dropdown_opened(self):
        if self.is_text_present_on_page("Lĩnh vực kinh doanh"):
            print("Dropdown 'Father Type' đã mở (tìm thấy 'Lĩnh vực kinh doanh').")
            return True
        else:
            print("Dropdown 'Father Type' chưa mở hoặc không tìm thấy 'Lĩnh vực kinh doanh'.")
            return False
    
    # Ham kiem tra dropdown Bo banner da mo chua
    def is_banner_dropdown_opened(self):
        if self.is_text_present_on_page("Banner icon"):
            print("Dropdown 'Banner Set' đã mở (tìm thấy 'Banner icon' trên toàn trang).")
            return True
        else:
            print("Dropdown 'Banner Set' chưa mở hoặc không tìm thấy 'Banner icon' trên toàn trang.")
            return False
    
    # Ham tim kiem tu khoa tren trang
    def is_text_present_on_page(self, text):
        try:
            body_element = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            return text in body_element.text
        except:
            return False
