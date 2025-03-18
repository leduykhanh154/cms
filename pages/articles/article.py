import logging
from selenium.webdriver.common.by import By
from locators.locator_article import LocatorArticle
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Article:
    # Hàm khởi tạo driver
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorArticle  
    
    # Hàm nhấn vào một menu cụ thể trên giao diện
    def click_menu(self, locator, menu_name):
        try:
            menu = self.wait.until(EC.element_to_be_clickable(locator))
            menu.click()
            logging.info(f"Đã nhấn menu {menu_name}.")
            return self
        except TimeoutException as e:
            logging.error(f"Không thể nhấn menu {menu_name}: {e}", exc_info=True)
            raise
    
    # Hàm nhấn vào menu Nội dung
    def click_content_menu(self):
        return self.click_menu(self.locators.CONTENT_MENU, "Nội dung")

    # Hàm nhấn vào menu Bài viết
    def click_article_menu(self):
        return self.click_menu(self.locators.ARTICLE_MENU, "Bài viết")

    # Hàm nhấn vào menu Tất cả bài viết
    def click_all_article_menu(self):
        self.click_menu(self.locators.ALL_ARTICLE_MENU, "Tất cả bài viết")
        expected_url = "https://mpire-cms-demo.mpire.asia/cms/article"
        try:
            self.wait.until(EC.url_to_be(expected_url))
            logging.info("Trang 'Tất cả bài viết' đã load thành công.")
            return True
        except TimeoutException:
            logging.error("Trang 'Tất cả bài viết' không tải được!")
            return False
    
    # Hàm nhấn vào nút Tạo mới
    def click_create_new_button(self):
        try:
            create_new_button = self.wait.until(EC.element_to_be_clickable(self.locators.CREATE_NEW_BUTTON))
            self.driver.execute_script("arguments[0].click();", create_new_button)
            logging.info("Đã nhấn nút Tạo mới.")
            expected_url = self.locators.CREATE_ARTICLE_PAGE
            self.wait.until(EC.url_to_be(expected_url))
            return self.driver.current_url == expected_url
        except TimeoutException as e:
            logging.error(f"Lỗi khi nhấn nút Tạo mới hoặc chuyển hướng: {e}", exc_info=True)
            return False
    
    # Hàm nhấn vào tab Tiếng Việt 
    def click_vi_tab(self):
        return self.click_menu(self.locators.VI_TAB, "Tiếng Việt")

    # Hàm nhấn vào tab English
    def click_en_tab(self):
        return self.click_menu(self.locators.EN_TAB, "English")
    
    # Hàm nhấn vào nút Dịch nội dung ở tab English
    def click_translate_content_button(self):
        try:
            translate_button = self.wait.until(EC.element_to_be_clickable(self.locators.TRANSLATE_CONTENT_BUTTON))
            self.driver.execute_script("arguments[0].click();", translate_button)
            logging.info("Đã nhấn nút Dịch nội dung trong tab English.")
            return True
        except TimeoutException as e:
            logging.error(f"Lỗi khi nhấn nút Dịch nội dung: {e}", exc_info=True)
            return False
    
    # Hàm nhấn vào tab Thông tin chung
    def click_tab_general_info(self):
        try:
            tab = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locators.GENERAL_INFO_TAB))
            self.driver.execute_script("arguments[0].scrollIntoView();", tab)
            tab.click()
            print("Đã click vào tab 'Thông tin chung'.")
        except Exception as e:
            print(f"Lỗi khi click vào tab 'Thông tin chung': {e}")
    
    # Hàm kiểm tra Tiêu đề bài viết bên ngoài trang Danh sách bài viết 
    def is_article_title_in_list(self, expected_title):
        try:
            article_xpath = f"//td[contains(@class, 'article-title') and contains(text(), '{expected_title}')]"
            self.wait.until(EC.presence_of_element_located((By.XPATH, article_xpath)))
            logging.info(f"Tiêu đề bài viết '{expected_title}' xuất hiện trong danh sách.")
            return True
        except TimeoutException:
            logging.error(f"Tiêu đề bài viết '{expected_title}' không xuất hiện trong danh sách.")
            return False

    # Hàm chờ đợi Tiêu đề bài viết xuất hiện ngoài trang Danh sách
    def wait_for_article_to_appear_in_list(self, article_title):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//div[@class='article-list']//h3[text()='{article_title}']")))
            logging.info(f"Bài viết '{article_title}' đã xuất hiện trong danh sách.")
        except TimeoutException:
            logging.error(f"Bài viết '{article_title}' không xuất hiện trong danh sách sau khi chờ.")
            return False
        return True
    
    def verify_article_edit_page(self, expected_title):
        try:
            WebDriverWait(self.driver, 10).until(EC.url_contains("/cms/article/edit/"))
            current_url = self.driver.current_url
            logging.info(f"Trang chuyển hướng đến: {current_url}")
            assert "/cms/article/edit/" in current_url, "Không ở lại trang chỉnh sửa sau khi nhấn 'Lưu và tiếp tục chỉnh sửa'"
            saved_title = self.get_title()
            assert saved_title == expected_title, f"Tiêu đề bài viết bị thay đổi: {saved_title}"
            logging.info("Test Case PASS: Hệ thống giữ nguyên trang chỉnh sửa sau khi lưu.")
            return True
        except Exception as e:
            logging.error(f"Test Case FAIL: Không giữ nguyên trang chỉnh sửa - {e}")
            return False
    
    # Hàm nhấn vào nút Lưu
    def click_save_button(self):
        try:
            save_button = self.wait.until(EC.element_to_be_clickable(self.locators.SAVE_BUTTON))
            self.driver.execute_script("arguments[0].click();", save_button)
            logging.info("Đã nhấn nút Lưu.")
            return True
        except Exception as e:
            logging.error(f"Lỗi khi nhấn nút Lưu: {e}", exc_info=True)
            return False
    
    # Hàm nhấn vào nút Lưu và tiếp tục cập nhật
    def click_save_and_continue_button(self):
        try:
            save_and_continue_button = self.wait.until(EC.element_to_be_clickable(self.locators.SAVE_AND_CONTINUE_BUTTON))
            self.driver.execute_script("arguments[0].click();", save_and_continue_button)
            logging.info("Đã nhấn nút Lưu.")
            return True
        except Exception as e:
            logging.error(f"Lỗi khi nhấn nút Lưu: {e}", exc_info=True)
            return False

    # Hàm thực hiện thao tác nhấn menu Nội dung -> menu Bài viết
    def navigate_to_article(self):
        self.click_content_menu()
        self.click_article_menu()

    # Hàm thực hiện thao tác nhấn menu Nội dung 
    def perform_tag_operations(self):
        self.navigate_to_article()
        self.click_all_article_menu()
    

