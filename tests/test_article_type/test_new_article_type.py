import time
import pytest
import logging
import datetime
from utils.login import Login
from utils.logger import LoggerConfig
from utils.driver_setup import get_driver
from pages.article_type.new_article_type.new_article_type_base import NewArticleTypeBase
from pages.article_type.new_article_type.is_displayed_new_article_type import IsDisplayedNewArticleType
from pages.article_type.new_article_type.get_field_new_article_type import GetFieldNewArticleType
from pages.article_type.new_article_type.enter_field_new_article_type import EnterFieldNewArticleType
from pages.article_type.new_article_type.meta_image_new_article_type import MetaImageNewArticleType
from pages.article_type.new_article_type.validation_article_type import ValidationArticleType
from pages.article_type.new_article_type.delete_last_char_new_article_type import DeleteLastCharNewArticleType
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
def new_article_type(setup_driver):
    return NewArticleTypeBase(setup_driver)

@pytest.fixture
def is_displayed_new_article_type(setup_driver):
    return IsDisplayedNewArticleType(setup_driver)

@pytest.fixture
def enter_field_new_article_type(setup_driver):
    return EnterFieldNewArticleType(setup_driver)

@pytest.fixture
def get_field_new_article_type(setup_driver):
    return GetFieldNewArticleType(setup_driver)

@pytest.fixture
def meta_image_new_article_type(setup_driver):
    return MetaImageNewArticleType(setup_driver)

@pytest.fixture
def validation_new_article_type(setup_driver):
    return ValidationArticleType(setup_driver)

@pytest.fixture
def delete_last_char_new_article_type(setup_driver):
    return DeleteLastCharNewArticleType(setup_driver)

