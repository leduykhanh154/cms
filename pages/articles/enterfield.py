import logging
from locators.locator_article import LocatorArticle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EnterFieldArticle:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorArticle
    
    # Hàm nhập Tiêu đề - VI
    def enter_title_vi(self, title):
        title_input = self.wait.until(EC.visibility_of_element_located(self.locators.TITLE_INPUT))
        title_input.clear()
        title_input.send_keys(title)
        logging.info(f"Đã nhập tiêu đề: {title}")
    
    def enter_title_en(self, title):
        title_input = self.wait.until(EC.visibility_of_element_located(self.locators.TITLE_EN_INPUT))
        title_input.clear()
        title_input.send_keys(title)
        logging.info(f"Đã nhập tiêu đề: {title}")

    def enter_short_description_vi(self, title):
        title_input = self.wait.until(EC.visibility_of_element_located(self.locators.SHORT_DESCRIPTION_VI_INPUT))
        title_input.clear()
        title_input.send_keys(title)
        logging.info(f"Đã nhập mô tả ngắn: {title}")
    
    def enter_short_description_en(self, title):
        title_input = self.wait.until(EC.visibility_of_element_located(self.locators.SHORT_DESCRIPTION_EN_INPUT))
        title_input.clear()
        title_input.send_keys(title)
        logging.info(f"Đã nhập mô tả ngắn: {title}")
    
    def enter_content_vi(self, content):
        try:
            self.wait.until(lambda driver: driver.execute_script("return CKEDITOR.instances['languages[vi][content]'] !== undefined"))
            ckeditor_content = self.driver.execute_script("return CKEDITOR.instances['languages[vi][content]'].getData();")
            logging.info(f"Nội dung trong CKEditor trước khi setData: {ckeditor_content}")
            self.driver.execute_script("""CKEDITOR.instances['languages[vi][content]'].setData(arguments[0]);""", content)
            self.driver.execute_script("CKEDITOR.instances['languages[vi][content]'].updateElement();")
            self.driver.execute_script("""let textarea = document.getElementById('languages[vi][content]');textarea.dispatchEvent(new Event('input', { bubbles: true }));textarea.dispatchEvent(new Event('change', { bubbles: true }));""")
            form_validation = self.driver.execute_script("""let form = $('textarea[name="languages[vi][content]"]').closest('form');return form.length > 0 && form.data('formValidation') !== undefined;""")
            if form_validation:
                self.driver.execute_script("""let form = $('textarea[name="languages[vi][content]"]').closest('form');form.data('formValidation').revalidateField('languages[vi][content]');""")
                logging.info("Nhập nội dung vào CKEditor và tái xác thực trường 'content' thành công.")
            else:
                logging.warning("Form chưa được khởi tạo validation hoặc không tìm thấy form.")
        except Exception as e:
            logging.error(f"Lỗi khi nhập nội dung vào CKEditor: {e}")
            raise
    
    def enter_content_en(self, content):
        try:
            self.wait.until(lambda driver: driver.execute_script("return CKEDITOR.instances['languages[en][content]'] !== undefined"))
            ckeditor_content = self.driver.execute_script("return CKEDITOR.instances['languages[en][content]'].getData();")
            logging.info(f"Nội dung trong CKEditor trước khi setData: {ckeditor_content}")
            self.driver.execute_script("""CKEDITOR.instances['languages[en][content]'].setData(arguments[0]);""", content)
            self.driver.execute_script("CKEDITOR.instances['languages[en][content]'].updateElement();")
            self.driver.execute_script("""let textarea = document.getElementById('languages[en][content]');textarea.dispatchEvent(new Event('input', { bubbles: true }));textarea.dispatchEvent(new Event('change', { bubbles: true }));""")
            form_validation = self.driver.execute_script("""let form = $('textarea[name="languages[en][content]"]').closest('form');return form.length > 0 && form.data('formValidation') !== undefined;""")
            if form_validation:
                self.driver.execute_script("""let form = $('textarea[name="languages[en][content]"]').closest('form');form.data('formValidation').revalidateField('languages[en][content]');""")
                logging.info("Nhập nội dung vào CKEditor và tái xác thực trường 'content' (English) thành công.")
            else:
                logging.warning("Form chưa được khởi tạo validation hoặc không tìm thấy form.")
        except Exception as e:
            logging.error(f"Lỗi khi nhập nội dung vào CKEditor (English): {e}")
            raise

    def ordering(self, ordering):
        ordering_input = self.wait.until(EC.visibility_of_element_located(self.locators.ORDERING))
        ordering_input.clear()
        ordering_input.send_keys(ordering)
        logging.info(f"Đã nhập tiêu đề: {ordering}")

    def enter_public_date(self, date_value):
        date_input = self.wait.until(EC.visibility_of_element_located(self.locators.PUBLIC_DATE))
        date_input.clear()
        date_input.send_keys(date_value)
        logging.info(f"Đã nhập Ngày đăng: {date_value}")


    

