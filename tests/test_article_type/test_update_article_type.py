import time
import pytest
import logging
import datetime
from utils.login import Login
from utils.logger import LoggerConfig
from utils.driver_setup import get_driver
from pages.article_type.update_article_type.update_article_type_base import UpdateArticleTypeBase
from pages.article_type.update_article_type.is_displayed_update_article_type import IsDisplayedUpdateArticleType
from pages.article_type.update_article_type.get_field_update_article_type import GetFieldUpdateArticleType
from pages.article_type.update_article_type.enter_field_update_article_type import EnterFieldUpdateArticleType
from pages.article_type.update_article_type.meta_image_update_article_type import MetaImageUpdateArticleType
from pages.article_type.update_article_type.validation_article_type import ValidationArticleType
from pages.article_type.update_article_type.delete_last_char_update_article_type import DeleteLastCharUpdateArticleType
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

# Khởi tạo logger
test_logger = LoggerConfig.get_logger()

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    global test_logger
    test_logger = LoggerConfig.get_logger()

@pytest.fixture(scope="function")
def setup_driver():
    driver = get_driver()
    try:
        login_page = Login(driver)
        if not login_page.login():
            pytest.fail("Không thể đăng nhập!")
        yield driver
    finally:
        time.sleep(3)
        driver.quit()

@pytest.fixture
def update_article_type(setup_driver):
    return UpdateArticleTypeBase(setup_driver)

@pytest.fixture
def is_displayed_update_article_type(setup_driver):
    return IsDisplayedUpdateArticleType(setup_driver)

@pytest.fixture
def enter_field_update_article_type(setup_driver):
    return EnterFieldUpdateArticleType(setup_driver)

@pytest.fixture
def get_field_update_article_type(setup_driver):
    return GetFieldUpdateArticleType(setup_driver)

@pytest.fixture
def meta_image_update_article_type(setup_driver):
    return MetaImageUpdateArticleType(setup_driver)

@pytest.fixture
def validation_update_article_type(setup_driver):
    return ValidationArticleType(setup_driver)

@pytest.fixture
def delete_last_char_update_article_type(setup_driver):
    return DeleteLastCharUpdateArticleType(setup_driver)