# Test Case 1: Click 'Trang chủ' trên breadcrumb -> Chuyển hướng về trang chủ.
def test_click_breadcrumb_home(new_article_type):
    test_logger.info("Bắt đầu Test Case 1: Verify khi nhấn vào breadcrumb 'Trang chủ' -> Hệ thống điều hướng về trang chủ thành công.")
    new_article_type.perform_tag_operations()
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    result = new_article_type.click_breadcrumb_home()
    expected_result = "Hệ thống điều hướng thành công đến trang 'Trang chủ'."
    actual_result = expected_result if result else "Hệ thống không điều hướng đến trang 'Trang chủ'."
    if result:
        test_logger.info(f"Test Case 1 PASS: test_click_breadcrumb_home | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 1 FAIL: test_click_breadcrumb_home | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 2: Click 'Danh sach loai bai viet' trên breadcrumb -> Chuyển hướng về trang Danh sach loai bai viet.
def test_click_breadcrumb_type_list(new_article_type):
    test_logger.info("Bắt đầu Test Case 2: Verify có thể nhấn vào 'Danh sách loại bài viết' trên breadcrumb và kiểm tra điều hướng.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    result = new_article_type.click_breadcrumb_type_list()
    assert result, "Không thể nhấn vào breadcrumb 'Danh sách loại bài viết'."
    test_logger.info("Đã nhấn vào breadcrumb 'Danh sách loại bài viết'.")
    expected_url = "https://mpire-cms-demo.mpire.asia/cms/category"
    actual_url_correct = new_article_type.verify_current_url(expected_url)
    expected_result = "Hệ thống điều hướng đúng đến trang 'Danh sách loại bài viết'."
    actual_result = expected_result if actual_url_correct else "Hệ thống không điều hướng đúng trang."
    if actual_url_correct:
        test_logger.info(f"Test Case 2 PASS: test_click_breadcrumb_type_list | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 2 FAIL: test_click_breadcrumb_type_list | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
 
# Test case 3: Click tab Thong tin chung    
def test_click_tab_general_information_and_check_label(new_article_type, is_displayed_new_article_type):
    test_logger.info("Bắt đầu Test Case 3: Nhấn vào tab 'Thông tin chung'.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    result = new_article_type.click_tab_general_information()
    assert result, "Không thể nhấn vào tab 'Thông tin chung'."
    test_logger.info("Đã nhấn vào tab 'Thông tin chung'.")
    label_correct = is_displayed_new_article_type.is_label_status_displayed()
    expected_result = "Tab 'Thong tin chung' duoc hien thi"
    actual_result = expected_result if label_correct else "Tab 'Thong tin chung' không hiển thị."
    if label_correct:
        test_logger.info(f"Test Case 3 PASS: test_click_tab_general_information_and_check_label | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 3 FAIL: test_click_tab_general_information_and_check_label | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test case 4: Click tab Noi dung chinh 
def test_click_tabs_and_check_labels(new_article_type, is_displayed_new_article_type):
    test_logger.info("Bắt đầu Test Case 4: Kiểm tra tab 'Thông tin chung' & 'Nội dung chính'.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    result_tab_info = new_article_type.click_tab_general_information()
    assert result_tab_info, "Không thể nhấn vào tab 'Thông tin chung'."
    test_logger.info("Đã nhấn vào tab 'Thông tin chung'.")
    label_status_correct = is_displayed_new_article_type.is_label_status_displayed()
    assert label_status_correct, "Tab 'Thông tin chung' không đúng hoặc không xuất hiện!"
    test_logger.info("Tab 'Thông tin chung' hiển thị đúng.")
    result_tab_main = new_article_type.click_tab_main_content()
    assert result_tab_main, "Không thể nhấn vào tab 'Nội dung chính'."
    test_logger.info("Đã nhấn vào tab 'Nội dung chính'.")
    label_article_correct = is_displayed_new_article_type.is_label_article_type_correct()
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
def test_click_tab_english_and_check_translate_button(new_article_type, is_displayed_new_article_type):
    test_logger.info("Bắt đầu Test Case 5: Kiểm tra tab 'English' và nút 'Dịch nội dung'.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Tạo mới'.")
    result_tab_english = new_article_type.click_tab_english()
    assert result_tab_english, "Không thể nhấn vào tab 'English'."
    test_logger.info("Đã nhấn vào tab 'English'.")
    is_translate_visible = is_displayed_new_article_type.is_translate_button_displayed()
    assert is_translate_visible, "Nút 'Dịch nội dung' không xuất hiện!"
    test_logger.info("Nút 'Dịch nội dung' xuất hiện đúng.")
    expected_result = "Tab 'English' hoạt động và nút 'Dịch nội dung' hiển thị đúng."
    actual_result = expected_result if is_translate_visible else "Nút 'Dịch nội dung' không hiển thị."
    if is_translate_visible:
        test_logger.info(f"Test Case 5 PASS: test_click_tab_english_and_check_translate_button | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 5 FAIL: test_click_tab_english_and_check_translate_button | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 6: Click tab 'Tieng Viet'
def test_click_tabs_english_vietnamese_and_check_labels(new_article_type, is_displayed_new_article_type):
    test_logger.info("Bắt đầu Test Case 6: Kiểm tra tab 'Tiếng Việt'.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    result_tab_english = new_article_type.click_tab_english()
    assert result_tab_english, "Không thể nhấn vào tab 'Tiếng Anh'."
    test_logger.info("Đã nhấn vào tab 'Tiếng Anh'.")
    translate_button_displayed = is_displayed_new_article_type.is_translate_button_displayed()
    assert translate_button_displayed, "Nút 'Dịch nội dung' không xuất hiện!"
    test_logger.info("Nút 'Dịch nội dung' hiển thị đúng.")
    result_tab_vietnamese = new_article_type.click_tab_tieng_viet()
    assert result_tab_vietnamese, "Không thể nhấn vào tab 'Tiếng Việt'."
    test_logger.info("Đã nhấn vào tab 'Tiếng Việt'.")
    label_article_correct = is_displayed_new_article_type.is_label_article_type_correct()
    assert label_article_correct, "Tab 'Tiếng Việt' không hiển thị đúng!"
    test_logger.info("Tab 'Tiếng Việt' hiển thị đúng.")
    expected_result = "Tab 'Tiếng Việt' hoạt động đúng."
    actual_result = expected_result if (translate_button_displayed and label_article_correct) else "Một trong các bước kiểm tra không đạt yêu cầu."
    if translate_button_displayed and label_article_correct:
        test_logger.info(f"Test Case 6 PASS: test_click_tabs_english_vietnamese_and_check_labels | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 6 FAIL: test_click_tabs_english_vietnamese_and_check_labels | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 7: Click nut 'Luu' khi chua nhap Loai bai viet
def test_click_save_and_check_error_message(new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 7: Click 'Tạo Mới' -> Click 'Lưu' -> Kiểm tra lỗi 'Vui lòng nhập loại bài viết'.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_save_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Lưu' mà không nhập dữ liệu.")
    error_message_displayed = validation_new_article_type.is_field_error_displayed()
    assert error_message_displayed, "Thông báo lỗi 'Vui lòng nhập loại bài viết' không xuất hiện!"
    test_logger.info("Thông báo lỗi 'Vui lòng nhập loại bài viết' đã xuất hiện như mong đợi.")
    expected_result = "Thông báo lỗi 'Vui lòng nhập loại bài viết' xuất hiện đúng."
    actual_result = expected_result if error_message_displayed else "Thông báo lỗi không xuất hiện."
    if error_message_displayed:
        test_logger.info(f"Test Case 7 PASS: test_click_save_and_check_error_message | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 7 FAIL: test_click_save_and_check_error_message | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 8: Click nút "Lưu và Tiếp Tục Cập Nhật" khi chưa nhập Loại bài viết
def test_click_save_and_continue_and_check_error_message(new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 8: Click 'Tạo Mới' -> Click 'Lưu và Tiếp Tục Cập Nhật' -> Kiểm tra lỗi 'Vui lòng nhập loại bài viết'.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_save_and_continue_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Lưu và Tiếp Tục Cập Nhật' mà không nhập dữ liệu.")
    error_message_displayed = validation_new_article_type.is_field_error_displayed()
    assert error_message_displayed, "Thông báo lỗi 'Vui lòng nhập loại bài viết' không xuất hiện!"
    test_logger.info("Thông báo lỗi 'Vui lòng nhập loại bài viết' đã xuất hiện như mong đợi.")
    expected_result = "Thông báo lỗi 'Vui lòng nhập loại bài viết' xuất hiện đúng."
    actual_result = expected_result if error_message_displayed else "Thông báo lỗi không xuất hiện."
    if error_message_displayed:
        test_logger.info(f"Test Case 8 PASS: test_click_save_and_continue_and_check_error_message | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 8 FAIL: test_click_save_and_continue_and_check_error_message | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test case 9: Click nut 'Luu' khi khong nhap loai bai viet o tab 'English'
def test_translate_and_save_without_article_type(new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 9.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab tiếng Anh.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    new_article_type.click_save_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Lưu' mà không nhập loại bài viết.")
    error_message_displayed = validation_new_article_type.is_en_field_error_displayed()
    assert error_message_displayed, "Thông báo lỗi 'Vui lòng nhập loại bài viết' không xuất hiện!"
    test_logger.info("Thông báo lỗi 'Vui lòng nhập loại bài viết' đã xuất hiện như mong đợi.")
    expected_result = "Thông báo lỗi 'Vui lòng nhập loại bài viết' xuất hiện đúng."
    actual_result = expected_result if error_message_displayed else "Thông báo lỗi không xuất hiện."
    if error_message_displayed:
        test_logger.info(f"Test Case 9 PASS: test_translate_and_save_without_article_type | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 9 FAIL: test_translate_and_save_without_article_type | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 10: Click nut 'Luu va tiep tuc cap nhat' o tab 'English' khi chua nhap loai bai viet
def test_translate_and_save_continue_without_article_type(new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 10: Tạo mới -> Click tab tiếng Anh -> Click 'Dịch nội dung' -> Click 'Lưu và Tiếp tục cập nhật' -> Kiểm tra lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab tiếng Anh.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    new_article_type.click_save_and_continue_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Lưu và Tiếp tục cập nhật' mà không nhập loại bài viết.")
    error_message_displayed = validation_new_article_type.is_en_field_error_displayed()
    assert error_message_displayed, "Thông báo lỗi 'Vui lòng nhập loại bài viết' không xuất hiện!"
    test_logger.info("Thông báo lỗi 'Vui lòng nhập loại bài viết' đã xuất hiện như mong đợi.")
    expected_result = "Thông báo lỗi 'Vui lòng nhập loại bài viết' xuất hiện đúng."
    actual_result = expected_result if error_message_displayed else "Thông báo lỗi không xuất hiện."
    if error_message_displayed:
        test_logger.info(f"Test Case 10 PASS: test_translate_and_save_continue_without_article_type | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 10 FAIL: test_translate_and_save_continue_without_article_type | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 11: Nhập loại bài viết o tab 'Tiếng Việt'
def test_enter_vi_article_type_and_verify(new_article_type, enter_field_new_article_type, get_field_new_article_type):
    test_logger.info("Bắt đầu Test Case 11: Nhập loại bài viết tiếng Việt -> Kiểm tra dữ liệu.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    expected_text = "Bài viết thử nghiệm"
    enter_field_new_article_type.enter_vi_article_type(expected_text)
    time.sleep(1)
    actual_text = get_field_new_article_type.get_vi_article_type_value()
    expected_result = f"Giá trị '{expected_text}' hiển thị đúng trong ô nhập liệu."
    actual_result = expected_result if actual_text == expected_text else f"Giá trị hiển thị không đúng: '{actual_text}'"
    if actual_text == expected_text:
        test_logger.info(f"Test Case 11 PASS: test_enter_vi_article_type_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 11 FAIL: test_enter_vi_article_type_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 12: Nhập đường dẫn o tab 'Tiếng Việt'     
def test_enter_vi_article_link_and_verify(new_article_type,  enter_field_new_article_type, get_field_new_article_type):
    test_logger.info("Bắt đầu Test Case 12: Nhập đường dẫn tiếng Việt -> Kiểm tra dữ liệu.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    expected_link = "bai-viet-thu-nghiem"
    enter_field_new_article_type.enter_vi_article_link(expected_link)
    time.sleep(1)
    actual_link = get_field_new_article_type.get_vi_article_link_value()
    expected_result = f"Giá trị '{expected_link}' hiển thị đúng trong ô nhập liệu."
    actual_result = expected_result if actual_link == expected_link else f"Giá trị hiển thị không đúng: '{actual_link}'"
    if actual_link == expected_link:
        test_logger.info(f"Test Case 12 PASS: test_enter_vi_article_link_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 12 FAIL: test_enter_vi_article_link_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 13: Nhập 'Từ khóa meta' o tab 'Tiếng Việt'
def test_enter_vi_meta_keyword_and_verify(new_article_type, enter_field_new_article_type, get_field_new_article_type):
    test_logger.info("Bắt đầu Test Case 13: Nhập 'Từ khóa meta' tiếng Việt -> Kiểm tra dữ liệu.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    expected_keyword = "tin-tuc, cong-nghe, review"
    enter_field_new_article_type.enter_vi_meta_keyword(expected_keyword)
    time.sleep(1)
    actual_keyword = get_field_new_article_type.get_vi_meta_keyword_value()
    expected_result = f"Giá trị '{expected_keyword}' hiển thị đúng trong ô nhập liệu."
    actual_result = expected_result if actual_keyword == expected_keyword else f"Giá trị hiển thị không đúng: '{actual_keyword}'"
    if actual_keyword == expected_keyword:
        test_logger.info(f"Test Case 13 PASS: test_enter_vi_meta_keyword_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 13 FAIL: test_enter_vi_meta_keyword_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 14: Nhập 'Mô tả' o tab 'Tiếng Việt'
def test_enter_vi_description_and_verify(new_article_type, enter_field_new_article_type, get_field_new_article_type):
    test_logger.info("Bắt đầu Test Case 14: Nhập 'Mô tả' tiếng Việt -> Kiểm tra dữ liệu.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    expected_description = "Đây là mô tả thử nghiệm cho bài viết mới."
    enter_field_new_article_type.enter_vi_description(expected_description)
    time.sleep(1)
    actual_description = get_field_new_article_type.get_vi_description_value()
    expected_result = f"Giá trị '{expected_description}' hiển thị đúng trong ô nhập liệu."
    actual_result = expected_result if actual_description == expected_description else f"Giá trị hiển thị không đúng: '{actual_description}'"
    if actual_description == expected_description:
        test_logger.info(f"Test Case 14 PASS: test_enter_vi_description_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 14 FAIL: test_enter_vi_description_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 15: Nhập 'Mô tả Meta' o tab 'Tiếng Việt'
def test_enter_vi_meta_description_and_verify(new_article_type, enter_field_new_article_type, get_field_new_article_type):
    test_logger.info("Bắt đầu Test Case 15: Nhập 'Meta Description' tiếng Việt -> Kiểm tra dữ liệu.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    expected_meta_description = "Đây là Meta Description thử nghiệm."
    enter_field_new_article_type.enter_vi_meta_description(expected_meta_description)
    time.sleep(1)
    actual_meta_description = get_field_new_article_type.get_vi_meta_description_value()
    expected_result = f"Giá trị '{expected_meta_description}' hiển thị đúng trong ô nhập liệu."
    actual_result = expected_result if actual_meta_description == expected_meta_description else f"Giá trị hiển thị không đúng: '{actual_meta_description}'"
    if actual_meta_description == expected_meta_description:
        test_logger.info(f"Test Case 15 PASS: test_enter_vi_meta_description_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 15 FAIL: test_enter_vi_meta_description_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test case 16: Click field 'Upload image'
def test_click_vi_meta_image_and_check_popup(new_article_type, meta_image_new_article_type, is_displayed_new_article_type):
    test_logger.info("Bắt đầu Test Case 16: Click vào hình ảnh -> Kiểm tra popup tải lên ảnh xuất hiện.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    meta_image_new_article_type.click_meta_image()
    time.sleep(1)
    test_logger.info("Đã click vào hình ảnh để mở popup tải lên.")
    popup_displayed = is_displayed_new_article_type.is_popup_upload_image_displayed()
    expected_result = "Popup tải lên ảnh hiển thị đúng."
    actual_result = expected_result if popup_displayed else "Popup tải lên ảnh không xuất hiện."
    if popup_displayed:
        test_logger.info(f"Test Case 16 PASS: test_click_vi_meta_image_and_check_popup | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 16 FAIL: test_click_vi_meta_image_and_check_popup | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test case 17: Click button 'Upload image'
def test_click_vi_upload_image_and_check_popup(new_article_type, meta_image_new_article_type, is_displayed_new_article_type):
    test_logger.info("Bắt đầu Test Case 17: Click vào nut 'Upload' hình ảnh -> Kiểm tra popup tải lên ảnh xuất hiện.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    meta_image_new_article_type.click_button_upload_image()
    time.sleep(1)
    popup_displayed = is_displayed_new_article_type.is_popup_upload_image_displayed()
    expected_result = "Popup tải lên ảnh hiển thị đúng."
    actual_result = expected_result if popup_displayed else "Popup tải lên ảnh không xuất hiện."
    if popup_displayed:
        test_logger.info(f"Test Case 17 PASS: test_click_vi_upload_image_and_check_popup | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 17 FAIL: test_click_vi_upload_image_and_check_popup | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
    
# Test Case 18: Upload ảnh và kiểm tra ảnh có hiển thị không
def test_upload_vi_image_and_check_display(new_article_type, meta_image_new_article_type, is_displayed_new_article_type):
    test_logger.info("Bắt đầu Test Case 18: Click tab Browser -> Chọn ảnh -> Click Upload -> Kiểm tra ảnh hiển thị.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    meta_image_new_article_type.click_button_upload_image()
    time.sleep(1)
    popup_displayed = is_displayed_new_article_type.is_popup_upload_image_displayed()
    assert popup_displayed, "Popup tải lên ảnh không xuất hiện!"
    meta_image_new_article_type.click_tab_browser()
    time.sleep(1)
    meta_image_new_article_type.click_first_image()
    time.sleep(1)
    meta_image_new_article_type.click_button_upload()
    time.sleep(2)
    image_displayed = is_displayed_new_article_type.is_uploaded_image_displayed()
    expected_result = "Ảnh hiển thị đúng sau khi tải lên."
    actual_result = expected_result if image_displayed else "Ảnh không hiển thị sau khi tải lên."
    if image_displayed:
        test_logger.info(f"Test Case 18 PASS: test_upload_vi_image_and_check_display | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 18 FAIL: test_upload_vi_image_and_check_display | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test case 19: Kiểm tra trạng thái nút 'Xóa ảnh' trước và sau khi tải ảnh, sau do click nut xoa anh
def test_check_vi_delete_button_before_and_after_upload(new_article_type, meta_image_new_article_type, is_displayed_new_article_type):
    test_logger.info("Bắt đầu Test Case 19: Kiểm tra trạng thái nút 'Xóa ảnh' trước và sau khi tải ảnh, sau đó click nút xóa ảnh.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    meta_image_new_article_type.click_button_upload_image()
    popup_displayed = is_displayed_new_article_type.is_popup_upload_image_displayed()
    assert popup_displayed, "Popup tải lên ảnh không xuất hiện!"
    meta_image_new_article_type.click_tab_browser()
    meta_image_new_article_type.click_first_image()
    meta_image_new_article_type.click_button_upload()
    is_displayed_new_article_type.is_delete_image_button_displayed()
    meta_image_new_article_type.click_button_delete_image()
    delete_button_after_delete = not is_displayed_new_article_type.is_delete_image_button_displayed()
    expected_result = "Nút 'Xóa ảnh' ẩn đi sau khi xóa ảnh."
    actual_result = expected_result if delete_button_after_delete else "LỖI: Nút 'Xóa ảnh' chưa ẩn đi sau khi xóa ảnh!"
    if delete_button_after_delete:
        test_logger.info(f"Test Case 19 PASS: test_check_vi_delete_button_before_and_after_upload | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 19 FAIL: test_check_vi_delete_button_before_and_after_upload | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 20: Không chọn ảnh và click 'Upload', kiểm tra nút 'Xóa ảnh
def test_vi_upload_without_selecting_image(new_article_type, meta_image_new_article_type, is_displayed_new_article_type):
    test_logger.info("Bắt đầu Test Case 20: Không chọn ảnh và click 'Upload', kiểm tra nút 'Xóa ảnh'.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    meta_image_new_article_type.click_button_upload_image()
    popup_displayed = is_displayed_new_article_type.is_popup_upload_image_displayed()
    assert popup_displayed, "Popup tải lên ảnh không xuất hiện!"
    meta_image_new_article_type.click_button_upload()
    delete_button_after_upload = not is_displayed_new_article_type.is_delete_image_button_displayed()
    expected_result = "Nút 'Xóa ảnh' không xuất hiện sau khi click 'Upload' mà không chọn ảnh."
    actual_result = expected_result if delete_button_after_upload else "Nút 'Xóa ảnh' xuất hiện sau khi click 'Upload' mà không chọn ảnh."
    if delete_button_after_upload:
        test_logger.info(f"Test Case 20 PASS: test_vi_upload_without_selecting_image | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 20 FAIL: test_vi_upload_without_selecting_image | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 21: Nhập 255 ký tự vào ô 'Loại bài viết' (Tiếng Việt)
def test_vi_article_type_255_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 21: Nhập 255 ký tự vào ô 'Loại bài viết' (Tiếng Việt) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    long_text = "A" * 255  # Tạo chuỗi 255 ký tự
    enter_field_new_article_type.enter_vi_article_type(long_text)
    time.sleep(2)
    error_displayed = validation_new_article_type.is_max_type_error_displayed()
    expected_result = "Thông báo lỗi xuất hiện: 'Vui lòng nhập Loại bài viết không quá 254 ký tự'."
    actual_result = expected_result if error_displayed else "Thông báo lỗi không xuất hiện!"
    if error_displayed:
        test_logger.info(f"Test Case 21 PASS: test_vi_article_type_255_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 21 FAIL: test_vi_article_type_255_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 22: Nhập dữ liệu vào ô 'Loại bài viết' (Tiếng Việt) và sau đó xóa, kiểm tra thông báo lỗi.
def test_vi_article_type_clear_and_check_error(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 22: Nhập dữ liệu vào ô 'Loại bài viết' (Tiếng Việt) và sau đó xóa, kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    test_text = "Bài viết test"
    enter_field_new_article_type.enter_vi_article_type(test_text)
    time.sleep(1)
    enter_field_new_article_type.clear_vi_article_type()
    time.sleep(2)
    error_displayed = validation_new_article_type.is_field_error_displayed()
    expected_result = "Thông báo lỗi xuất hiện: 'Trường này không được để trống'."
    actual_result = expected_result if error_displayed else "Thông báo lỗi không xuất hiện!"
    if error_displayed:
        test_logger.info(f"Test Case 22 PASS: test_vi_article_type_clear_and_check_error | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 22 FAIL: test_vi_article_type_clear_and_check_error | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test case Test Case 23: Nhập 255 ký tự vào ô 'Duong dan' (Tiếng Việt)
def test_vi_article_link_255_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 23: Nhập 255 ký tự vào ô 'Duong dan' (Tiếng Việt) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    long_text = "A" * 255
    enter_field_new_article_type.enter_vi_article_link(long_text)
    time.sleep(2)
    error_displayed = validation_new_article_type.is_max_link_error_displayed()
    expected_result = "Thông báo lỗi xuất hiện: 'Vui lòng nhập Duong dan không quá 254 ký tự'."
    actual_result = expected_result if error_displayed else "Thông báo lỗi không xuất hiện!"
    if error_displayed:
        test_logger.info(f"Test Case 23 PASS: test_vi_article_link_255_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 23 FAIL: test_vi_article_link_255_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 24: Nhập 201 ký tự vào ô 'Mô tả ngắn' (Tiếng Việt)
def test_vi_short_description_201_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 24: Nhập 201 ký tự vào ô 'Mô tả ngắn' (Tiếng Việt) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    long_text = "A" * 201
    enter_field_new_article_type.enter_vi_description(long_text)
    time.sleep(2)
    error_displayed = validation_new_article_type.is_max_short_description_error_displayed()
    expected_result = "Thông báo lỗi xuất hiện: 'Vui lòng nhập Mô tả ngắn không quá 200 ký tự'."
    actual_result = expected_result if error_displayed else "Thông báo lỗi không xuất hiện!"
    if error_displayed:
        test_logger.info(f"Test Case 24 PASS: test_vi_short_description_201_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 24 FAIL: test_vi_short_description_201_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 25: Nhập 101 ký tự vào ô 'Meta Keyword' (Tiếng Việt)
def test_vi_meta_keyword_101_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 25: Nhập 101 ký tự vào ô 'Meta Keyword' (Tiếng Việt) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    long_text = "A" * 101
    enter_field_new_article_type.enter_vi_meta_keyword(long_text)
    time.sleep(2)
    error_displayed = validation_new_article_type.is_meta_keyword_error_displayed()
    expected_result = "Thông báo lỗi xuất hiện: 'Vui lòng nhập Meta Keyword không quá 100 ký tự'."
    actual_result = expected_result if error_displayed else "Thông báo lỗi không xuất hiện!"
    if error_displayed:
        test_logger.info(f"Test Case 25 PASS: test_vi_meta_keyword_101_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 25 FAIL: test_vi_meta_keyword_101_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 26: Nhập 501 ký tự vào ô 'Meta Description' (Tiếng Việt)
def test_vi_meta_description_501_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 26: Nhập 501 ký tự vào ô 'Meta Description' (Tiếng Việt) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    long_text = "A" * 501
    enter_field_new_article_type.enter_vi_meta_description(long_text)
    time.sleep(2)
    error_displayed = validation_new_article_type.is_meta_description_error_displayed()
    expected_result = "Thông báo lỗi xuất hiện: 'Vui lòng nhập Meta Description không quá 500 ký tự'."
    actual_result = expected_result if error_displayed else "Thông báo lỗi không xuất hiện!"
    if error_displayed:
        test_logger.info(f"Test Case 26 PASS: test_vi_meta_description_501_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 26 FAIL: test_vi_meta_description_501_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 27: Nhập loại bài viết o tab 'English'
def test_enter_en_article_type_and_verify(new_article_type, enter_field_new_article_type, get_field_new_article_type):
    test_logger.info("Bắt đầu Test Case 27: Nhập loại bài viết tab English -> Kiểm tra dữ liệu.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab tiếng Anh.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    expected_text = "Bài viết thử nghiệm"
    enter_field_new_article_type.enter_en_article_type(expected_text)
    time.sleep(1)
    actual_text = get_field_new_article_type.get_en_article_type_value()
    expected_result = f"Giá trị '{expected_text}' hiển thị đúng trong ô nhập liệu."
    actual_result = expected_result if actual_text == expected_text else f"Giá trị hiển thị không đúng: '{actual_text}'"
    if actual_text == expected_text:
        test_logger.info(f"Test Case 27 PASS: test_enter_en_article_type_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 27 FAIL: test_enter_en_article_type_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 28: Nhập đường dẫn o tab 'Tiếng Việt'     
def test_enter_en_article_link_and_verify(new_article_type, enter_field_new_article_type, get_field_new_article_type):
    test_logger.info("Bắt đầu Test Case 28: Nhập đường dẫn ở tab English -> Kiểm tra dữ liệu.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    expected_link = "bai-viet-thu-nghiem"
    enter_field_new_article_type.enter_en_article_link(expected_link)
    time.sleep(1)
    actual_link = get_field_new_article_type.get_en_article_link_value()
    expected_result = f"Giá trị '{expected_link}' hiển thị đúng trong ô nhập liệu."
    actual_result = expected_result if actual_link == expected_link else f"Giá trị hiển thị không đúng: '{actual_link}'"
    if actual_link == expected_link:
        test_logger.info(f"Test Case 28 PASS: test_enter_en_article_link_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 28 FAIL: test_enter_en_article_link_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 29: Nhập 'Từ khóa meta' o tab 'English'
def test_enter_en_meta_keyword_and_verify(new_article_type, enter_field_new_article_type, get_field_new_article_type):
    test_logger.info("Bắt đầu Test Case 29: Nhập 'Từ khóa meta' tab English -> Kiểm tra dữ liệu.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    expected_keyword = "tin-tuc, cong-nghe, review"
    enter_field_new_article_type.enter_en_meta_keyword(expected_keyword)
    time.sleep(1)
    actual_keyword = get_field_new_article_type.get_en_meta_keyword_value()
    expected_result = f"Giá trị '{expected_keyword}' hiển thị đúng trong ô nhập liệu."
    actual_result = expected_result if actual_keyword == expected_keyword else f"Giá trị hiển thị không đúng: '{actual_keyword}'"
    if actual_keyword == expected_keyword:
        test_logger.info(f"Test Case 29 PASS: test_enter_en_meta_keyword_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 29 FAIL: test_enter_en_meta_keyword_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 30: Nhập 'Mô tả' o tab 'English'
def test_enter_en_description_and_verify(new_article_type, enter_field_new_article_type, get_field_new_article_type):
    test_logger.info("Bắt đầu Test Case 30: Nhập 'Mô tả' tab English -> Kiểm tra dữ liệu.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    expected_description = "Đây là mô tả thử nghiệm cho bài viết mới."
    enter_field_new_article_type.enter_en_description(expected_description)
    time.sleep(1)
    actual_description = get_field_new_article_type.get_en_description_value()
    expected_result = f"Giá trị '{expected_description}' hiển thị đúng trong ô nhập liệu."
    actual_result = expected_result if actual_description == expected_description else f"Giá trị hiển thị không đúng: '{actual_description}'"
    if actual_description == expected_description:
        test_logger.info(f"Test Case 30 PASS: test_enter_en_description_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 30 FAIL: test_enter_en_description_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 31: Nhập 'Mô tả Meta' o tab 'English'
def test_enter_en_meta_description_and_verify(new_article_type, enter_field_new_article_type, get_field_new_article_type):
    test_logger.info("Bắt đầu Test Case 31: Nhập 'Meta Description' tab English -> Kiểm tra dữ liệu.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    expected_meta_description = "Đây là Meta Description thử nghiệm."
    enter_field_new_article_type.enter_en_meta_description(expected_meta_description)
    time.sleep(1)
    actual_meta_description = get_field_new_article_type.get_en_meta_description_value()
    expected_result = f"Giá trị '{expected_meta_description}' hiển thị đúng trong ô nhập liệu."
    actual_result = expected_result if actual_meta_description == expected_meta_description else f"Giá trị hiển thị không đúng: '{actual_meta_description}'"
    if actual_meta_description == expected_meta_description:
        test_logger.info(f"Test Case 31 PASS: test_enter_en_meta_description_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 31 FAIL: test_enter_en_meta_description_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test case 32: Click field 'Upload image' ( Tab English )
def test_click_en_meta_image_and_check_popup(new_article_type, meta_image_new_article_type, is_displayed_new_article_type):
    test_logger.info("Bắt đầu Test Case 32: Click vào hình ảnh tab English -> Kiểm tra popup tải lên ảnh xuất hiện.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    meta_image_new_article_type.click_en_meta_image()
    time.sleep(1)
    test_logger.info("Đã click vào hình ảnh để mở popup tải lên.")
    popup_displayed = is_displayed_new_article_type.is_popup_upload_image_displayed()
    expected_result = "Popup tải lên ảnh hiển thị đúng."
    actual_result = expected_result if popup_displayed else "Popup tải lên ảnh không xuất hiện."
    if popup_displayed:
        test_logger.info(f"Test Case 32 PASS: test_click_en_meta_image_and_check_popup | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 32 FAIL: test_click_en_meta_image_and_check_popup | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test case 33: Click button 'Upload image' tab English
def test_click_en_upload_image_and_check_popup(new_article_type, meta_image_new_article_type, is_displayed_new_article_type):
    test_logger.info("Bắt đầu Test Case 33: Click vào nut 'Upload' hình ảnh tab English -> Kiểm tra popup tải lên ảnh xuất hiện.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    meta_image_new_article_type.click_en_button_upload_image()
    time.sleep(1)
    popup_displayed = is_displayed_new_article_type.is_popup_upload_image_displayed()
    expected_result = "Popup tải lên ảnh hiển thị đúng."
    actual_result = expected_result if popup_displayed else "Popup tải lên ảnh không xuất hiện."
    if popup_displayed:
        test_logger.info(f"Test Case 33 PASS: test_click_en_upload_image_and_check_popup | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 33 FAIL: test_click_en_upload_image_and_check_popup | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
    
# Test Case 34: Upload ảnh và kiểm tra ảnh có hiển thị không
def test_upload_en_image_and_check_display(new_article_type, meta_image_new_article_type, is_displayed_new_article_type):
    test_logger.info("Bắt đầu Test Case 34: Click tab Browser -> Chọn ảnh -> Click Upload -> Kiểm tra ảnh hiển thị tab English.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    meta_image_new_article_type.click_en_button_upload_image()
    time.sleep(1)
    popup_displayed = is_displayed_new_article_type.is_popup_upload_image_displayed()
    assert popup_displayed, "Popup tải lên ảnh không xuất hiện!"
    meta_image_new_article_type.click_tab_browser()
    time.sleep(1)
    meta_image_new_article_type.click_first_image()
    time.sleep(1)
    meta_image_new_article_type.click_button_upload()
    time.sleep(2)
    image_displayed = is_displayed_new_article_type.is_en_uploaded_image_displayed()
    expected_result = "Ảnh hiển thị đúng sau khi tải lên."
    actual_result = expected_result if image_displayed else "Ảnh không hiển thị sau khi tải lên."
    if image_displayed:
        test_logger.info(f"Test Case 34 PASS: test_upload_en_image_and_check_display | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 34 FAIL: test_upload_en_image_and_check_display | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test case 35: Kiểm tra trạng thái nút 'Xóa ảnh' trước và sau khi tải ảnh, sau do click nut xoa anh
def test_check_en_delete_button_before_and_after_upload(new_article_type, meta_image_new_article_type, is_displayed_new_article_type):
    test_logger.info("Bắt đầu Test Case 35: Kiểm tra trạng thái nút 'Xóa ảnh' trước và sau khi tải ảnh, sau đó click nút xóa ảnh tab English.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    meta_image_new_article_type.click_en_button_upload_image()
    popup_displayed = is_displayed_new_article_type.is_popup_upload_image_displayed()
    assert popup_displayed, "Popup tải lên ảnh không xuất hiện!"
    meta_image_new_article_type.click_tab_browser()
    meta_image_new_article_type.click_first_image()
    meta_image_new_article_type.click_button_upload()
    is_displayed_new_article_type.is_en_delete_image_button_displayed()
    meta_image_new_article_type.click_en_button_delete_image()
    delete_button_after_delete = not is_displayed_new_article_type.is_en_delete_image_button_displayed()
    expected_result = "Nút 'Xóa ảnh' ẩn đi sau khi xóa ảnh."
    actual_result = expected_result if delete_button_after_delete else "LỖI: Nút 'Xóa ảnh' chưa ẩn đi sau khi xóa ảnh!"
    if delete_button_after_delete:
        test_logger.info(f"Test Case 35 PASS: test_check_en_delete_button_before_and_after_upload | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 35 FAIL: test_check_en_delete_button_before_and_after_upload | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 36: Không chọn ảnh và click 'Upload', kiểm tra nút 'Xóa ảnh
def test_en_upload_without_selecting_image(new_article_type, meta_image_new_article_type, is_displayed_new_article_type):
    test_logger.info("Bắt đầu Test Case 36: Không chọn ảnh và click 'Upload', kiểm tra nút 'Xóa ảnh' tab English.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    meta_image_new_article_type.click_en_button_upload_image()
    popup_displayed = is_displayed_new_article_type.is_popup_upload_image_displayed()
    assert popup_displayed, "Popup tải lên ảnh không xuất hiện!"
    meta_image_new_article_type.click_button_upload()
    delete_button_after_upload = not is_displayed_new_article_type.is_en_delete_image_button_displayed()
    expected_result = "Nút 'Xóa ảnh' không xuất hiện sau khi click 'Upload' mà không chọn ảnh."
    actual_result = expected_result if delete_button_after_upload else "Nút 'Xóa ảnh' xuất hiện sau khi click 'Upload' mà không chọn ảnh."
    if delete_button_after_upload:
        test_logger.info(f"Test Case 36 PASS: test_en_upload_without_selecting_image | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 36 FAIL: test_en_upload_without_selecting_image | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 37: Nhập 255 ký tự vào ô 'Loại bài viết' (English)
def test_en_article_type_255_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 37: Nhập 255 ký tự vào ô 'Loại bài viết' (English) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    long_text = "A" * 255
    enter_field_new_article_type.enter_en_article_type(long_text)
    time.sleep(2)
    error_displayed = validation_new_article_type.is_en_max_type_error_displayed()
    expected_result = "Thông báo lỗi xuất hiện: 'Vui lòng nhập Loại bài viết không quá 254 ký tự'."
    actual_result = expected_result if error_displayed else "Thông báo lỗi không xuất hiện!"
    if error_displayed:
        test_logger.info(f"Test Case 37 PASS: test_en_article_type_255_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 37 FAIL: test_en_article_type_255_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 38: Nhập dữ liệu vào ô 'Loại bài viết' (English) và sau đó xóa, kiểm tra thông báo lỗi.
def test_en_article_type_clear_and_check_error(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 38: Nhập dữ liệu vào ô 'Loại bài viết' (English) và sau đó xóa, kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    test_text = "Bài viết test"
    enter_field_new_article_type.enter_en_article_type(test_text)
    time.sleep(1)
    enter_field_new_article_type.clear_en_article_type()
    time.sleep(2)
    error_displayed = validation_new_article_type.is_en_field_error_displayed()
    expected_result = "Thông báo lỗi xuất hiện: 'Trường này không được để trống'."
    actual_result = expected_result if error_displayed else "Thông báo lỗi không xuất hiện!"
    if error_displayed:
        test_logger.info(f"Test Case 38 PASS: test_en_article_type_clear_and_check_error | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 38 FAIL: test_en_article_type_clear_and_check_error | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 39: Nhập 255 ký tự vào ô 'Duong dan' (English)
def test_en_article_link_255_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 39: Nhập 255 ký tự vào ô 'Duong dan' (English) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    long_text = "A" * 255
    enter_field_new_article_type.enter_en_article_link(long_text)
    time.sleep(2)
    error_displayed = validation_new_article_type.is_en_max_link_error_displayed()
    expected_result = "Thông báo lỗi xuất hiện: 'Vui lòng nhập Duong dan không quá 254 ký tự'."
    actual_result = expected_result if error_displayed else "Thông báo lỗi không xuất hiện!"
    if error_displayed:
        test_logger.info(f"Test Case 39 PASS: test_en_article_link_255_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 39 FAIL: test_en_article_link_255_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 40: Nhập 255 ký tự vào ô 'Mô tả ngắn' (English)
def test_en_short_description_255_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 40: Nhập 255 ký tự vào ô 'Mô tả ngắn' (English) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    long_text = "A" * 255
    enter_field_new_article_type.enter_en_description(long_text)
    time.sleep(2)
    error_displayed = validation_new_article_type.is_en_max_short_description_error_displayed()
    expected_result = "Thông báo lỗi xuất hiện: 'Vui lòng nhập Mô tả ngắn không quá 254 ký tự'."
    actual_result = expected_result if error_displayed else "Thông báo lỗi không xuất hiện!"
    if error_displayed:
        test_logger.info(f"Test Case 40 PASS: test_en_short_description_255_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 40 FAIL: test_en_short_description_255_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test case 41: Nhập 101 ký tự vào ô 'Meta Keyword' (English)
def test_en_meta_keyword_101_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 41: Nhập 101 ký tự vào ô 'Meta Keyword' (English) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    long_text = "A" * 101
    enter_field_new_article_type.enter_en_meta_keyword(long_text)
    time.sleep(2)
    error_displayed = validation_new_article_type.is_en_meta_keyword_error_displayed()
    expected_result = "Thông báo lỗi xuất hiện: 'Vui lòng nhập Meta Keyword không quá 100 ký tự'."
    actual_result = expected_result if error_displayed else "Thông báo lỗi không xuất hiện!"
    if error_displayed:
        test_logger.info(f"Test Case 41 PASS: test_en_meta_keyword_101_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 41 FAIL: test_en_meta_keyword_101_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 42: Nhập 501 ký tự vào ô 'Meta Description' (English)
def test_en_meta_description_501_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 42: Nhập 501 ký tự vào ô 'Meta Description' (English) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    long_text = "A" * 501
    enter_field_new_article_type.enter_en_meta_description(long_text)
    time.sleep(2)
    error_displayed = validation_new_article_type.is_en_meta_description_error_displayed()
    expected_result = "Thông báo lỗi xuất hiện: 'Vui lòng nhập Meta Description không quá 500 ký tự'."
    actual_result = expected_result if error_displayed else "Thông báo lỗi không xuất hiện!"
    if error_displayed:
        test_logger.info(f"Test Case 42 PASS: test_en_meta_description_501_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 42 FAIL: test_en_meta_description_501_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 43: Click dropdown 'Status' và kiểm tra dropdown có mở không
def test_click_status_dropdown_and_verify(new_article_type, is_displayed_new_article_type):
    test_logger.info("Bắt đầu Test Case 43: Click dropdown 'Status' và kiểm tra dropdown có mở không.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    test_logger.info("Đã vào trang 'Tạo mới loại bài viết'.")
    new_article_type.click_tab_general_information()
    new_article_type.click_dropdown_status()
    time.sleep(2)
    test_logger.info("Đã click vào dropdown 'Status'.")
    dropdown_opened = is_displayed_new_article_type.is_dropdown_opened()
    expected_result = "Dropdown 'Status' mở thành công (tìm thấy 'Chờ xử lý' trên trang)."
    actual_result = expected_result if dropdown_opened else "Dropdown 'Status' KHÔNG mở hoặc không tìm thấy 'Chờ xử lý'!"
    if dropdown_opened:
        test_logger.info(f"Test Case 43 PASS: test_click_status_dropdown_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 43 FAIL: test_click_status_dropdown_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 44: Nhập giá trị vào ô 'Thứ tự sắp xếp' và kiểm tra thông báo lỗi
def test_sort_order_validation(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 44: Nhập giá trị vào ô 'Thứ tự sắp xếp' và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    test_logger.info("Đã vào trang 'Tạo mới loại bài viết'.")
    new_article_type.click_tab_general_information()
    test_value = "5"
    enter_field_new_article_type.enter_sort_order(test_value)
    time.sleep(2)
    test_logger.info(f"Đã nhập '{test_value}' vào ô 'Thứ tự sắp xếp'.")
    enter_field_new_article_type.clear_sort_order()
    time.sleep(2)
    test_logger.info("Đã xóa nội dung trong ô 'Thứ tự sắp xếp'.")
    error_displayed = validation_new_article_type.is_miss_sort_order_error_displayed()
    expected_result = "Thông báo lỗi xuất hiện: 'Vui lòng nhập Thứ tự sắp xếp'."
    actual_result = expected_result if error_displayed else "Thông báo lỗi không xuất hiện!"
    if error_displayed:
        test_logger.info(f"Test Case 44 PASS: test_sort_order_validation | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 44 FAIL: test_sort_order_validation | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 45: Nhập ký tự chữ vào ô 'Thứ tự sắp xếp' và kiểm tra không hiển thị
def test_sort_order_rejects_text(new_article_type, enter_field_new_article_type, get_field_new_article_type):
    test_logger.info("Bắt đầu Test Case 45: Nhập ký tự chữ vào ô 'Thứ tự sắp xếp' và kiểm tra không hiển thị.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    test_logger.info("Đã vào trang 'Tạo mới loại bài viết'.")
    new_article_type.click_tab_general_information()
    invalid_text = "abc"
    enter_field_new_article_type.enter_sort_order(invalid_text)
    time.sleep(2)
    test_logger.info(f"Đã nhập '{invalid_text}' vào ô 'Thứ tự sắp xếp'.")
    actual_value = get_field_new_article_type.get_sort_order_value()
    expected_result = "Không có giá trị nào hiển thị trong ô 'Thứ tự sắp xếp' khi nhập chữ."
    actual_result = expected_result if actual_value == "" else f"Giá trị '{actual_value}' không hợp lệ được hiển thị!"
    if actual_value == "":
        test_logger.info(f"Test Case 45 PASS: test_sort_order_rejects_text | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 45 FAIL: test_sort_order_rejects_text | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 46: Nhập quá 6 ký tự số vào ô 'Thứ tự sắp xếp' và kiểm tra thông báo lỗi
def test_sort_order_exceeds_max_length(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 46: Nhập quá 7 ký tự số vào ô 'Thứ tự sắp xếp' và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_general_information()
    time.sleep(1)
    test_logger.info("Đã vào trang 'Tạo mới loại bài viết'.")
    long_number = "1234567"
    enter_field_new_article_type.enter_sort_order(long_number)
    time.sleep(2)
    test_logger.info(f"Đã nhập '{long_number}' vào ô 'Thứ tự sắp xếp'.")
    error_displayed = validation_new_article_type.is_max_sort_order_error_displayed()
    expected_result = "Thông báo lỗi xuất hiện: 'Vui lòng nhập Thứ tự sắp xếp không quá 6 ký tự số'."
    actual_result = expected_result if error_displayed else "Thông báo lỗi không xuất hiện hoac hien thi sai!"
    if error_displayed:
        test_logger.info(f"Test Case 46 PASS: test_sort_order_exceeds_max_length | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 46 FAIL: test_sort_order_exceeds_max_length | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 47: Click dropdown 'Father Type' và kiểm tra dropdown có mở không
def test_click_father_type_dropdown_and_verify(new_article_type, is_displayed_new_article_type):
    test_logger.info("Bắt đầu Test Case 47: Click dropdown 'Father Type' và kiểm tra dropdown có mở không.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    test_logger.info("Đã vào trang 'Tạo mới loại bài viết'.")
    new_article_type.click_tab_general_information()
    new_article_type.click_dropdown_father_type()
    time.sleep(2)
    test_logger.info("Đã click vào dropdown 'Father Type'.")
    dropdown_opened = is_displayed_new_article_type.is_father_dropdown_opened()
    expected_result = "Dropdown 'Father Type' mở thành công (tìm thấy 'Lĩnh vực kinh doanh' trên trang)."
    actual_result = expected_result if dropdown_opened else "Dropdown 'Father Type' KHÔNG mở hoặc không tìm thấy 'Lĩnh vực kinh doanh'!"
    if dropdown_opened:
        test_logger.info(f"Test Case 47 PASS: test_click_father_type_dropdown_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 47 FAIL: test_click_father_type_dropdown_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 48: Click dropdown 'Banner Set' và kiểm tra dropdown có mở không
def test_click_banner_set_dropdown_and_verify(new_article_type, is_displayed_new_article_type):
    test_logger.info("Bắt đầu Test Case 48: Click dropdown 'Banner Set' và kiểm tra dropdown có mở không.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    test_logger.info("Đã vào trang 'Tạo mới loại bài viết'.")
    new_article_type.click_tab_general_information()
    new_article_type.click_dropdown_banner_set()
    time.sleep(2)
    test_logger.info("Đã click vào dropdown 'Banner Set'.")
    dropdown_opened = is_displayed_new_article_type.is_banner_dropdown_opened()
    expected_result = "Dropdown 'Banner Set' mở thành công (tìm thấy 'Banner icon' trên trang)."
    actual_result = expected_result if dropdown_opened else "Dropdown 'Banner Set' KHÔNG mở hoặc không tìm thấy 'Banner icon'!"
    if dropdown_opened:
        test_logger.info(f"Test Case 48 PASS: test_click_banner_set_dropdown_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 48 FAIL: test_click_banner_set_dropdown_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 49: Nhập loại bài viết, click nút 'Lưu' và kiểm tra đường dẫn có hiển thị loại bài viết
def test_save_and_check_article_type(new_article_type, enter_field_new_article_type, is_displayed_new_article_type):
    test_logger.info("Bắt đầu Test Case 49: Nhập loại bài viết, click nút 'Lưu' và kiểm tra đường dẫn có hiển thị loại bài viết vừa tạo.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    expected_text = "Bài viết thử nghiệm"
    enter_field_new_article_type.enter_vi_article_type(expected_text)
    time.sleep(1)
    test_logger.info(f"Đã nhập loại bài viết: {expected_text}.")
    new_article_type.click_save_button()
    time.sleep(1)
    test_logger.info("Đã nhấn nút 'Lưu'.")
    time.sleep(2)
    expected_url = "https://mpire-cms-demo.mpire.asia/cms/category?page=1" 
    if not new_article_type.verify_current_url(expected_url):
        test_logger.error(f"Test Case 49 FAIL: test_save_and_check_article_type | Expected: {expected_url} | Actual: {new_article_type.driver.current_url} | Status: FAIL")
        assert False, f"Test Case 49 FAIL: test_save_and_check_article_type | Expected: {expected_url} | Actual: {new_article_type.driver.current_url} | Status: FAIL"
    is_text_displayed = is_displayed_new_article_type.is_text_present_on_page(expected_text)
    expected_result = f"Chuyển hướng về trang danh sách và hiển thị đúng loại bài viết: '{expected_text}'."
    actual_result = expected_result if is_text_displayed else f"Loại bài viết '{expected_text}' không được hiển thị trong danh sách."
    if is_text_displayed:
        test_logger.info(f"Test Case 49 PASS: test_save_and_check_article_type | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 49 FAIL: test_save_and_check_article_type | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 50: Nhấn nút 'Lưu và Tiếp tục', kiểm tra trang có chứa thông tin "Chỉnh sửa"
def test_save_and_continue_check_edit(new_article_type, enter_field_new_article_type, is_displayed_new_article_type):
    test_logger.info("Bắt đầu Test Case 50: Nhấn nút 'Lưu' và 'Lưu và Tiếp tục', kiểm tra trang có chứa thông tin 'Chỉnh sửa'.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    expected_text = "Bài viết thử nghiệm"
    enter_field_new_article_type.enter_vi_article_type(expected_text)
    time.sleep(1)
    test_logger.info(f"Đã nhập loại bài viết: {expected_text}.")
    new_article_type.click_save_and_continue_button()
    time.sleep(2)
    test_logger.info("Đã nhấn nút 'Lưu và Tiếp tục'.")
    is_text_displayed = is_displayed_new_article_type.is_text_present_on_page("Chỉnh sửa: Bài viết thử nghiệm")
    expected_result = "Trang đã chuyển sang trạng thái chỉnh sửa sau khi nhấn 'Lưu và Tiếp tục'."
    actual_result = expected_result if is_text_displayed else "Không tìm thấy thông tin 'Chỉnh sửa' trên trang."
    if is_text_displayed:
        test_logger.info(f"Test Case 50 PASS: test_save_and_continue_check_edit | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 50 FAIL: test_save_and_continue_check_edit | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 51: Nhập 253 ký tự vào ô 'Loại bài viết' (Tiếng Việt)
def test_vi_article_type_253_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 51: Nhập 253 ký tự vào ô 'Loại bài viết' (Tiếng Việt) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    long_text = "A" * 253
    enter_field_new_article_type.enter_vi_article_type(long_text)
    time.sleep(2)
    error_not_displayed = not validation_new_article_type.is_max_type_error_displayed()
    expected_result = "Thông báo lỗi không xuất hiện!"
    actual_result = expected_result if error_not_displayed else "Thông báo lỗi xuất hiện: 'Vui lòng nhập Loại bài viết không quá 254 ký tự'."
    if error_not_displayed:
        test_logger.info(f"Test Case 51 PASS: test_vi_article_type_253_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 51 FAIL: test_vi_article_type_253_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# Test Case 52: Nhập 254 ký tự vào ô 'Loại bài viết' (Tiếng Việt)
def test_vi_article_type_254_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 52: Nhập 254 ký tự vào ô 'Loại bài viết' (Tiếng Việt) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    long_text = "A" * 254  
    enter_field_new_article_type.enter_vi_article_type(long_text)
    time.sleep(2)
    error_not_displayed = not validation_new_article_type.is_max_type_error_displayed()
    expected_result = "Thông báo lỗi không xuất hiện!"
    actual_result = expected_result if error_not_displayed else "Thông báo lỗi xuất hiện: 'Vui lòng nhập Loại bài viết không quá 254 ký tự'."
    if error_not_displayed:
        test_logger.info(f"Test Case 52 PASS: test_vi_article_type_254_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 52 FAIL: test_vi_article_type_254_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test case Test Case 53: Nhập 253 ký tự vào ô 'Duong dan' (Tiếng Việt)
def test_vi_article_link_253_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 53: Nhập 253 ký tự vào ô 'Duong dan' (Tiếng Việt) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    long_text = "A" * 253
    enter_field_new_article_type.enter_vi_article_link(long_text)
    time.sleep(2)
    error_not_displayed = not validation_new_article_type.is_max_link_error_displayed()
    expected_result = "Thông báo lỗi không xuất hiện!"
    actual_result = expected_result if error_not_displayed else "Thông báo lỗi xuất hiện: 'Vui lòng nhập Duong dan không quá 254 ký tự'."
    if error_not_displayed:
        test_logger.info(f"Test Case 53 PASS: test_vi_article_link_253_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 53 FAIL: test_vi_article_link_253_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# Test case Test Case 54: Nhập 254 ký tự vào ô 'Duong dan' (Tiếng Việt)
def test_vi_article_link_254_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 54: Nhập 254 ký tự vào ô 'Duong dan' (Tiếng Việt) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    long_text = "A" * 254
    enter_field_new_article_type.enter_vi_article_link(long_text)
    time.sleep(2)
    error_not_displayed = not validation_new_article_type.is_max_link_error_displayed()
    expected_result = "Thông báo lỗi không xuất hiện!"
    actual_result = expected_result if error_not_displayed else "Thông báo lỗi xuất hiện: 'Vui lòng nhập Duong dan không quá 254 ký tự'."
    if error_not_displayed:
        test_logger.info(f"Test Case 54 PASS: test_vi_article_link_254_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 54 FAIL: test_vi_article_link_254_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 55: Nhập 199 ký tự vào ô 'Mô tả ngắn' (Tiếng Việt)
def test_vi_short_description_199_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 55: Nhập 199 ký tự vào ô 'Mô tả ngắn' (Tiếng Việt) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    long_text = "A" * 199
    enter_field_new_article_type.enter_vi_description(long_text)
    time.sleep(2)
    error_not_displayed = not validation_new_article_type.is_max_short_description_error_displayed()
    expected_result = "Thông báo lỗi không xuất hiện!"
    actual_result = expected_result if error_not_displayed else "Thông báo lỗi xuất hiện: 'Vui lòng nhập Mô tả ngắn không quá 200 ký tự'."
    if error_not_displayed:
        test_logger.info(f"Test Case 55 PASS: test_vi_short_description_199_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 55 FAIL: test_vi_short_description_199_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# Test Case 56: Nhập 200 ký tự vào ô 'Mô tả ngắn' (Tiếng Việt)
def test_vi_short_description_200_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 56: Nhập 200 ký tự vào ô 'Mô tả ngắn' (Tiếng Việt) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    long_text = "A" * 200
    enter_field_new_article_type.enter_vi_description(long_text)
    time.sleep(2)
    error_not_displayed = not validation_new_article_type.is_max_short_description_error_displayed()
    expected_result = "Thông báo lỗi không xuất hiện!"
    actual_result = expected_result if error_not_displayed else "Thông báo lỗi xuất hiện: 'Vui lòng nhập Mô tả ngắn không quá 200 ký tự'."
    if error_not_displayed:
        test_logger.info(f"Test Case 56 PASS: test_vi_short_description_200_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 56 FAIL: test_vi_short_description_200_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 57: Nhập 99 ký tự vào ô 'Meta Keyword' (Tiếng Việt)
def test_vi_meta_keyword_99_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 57: Nhập 99 ký tự vào ô 'Meta Keyword' (Tiếng Việt) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    long_text = "A" * 99
    enter_field_new_article_type.enter_vi_meta_keyword(long_text)
    time.sleep(2)
    error_not_displayed = not validation_new_article_type.is_meta_keyword_error_displayed()
    expected_result = "Thông báo lỗi không xuất hiện!"
    actual_result = expected_result if error_not_displayed else "Thông báo lỗi xuất hiện: 'Vui lòng nhập Meta Keyword không quá 100 ký tự'."
    if error_not_displayed:
        test_logger.info(f"Test Case 57 PASS: test_vi_meta_keyword_99_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 57 FAIL: test_vi_meta_keyword_99_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# Test Case 58: Nhập 100 ký tự vào ô 'Meta Keyword' (Tiếng Việt)
def test_vi_meta_keyword_100_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 58: Nhập 100 ký tự vào ô 'Meta Keyword' (Tiếng Việt) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    long_text = "A" * 100
    enter_field_new_article_type.enter_vi_meta_keyword(long_text)
    time.sleep(2)
    error_not_displayed = not validation_new_article_type.is_meta_keyword_error_displayed()
    expected_result = "Thông báo lỗi không xuất hiện!"
    actual_result = expected_result if error_not_displayed else "Thông báo lỗi xuất hiện: 'Vui lòng nhập Meta Keyword không quá 100 ký tự'."
    if error_not_displayed:
        test_logger.info(f"Test Case 58 PASS: test_vi_meta_keyword_100_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 58 FAIL: test_vi_meta_keyword_100_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 59: Nhập 499 ký tự vào ô 'Meta Description' (Tiếng Việt)
def test_vi_meta_description_499_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 59: Nhập 499 ký tự vào ô 'Meta Description' (Tiếng Việt) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    long_text = "A" * 499
    enter_field_new_article_type.enter_vi_meta_description(long_text)
    time.sleep(2)
    error_displayed = not validation_new_article_type.is_meta_description_error_displayed()
    expected_result = "Thông báo lỗi không xuất hiện!"
    actual_result = expected_result if error_displayed else "Thông báo lỗi xuất hiện: 'Vui lòng nhập Meta Description không quá 499 ký tự'."
    if error_displayed:
        test_logger.info(f"Test Case 59 PASS: test_vi_meta_description_499_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 59 FAIL: test_vi_meta_description_499_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# Test Case 60: Nhập 500 ký tự vào ô 'Meta Description' (Tiếng Việt)
def test_vi_meta_description_500_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 60: Nhập 500 ký tự vào ô 'Meta Description' (Tiếng Việt) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    long_text = "A" * 500
    enter_field_new_article_type.enter_vi_meta_description(long_text)
    time.sleep(2)
    error_displayed = not validation_new_article_type.is_meta_description_error_displayed()
    expected_result = "Thông báo lỗi không xuất hiện!"
    actual_result = expected_result if error_displayed else "Thông báo lỗi xuất hiện: 'Vui lòng nhập Meta Description không quá 499 ký tự'."
    if error_displayed:
        test_logger.info(f"Test Case 60 PASS: test_vi_meta_description_500_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 60 FAIL: test_vi_meta_description_500_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 61: Nhập 253 ký tự vào ô 'Loại bài viết' (English)
def test_en_article_type_253_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 61: Nhập 253 ký tự vào ô 'Loại bài viết' (English) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    long_text = "A" * 253 
    enter_field_new_article_type.enter_en_article_type(long_text)
    time.sleep(2)
    error_not_displayed = not validation_new_article_type.is_en_max_type_error_displayed()
    expected_result = "Thông báo lỗi không xuất hiện!"
    actual_result = expected_result if error_not_displayed else "Thông báo lỗi xuất hiện: 'Vui lòng nhập Loại bài viết không quá 254 ký tự'."
    if error_not_displayed:
        test_logger.info(f"Test Case 61 PASS: test_en_article_type_253_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 61 FAIL: test_en_article_type_253_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# Test Case 62: Nhập 254 ký tự vào ô 'Loại bài viết' (English)
def test_en_article_type_254_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 62: Nhập 254 ký tự vào ô 'Loại bài viết' (English) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    long_text = "A" * 254
    enter_field_new_article_type.enter_en_article_type(long_text)
    time.sleep(2)
    error_not_displayed = not validation_new_article_type.is_en_max_type_error_displayed()
    expected_result = "Thông báo lỗi không xuất hiện!"
    actual_result = expected_result if error_not_displayed else "Thông báo lỗi xuất hiện: 'Vui lòng nhập Loại bài viết không quá 254 ký tự'."
    if error_not_displayed:
        test_logger.info(f"Test Case 62 PASS: test_en_article_type_254_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 62 FAIL: test_en_article_type_254_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test case Test Case 63: Nhập 253 ký tự vào ô 'Duong dan' (English)
def test_en_article_link_253_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 63: Nhập 253 ký tự vào ô 'Duong dan' (English) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    long_text = "A" * 253
    enter_field_new_article_type.enter_en_article_link(long_text)
    time.sleep(2)
    error_not_displayed = not validation_new_article_type.is_en_max_link_error_displayed()
    expected_result = "Thông báo lỗi không xuất hiện!"
    actual_result = expected_result if error_not_displayed else "Thông báo lỗi xuất hiện: 'Vui lòng nhập Duong dan không quá 254 ký tự'."
    if error_not_displayed:
        test_logger.info(f"Test Case 63 PASS: test_en_article_link_253_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 63 FAIL: test_en_article_link_253_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# Test case Test Case 64: Nhập 254 ký tự vào ô 'Duong dan' (English)
def test_en_article_link_254_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 64: Nhập 254 ký tự vào ô 'Duong dan' (English) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    long_text = "A" * 254
    enter_field_new_article_type.enter_en_article_link(long_text)
    time.sleep(2)
    error_not_displayed = not validation_new_article_type.is_en_max_link_error_displayed()
    expected_result = "Thông báo lỗi không xuất hiện!"
    actual_result = expected_result if error_not_displayed else "Thông báo lỗi xuất hiện: 'Vui lòng nhập Duong dan không quá 254 ký tự'."
    if error_not_displayed:
        test_logger.info(f"Test Case 64 PASS: test_en_article_link_254_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 64 FAIL: test_en_article_link_254_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 65: Nhập 199 ký tự vào ô 'Mô tả ngắn' (English)
def test_en_short_description_199_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 65: Nhập 199 ký tự vào ô 'Mô tả ngắn' (English) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    long_text = "A" * 199
    enter_field_new_article_type.enter_en_description(long_text)
    time.sleep(2)
    error_not_displayed = not validation_new_article_type.is_en_max_short_description_error_displayed()
    expected_result = "Thông báo lỗi không xuất hiện!"
    actual_result = expected_result if error_not_displayed else "Thông báo lỗi xuất hiện: 'Vui lòng nhập Mô tả ngắn không quá 200 ký tự'."
    if error_not_displayed:
        test_logger.info(f"Test Case 65 PASS: test_en_short_description_199_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 65 FAIL: test_en_short_description_199_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# Test Case 66: Nhập 200 ký tự vào ô 'Mô tả ngắn' (English)
def test_en_short_description_200_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 66: Nhập 200 ký tự vào ô 'Mô tả ngắn' (English) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    long_text = "A" * 200
    enter_field_new_article_type.enter_en_description(long_text)
    time.sleep(2)
    error_not_displayed = not validation_new_article_type.is_en_max_short_description_error_displayed()
    expected_result = "Thông báo lỗi không xuất hiện!"
    actual_result = expected_result if error_not_displayed else "Thông báo lỗi xuất hiện: 'Vui lòng nhập Mô tả ngắn không quá 200 ký tự'."
    if error_not_displayed:
        test_logger.info(f"Test Case 66 PASS: test_en_short_description_200_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 66 FAIL: test_en_short_description_200_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 67: Nhập 99 ký tự vào ô 'Meta Keyword' (English)
def test_en_meta_keyword_99_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 67: Nhập 99 ký tự vào ô 'Meta Keyword' (English) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    long_text = "A" * 99
    enter_field_new_article_type.enter_en_meta_keyword(long_text)
    time.sleep(2)
    error_not_displayed = not validation_new_article_type.is_en_meta_keyword_error_displayed()
    expected_result = "Thông báo lỗi không xuất hiện!"
    actual_result = expected_result if error_not_displayed else "Thông báo lỗi xuất hiện: 'Vui lòng nhập Meta Keyword không quá 100 ký tự'."
    if error_not_displayed:
        test_logger.info(f"Test Case 67 PASS: test_en_meta_keyword_99_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 67 FAIL: test_en_meta_keyword_99_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# Test Case 68: Nhập 100 ký tự vào ô 'Meta Keyword' (English)
def test_en_meta_keyword_100_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 68: Nhập 100 ký tự vào ô 'Meta Keyword' (English) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    long_text = "A" * 100
    enter_field_new_article_type.enter_en_meta_keyword(long_text)
    time.sleep(2)
    error_not_displayed = not validation_new_article_type.is_en_meta_keyword_error_displayed()
    expected_result = "Thông báo lỗi không xuất hiện!"
    actual_result = expected_result if error_not_displayed else "Thông báo lỗi xuất hiện: 'Vui lòng nhập Meta Keyword không quá 100 ký tự'."
    if error_not_displayed:
        test_logger.info(f"Test Case 68 PASS: test_en_meta_keyword_100_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 68 FAIL: test_en_meta_keyword_100_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 69: Nhập 499 ký tự vào ô 'Meta Description' (English)
def test_en_meta_description_499_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 69: Nhập 499 ký tự vào ô 'Meta Description' (English) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    long_text = "A" * 499
    enter_field_new_article_type.enter_en_meta_description(long_text)
    time.sleep(2)
    error_displayed = not validation_new_article_type.is_en_meta_description_error_displayed()
    expected_result = "Thông báo lỗi không xuất hiện!"
    actual_result = expected_result if error_displayed else "Thông báo lỗi xuất hiện: 'Vui lòng nhập Meta Description không quá 499 ký tự'."
    if error_displayed:
        test_logger.info(f"Test Case 69 PASS: test_en_meta_description_499_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 69 FAIL: test_en_meta_description_499_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# Test Case 70: Nhập 500 ký tự vào ô 'Meta Description' (English)
def test_en_meta_description_500_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 70: Nhập 500 ký tự vào ô 'Meta Description' (English) và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    long_text = "A" * 500
    enter_field_new_article_type.enter_en_meta_description(long_text)
    time.sleep(2)
    error_displayed = not validation_new_article_type.is_en_meta_description_error_displayed()
    expected_result = "Thông báo lỗi không xuất hiện!"
    actual_result = expected_result if error_displayed else "Thông báo lỗi xuất hiện: 'Vui lòng nhập Meta Description không quá 499 ký tự'."
    if error_displayed:
        test_logger.info(f"Test Case 70 PASS: test_en_meta_description_500_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 70 FAIL: test_en_meta_description_500_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 71: Nhập 5 ký tự số vào ô 'Thứ tự sắp xếp' và kiểm tra thông báo lỗi
def test_sort_order_exceeds_5_numbers(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 71: Nhập 5 ký tự số vào ô 'Thứ tự sắp xếp' và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_general_information()
    time.sleep(1)
    test_logger.info("Đã vào trang 'Tạo mới loại bài viết'.")
    long_number = "12345"
    enter_field_new_article_type.enter_sort_order(long_number)
    time.sleep(2)
    test_logger.info(f"Đã nhập '{long_number}' vào ô 'Thứ tự sắp xếp'.")
    error_displayed = not validation_new_article_type.is_max_sort_order_error_displayed()
    expected_result = "Thông báo lỗi không xuất hiện!"
    actual_result = expected_result if error_displayed else "Thông báo lỗi xuất hiện: 'Vui lòng nhập Thứ tự sắp xếp không quá 6 ký tự số'."
    if error_displayed:
        test_logger.info(f"Test Case 71 PASS: test_sort_order_exceeds_5_numbers | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 71 FAIL: test_sort_order_exceeds_5_numbers | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# Test Case 72: Nhập 6 ký tự số vào ô 'Thứ tự sắp xếp' và kiểm tra thông báo lỗi
def test_sort_order_exceeds_6_numbers(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 72: Nhập 6 ký tự số vào ô 'Thứ tự sắp xếp' và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_general_information()
    time.sleep(1)
    test_logger.info("Đã vào trang 'Tạo mới loại bài viết'.")
    long_number = "123456"
    enter_field_new_article_type.enter_sort_order(long_number)
    time.sleep(2)
    test_logger.info(f"Đã nhập '{long_number}' vào ô 'Thứ tự sắp xếp'.")
    error_displayed = not validation_new_article_type.is_max_sort_order_error_displayed()
    expected_result = "Thông báo lỗi không xuất hiện!"
    actual_result = expected_result if error_displayed else "Thông báo lỗi xuất hiện: 'Vui lòng nhập Thứ tự sắp xếp không quá 6 ký tự số'."
    if error_displayed:
        test_logger.info(f"Test Case 72 PASS: test_sort_order_exceeds_6_numbers | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 72 FAIL: test_sort_order_exceeds_6_numbers | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 73: Nhập 255 ký tự vào ô 'Loại bài viết' (Tiếng Việt) sau đó xóa ký tự cuối cùng và kiểm tra thông báo lỗi.
def test_vi_article_type_255_chars_and_remove_last(new_article_type, enter_field_new_article_type, validation_new_article_type, delete_last_char_new_article_type):
    test_logger.info("Bắt đầu Test Case 73: Nhập 255 ký tự vào ô 'Loại bài viết' (Tiếng Việt) sau đó xóa 1 ký tự và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    long_text = "A" * 255
    enter_field_new_article_type.enter_vi_article_type(long_text)
    time.sleep(2)
    test_logger.info("Đã nhập 255 ký tự vào ô 'Loại bài viết'.")
    validation_new_article_type.is_max_type_error_displayed()
    test_logger.info("Đã kiểm tra thông báo lỗi khi nhập 255 ký tự.")
    delete_last_char_new_article_type.delete_vi_article_type_character()
    time.sleep(2)
    test_logger.info("Đã xóa ký tự cuối cùng trong ô 'Loại bài viết'.")
    error_displayed = not validation_new_article_type.is_max_type_error_displayed()
    expected_result = "Thông báo lỗi đã được ẩn đi."
    actual_result = expected_result if error_displayed else "Thông báo lỗi vẫn được hiển thị!"
    if error_displayed:
        test_logger.info(f"Test Case 73 PASS: test_vi_article_type_255_chars_and_remove_last | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 73 FAIL: test_vi_article_type_255_chars_and_remove_last | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 74: Nhập dữ liệu vào ô 'Loại bài viết' (Tiếng Việt), sau đó xóa và kiểm tra thông báo lỗi.
def test_vi_article_type_clear_and_check_error_and_retype(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 74: Nhập dữ liệu vào ô 'Loại bài viết' (Tiếng Việt), sau đó xóa và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    test_text = "Bài viết test"
    enter_field_new_article_type.enter_vi_article_type(test_text)
    time.sleep(1)
    test_logger.info(f"Đã nhập '{test_text}' vào ô 'Loại bài viết'.")
    enter_field_new_article_type.clear_vi_article_type()
    time.sleep(2)
    test_logger.info("Đã xóa nội dung trong ô 'Loại bài viết'.")
    validation_new_article_type.is_field_error_displayed()
    test_logger.info("Đã kiểm tra thông báo lỗi khi ô 'Loại bài viết' bị xóa.")
    enter_field_new_article_type.enter_vi_article_type(test_text)
    time.sleep(1)
    test_logger.info(f"Đã nhập lại '{test_text}' vào ô 'Loại bài viết'.")
    error_displayed = not validation_new_article_type.is_field_error_displayed()
    expected_result = "Thông báo lỗi đã được ẩn đi."
    actual_result = expected_result if error_displayed else "Thông báo lỗi vẫn hiển thị!"
    if error_displayed:
        test_logger.info(f"Test Case 74 PASS: test_vi_article_type_clear_and_check_error_and_retype | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 74 FAIL: test_vi_article_type_clear_and_check_error_and_retype | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 75: Nhập 255 ký tự vào ô 'Đường dẫn' (Tiếng Việt), sau đó xóa ký tự cuối cùng và kiểm tra thông báo lỗi.
def test_vi_article_link_255_chars_and_remove_last(new_article_type, enter_field_new_article_type, validation_new_article_type, delete_last_char_new_article_type):
    test_logger.info("Bắt đầu Test Case 75: Nhập 255 ký tự vào ô 'Đường dẫn' (Tiếng Việt), sau đó xóa ký tự cuối cùng và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    long_text = "A" * 255
    enter_field_new_article_type.enter_vi_article_link(long_text)
    time.sleep(2)
    test_logger.info(f"Đã nhập {len(long_text)} ký tự vào ô 'Đường dẫn'.")
    validation_new_article_type.is_max_link_error_displayed()
    test_logger.info("Đã kiểm tra sự xuất hiện của thông báo lỗi khi nhập đủ 255 ký tự.")
    delete_last_char_new_article_type.delete_vi_article_link_character()
    test_logger.info("Đã xóa ký tự cuối cùng khỏi ô 'Đường dẫn'.")
    error_displayed = not validation_new_article_type.is_max_link_error_displayed()
    expected_result = "Thông báo lỗi đã được ẩn đi."
    actual_result = expected_result if error_displayed else "Thông báo lỗi vẫn hiển thị!"
    if error_displayed:
        test_logger.info(f"Test Case 75 PASS: test_vi_article_link_255_chars_and_remove_last | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 75 FAIL: test_vi_article_link_255_chars_and_remove_last | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 76: Nhập 201 ký tự vào ô 'Mô tả ngắn' (Tiếng Việt), sau đó xóa ký tự cuối cùng và kiểm tra thông báo lỗi.
def test_vi_short_description_201_chars_and_remove_last(new_article_type, enter_field_new_article_type, validation_new_article_type, delete_last_char_new_article_type):
    test_logger.info("Bắt đầu Test Case 76: Nhập 201 ký tự vào ô 'Mô tả ngắn' (Tiếng Việt), sau đó xóa ký tự cuối cùng và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    long_text = "A" * 201  
    enter_field_new_article_type.enter_vi_description(long_text)
    time.sleep(2)
    test_logger.info(f"Đã nhập {len(long_text)} ký tự vào ô 'Mô tả ngắn'.")
    validation_new_article_type.is_max_short_description_error_displayed()
    test_logger.info("Đã kiểm tra sự xuất hiện của thông báo lỗi khi nhập quá 200 ký tự.")
    delete_last_char_new_article_type.delete_vi_description_character()
    test_logger.info("Đã xóa ký tự cuối cùng khỏi ô 'Mô tả ngắn'.")
    error_displayed = not validation_new_article_type.is_max_short_description_error_displayed()
    expected_result = "Thông báo lỗi đã được ẩn đi."
    actual_result = expected_result if error_displayed else "Thông báo lỗi vẫn hiển thị!"
    if error_displayed:
        test_logger.info(f"Test Case 76 PASS: test_vi_short_description_201_chars_and_remove_last | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 76 FAIL: test_vi_short_description_201_chars_and_remove_last | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 77: Nhập 101 ký tự vào ô 'Meta Keyword' (Tiếng Việt), sau đó xóa ký tự cuối cùng và kiểm tra thông báo lỗi.
def test_vi_meta_keyword_101_chars_and_remove_last(new_article_type, enter_field_new_article_type, validation_new_article_type, delete_last_char_new_article_type):
    test_logger.info("Bắt đầu Test Case 77: Nhập 101 ký tự vào ô 'Meta Keyword' (Tiếng Việt), sau đó xóa ký tự cuối cùng và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    long_text = "A" * 101
    enter_field_new_article_type.enter_vi_meta_keyword(long_text)
    time.sleep(2)
    test_logger.info(f"Đã nhập {len(long_text)} ký tự vào ô 'Meta Keyword'.")
    validation_new_article_type.is_meta_keyword_error_displayed()
    test_logger.info("Đã kiểm tra sự xuất hiện của thông báo lỗi khi nhập quá 100 ký tự.")
    delete_last_char_new_article_type.delete_vi_meta_keyword_character()
    test_logger.info("Đã xóa ký tự cuối cùng khỏi ô 'Meta Keyword'.")
    error_displayed = not validation_new_article_type.is_meta_keyword_error_displayed()
    expected_result = "Thông báo lỗi đã được ẩn đi."
    actual_result = expected_result if error_displayed else "Thông báo lỗi vẫn hiển thị!"

    if error_displayed:
        test_logger.info(f"Test Case 77 PASS: test_vi_meta_keyword_101_chars_and_remove_last | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 77 FAIL: test_vi_meta_keyword_101_chars_and_remove_last | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 78: Nhập 501 ký tự vào ô 'Meta Description' (Tiếng Việt), sau đó xóa ký tự cuối cùng và kiểm tra thông báo lỗi.
def test_vi_meta_description_501_chars_and_remove_last(new_article_type, enter_field_new_article_type, validation_new_article_type, delete_last_char_new_article_type):
    test_logger.info("Bắt đầu Test Case 78: Nhập 501 ký tự vào ô 'Meta Description' (Tiếng Việt), sau đó xóa ký tự cuối cùng và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    long_text = "A" * 501
    enter_field_new_article_type.enter_vi_meta_description(long_text)
    time.sleep(2)
    test_logger.info(f"Đã nhập {len(long_text)} ký tự vào ô 'Meta Description'.")
    validation_new_article_type.is_meta_description_error_displayed()
    test_logger.info("Đã kiểm tra sự xuất hiện của thông báo lỗi khi nhập quá 500 ký tự.")
    delete_last_char_new_article_type.delete_vi_meta_description_character()
    test_logger.info("Đã xóa ký tự cuối cùng khỏi ô 'Meta Description'.")
    error_displayed = not validation_new_article_type.is_meta_description_error_displayed()
    expected_result = "Thông báo lỗi đã được ẩn đi."
    actual_result = expected_result if error_displayed else "Thông báo lỗi vẫn hiển thị!"
    if error_displayed:
        test_logger.info(f"Test Case 78 PASS: test_vi_meta_description_501_chars_and_remove_last | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 78 FAIL: test_vi_meta_description_501_chars_and_remove_last | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 79: Nhập 255 ký tự vào ô 'Loại bài viết' (Tiếng Việt) sau đó xóa ký tự cuối cùng và kiểm tra thông báo lỗi.
def test_en_article_type_255_chars_and_remove_last(new_article_type, enter_field_new_article_type, validation_new_article_type, delete_last_char_new_article_type):
    test_logger.info("Bắt đầu Test Case 73: Nhập 255 ký tự vào ô 'Loại bài viết' (English) sau đó xóa 1 ký tự và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    long_text = "A" * 255 
    enter_field_new_article_type.enter_en_article_type(long_text)
    time.sleep(2)
    test_logger.info("Đã nhập 255 ký tự vào ô 'Loại bài viết'.")
    validation_new_article_type.is_en_max_type_error_displayed()
    test_logger.info("Đã kiểm tra thông báo lỗi khi nhập 255 ký tự.")
    delete_last_char_new_article_type.delete_en_article_type_character()
    time.sleep(2)
    test_logger.info("Đã xóa ký tự cuối cùng trong ô 'Loại bài viết'.")
    error_displayed = not validation_new_article_type.is_en_max_type_error_displayed()
    expected_result = "Thông báo lỗi đã được ẩn đi."
    actual_result = expected_result if error_displayed else "Thông báo lỗi vẫn được hiển thị!"
    if error_displayed:
        test_logger.info(f"Test Case 79 PASS: test_en_article_type_255_chars_and_remove_last | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 79 FAIL: test_en_article_type_255_chars_and_remove_last | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 80: Nhập dữ liệu vào ô 'Loại bài viết' (English), sau đó xóa và kiểm tra thông báo lỗi.
def test_en_article_type_clear_and_check_error_and_retype(new_article_type, enter_field_new_article_type, validation_new_article_type):
    test_logger.info("Bắt đầu Test Case 80: Nhập dữ liệu vào ô 'Loại bài viết' (English), sau đó xóa và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    test_text = "Bài viết test"
    enter_field_new_article_type.enter_en_article_type(test_text)
    time.sleep(1)
    test_logger.info(f"Đã nhập '{test_text}' vào ô 'Loại bài viết'.")
    enter_field_new_article_type.clear_en_article_type()
    time.sleep(2)
    test_logger.info("Đã xóa nội dung trong ô 'Loại bài viết'.")
    validation_new_article_type.is_en_field_error_displayed()
    test_logger.info("Đã kiểm tra thông báo lỗi khi ô 'Loại bài viết' bị xóa.")
    enter_field_new_article_type.enter_en_article_type(test_text)
    time.sleep(1)
    test_logger.info(f"Đã nhập lại '{test_text}' vào ô 'Loại bài viết'.")
    error_displayed = not validation_new_article_type.is_en_field_error_displayed()
    expected_result = "Thông báo lỗi đã được ẩn đi."
    actual_result = expected_result if error_displayed else "Thông báo lỗi vẫn hiển thị!"
    if error_displayed:
        test_logger.info(f"Test Case 80 PASS: test_en_article_type_clear_and_check_error_and_retype | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 80 FAIL: test_en_article_type_clear_and_check_error_and_retype | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 81: Nhập 255 ký tự vào ô 'Đường dẫn' (English), sau đó xóa ký tự cuối cùng và kiểm tra thông báo lỗi.
def test_en_article_link_255_chars_and_remove_last(new_article_type, enter_field_new_article_type, validation_new_article_type, delete_last_char_new_article_type):
    test_logger.info("Bắt đầu Test Case 81: Nhập 255 ký tự vào ô 'Đường dẫn' (English), sau đó xóa ký tự cuối cùng và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    long_text = "A" * 255
    enter_field_new_article_type.enter_en_article_link(long_text)
    time.sleep(2)
    test_logger.info(f"Đã nhập {len(long_text)} ký tự vào ô 'Đường dẫn'.")
    validation_new_article_type.is_en_max_link_error_displayed()
    test_logger.info("Đã kiểm tra sự xuất hiện của thông báo lỗi khi nhập đủ 255 ký tự.")
    delete_last_char_new_article_type.delete_en_article_link_character()
    test_logger.info("Đã xóa ký tự cuối cùng khỏi ô 'Đường dẫn'.")
    error_displayed = not validation_new_article_type.is_en_max_link_error_displayed()
    expected_result = "Thông báo lỗi đã được ẩn đi."
    actual_result = expected_result if error_displayed else "Thông báo lỗi vẫn hiển thị!"
    if error_displayed:
        test_logger.info(f"Test Case 81 PASS: test_en_article_link_255_chars_and_remove_last | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 81 FAIL: test_en_article_link_255_chars_and_remove_last | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 82: Nhập 201 ký tự vào ô 'Mô tả ngắn' (Tiếng Việt), sau đó xóa ký tự cuối cùng và kiểm tra thông báo lỗi.
def test_en_short_description_201_chars_and_remove_last(new_article_type, enter_field_new_article_type, validation_new_article_type, delete_last_char_new_article_type):
    test_logger.info("Bắt đầu Test Case 82: Nhập 201 ký tự vào ô 'Mô tả ngắn' (English), sau đó xóa ký tự cuối cùng và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    long_text = "A" * 201
    enter_field_new_article_type.enter_en_description(long_text)
    time.sleep(2)
    test_logger.info(f"Đã nhập {len(long_text)} ký tự vào ô 'Mô tả ngắn'.")
    validation_new_article_type.is_en_max_short_description_error_displayed()
    test_logger.info("Đã kiểm tra sự xuất hiện của thông báo lỗi khi nhập quá 200 ký tự.")
    delete_last_char_new_article_type.delete_en_description_character()
    test_logger.info("Đã xóa ký tự cuối cùng khỏi ô 'Mô tả ngắn'.")
    error_displayed = not validation_new_article_type.is_en_max_short_description_error_displayed()
    expected_result = "Thông báo lỗi đã được ẩn đi."
    actual_result = expected_result if error_displayed else "Thông báo lỗi vẫn hiển thị!"
    if error_displayed:
        test_logger.info(f"Test Case 82 PASS: test_en_short_description_201_chars_and_remove_last | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 82 FAIL: test_en_short_description_201_chars_and_remove_last | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 83: Nhập 101 ký tự vào ô 'Meta Keyword' (English), sau đó xóa ký tự cuối cùng và kiểm tra thông báo lỗi.
def test_en_meta_keyword_101_chars_and_remove_last(new_article_type, enter_field_new_article_type, validation_new_article_type, delete_last_char_new_article_type):
    test_logger.info("Bắt đầu Test Case 83: Nhập 101 ký tự vào ô 'Meta Keyword' (English), sau đó xóa ký tự cuối cùng và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    long_text = "A" * 101 
    enter_field_new_article_type.enter_en_meta_keyword(long_text)
    time.sleep(2)
    test_logger.info(f"Đã nhập {len(long_text)} ký tự vào ô 'Meta Keyword'.")
    validation_new_article_type.is_en_meta_keyword_error_displayed()
    test_logger.info("Đã kiểm tra sự xuất hiện của thông báo lỗi khi nhập quá 100 ký tự.")
    delete_last_char_new_article_type.delete_en_meta_keyword_character()
    test_logger.info("Đã xóa ký tự cuối cùng khỏi ô 'Meta Keyword'.")
    error_displayed = not validation_new_article_type.is_en_meta_keyword_error_displayed()
    expected_result = "Thông báo lỗi đã được ẩn đi."
    actual_result = expected_result if error_displayed else "Thông báo lỗi vẫn hiển thị!"
    if error_displayed:
        test_logger.info(f"Test Case 83 PASS: test_en_meta_keyword_101_chars_and_remove_last | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 83 FAIL: test_en_meta_keyword_101_chars_and_remove_last | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 84: Nhập 501 ký tự vào ô 'Meta Description' (English), sau đó xóa ký tự cuối cùng và kiểm tra thông báo lỗi.
def test_en_meta_description_501_chars_and_remove_last(new_article_type, enter_field_new_article_type, validation_new_article_type, delete_last_char_new_article_type):
    test_logger.info("Bắt đầu Test Case 84: Nhập 501 ký tự vào ô 'Meta Description' (English), sau đó xóa ký tự cuối cùng và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.leep(1)
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab 'English'.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    long_text = "A" * 501
    enter_field_new_article_type.enter_en_meta_description(long_text)
    time.sleep(2)
    test_logger.info(f"Đã nhập {len(long_text)} ký tự vào ô 'Meta Description'.")
    validation_new_article_type.is_en_meta_description_error_displayed()
    test_logger.info("Đã kiểm tra sự xuất hiện của thông báo lỗi khi nhập quá 500 ký tự.")
    delete_last_char_new_article_type.delete_en_meta_description_character()
    test_logger.info("Đã xóa ký tự cuối cùng khỏi ô 'Meta Description'.")
    error_displayed = not validation_new_article_type.is_en_meta_description_error_displayed()
    expected_result = "Thông báo lỗi đã được ẩn đi."
    actual_result = expected_result if error_displayed else "Thông báo lỗi vẫn hiển thị!"
    if error_displayed:
        test_logger.info(f"Test Case 84 PASS: test_en_meta_description_501_chars_and_remove_last | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 84 FAIL: test_en_meta_description_501_chars_and_remove_last | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 85: Nhập quá 6 ký tự số vào ô 'Thứ tự sắp xếp' và kiểm tra thông báo lỗi
def test_sort_order_exceeds_max_length_and_remove_last(new_article_type, enter_field_new_article_type, validation_new_article_type, delete_last_char_new_article_type):
    test_logger.info("Bắt đầu Test Case 85: Nhập quá 6 ký tự số vào ô 'Thứ tự sắp xếp' và kiểm tra thông báo lỗi.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    new_article_type.click_tab_general_information()
    time.sleep(1)
    test_logger.info("Đã vào trang 'Tạo mới loại bài viết'.")
    long_number = "1234567"  # Chuỗi có 7 ký tự
    enter_field_new_article_type.enter_sort_order(long_number)
    time.sleep(2)
    test_logger.info(f"Đã nhập '{long_number}' vào ô 'Thứ tự sắp xếp'.")
    validation_new_article_type.is_max_sort_order_error_displayed()
    test_logger.info("Đã kiểm tra sự xuất hiện của thông báo lỗi khi nhập quá 6 ký tự vào ô 'Thứ tự sắp xếp'.")
    delete_last_char_new_article_type.delete_last_character_in_sort_order()
    test_logger.info("Đã xóa ký tự cuối cùng khỏi ô 'Thứ tự sắp xếp'.")
    error_displayed = not validation_new_article_type.is_max_sort_order_error_displayed()
    expected_result = "Thông báo lỗi đã được ẩn đi."
    actual_result = expected_result if error_displayed else "Thông báo lỗi vẫn hiển thị!"
    if error_displayed:
        test_logger.info(f"Test Case 85 PASS: test_sort_order_exceeds_max_length_and_remove_last | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 85 FAIL: test_sort_order_exceeds_max_length_and_remove_last | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 86: Nhập Loại bài viết sau khi đã click nút 'Lưu' khi chưa nhập Loại bài viết ( Tieng Viet )
def test_click_save_and_field_information(new_article_type, validation_new_article_type, enter_field_new_article_type):
    test_logger.info("Bắt đầu Test Case 86: Click 'Tạo Mới' -> Click 'Lưu' -> Kiểm tra lỗi 'Vui lòng nhập loại bài viết' ( Tieng Viet ).")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    test_logger.info("Đã vào trang 'Tạo mới loại bài viết'.")
    new_article_type.click_save_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Lưu' mà không nhập dữ liệu vào ô 'Loại bài viết'.")
    error_message_displayed = validation_new_article_type.is_field_error_displayed()
    test_logger.info("Đã kiểm tra thông báo lỗi hiển thị khi không nhập loại bài viết.")
    expected_text = "Bài viết thử nghiệm"
    enter_field_new_article_type.enter_vi_article_type(expected_text)
    time.sleep(1)
    test_logger.info(f"Đã nhập '{expected_text}' vào ô 'Loại bài viết'.")
    error_message_displayed = not validation_new_article_type.is_field_error_displayed()
    expected_result = "Thông báo lỗi đã được ẩn đi."
    actual_result = expected_result if error_message_displayed else "Thông báo lỗi vẫn hiển thị."
    if error_message_displayed:
        test_logger.info(f"Test Case 86 PASS: test_click_save_and_field_information | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 86 FAIL: test_click_save_and_field_information | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 87: Nhập Loại bài viết sau khi đã click nút 'Lưu' khi chưa nhập Loại bài viết ( Tieng Viet )
def test_click_save_and_continue_and_field_information(new_article_type, validation_new_article_type, enter_field_new_article_type):
    test_logger.info("Bắt đầu Test Case 87: Click 'Tạo Mới' -> Click 'Lưu' -> Kiểm tra lỗi 'Vui lòng nhập loại bài viết' ( Tieng Viet ).")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    test_logger.info("Đã vào trang 'Tạo mới loại bài viết'.")
    new_article_type.click_save_and_continue_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Lưu' mà không nhập dữ liệu vào ô 'Loại bài viết'.")
    error_message_displayed = validation_new_article_type.is_field_error_displayed()
    test_logger.info("Đã kiểm tra thông báo lỗi hiển thị khi không nhập loại bài viết.")
    expected_text = "Bài viết thử nghiệm"
    enter_field_new_article_type.enter_vi_article_type(expected_text)
    time.sleep(1)
    test_logger.info(f"Đã nhập '{expected_text}' vào ô 'Loại bài viết'.")
    error_message_displayed = not validation_new_article_type.is_field_error_displayed()
    expected_result = "Thông báo lỗi đã được ẩn đi."
    actual_result = expected_result if error_message_displayed else "Thông báo lỗi vẫn hiển thị."
    if error_message_displayed:
        test_logger.info(f"Test Case 87 PASS: test_click_save_and_continue_and_field_information | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 87 FAIL: test_click_save_and_continue_and_field_information | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 88: Nhập Loại bài viết sau khi đã click nút 'Lưu' khi chưa nhập Loại bài viết (Tiếng Việt)
def test_translate_and_save_and_field_information(new_article_type, validation_new_article_type, enter_field_new_article_type):
    test_logger.info("Bắt đầu Test Case 88: Click 'Tạo Mới' -> Click 'Lưu' -> Kiểm tra lỗi 'Vui lòng nhập loại bài viết' (Tiếng Việt).")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    test_logger.info("Đã vào trang 'Tạo mới loại bài viết'.")
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab tiếng Anh.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung' để dịch thông tin sang tiếng Anh.")
    new_article_type.click_save_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Lưu' mà không nhập dữ liệu vào ô 'Loại bài viết'.")
    error_message_displayed = validation_new_article_type.is_en_field_error_displayed()
    test_logger.info("Đã kiểm tra thông báo lỗi hiển thị khi không nhập loại bài viết.")
    expected_text = "Bài viết thử nghiệm"
    enter_field_new_article_type.enter_en_article_type(expected_text)
    time.sleep(1)
    test_logger.info(f"Đã nhập '{expected_text}' vào ô 'Loại bài viết'.")
    error_message_displayed = not validation_new_article_type.is_en_field_error_displayed()
    expected_result = "Thông báo lỗi đã được ẩn đi."
    actual_result = expected_result if error_message_displayed else "Thông báo lỗi vẫn hiển thị."
    if error_message_displayed:
        test_logger.info(f"Test Case 88 PASS: test_translate_and_save_and_field_information | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 88 FAIL: test_translate_and_save_and_field_information | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 89: Nhập Loại bài viết sau khi đã click nút 'Lưu' khi chưa nhập Loại bài viết (English)
def test_translate_and_continuing_save_and_field_information(new_article_type, validation_new_article_type, enter_field_new_article_type):
    test_logger.info("Bắt đầu Test Case 89: Click 'Tạo Mới' -> Click 'Lưu' -> Kiểm tra lỗi 'Vui lòng nhập loại bài viết' (English).")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    test_logger.info("Đã vào trang 'Tạo mới loại bài viết'.")
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab tiếng Anh để đảm bảo rằng đang làm việc với phiên bản tiếng Anh của trang.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung' để dịch các trường nhập liệu sang tiếng Anh.")
    new_article_type.click_save_and_continue_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Lưu' mà không nhập dữ liệu vào ô 'Loại bài viết'.")
    error_message_displayed = validation_new_article_type.is_en_field_error_displayed()
    test_logger.info("Đã kiểm tra thông báo lỗi hiển thị khi không nhập loại bài viết.")
    expected_text = "Bài viết thử nghiệm"
    enter_field_new_article_type.enter_en_article_type(expected_text)
    time.sleep(1)
    test_logger.info(f"Đã nhập '{expected_text}' vào ô 'Loại bài viết'.")
    error_message_displayed = not validation_new_article_type.is_en_field_error_displayed()
    expected_result = "Thông báo lỗi đã được ẩn đi sau khi nhập dữ liệu hợp lệ."
    actual_result = expected_result if error_message_displayed else "Thông báo lỗi vẫn hiển thị."
    if error_message_displayed:
        test_logger.info(f"Test Case 89 PASS: test_translate_and_continuing_save_and_field_information | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 89 FAIL: test_translate_and_continuing_save_and_field_information | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# Test Case 90 Thap cam
def test_enter_content_and_upload_image(new_article_type, enter_field_new_article_type, get_field_new_article_type, meta_image_new_article_type, is_displayed_new_article_type):
    test_logger.info("Bắt đầu Test Case: Nhập toàn bộ nội dung và tải lên ảnh.")
    new_article_type.perform_tag_operations()
    time.sleep(1)
    new_article_type.click_new_article_type_button()
    time.sleep(1)
    expected_text = "Bài viết thử nghiệm"
    enter_field_new_article_type.enter_vi_article_type(expected_text)
    expected_link = "bai-viet-thu-nghiem"
    enter_field_new_article_type.enter_vi_article_link(expected_link)
    expected_keyword = "tin-tuc, cong-nghe, review"
    enter_field_new_article_type.enter_vi_meta_keyword(expected_keyword)
    expected_description = "Đây là mô tả thử nghiệm cho bài viết mới."
    enter_field_new_article_type.enter_vi_description(expected_description)
    expected_meta_description = "Đây là Meta Description thử nghiệm."
    enter_field_new_article_type.enter_vi_meta_description(expected_meta_description)
    time.sleep(1)
    assert get_field_new_article_type.get_vi_article_type_value() == expected_text, "Loại bài viết không đúng!"
    assert get_field_new_article_type.get_vi_article_link_value() == expected_link, "Đường dẫn không đúng!"
    assert get_field_new_article_type.get_vi_meta_keyword_value() == expected_keyword, "Từ khóa meta không đúng!"
    assert get_field_new_article_type.get_vi_description_value() == expected_description, "Mô tả không đúng!"
    assert get_field_new_article_type.get_vi_meta_description_value() == expected_meta_description, "Meta Description không đúng!"
    test_logger.info("Tiến hành tải lên ảnh.")
    meta_image_new_article_type.click_button_upload_image()
    time.sleep(1)
    assert is_displayed_new_article_type.is_popup_upload_image_displayed(), "Popup tải lên ảnh không xuất hiện!"
    meta_image_new_article_type.click_tab_browser()
    time.sleep(1)
    meta_image_new_article_type.click_first_image()
    time.sleep(1)
    meta_image_new_article_type.click_button_upload()
    time.sleep(2)  
    assert is_displayed_new_article_type.is_uploaded_image_displayed(), "Ảnh không hiển thị sau khi tải lên!"
    new_article_type.click_tab_english()
    time.sleep(1)
    test_logger.info("Đã chuyển sang tab tiếng Anh.")
    new_article_type.click_translate_button()
    time.sleep(1)
    test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")
    expected_text = "Test Article"
    enter_field_new_article_type.enter_en_article_type(expected_text)
    expected_link = "test-article"
    enter_field_new_article_type.enter_en_article_link(expected_link)
    expected_keyword = "news, technology, review"
    enter_field_new_article_type.enter_en_meta_keyword(expected_keyword)
    expected_description = "This is a test description for the new article."
    enter_field_new_article_type.enter_en_description(expected_description)
    expected_meta_description = "This is a test Meta Description."
    enter_field_new_article_type.enter_en_meta_description(expected_meta_description)
    time.sleep(1)
    assert get_field_new_article_type.get_en_article_type_value() == expected_text, "Article type does not match!"
    assert get_field_new_article_type.get_en_article_link_value() == expected_link, "Article link does not match!"
    assert get_field_new_article_type.get_en_meta_keyword_value() == expected_keyword, "Meta keywords do not match!"
    assert get_field_new_article_type.get_en_description_value() == expected_description, "Description does not match!"
    assert get_field_new_article_type.get_en_meta_description_value() == expected_meta_description, "Meta Description does not match!"
    test_logger.info("Proceeding to upload an image.")
    meta_image_new_article_type.click_en_button_upload_image()
    time.sleep(1)
    assert is_displayed_new_article_type.is_popup_upload_image_displayed(), "Image upload popup did not appear!"
    meta_image_new_article_type.click_tab_browser()
    time.sleep(1)
    meta_image_new_article_type.click_first_image()
    time.sleep(1)
    meta_image_new_article_type.click_button_upload()
    assert is_displayed_new_article_type.is_en_uploaded_image_displayed(), "Uploaded image is not displayed!"
    new_article_type.click_save_button()
    time.sleep(2)
    expected_url = "https://mpire-cms-demo.mpire.asia/cms/category"
    created = new_article_type.verify_current_url(expected_url)
    expected_result = "Luu thanh cong."
    actual_result = expected_result if created else "Luu khong thanh cong."
    if created:
        test_logger.info(f"Test Case 90 PASS: test_enter_content_and_upload_image | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 90 FAIL: test_enter_content_and_upload_image | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"