import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Login:
    URL = "https://mpire-cms-demo.mpire.asia/cms/login"
    USERNAME_FIELD = (By.XPATH, "//input[@id='inputName']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='inputPassword']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@type,'submit')]")
    ERROR_MESSAGE = (By.XPATH, "//*[@id='login-form']/div")

    @classmethod
    def __init__(self, driver, username="admin", password="Mpire4dmin", timeout=5, dashboard_url="https://mpire-cms-demo.mpire.asia/cms/dashboard"):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.dashboard_url = dashboard_url
        self.username = username
        self.password = password

    def open(self):
        logging.info("Mở trang login: %s", self.URL)
        self.driver.get(self.URL)

    def enter_username(self):
        logging.info("Nhập username")
        username_field = self.wait.until(EC.visibility_of_element_located(self.USERNAME_FIELD))
        username_field.clear()
        username_field.send_keys(self.username)

    def enter_password(self):
        logging.info("Nhập password")
        password_field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD))
        password_field.clear()
        password_field.send_keys(self.password)

    def click_login_button(self):
        logging.info("Nhấn nút đăng nhập")
        login_button = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_button.click()

    def login(self):
        try:
            self.open()
            self.enter_username()
            self.enter_password()
            self.click_login_button()
            return self.is_login_successful()
        except Exception as e:
            logging.error("Đăng nhập thất bại: %s", str(e))
            return False

    def is_login_successful(self):
        try:
            self.wait.until(EC.url_to_be(self.dashboard_url))
            logging.info("Đăng nhập thành công!")
            return True
        except:
            try:
                error_msg = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE)).text
                logging.warning("Đăng nhập thất bại! Lỗi: %s", error_msg)
            except:
                logging.warning("Đăng nhập thất bại nhưng không có thông báo lỗi rõ ràng.")
            return False

    def close(self):
        logging.info("Đóng trình duyệt")
        self.driver.quit()