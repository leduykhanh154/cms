import re
import time
import logging
import unicodedata
from datetime import datetime
from selenium.webdriver.common.by import By
from locators.locator_article import LocatorArticle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Article:
    def __init__(self, driver, timeout=5):
        if not driver:
            raise ValueError("Driver không được để trống hoặc None!")
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.locators = LocatorArticle  

    def click_menu(self, locator, menu_name):
        try:
            menu = self.wait.until(EC.element_to_be_clickable(locator))
            menu.click()
            logging.info(f"Đã nhấn menu {menu_name}.")
            return self
        except TimeoutException as e:
            logging.error(f"Không thể nhấn menu {menu_name}: {e}", exc_info=True)
            raise

    def click_content_menu(self):
        return self.click_menu(self.locators.CONTENT_MENU, "Nội dung")

    def click_article_menu(self):
        return self.click_menu(self.locators.ARTICLE_MENU, "Bài viết")

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
    
    def is_error_message_displayed(self, locator, message):
        try:
            error_element = self.wait.until(EC.visibility_of_element_located(locator))
            logging.info(f"Lỗi '{message}' hiển thị.")
            return True
        except TimeoutException:
            logging.info(f"Lỗi '{message}' không hiển thị.")
            return False
     
    def enter_title(self, title):
        title_input = self.wait.until(EC.visibility_of_element_located(self.locators.TITLE_INPUT))
        title_input.clear()
        title_input.send_keys(title)
        logging.info(f"Đã nhập tiêu đề: {title}")

    def is_title_error_displayed(self):
        return self.is_error_message_displayed(self.locators.TITLE_ERROR_MESSAGE, "Vui lòng nhập Tiêu đề")

    def is_title_max_length_error_displayed(self):
        return self.is_error_message_displayed(self.locators.TITLE_MAX_LENGTH_ERROR_LOCATOR, "Tiêu đề không quá 250 ký tự")

    def ordering(self, ordering):
        ordering_input = self.wait.until(EC.visibility_of_element_located(self.locators.ORDERING))
        ordering_input.clear()
        ordering_input.send_keys(ordering)
        logging.info(f"Đã nhập tiêu đề: {ordering}")

    def get_text(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.text.strip()
        except TimeoutException:
            logging.error(f"Lỗi: Không tìm thấy phần tử {locator}")
            return None

    def is_ordering_error_displayed(self):
        error_message = self.get_text(self.locators.ORDERING_MAX_LENGHT_ERROR_MESSAGE)
        expected_message = "Vui lòng nhập không quá 7 số"
        if error_message == expected_message:
            logging.info("Thông báo lỗi hiển thị đúng.")
            return True
        elif error_message == "global.validation.maxlength":
            logging.error("Lỗi: Hệ thống hiển thị key thay vì nội dung dịch.")
        else:
            logging.error(f"Lỗi: Thông báo không đúng, nhận được: {error_message}")
        return False

    def is_ordering_error_displayed(self):
        error_message = self.get_text(self.locators.ORDERING_ERROR_MESSAGE)
        expected_message = "Vui lòng nhập Thứ tự sắp xếp"
        if error_message == expected_message:
            logging.info("Thông báo lỗi hiển thị đúng.")
            return True
        elif error_message == "global.validation.required":
            logging.error("Lỗi: Hệ thống hiển thị key thay vì nội dung dịch.")
        else:
            logging.error(f"Lỗi: Thông báo không đúng, nhận được: {error_message}")
        return False

    def is_ordering_max_lenght_error_displayed(self):
        error_message = self.get_text(self.locators.ORDERING_ERROR_MESSAGE)
        expected_message = "Vui lòng nhập Thứ tự sắp xếp"
        if error_message == expected_message:
            logging.info("Thông báo lỗi hiển thị đúng.")
            return True
        elif error_message == "global.validation.required":
            logging.error("Lỗi: Hệ thống hiển thị key thay vì nội dung dịch.")
        else:
            logging.error(f"Lỗi: Thông báo không đúng, nhận được: {error_message}")
        return False
    
    def is_ordering_max_lenght_error_displayed(self):
        return self.is_error_message_displayed(self.locators.ORDERING_ERROR_MESSAGE, "Vui lòng nhập không quá 7 số")
    
    def enter_content(self, content):
        try:
            self.wait.until(lambda driver: driver.execute_script("return CKEDITOR.instances['languages[vi][content]'] !== undefined"))
            ckeditor_content = self.driver.execute_script("return CKEDITOR.instances['languages[vi][content]'].getData();")
            logging.info(f"Nội dung trong CKEditor trước khi setData: {ckeditor_content}")
            self.driver.execute_script("""CKEDITOR.instances['languages[vi][content]'].setData(arguments[0]);""", content)
            self.driver.execute_script("CKEDITOR.instances['languages[vi][content]'].updateElement();")
            self.driver.execute_script("""let textarea = document.getElementById('languages[vi][content]');textarea.dispatchEvent(new Event('input', { bubbles: true }));textarea.dispatchEvent(new Event('change', { bubbles: true }));""")
            form_validation = self.driver.execute_script("""let form = $('textarea[name="languages[vi][content]"]').closest('form');return form.length > 0 && form.data('formValidation') !== undefined;""")
            if form_validation:
                self.driver.execute_script("""
                    let form = $('textarea[name="languages[vi][content]"]').closest('form');
                    form.data('formValidation').revalidateField('languages[vi][content]');
                """)
                logging.info("Nhập nội dung vào CKEditor và tái xác thực trường 'content' thành công.")
            else:
                logging.warning("Form chưa được khởi tạo validation hoặc không tìm thấy form.")
        except Exception as e:
            logging.error(f"Lỗi khi nhập nội dung vào CKEditor: {e}")
            raise

    def is_content_error_displayed(self):
        return self.is_error_message_displayed(self.locators.CONTENT_ERROR_MESSAGE, "Vui lòng nhập Nội dung")

    def click_tab_general_info(self):
        try:
            tab = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "MainTab"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", tab)
            tab.click()
            print("Đã click vào tab 'Thông tin chung'.")
        except Exception as e:
            print(f"Lỗi khi click vào tab 'Thông tin chung': {e}")
    
    def is_article_type_error_displayed(self):
        return self.is_error_message_displayed(self.locators.ARTICLE_TYPE_ERROR_MESSAGE, "Vui lòng nhập Loại bài viết")

    def click_select(self):
        select_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locators.DROPDOWN_ARTICLE_TYPE))
        select_element.click()

    def is_dropdown_visible(self):
        try:
            dropdown_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.locators.DROPDOWN_ARTICLE_TYPE)
            )
            return dropdown_element.is_displayed()
        except TimeoutException:
            return False

    def select_article_type(self, article_type):
        article_type_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(), '{article_type}')]")))
        article_type_element.click()

    def is_selected_article_type_displayed(self, expected_article_type):
        selected_article_type = self.driver.find_element(self.locators.DROPDOWN_ARTICLE_TYPE_DISPLAY[0], self.locators.DROPDOWN_ARTICLE_TYPE_DISPLAY[1]).text.strip()
        return selected_article_type == expected_article_type
        
    def is_article_title_in_list(self, expected_title):
        try:
            article_xpath = f"//td[contains(@class, 'article-title') and contains(text(), '{expected_title}')]"
            self.wait.until(EC.presence_of_element_located((By.XPATH, article_xpath)))
            logging.info(f"Tiêu đề bài viết '{expected_title}' xuất hiện trong danh sách.")
            return True
        except TimeoutException:
            logging.error(f"Tiêu đề bài viết '{expected_title}' không xuất hiện trong danh sách.")
            return False

    def wait_for_article_to_appear_in_list(self, article_title):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//div[@class='article-list']//h3[text()='{article_title}']")))
            logging.info(f"Bài viết '{article_title}' đã xuất hiện trong danh sách.")
        except TimeoutException:
            logging.error(f"Bài viết '{article_title}' không xuất hiện trong danh sách sau khi chờ.")
            return False
        return True

    def get_title(self):
        try:
            title_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="save-article"]/div[1]/div[1]/h1'))
            )
            return title_element.text.replace("Sửa bài viết: ", "").strip()
        except Exception as e:
            logging.error(f"Lỗi khi lấy tiêu đề bài viết: {e}")
            return None

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
    
    def click_save_button(self):
        try:
            save_button = self.wait.until(EC.element_to_be_clickable(self.locators.SAVE_BUTTON))
            self.driver.execute_script("arguments[0].click();", save_button)
            logging.info("Đã nhấn nút Lưu.")
            return True
        except Exception as e:
            logging.error(f"Lỗi khi nhấn nút Lưu: {e}", exc_info=True)
            return False
    
    def click_save_and_continue_button(self):
        try:
            save_and_continue_button = self.wait.until(EC.element_to_be_clickable(self.locators.SAVE_AND_CONTINUE_BUTTON))
            self.driver.execute_script("arguments[0].click();", save_and_continue_button)
            logging.info("Đã nhấn nút Lưu.")
            return True
        except Exception as e:
            logging.error(f"Lỗi khi nhấn nút Lưu: {e}", exc_info=True)
            return False

    def click_status_dropdown(self):
        try:
            dropdown = self.wait.until(EC.element_to_be_clickable(LocatorArticle.DROPDOWN_STATUS))
            dropdown.click()
            logging.info("Đã mở dropdown 'Trạng thái'.")
        except TimeoutException:
            logging.error("Không thể mở dropdown 'Trạng thái'.")
            raise

    def is_status_dropdown_visible(self):
        try:
            dropdown = self.wait.until(EC.visibility_of_element_located(LocatorArticle.DROPDOWN_STATUS))
            return dropdown.is_displayed()
        except TimeoutException:
            return False
        
    def select_status(self, status_name):
        try:
            option_locator = (By.XPATH, f"//li[contains(@class, 'select2-results__option') and text()='{status_name}']")
            option = self.wait.until(EC.element_to_be_clickable(option_locator))
            option.click()
            logging.info(f"Đã chọn trạng thái: {status_name}")
        except TimeoutException:
            logging.error(f"Không thể chọn trạng thái: {status_name}")
            raise

    def is_selected_status_correct(self, expected_status):
        try:
            selected_text = self.wait.until(EC.visibility_of_element_located(LocatorArticle.DROPDOWN_STATUS_SELECTED)).text.strip()
            return selected_text == expected_status
        except TimeoutException:
            logging.error("Không thể lấy giá trị 'Trạng thái' đã chọn.")
            return False
        
    def is_status_selected(self, expected_status):
        selected_status = self.driver.find_element(self.locators.DROPDOWN_STATUS_SELECTED[0], self.locators.DROPDOWN_STATUS_SELECTED[1]).text.strip()
        return selected_status == expected_status

    def is_ordering_specific_error_displayed(self, expected_message):
        error_message = self.get_text(self.locators.ORDERING_ERROR_MESSAGE)
        if error_message is None:
            logging.error("Không có thông báo lỗi hiển thị!")
            return False
        if error_message == expected_message:
            logging.info(f"Thông báo lỗi hiển thị đúng: {expected_message}")
            return True
        else:
            logging.error(f"Lỗi: Thông báo không đúng, nhận được: {error_message}, mong đợi: {expected_message}")
        return False

    def enter_public_date(self, date_value):
        date_input = self.wait.until(EC.visibility_of_element_located(self.locators.PUBLIC_DATE))
        date_input.clear()
        date_input.send_keys(date_value)
        logging.info(f"Đã nhập Ngày đăng: {date_value}")

    def get_public_date(self):
        date_input = self.wait.until(EC.visibility_of_element_located(self.locators.PUBLIC_DATE))
        return date_input.get_attribute("value")
    
    def set_public_date(self, date_value):
        public_date_field = self.wait.until(EC.visibility_of_element_located(self.locators.PUBLIC_DATE))
        public_date_field.clear() 
        public_date_field.send_keys(date_value)
    

    def click_switch(self, switch_label_locator):
        switch_label = self.wait.until(EC.element_to_be_clickable(switch_label_locator))
        switch_label.click()

    def is_switch_on(self, switch_locator):
        switch = self.wait.until(EC.presence_of_element_located(switch_locator))
        return switch.get_attribute("checked") is not None  # Kiểm tra xem có thuộc tính 'checked' không

    def reset_switch(self, switch_locator, switch_label_locator):
        if self.is_switch_on(switch_locator):
            self.click_switch(switch_label_locator) 
    
    def click_upload_button(self):
        upload_field = self.wait.until(EC.element_to_be_clickable(LocatorArticle.UPLOAD_BUTTON))
        upload_field.click()
        
    def click_upload_thumbnail_image_field(self):
        upload_field = self.wait.until(EC.element_to_be_clickable(LocatorArticle.UPLOAD_THUMBNAIL_IMAGE_FIELD))
        upload_field.click()

    def click_upload_feature_image_field(self):
        upload_field = self.wait.until(EC.element_to_be_clickable(LocatorArticle.UPLOAD_FEATURE_IMAGE_FIELD))
        self.driver.execute_script("window.scrollTo({top: arguments[0].getBoundingClientRect().top + window.scrollY - 100, behavior: 'smooth'});", upload_field)
        WebDriverWait(self.driver, 2).until(EC.visibility_of(upload_field))
        ActionChains(self.driver).move_to_element(upload_field).click().perform()

    def is_upload_popup_displayed(self):
        return self.wait.until(EC.visibility_of_element_located(LocatorArticle.UPLOAD_IMAGE_POPUP)) is not None

    def click_tab_browser_by_href(self):
        try:
            tab_browser = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='#browse-content']"))
            )
            tab_browser.click()
            print("Click tab Browse thành công (Cách 2 - Click bằng href).")
        except Exception as e:
            print(f"Không thể click vào tab Browse bằng href: {e}")

    def wait_for_file_listing(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.locators.FILE_LISTING)
            )
            print("Danh sách file hình ảnh đã xuất hiện.")
        except Exception as e:
            print(f"Không tìm thấy danh sách file hình ảnh: {e}")

    def select_first_image(self):
        try:
            images = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(self.locators.FILE_LISTING)
            )
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
                    self.driver.execute_script("arguments[0].click();", first_image)  # Click bằng JS
                    print("Đã chọn ảnh đầu tiên (Click JS).")
            else:
                print("Không tìm thấy ảnh nào trong danh sách.")

        except Exception as e:
            print(f"Lỗi khi click vào ảnh đầu tiên: {e}")

    def click_choose_upload_button(self):
        try:
            upload_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.locators.CHOOSE_UPLOAD_BUTTON)
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", upload_button)
            time.sleep(1)
            self.driver.execute_script("arguments[0].click();", upload_button)
            print("Đã click vào nút 'Upload' (Cách 2 - JS).")
        except Exception as e:
            print(f"Không thể click vào nút 'Upload': {e}")

    def is_feature_image_uploaded(self):
        try:
            uploaded_image = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='article-image-id_upload']/div/div[1]/a"))
            )
            return uploaded_image.is_displayed()
        except:
            return False

    def is_thumbnail_image_uploaded(self):
        try:
            uploaded_image = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='article-image-id_upload']/div/div[1]/a"))
            )
            return uploaded_image.is_displayed()
        except:
            return False

    def delete_thumbnail_image(self):
        """Xóa ảnh Thumbnail của bài viết."""
        try:
            # Chờ ảnh xuất hiện trước khi xóa
            self.wait.until(EC.presence_of_element_located(LocatorArticle.DELETE_THUMBNAIL_IMAGE))

            # Cuộn xuống phần tử và đợi nó hiển thị
            delete_button = self.wait.until(EC.element_to_be_clickable(LocatorArticle.DELETE_THUMBNAIL_IMAGE))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", delete_button)
            time.sleep(2)  # Đợi hiệu ứng scroll hoàn tất
            
            # Thử click trực tiếp, nếu lỗi thì dùng JS
            try:
                delete_button.click()
            except:
                self.driver.execute_script("arguments[0].click();", delete_button)

            print("✔ Đã xóa ảnh Thumbnail.")
        except Exception as e:
            print(f"❌ Lỗi khi xóa ảnh Thumbnail: {e}")

    def is_thumbnail_image_deleted(self):
        """Kiểm tra xem ảnh Thumbnail đã bị xóa chưa."""
        try:
            self.wait.until(EC.invisibility_of_element_located(LocatorArticle.DELETE_THUMBNAIL_IMAGE))
            return True
        except:
            return False

    def delete_feature_image(self):
        """Xóa ảnh Feature của bài viết."""
        try:
            # Chờ ảnh xuất hiện trước khi xóa
            self.wait.until(EC.presence_of_element_located(LocatorArticle.DELETE_FEATURE_IMAGE))

            # Cuộn xuống phần tử trước khi thao tác
            delete_button = self.wait.until(EC.element_to_be_clickable(LocatorArticle.DELETE_FEATURE_IMAGE))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", delete_button)
            time.sleep(2)  # Đợi hiệu ứng scroll hoàn tất
            
            # Thử click trực tiếp, nếu lỗi thì dùng JS
            try:
                delete_button.click()
            except:
                self.driver.execute_script("arguments[0].click();", delete_button)

            print("✔ Đã xóa ảnh Feature.")
        except Exception as e:
            print(f"❌ Lỗi khi xóa ảnh Feature: {e}")

    def is_feature_image_deleted(self):
        """Kiểm tra xem ảnh Feature đã bị xóa chưa."""
        try:
            self.wait.until(EC.invisibility_of_element_located(LocatorArticle.DELETE_FEATURE_IMAGE))
            return True
        except:
            return False


    def click_tag_dropdown(self):
        try:
            dropdown = self.wait.until(EC.element_to_be_clickable(LocatorArticle.DROPDOWN_SELECT_TAG))
            dropdown.click()
            logging.info("Đã mở dropdown 'Tag'.")
        except TimeoutException:
            logging.error("Không thể mở dropdown 'Tag'.")
            raise

    def select_tag(self, tag_name):
        try:
            option_locator = (By.XPATH, f"//li[contains(@class, 'select2-results__option') and contains(text(), '{tag_name}')]")
            self.wait.until(EC.presence_of_element_located(option_locator))
            tags = self.driver.find_elements(By.XPATH, "//li[contains(@class, 'select2-results__option')]")
            logging.info(f"Danh sách tag tìm thấy: {[tag.text for tag in tags]}")
            option = self.wait.until(EC.element_to_be_clickable(option_locator))
            option.click()
            logging.info(f"Đã chọn tag: {tag_name}")
        except TimeoutException:
            logging.error(f"Không tìm thấy tag: {tag_name}. Kiểm tra lại tên hoặc dropdown.")
            raise

    def is_selected_tag_correct(self, expected_tag):
        try:
            selected_tag_element = self.wait.until(
                EC.presence_of_element_located(LocatorArticle.SELECTED_TAG_FIELD)
            )
            selected_tag_text = selected_tag_element.text.strip()
            logging.info(f"Tag hiển thị sau khi chọn: '{selected_tag_text}'")

            return selected_tag_text == expected_tag
        except TimeoutException:
            logging.error("Không thể lấy giá trị 'Tag' đã chọn.")
            return False
    
    def click_create_keyword_button(self):
        self.wait.until(EC.element_to_be_clickable(LocatorArticle.CREATE_KEYWORD_BUTTON)).click()

    def is_add_keyword_sidebar_visible(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(LocatorArticle.ADD_KEYWORD_SIDEBAR))
        except:
            return False

    def scroll_to_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        time.sleep(0.5)
        return element

    def click_related_article_dropdown(self):
        try:
            dropdown = self.wait.until(EC.element_to_be_clickable(LocatorArticle.RELATED_ARTICLE_DROPDOWN))
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", dropdown)
            time.sleep(0.5)
            dropdown.click()
            logging.info("Đã mở dropdown 'Bài viết liên quan'.")
        except TimeoutException:
            logging.error("Không thể mở dropdown 'Bài viết liên quan'.")
            raise

    def select_related_article(self, article_name):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'select2-results__option')]")))
            articles = self.driver.find_elements(By.XPATH, "//li[contains(@class, 'select2-results__option')]")
            logging.info(f"Danh sách bài viết trong dropdown: {[article.text for article in articles]}")
            for article in articles:
                if article_name.strip() in article.text.strip():
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", article)
                    time.sleep(1)
                    article.click()
                    logging.info(f"Đã chọn bài viết: {article_name}")
                    return
            logging.error(f"Không tìm thấy bài viết: {article_name}. Kiểm tra lại tên hoặc dropdown.")
            raise TimeoutException(f"Không tìm thấy bài viết: {article_name}")
        except TimeoutException:
            logging.error(f"Timeout khi tìm bài viết: {article_name}")
            raise

    def is_selected_related_article_correct(self, expected_article):
        try:
            selected_article_element = self.wait.until(
                EC.presence_of_element_located(LocatorArticle.SELECTED_RELATED_ARTICLE_FIELD)
            )
            selected_article_text = selected_article_element.text.strip()
            logging.info(f"Bài viết hiển thị sau khi chọn: '{selected_article_text}'")
            logging.info(f"Expected: '{expected_article}'")
            return selected_article_text.strip() == expected_article.strip()
        except TimeoutException:
            logging.error("Không thể lấy giá trị bài viết đã chọn.")
            return False

    def is_related_article_dropdown_visible(self):
        try:
            dropdown_element = self.wait.until(
                EC.visibility_of_element_located(LocatorArticle.RELATED_ARTICLE_DROPDOWN)
            )
            logging.info("Dropdown 'Bài viết liên quan' đã mở.")
            return True
        except TimeoutException:
            logging.error("Dropdown 'Bài viết liên quan' không hiển thị!")
            return False

    def print_related_articles_list(self):
        try:
            articles = self.driver.find_elements(By.XPATH, "//li[contains(@class, 'select2-results__option')]")
            logging.info(f"Danh sách bài viết trong dropdown: {[article.text for article in articles]}")
        except Exception as e:
            logging.error(f"Lỗi khi lấy danh sách bài viết: {str(e)}")

    def get_selected_related_article(self):
        try:
            selected_article_element = self.wait.until(
                EC.presence_of_element_located(LocatorArticle.SELECTED_RELATED_ARTICLE_FIELD)
            )
            selected_article_text = selected_article_element.text.strip()

            logging.info(f"Giá trị bài viết hiển thị: '{selected_article_text}'")
            return selected_article_text
        except TimeoutException:
            logging.error("Không thể lấy giá trị bài viết đã chọn.")
            return ""
    
    def wait_for_selected_related_article_to_update(self, expected_text, timeout=5):
        try:
            self.wait.until(lambda driver: self.get_selected_related_article() == expected_text, f"Không tìm thấy bài viết mong đợi: {expected_text}")
            logging.info("Bài viết đã chọn hiển thị đúng.")
        except TimeoutException:
            logging.error(f"Bài viết đã chọn không cập nhật đúng. Expected: '{expected_text}'")

    def enter_url_key(self, url_key):
        url_input = self.driver.find_element(*LocatorArticle.URL_KEY_INPUT)
        url_input.clear()
        url_input.send_keys(url_key)

    def get_url_key_value(self):
        try:
            url_input = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='languages[vi][url_key]']"))
            )
            return url_input.get_attribute("value")
        except TimeoutException:
            logging.error("Không tìm thấy trường URL Key sau 5 giây.")
            return None  

    def check_url_key_generated(self):
        title_input = self.driver.find_element(*LocatorArticle.TITLE_INPUT).get_attribute("value")
        url_input = self.get_url_key_value()
        expected_url_key = self.generate_expected_url_key(title_input)
        return expected_url_key in url_input

    def generate_expected_url_key(self, title):
        title = title.strip().lower()
        title = title.replace("đ", "d").replace("Đ", "d")
        title = unicodedata.normalize("NFKD", title)
        title = "".join([c for c in title if not unicodedata.combining(c)])
        title = re.sub(r"\s+", "-", title)  # Thay khoảng trắng thành dấu "-"
        title = re.sub(r"[^a-z0-9-]", "", title)  # Xóa ký tự đặc biệt
        title = re.sub(r"-+", "-", title)  # Hợp nhất các dấu "-"
        return title


    def perform_tag_operations(self):
        self.click_content_menu()
        self.click_article_menu()
        self.click_all_article_menu()

    