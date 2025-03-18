import time
from locators.locator_article import LocatorArticle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class ImageArticle:
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorArticle

    def click_upload_thumbnail_image_field(self):
        upload_field = self.wait.until(EC.element_to_be_clickable(self.locators.UPLOAD_THUMBNAIL_IMAGE_FIELD))
        upload_field.click()
    
    def click_upload_thumbnail_image_button(self):
        upload_field = self.wait.until(EC.element_to_be_clickable(self.locators.UPLOAD_THUMBNAIL_IMAGE_BUTTON))
        upload_field.click()
    
    def click_upload_feature_image_field(self):
        upload_field = self.wait.until(EC.element_to_be_clickable(self.locators.UPLOAD_FEATURE_IMAGE_FIELD))
        self.driver.execute_script("window.scrollTo({top: arguments[0].getBoundingClientRect().top + window.scrollY - 100, behavior: 'smooth'});", upload_field) 
        WebDriverWait(self.driver, 5).until(EC.visibility_of(upload_field))
        ActionChains(self.driver).move_to_element(upload_field).click().perform()

    def click_upload_feature_image_button(self):
        feature_button = self.wait.until(EC.element_to_be_clickable(self.locators.UPLOAD_FEATURE_IMAGE_BUTTON))
        self.driver.execute_script("window.scrollTo({top: arguments[0].getBoundingClientRect().top + window.scrollY - 100, behavior: 'smooth'});",feature_button)
        WebDriverWait(self.driver, 2).until(EC.visibility_of(feature_button))
        ActionChains(self.driver).move_to_element(feature_button).click().perform()
    
    def is_upload_popup_displayed(self):
        try:
            print("Checking if upload popup is displayed...")
            return self.wait.until(EC.visibility_of_element_located(self.locators.UPLOAD_IMAGE_POPUP)) is not None
        except TimeoutException:
            print("Upload popup not found within timeout!")
            return False
    
    def click_tab_browser_by_href(self):
        try:
            tab_browser = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='#browse-content']")))
            tab_browser.click()
            print("Click tab Browse thành công (Cách 2 - Click bằng href).")
        except Exception as e:
            print(f"Không thể click vào tab Browse bằng href: {e}")

    def wait_for_file_listing(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.locators.FILE_LISTING))
            print("Danh sách file hình ảnh đã xuất hiện.")
        except Exception as e:
            print(f"Không tìm thấy danh sách file hình ảnh: {e}")

    def select_first_image(self):
        try:
            images = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.locators.FILE_LISTING))
            if images:
                first_image = images[0]
                if not first_image.is_displayed():
                    self.driver.execute_script("arguments[0].style.display = 'block';", first_image)
                    time.sleep(1)
                self.driver.execute_script("arguments[0].scrollIntoView();", first_image)
                try:
                    first_image.click()
                    print("Đã chọn ảnh đầu tiên (Click thường).")
                except:
                    self.driver.execute_script("arguments[0].click();", first_image)
                    print("Đã chọn ảnh đầu tiên (Click JS).")
            else:
                print("Không tìm thấy ảnh nào trong danh sách.")
        except Exception as e:
            print(f"Lỗi khi click vào ảnh đầu tiên: {e}")
    
    def click_choose_upload_button(self):
        try:
            upload_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locators.CHOOSE_UPLOAD_BUTTON))
            self.driver.execute_script("arguments[0].scrollIntoView();", upload_button)
            time.sleep(1)
            self.driver.execute_script("arguments[0].click();", upload_button)
            print("Đã click vào nút 'Upload'")
        except Exception as e:
            print(f"Không thể click vào nút 'Upload': {e}")
    
    def is_thumbnail_image_uploaded(self):
        try:
            uploaded_image = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='article-image-id_upload']/div/div[1]/a")))
            return uploaded_image.is_displayed()
        except:
            return False
    
    def is_feature_image_uploaded(self):
        try:
            uploaded_image = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='article-image-id_upload']/div/div[1]/a")))
            return uploaded_image.is_displayed()
        except:
            return False
    
    def delete_thumbnail_image(self):
        try:
            self.wait.until(EC.presence_of_element_located(LocatorArticle.DELETE_THUMBNAIL_IMAGE))
            delete_button = self.wait.until(EC.element_to_be_clickable(LocatorArticle.DELETE_THUMBNAIL_IMAGE))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", delete_button)
            time.sleep(2) 
            try:
                delete_button.click()
            except:
                self.driver.execute_script("arguments[0].click();", delete_button)
            print("Đã xóa ảnh Thumbnail.")
        except Exception as e:
            print(f"Lỗi khi xóa ảnh Thumbnail: {e}")
    
    def is_thumbnail_image_deleted(self):
        try:
            self.wait.until(EC.invisibility_of_element_located(LocatorArticle.DELETE_THUMBNAIL_IMAGE))
            return True
        except:
            return False
    
    def delete_feature_image(self):
        try:
            self.wait.until(EC.presence_of_element_located(LocatorArticle.DELETE_FEATURE_IMAGE))
            delete_button = self.wait.until(EC.element_to_be_clickable(LocatorArticle.DELETE_FEATURE_IMAGE))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", delete_button)
            time.sleep(2) 
            try:
                delete_button.click()
            except:
                self.driver.execute_script("arguments[0].click();", delete_button)
            print("Đã xóa ảnh Feature.")
        except Exception as e:
            print(f"Lỗi khi xóa ảnh Feature: {e}")
    
    def is_feature_image_deleted(self):
        try:
            self.wait.until(EC.invisibility_of_element_located(LocatorArticle.DELETE_FEATURE_IMAGE))
            return True
        except:
            return False


