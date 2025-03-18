from selenium.webdriver.common.by import By
from locators.locator_article import LocatorArticle
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DateArticle:
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorArticle

    def get_public_date(self):
        date_input = self.wait.until(EC.visibility_of_element_located(self.locators.PUBLIC_DATE))
        return date_input.get_attribute("value")
    
    def set_public_date(self, date_value):
        public_date_field = self.wait.until(EC.visibility_of_element_located(self.locators.PUBLIC_DATE))
        public_date_field.clear() 
        public_date_field.send_keys(date_value)
    
    def open_date_picker(self):
        try:
            date_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locators.PUBLIC_DATE_INPUT))
            self.driver.execute_script("arguments[0].scrollIntoView();", date_input)
            date_input.click()
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.locators.DATE_PICKER))
        except TimeoutException:
            raise Exception("Lỗi: Không thể mở Date Picker!")
        
    def click_day_in_date_picker(self, day):
        try:
            day_locator = (By.XPATH, self.locators.DATE_PICKER_DAY[1].format(day))
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(day_locator)).click()
        except TimeoutException:
            raise Exception(f"Lỗi: Không thể chọn ngày {day} trong Date Picker!")
