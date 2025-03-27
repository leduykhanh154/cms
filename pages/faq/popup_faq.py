import time
import logging
from locators.faq.locator_faq import LocatorFAQ
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class PopupFAQ:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorFAQ

    # Hàm kiểm tra xem popup 'Vui lòng chọn Câu hỏi để xóa.' có hiển thị không
    def is_select_question_to_delete_popup_displayed(self): 
        try:
            time.sleep(1)
            popup_element = self.wait.until(EC.visibility_of_element_located(self.locators.SELECT_QUESTION_POPUP))
            logging.info("Popup 'Vui lòng chọn Câu hỏi để xóa.' được hiển thị!")
            return popup_element.is_displayed()
        except Exception as e:
            logging.error(f"Lỗi khi kiểm tra pop-up 'Vui lòng chọn Câu hỏi để xóa.': {e}", exc_info=True)
            return False
        
    # Hàm kiểm tra xem popup 'Bạn có chắc chắn ?' có hiển thị không
    def is_secure_popup_displayed(self): 
        try:
            time.sleep(1)
            popup_element = self.wait.until(EC.visibility_of_element_located(self.locators.SECURE_POPUP))
            logging.info("Popup 'Bạn có chắc chắn ?' được hiển thị!")
            return popup_element.is_displayed()
        except Exception as e:
            logging.error(f"Lỗi khi kiểm tra pop-up 'Bạn có chắc chắn ?': {e}", exc_info=True)
            return False