# Test Case 1: Click 'Trang chủ' trên breadcrumb -> Chuyển hướng về trang chủ.
def test_click_breadcrumb_home(update_article_type):
    test_logger.info("Bắt đầu Test Case 1: Verify khi nhấn vào breadcrumb 'Trang chủ' -> Hệ thống điều hướng về trang chủ thành công.")
    update_article_type.perform_tag_operations()
    update_article_type.click_first_link()
    time.sleep(1)
    result = update_article_type.click_breadcrumb_home()
    expected_result = "Hệ thống điều hướng thành công đến trang 'Trang chủ'."
    actual_result = expected_result if result else "Hệ thống không điều hướng đến trang 'Trang chủ'."
    if result:
        test_logger.info(f"Test Case 1 PASS: test_click_breadcrumb_home | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 1 FAIL: test_click_breadcrumb_home | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 2: Click 'Danh sach loai bai viet' trên breadcrumb -> Chuyển hướng về trang Danh sach loai bai viet.
def test_click_breadcrumb_type_list(update_article_type):
    test_logger.info("Bắt đầu Test Case 2: Verify có thể nhấn vào 'Danh sách loại bài viết' trên breadcrumb và kiểm tra điều hướng.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    result = update_article_type.click_breadcrumb_type_list()
    assert result, "Không thể nhấn vào breadcrumb 'Danh sách loại bài viết'."
    test_logger.info("Đã nhấn vào breadcrumb 'Danh sách loại bài viết'.")
    expected_url = "https://mpire-cms-demo.mpire.asia/cms/category"
    actual_url_correct = update_article_type.verify_current_url(expected_url)
    expected_result = "Hệ thống điều hướng đúng đến trang 'Danh sách loại bài viết'."
    actual_result = expected_result if actual_url_correct else "Hệ thống không điều hướng đúng trang."
    if actual_url_correct:
        test_logger.info(f"Test Case 2 PASS: test_click_breadcrumb_type_list | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 2 FAIL: test_click_breadcrumb_type_list | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
 
# Test case 3: Click tab Thong tin chung    
def test_click_tab_general_information_and_check_label(update_article_type, is_displayed_update_article_type):
    test_logger.info("Bắt đầu Test Case 3: Nhấn vào tab 'Thông tin chung'.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    result = update_article_type.click_tab_general_information()
    assert result, "Không thể nhấn vào tab 'Thông tin chung'."
    test_logger.info("Đã nhấn vào tab 'Thông tin chung'.")
    label_correct = is_displayed_update_article_type.is_label_status_displayed()
    expected_result = "Tab 'Thong tin chung' duoc hien thi"
    actual_result = expected_result if label_correct else "Tab 'Thong tin chung' không hiển thị."
    if label_correct:
        test_logger.info(f"Test Case 3 PASS: test_click_tab_general_information_and_check_label | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 3 FAIL: test_click_tab_general_information_and_check_label | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test case 4: Click tab Noi dung chinh 
def test_click_tabs_and_check_labels(update_article_type, is_displayed_update_article_type):
    test_logger.info("Bắt đầu Test Case 4: Kiểm tra tab 'Thông tin chung' & 'Nội dung chính'.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    result_tab_info = update_article_type.click_tab_general_information()
    assert result_tab_info, "Không thể nhấn vào tab 'Thông tin chung'."
    test_logger.info("Đã nhấn vào tab 'Thông tin chung'.")
    label_status_correct = is_displayed_update_article_type.is_label_status_displayed()
    assert label_status_correct, "Tab 'Thông tin chung' không đúng hoặc không xuất hiện!"
    test_logger.info("Tab 'Thông tin chung' hiển thị đúng.")
    result_tab_main = update_article_type.click_tab_main_content()
    assert result_tab_main, "Không thể nhấn vào tab 'Nội dung chính'."
    test_logger.info("Đã nhấn vào tab 'Nội dung chính'.")
    label_article_correct = is_displayed_update_article_type.is_label_article_type_correct()
    assert label_article_correct, "Tab 'Nội dung chính' không đúng hoặc không xuất hiện!"
    test_logger.info("Tab 'Nội dung chính' hiển thị đúng.")
    expected_result = "Tab 'Thông tin chung' và 'Nội dung chính' hoạt động đúng."
    actual_result = expected_result if (label_status_correct and label_article_correct) else "Một trong các bước kiểm tra không đạt yêu cầu."
    if label_status_correct and label_article_correct:
        test_logger.info(f"Test Case 4 PASS: test_click_tabs_and_check_labels | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 4 FAIL: test_click_tabs_and_check_labels | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 5: Click tab 'English'
def test_click_tab_english(update_article_type, is_displayed_update_article_type):
    test_logger.info("Bắt đầu Test Case 5: Kiểm tra tab 'English'.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Tạo mới'.")
    result_tab_english = update_article_type.click_tab_english()
    assert result_tab_english, "Không thể nhấn vào tab 'English'."
    test_logger.info("Đã nhấn vào tab 'English'.")
    expected_result = "Tab 'English' hoạt động."
    actual_result = expected_result if result_tab_english else "Tab 'English' không hoạt động."
    if result_tab_english:
        test_logger.info(f"Test Case 5 PASS: test_click_tab_english | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 5 FAIL: test_click_tab_english | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 6: Click tab 'Tieng Viet'
def test_click_tabs_english_vietnamese_and_check_labels(update_article_type, is_displayed_update_article_type):
    test_logger.info("Bắt đầu Test Case 6: Kiểm tra tab 'Tiếng Việt'.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    result_tab_english = update_article_type.click_tab_english()
    assert result_tab_english, "Không thể nhấn vào tab 'Tiếng Anh'."
    test_logger.info("Đã nhấn vào tab 'Tiếng Anh'.")
    result_tab_vietnamese = update_article_type.click_tab_tieng_viet()
    assert result_tab_vietnamese, "Không thể nhấn vào tab 'Tiếng Việt'."
    test_logger.info("Đã nhấn vào tab 'Tiếng Việt'.")
    label_article_correct = is_displayed_update_article_type.is_label_article_type_correct()
    assert label_article_correct, "Tab 'Tiếng Việt' không hiển thị đúng!"
    test_logger.info("Tab 'Tiếng Việt' hiển thị đúng.")
    expected_result = "Tab 'Tiếng Việt' hoạt động đúng."
    actual_result = expected_result if (result_tab_english and label_article_correct) else "Một trong các bước kiểm tra không đạt yêu cầu."
    if result_tab_english and label_article_correct:
        test_logger.info(f"Test Case 6 PASS: test_click_tabs_english_vietnamese_and_check_labels | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 6 FAIL: test_click_tabs_english_vietnamese_and_check_labels | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# Test Case 7: Click nut 'Huy'
def test_click_button_cancel_and_check_url(update_article_type):
    test_logger.info("Bắt đầu Test Case 7: Click nut 'Huy' va kiem tra duong dan.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    result_button_cancel = update_article_type.click_cancel_button()
    assert result_button_cancel, "Không thể nhấn vào nut 'Huy'."
    expected_url = "https://mpire-cms-demo.mpire.asia/cms/category"
    actual_url_correct = update_article_type.verify_current_url(expected_url)
    expected_result = "Hệ thống huy thay doi va điều hướng đúng đến trang 'Danh sách loại bài viết'."
    actual_result = expected_result if actual_url_correct else "Hệ thống không huy thay doi va điều hướng đúng trang."
    if actual_url_correct:
        test_logger.info(f"Test Case 7 PASS: test_click_button_cancel_and_check_url | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 7 FAIL: test_click_button_cancel_and_check_url | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# Test Case 8: Nhập loại bài viết, click nút 'Lưu' và kiểm tra đường dẫn và có hiển thị loại bài viết
def test_save_and_check_article_type(update_article_type, enter_field_update_article_type, is_displayed_update_article_type):
    test_logger.info("Bắt đầu Test Case 8: Nhập loại bài viết, click nút 'Lưu' và kiểm tra đường dẫn có hiển thị loại bài viết vừa tạo.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    expected_text = "Bài viết thử nghiệm"
    enter_field_update_article_type.enter_vi_article_type(expected_text)
    time.sleep(1)
    test_logger.info(f"Đã nhập loại bài viết: {expected_text}.")
    update_article_type.click_save_button()
    time.sleep(1)
    test_logger.info("Đã nhấn nút 'Lưu'.")
    time.sleep(2)
    expected_url = "https://mpire-cms-demo.mpire.asia/cms/category?page=1" 
    if not update_article_type.verify_current_url(expected_url):
        test_logger.error(f"Test Case 8 FAIL: test_save_and_check_article_type | Expected: {expected_url} | Actual: {update_article_type.driver.current_url} | Status: FAIL")
        assert False, f"Test Case 8 FAIL: test_save_and_check_article_type | Expected: {expected_url} | Actual: {update_article_type.driver.current_url} | Status: FAIL"
    is_text_displayed = is_displayed_update_article_type.is_text_present_on_page(expected_text)
    expected_result = f"Chuyển hướng về trang danh sách và hiển thị đúng loại bài viết: '{expected_text}'."
    actual_result = expected_result if is_text_displayed else f"Loại bài viết '{expected_text}' không được hiển thị trong danh sách."
    if is_text_displayed:
        test_logger.info(f"Test Case 8 PASS: test_save_and_check_article_type | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 8 FAIL: test_save_and_check_article_type | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 9: Cập nhật Loại bài viết ( Tab Tiếng Việt )
def test_save_and_continue_check_edit(update_article_type, enter_field_update_article_type, is_displayed_update_article_type):
    test_logger.info("Bắt đầu Test Case 9: Cập nhật Loại bài viết tab Tiếng Việt -> Lưu và kiểm tra sau khi lưu.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    expected_text = "Bài viết thử nghiệm"
    enter_field_update_article_type.enter_vi_article_type(expected_text)
    time.sleep(1)
    test_logger.info(f"Đã nhập loại bài viết: {expected_text}.")
    update_article_type.click_save_and_continue_button()
    time.sleep(2)
    test_logger.info("Đã nhấn nút 'Lưu và Tiếp tục'.")
    is_text_displayed = is_displayed_update_article_type.is_text_present_on_page("Chỉnh sửa: Bài viết thử nghiệm")
    expected_result = "Cập nhật thành công Loại bài viết."
    actual_result = expected_result if is_text_displayed else "Lỗi cập nhật."
    if is_text_displayed:
        test_logger.info(f"Test Case 9 PASS: test_save_and_continue_check_edit | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 9 FAIL: test_save_and_continue_check_edit | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 10: Xóa dữ liệu vào ô 'Loại bài viết' (Tiếng Việt), kiểm tra thông báo lỗi.
def test_vi_article_type_clear_and_check_error(update_article_type, enter_field_update_article_type, validation_update_article_type):
    test_logger.info("Bắt đầu Test Case 10: Nhập dữ liệu vào ô 'Loại bài viết' (Tiếng Việt) và sau đó xóa, kiểm tra thông báo lỗi.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    enter_field_update_article_type.clear_vi_article_type()
    time.sleep(2)
    error_displayed = validation_update_article_type.is_field_error_displayed()
    expected_result = "Thông báo lỗi xuất hiện: 'Trường này không được để trống'."
    actual_result = expected_result if error_displayed else "Thông báo lỗi không xuất hiện!"
    if error_displayed:
        test_logger.info(f"Test Case 10 PASS: test_vi_article_type_clear_and_check_error | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 10 FAIL: test_vi_article_type_clear_and_check_error | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 11: Cập nhật Đường dẫn ( Tab Tiếng Việt )  
def test_update_vi_article_link_and_verify(update_article_type,  enter_field_update_article_type, get_field_update_article_type):
    test_logger.info("Bắt đầu Test Case 11: Cập nhật Đường dẫn tab Tiếng Việt -> Lưu và kiểm tra sau khi lưu.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    expected_link = "bai-viet-thu-nghiem-666"
    enter_field_update_article_type.enter_vi_article_link(expected_link)
    time.sleep(1)
    update_article_type.click_save_and_continue_button()
    time.sleep(2)
    test_logger.info("Đã nhấn nút 'Lưu và Tiếp tục'.")
    actual_link = get_field_update_article_type.get_vi_article_link_value()
    expected_result = f"Giá trị '{expected_link}' hiển thị đúng trong ô nhập liệu."
    actual_result = expected_result if actual_link == expected_link else f"Giá trị hiển thị không đúng: '{actual_link}'"
    if actual_link == expected_link:
        test_logger.info(f"Test Case 11 PASS: test_update_vi_article_link_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 11 FAIL: test_update_vi_article_link_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# Test Case 12: Cập nhật Mô tả ngắn ( Tab Tiếng Việt )
def test_update_vi_description_and_verify(update_article_type, enter_field_update_article_type, get_field_update_article_type):
    test_logger.info("Bắt đầu Test Case 12: Nhập 'Mô tả' tab tiếng Việt -> Lưu và kiểm tra dữ liệu.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    expected_description = "Đây là mô tả thử nghiệm cho bài viết mới."
    enter_field_update_article_type.enter_vi_description(expected_description)
    time.sleep(1)
    update_article_type.click_save_and_continue_button()
    time.sleep(2)
    test_logger.info("Đã nhấn nút 'Lưu và Tiếp tục'.")
    actual_description = get_field_update_article_type.get_vi_description_value()
    expected_result = f"Giá trị '{expected_description}' hiển thị đúng trong ô nhập liệu."
    actual_result = expected_result if actual_description == expected_description else f"Giá trị hiển thị không đúng: '{actual_description}'"
    if actual_description == expected_description:
        test_logger.info(f"Test Case 12 PASS: test_update_vi_description_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 12 FAIL: test_update_vi_description_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# Test Case 13: Cập nhật Meta Keyword ( Tab Tiếng Việt )
def test_update_vi_meta_keyword_and_verify(update_article_type, enter_field_update_article_type, get_field_update_article_type):
    test_logger.info("Bắt đầu Test Case 13: Nhập 'Từ khóa meta' tab tiếng Việt -> Lưu và kiểm tra dữ liệu.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    expected_keyword = "tin-tuc, cong-nghe, review"
    enter_field_update_article_type.enter_vi_meta_keyword(expected_keyword)
    time.sleep(1)
    update_article_type.click_save_and_continue_button()
    time.sleep(2)
    test_logger.info("Đã nhấn nút 'Lưu và Tiếp tục'.")
    actual_keyword = get_field_update_article_type.get_vi_meta_keyword_value()
    expected_result = f"Giá trị '{expected_keyword}' hiển thị đúng trong ô nhập liệu."
    actual_result = expected_result if actual_keyword == expected_keyword else f"Giá trị hiển thị không đúng: '{actual_keyword}'"
    if actual_keyword == expected_keyword:
        test_logger.info(f"Test Case 13 PASS: test_update_vi_meta_keyword_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 13 FAIL: test_update_vi_meta_keyword_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# Test Case 14: Cập nhật Meta Description ( Tab Tiếng Việt )
def test_update_vi_meta_description_and_verify(update_article_type, enter_field_update_article_type, get_field_update_article_type):
    test_logger.info("Bắt đầu Test Case 14: Nhập 'Meta Description' tab tiếng Việt -> Lưu và kiểm tra dữ liệu.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    expected_meta_description = "Đây là Meta Description thử nghiệm."
    enter_field_update_article_type.enter_vi_meta_description(expected_meta_description)
    time.sleep(1)
    update_article_type.click_save_and_continue_button()
    time.sleep(2)
    test_logger.info("Đã nhấn nút 'Lưu và Tiếp tục'.")
    actual_meta_description = get_field_update_article_type.get_vi_meta_description_value()
    expected_result = f"Giá trị '{expected_meta_description}' hiển thị đúng trong ô nhập liệu."
    actual_result = expected_result if actual_meta_description == expected_meta_description else f"Giá trị hiển thị không đúng: '{actual_meta_description}'"
    if actual_meta_description == expected_meta_description:
        test_logger.info(f"Test Case 14 PASS: test_update_vi_meta_description_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 14 FAIL: test_update_vi_meta_description_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# Test Case 15: Cập nhật Meta image ( Tab Tiếng Việt )
def test_update_vi_image_and_check_display(update_article_type, meta_image_update_article_type, is_displayed_update_article_type):
    test_logger.info("Bắt đầu Test Case 15: Click tab Browser -> Chọn ảnh -> Click Upload -> Lưu và kiểm tra ảnh hiển thị.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    meta_image_update_article_type.click_button_upload_image()
    time.sleep(1)
    popup_displayed = is_displayed_update_article_type.is_popup_upload_image_displayed()
    assert popup_displayed, "Popup tải lên ảnh không xuất hiện!"
    meta_image_update_article_type.click_tab_browser()
    time.sleep(1)
    meta_image_update_article_type.click_first_image()
    time.sleep(1)
    meta_image_update_article_type.click_button_upload()
    time.sleep(2)
    update_article_type.click_save_and_continue_button()
    time.sleep(2)
    test_logger.info("Đã nhấn nút 'Lưu và Tiếp tục'.")    
    image_displayed = is_displayed_update_article_type.is_uploaded_image_displayed()
    expected_result = "Ảnh hiển thị đúng sau khi tải lên."
    actual_result = expected_result if image_displayed else "Ảnh không hiển thị sau khi tải lên."
    if image_displayed:
        test_logger.info(f"Test Case 15 PASS: test_upload_vi_image_and_check_display | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 15 FAIL: test_upload_vi_image_and_check_display | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
 
# Test Case 16: Cập nhật Loại bài viết ( Tab English )
def test_update_en_article_type_and_verify(update_article_type, enter_field_update_article_type, get_field_update_article_type):
    test_logger.info("Bắt đầu Test Case 16: Nhập loại bài viết tab English -> Lưu và kiểm tra dữ liệu.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    update_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab tiếng Anh.")
    update_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung' hoặc bỏ qua nếu không cần thiết.")
    expected_text = "Bài viết thử nghiệm"
    enter_field_update_article_type.enter_en_article_type(expected_text)
    time.sleep(1)
    update_article_type.click_save_and_continue_button()
    time.sleep(2)
    test_logger.info("Đã nhấn nút 'Lưu và Tiếp tục'.")
    update_article_type.click_tab_english()
    time.sleep(1)    
    actual_text = get_field_update_article_type.get_en_article_type_value()
    expected_result = f"Giá trị '{expected_text}' hiển thị đúng trong ô nhập liệu."
    actual_result = expected_result if actual_text == expected_text else f"Giá trị hiển thị không đúng: '{actual_text}'"
    if actual_text == expected_text:
        test_logger.info(f"Test Case 16 PASS: test_update_en_article_type_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 16 FAIL: test_update_en_article_type_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}" 
        
# Test Case 17: Xóa dữ liệu vào ô 'Loại bài viết' (English), kiểm tra thông báo lỗi.
def test_en_article_type_clear_and_check_error(update_article_type, enter_field_update_article_type, validation_update_article_type):
    test_logger.info("Bắt đầu Test Case 17: Nhập dữ liệu vào ô 'Loại bài viết' English và sau đó xóa, kiểm tra thông báo lỗi.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    update_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    enter_field_update_article_type.clear_en_article_type()
    time.sleep(2)
    error_displayed = validation_update_article_type.is_en_field_error_displayed()
    expected_result = "Thông báo lỗi xuất hiện: 'Trường này không được để trống'."
    actual_result = expected_result if error_displayed else "Thông báo lỗi không xuất hiện!"
    if error_displayed:
        test_logger.info(f"Test Case 17 PASS: test_en_article_type_clear_and_check_error | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 17 FAIL: test_en_article_type_clear_and_check_error | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# Test Case 18: Cập nhật Đường dẫn ( Tab English )
def test_update_en_article_link_and_verify(update_article_type, enter_field_update_article_type, get_field_update_article_type):
    test_logger.info("Bắt đầu Test Case 18: Nhập đường dẫn ở tab English -> Lưu và kiểm tra dữ liệu.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    update_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    update_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung' hoặc bỏ qua nếu không cần thiết.")
    expected_link = "bai-viet-thu-nghiem-888"
    enter_field_update_article_type.enter_en_article_link(expected_link)
    time.sleep(1)
    update_article_type.click_save_and_continue_button()
    time.sleep(2)
    update_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã nhấn nút 'Lưu và Tiếp tục'.") 
    actual_link = get_field_update_article_type.get_en_article_link_value()
    expected_result = f"Giá trị '{expected_link}' hiển thị đúng trong ô nhập liệu."
    actual_result = expected_result if actual_link == expected_link else f"Giá trị hiển thị không đúng: '{actual_link}'"
    if actual_link == expected_link:
        test_logger.info(f"Test Case 18 PASS: test_update_en_article_link_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 18 FAIL: test_update_en_article_link_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 19: Cập nhật Mô tả ngắn ( Tab English )
def test_update_en_description_and_verify(update_article_type, enter_field_update_article_type, get_field_update_article_type):
    test_logger.info("Bắt đầu Test Case 19: Nhập 'Mô tả' tab English -> Lưu và kiểm tra dữ liệu.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    update_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    update_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung' hoặc bỏ qua nếu không cần thiết.")
    expected_description = "Đây là mô tả thử nghiệm cho bài viết mới."
    enter_field_update_article_type.enter_en_description(expected_description)
    time.sleep(1)
    update_article_type.click_save_and_continue_button()
    time.sleep(2)
    update_article_type.click_tab_english()
    time.sleep(1)
    actual_description = get_field_update_article_type.get_en_description_value()
    expected_result = f"Giá trị '{expected_description}' hiển thị đúng trong ô nhập liệu."
    actual_result = expected_result if actual_description == expected_description else f"Giá trị hiển thị không đúng: '{actual_description}'"
    if actual_description == expected_description:
        test_logger.info(f"Test Case 19 PASS: test_update_en_description_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 19 FAIL: test_update_en_description_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 20: Cập nhật Meta Keyword ( Tab English )
def test_update_en_meta_keyword_and_verify(update_article_type, enter_field_update_article_type, get_field_update_article_type):
    test_logger.info("Bắt đầu Test Case 29: Nhập 'Từ khóa meta' tab English -> Lưu và kiểm tra dữ liệu.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    update_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    update_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung' hoặc bỏ qua nếu không cần thiết.")
    expected_keyword = "tin-tuc, cong-nghe, review"
    enter_field_update_article_type.enter_en_meta_keyword(expected_keyword)
    time.sleep(1)
    update_article_type.click_save_and_continue_button()
    time.sleep(2)
    update_article_type.click_tab_english()
    time.sleep(1)
    actual_keyword = get_field_update_article_type.get_en_meta_keyword_value()
    expected_result = f"Giá trị '{expected_keyword}' hiển thị đúng trong ô nhập liệu."
    actual_result = expected_result if actual_keyword == expected_keyword else f"Giá trị hiển thị không đúng: '{actual_keyword}'"
    if actual_keyword == expected_keyword:
        test_logger.info(f"Test Case 20 PASS: test_update_en_meta_keyword_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 20 FAIL: test_update_en_meta_keyword_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# Test Case 21: Cập nhật Meta Description ( Tab English )
def test_update_en_meta_description_and_verify(update_article_type, enter_field_update_article_type, get_field_update_article_type):
    test_logger.info("Bắt đầu Test Case 21: Nhập 'Meta Description' tab English -> Lưu và kiểm tra dữ liệu.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    update_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    update_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung' hoặc bỏ qua nếu không cần thiết.")
    expected_meta_description = "Đây là Meta Description thử nghiệm."
    enter_field_update_article_type.enter_en_meta_description(expected_meta_description)
    time.sleep(1)
    update_article_type.click_save_and_continue_button()
    time.sleep(2)
    update_article_type.click_tab_english()
    time.sleep(1)
    actual_meta_description = get_field_update_article_type.get_en_meta_description_value()
    expected_result = f"Giá trị '{expected_meta_description}' hiển thị đúng trong ô nhập liệu."
    actual_result = expected_result if actual_meta_description == expected_meta_description else f"Giá trị hiển thị không đúng: '{actual_meta_description}'"
    if actual_meta_description == expected_meta_description:
        test_logger.info(f"Test Case 21 PASS: test_update_en_meta_description_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 21 FAIL: test_update_en_meta_description_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# Test Case 22: Cập nhật Meta image ( Tab English )
def test_update_en_image_and_check_display(update_article_type, meta_image_update_article_type, is_displayed_update_article_type):
    test_logger.info("Bắt đầu Test Case 22: Cập nhật Meta image tab English -> Lưu và kiểm tra ảnh hiển thị tab English.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    update_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    update_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung' hoặc bỏ qua nếu không cần thiết.")
    meta_image_update_article_type.click_en_button_upload_image()
    time.sleep(1)
    popup_displayed = is_displayed_update_article_type.is_popup_upload_image_displayed()
    assert popup_displayed, "Popup tải lên ảnh không xuất hiện!"
    meta_image_update_article_type.click_tab_browser()
    time.sleep(1)
    meta_image_update_article_type.click_first_image()
    time.sleep(1)
    meta_image_update_article_type.click_button_upload()
    time.sleep(2)
    update_article_type.click_save_and_continue_button()
    time.sleep(2)
    update_article_type.click_tab_english()
    time.sleep(1)
    image_displayed = is_displayed_update_article_type.is_en_uploaded_image_displayed()
    expected_result = "Ảnh hiển thị đúng sau khi tải lên."
    actual_result = expected_result if image_displayed else "Ảnh không hiển thị sau khi tải lên."
    if image_displayed:
        test_logger.info(f"Test Case 22 PASS: test_upload_en_image_and_check_display | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 22 FAIL: test_upload_en_image_and_check_display | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 23: Click dropdown 'Status' và kiểm tra dropdown có mở không
def test_click_status_dropdown_and_verify(update_article_type, is_displayed_update_article_type):
    test_logger.info("Bắt đầu Test Case 23: Click dropdown 'Status' và kiểm tra dropdown có mở không.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    update_article_type.click_tab_general_information()
    update_article_type.click_dropdown_status()
    time.sleep(2)
    test_logger.info("Đã click vào dropdown 'Status'.")
    dropdown_opened = is_displayed_update_article_type.is_dropdown_opened()
    expected_result = "Dropdown 'Status' mở thành công (tìm thấy 'Chờ xử lý' trên trang)."
    actual_result = expected_result if dropdown_opened else "Dropdown 'Status' KHÔNG mở hoặc không tìm thấy 'Chờ xử lý'!"
    if dropdown_opened:
        test_logger.info(f"Test Case 23 PASS: test_click_status_dropdown_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 23 FAIL: test_click_status_dropdown_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 24: Nhập giá trị vào ô 'Thứ tự sắp xếp' và kiểm tra thông báo lỗi
def test_sort_order_validation(update_article_type, enter_field_update_article_type, validation_update_article_type):
    test_logger.info("Bắt đầu Test Case 24: Nhập giá trị vào ô 'Thứ tự sắp xếp' và kiểm tra thông báo lỗi.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    update_article_type.click_tab_general_information()
    test_value = "5"
    enter_field_update_article_type.enter_sort_order(test_value)
    time.sleep(2)
    test_logger.info(f"Đã nhập '{test_value}' vào ô 'Thứ tự sắp xếp'.")
    enter_field_update_article_type.clear_sort_order()
    time.sleep(2)
    test_logger.info("Đã xóa nội dung trong ô 'Thứ tự sắp xếp'.")
    error_displayed = validation_update_article_type.is_miss_sort_order_error_displayed()
    expected_result = "Thông báo lỗi xuất hiện: 'Vui lòng nhập Thứ tự sắp xếp'."
    actual_result = expected_result if error_displayed else "Thông báo lỗi không xuất hiện!"
    if error_displayed:
        test_logger.info(f"Test Case 24 PASS: test_sort_order_validation | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 24 FAIL: test_sort_order_validation | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 25: Nhập ký tự chữ vào ô 'Thứ tự sắp xếp' và kiểm tra không hiển thị
def test_sort_order_rejects_text(update_article_type, enter_field_update_article_type, get_field_update_article_type):
    test_logger.info("Bắt đầu Test Case 25: Nhập ký tự chữ vào ô 'Thứ tự sắp xếp' và kiểm tra không hiển thị.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    update_article_type.click_tab_general_information()
    invalid_text = "abc"
    enter_field_update_article_type.enter_sort_order(invalid_text)
    time.sleep(2)
    test_logger.info(f"Đã nhập '{invalid_text}' vào ô 'Thứ tự sắp xếp'.")
    actual_value = get_field_update_article_type.get_sort_order_value()
    expected_result = "Không có giá trị nào hiển thị trong ô 'Thứ tự sắp xếp' khi nhập chữ."
    actual_result = expected_result if actual_value == "" else f"Giá trị '{actual_value}' không hợp lệ được hiển thị!"
    if actual_value == "":
        test_logger.info(f"Test Case 25 PASS: test_sort_order_rejects_text | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 25 FAIL: test_sort_order_rejects_text | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 26: Nhập ký tự chữ vào ô 'Thứ tự sắp xếp' và kiểm tra không hiển thị
def test_sort_order_rejects_text(update_article_type, enter_field_update_article_type, get_field_update_article_type):
    test_logger.info("Bắt đầu Test Case 25: Nhập ký tự chữ vào ô 'Thứ tự sắp xếp' và kiểm tra không hiển thị.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    update_article_type.click_tab_general_information()
    valid_text = "5"
    enter_field_update_article_type.enter_sort_order(valid_text)
    time.sleep(2)
    test_logger.info(f"Đã nhập '{valid_text}' vào ô 'Thứ tự sắp xếp'.")
    update_article_type.click_save_and_continue_button()
    time.sleep(2)
    update_article_type.click_tab_general_information()
    actual_value = get_field_update_article_type.get_sort_order_value()
    expected_result = "Giá trị trong ô 'Thứ tự sắp xếp' hiển thị đúng."
    actual_result = expected_result if actual_value == "5" else f"Giá trị '{valid_text}' không được hiển thị!"
    if actual_value == "5":
        test_logger.info(f"Test Case 25 PASS: test_sort_order_rejects_text | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 25 FAIL: test_sort_order_rejects_text | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# Test Case 27: Click dropdown 'Father Type' và kiểm tra dropdown có mở không
def test_click_father_type_dropdown_and_verify(update_article_type, is_displayed_update_article_type):
    test_logger.info("Bắt đầu Test Case 26: Click dropdown 'Father Type' và kiểm tra dropdown có mở không.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    update_article_type.click_tab_general_information()
    update_article_type.click_dropdown_father_type()
    time.sleep(2)
    test_logger.info("Đã click vào dropdown 'Father Type'.")
    dropdown_opened = is_displayed_update_article_type.is_father_dropdown_opened()
    expected_result = "Dropdown 'Father Type' mở thành công (tìm thấy 'Lĩnh vực kinh doanh' trên trang)."
    actual_result = expected_result if dropdown_opened else "Dropdown 'Father Type' KHÔNG mở hoặc không tìm thấy 'Lĩnh vực kinh doanh'!"
    if dropdown_opened:
        test_logger.info(f"Test Case 26 PASS: test_click_father_type_dropdown_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 26 FAIL: test_click_father_type_dropdown_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 28: Click dropdown 'Banner Set' và kiểm tra dropdown có mở không
def test_click_banner_set_dropdown_and_verify(update_article_type, is_displayed_update_article_type):
    test_logger.info("Bắt đầu Test Case 48: Click dropdown 'Banner Set' và kiểm tra dropdown có mở không.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    update_article_type.click_tab_general_information()
    update_article_type.click_dropdown_banner_set()
    time.sleep(2)
    test_logger.info("Đã click vào dropdown 'Banner Set'.")
    dropdown_opened = is_displayed_update_article_type.is_banner_dropdown_opened()
    expected_result = "Dropdown 'Banner Set' mở thành công (tìm thấy 'Banner icon' trên trang)."
    actual_result = expected_result if dropdown_opened else "Dropdown 'Banner Set' KHÔNG mở hoặc không tìm thấy 'Banner icon'!"
    if dropdown_opened:
        test_logger.info(f"Test Case 27 PASS: test_click_banner_set_dropdown_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 27 FAIL: test_click_banner_set_dropdown_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 29: Verify Đường dẫn tự động điền ( Tab Tiếng Việt )  
def test_vi_article_link_auto_field(update_article_type,  enter_field_update_article_type, get_field_update_article_type):
    test_logger.info("Bắt đầu Test Case 29: Verify Đường dẫn tự động điền tab Tiếng Việt.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    expected_link = ""
    enter_field_update_article_type.clear_vi_article_type_link()
    time.sleep(1)
    update_article_type.click_save_and_continue_button()
    time.sleep(2)
    test_logger.info("Đã nhấn nút 'Lưu và Tiếp tục'.")
    time.sleep(2)
    actual_link = get_field_update_article_type.get_vi_article_link_value()
    expected_result = f"Đường dẫn được điền tự động"
    actual_result = expected_result if actual_link != expected_link else f"Đường dẫn không được tự động điền"
    if actual_link != expected_link:
        test_logger.info(f"Test Case 29 PASS: test_vi_article_link_auto_field | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 29 FAIL: test_vi_article_link_auto_field | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# Test Case 30: Verify Đường dẫn tự động điền ( Tab English )  
def test_en_article_link_auto_field(update_article_type,  enter_field_update_article_type, get_field_update_article_type):
    test_logger.info("Bắt đầu Test Case 30: Verify Đường dẫn tự động điền tab English.")
    update_article_type.perform_tag_operations()
    time.sleep(1)
    update_article_type.click_first_link()
    time.sleep(1)
    update_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    update_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung' hoặc bỏ qua nếu không cần thiết.")
    expected_link = ""
    enter_field_update_article_type.clear_en_article_type_link()
    time.sleep(1)
    update_article_type.click_save_and_continue_button()
    time.sleep(2)
    test_logger.info("Đã nhấn nút 'Lưu và Tiếp tục'.")
    time.sleep(2)
    update_article_type.click_tab_english()
    time.sleep(1)
    actual_link = get_field_update_article_type.get_en_article_link_value()
    expected_result = f"Đường dẫn được điền tự động"
    actual_result = expected_result if actual_link != expected_link else f"Đường dẫn không được tự động điền"
    if actual_link != expected_link:
        test_logger.info(f"Test Case 30 PASS: test_en_article_link_auto_field | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 30 FAIL: test_en_article_link_auto_field | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"        