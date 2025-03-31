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

# # Test Case 1: Click 'Trang chủ' trên breadcrumb -> Chuyển hướng về trang chủ.
# def test_click_breadcrumb_home(new_article_type):
#     test_logger.info("Bắt đầu Test Case 1: Verify khi nhấn vào breadcrumb 'Trang chủ' -> Hệ thống điều hướng về trang chủ thành công.")

#     new_article_type.perform_tag_operations()

#     # Nhan nut tao moi
#     new_article_type.click_new_article_type_button()
#     time.sleep(1)

#     # Nhấn vào breadcrumb 'Trang chủ'
#     result = new_article_type.click_breadcrumb_home()

#     # Xác định kết quả mong đợi
#     expected_result = "Hệ thống điều hướng thành công đến trang 'Trang chủ'."
#     actual_result = expected_result if result else "Hệ thống không điều hướng đến trang 'Trang chủ'."

#     # Ghi lại kết quả
#     if result:
#         test_logger.info(f"Test Case 1 PASS: test_click_breadcrumb_home | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 1 FAIL: test_click_breadcrumb_home | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 2: Click 'Danh sach loai bai viet' trên breadcrumb -> Chuyển hướng về trang Danh sach loai bai viet.
# def test_click_breadcrumb_type_list(new_article_type):
#     test_logger.info("Bắt đầu Test Case 2: Verify có thể nhấn vào 'Danh sách loại bài viết' trên breadcrumb và kiểm tra điều hướng.")

#     new_article_type.perform_tag_operations()
#     time.sleep(1)

#     # Nhan nut tao moi
#     new_article_type.click_new_article_type_button()
#     time.sleep(1)

#     # Nhấn vào breadcrumb "Danh sách loại bài viết"
#     result = new_article_type.click_breadcrumb_type_list()
#     assert result, "Không thể nhấn vào breadcrumb 'Danh sách loại bài viết'."
#     test_logger.info("Đã nhấn vào breadcrumb 'Danh sách loại bài viết'.")

#     # Xác minh URL sau khi nhấn
#     expected_url = "https://mpire-cms-demo.mpire.asia/cms/category"
#     actual_url_correct = new_article_type.verify_current_url(expected_url)

#     # Kết quả mong đợi
#     expected_result = "Hệ thống điều hướng đúng đến trang 'Danh sách loại bài viết'."
#     actual_result = expected_result if actual_url_correct else "Hệ thống không điều hướng đúng trang."

#     # Kiểm tra kết quả
#     if actual_url_correct:
#         test_logger.info(f"Test Case 2 PASS: test_click_breadcrumb_type_list | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 2 FAIL: test_click_breadcrumb_type_list | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"
 
# # Test case 3: Click tab Thong tin chung    
# def test_click_tab_general_information_and_check_label(new_article_type, is_displayed_new_article_type):
#     test_logger.info("Bắt đầu Test Case 3: Nhấn vào tab 'Thông tin chung'.")

#     new_article_type.perform_tag_operations()
#     time.sleep(1)

#     # Nhấn vào breadcrumb "Danh sách loại bài viết" để đảm bảo đang ở trang cần kiểm tra
#     new_article_type.click_new_article_type_button()
#     time.sleep(1)

#     # Click vào tab "Thông tin chung"
#     result = new_article_type.click_tab_general_information()
#     assert result, "Không thể nhấn vào tab 'Thông tin chung'."
#     test_logger.info("Đã nhấn vào tab 'Thông tin chung'.")

#     # Kiểm tra giá trị của LABEL_STATUS
#     label_correct = is_displayed_new_article_type.is_label_status_displayed()

#     # Kết quả mong đợi
#     expected_result = "Tab 'Thong tin chung' duoc hien thi"
#     actual_result = expected_result if label_correct else "Tab 'Thong tin chung' không hiển thị."

#     # Kiểm tra kết quả
#     if label_correct:
#         test_logger.info(f"Test Case 3 PASS: test_click_tab_general_information_and_check_label | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 3 FAIL: test_click_tab_general_information_and_check_label | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test case 4: Click tab Noi dung chinh 
# def test_click_tabs_and_check_labels(new_article_type, is_displayed_new_article_type):
#     test_logger.info("Bắt đầu Test Case 4: Kiểm tra tab 'Thông tin chung' & 'Nội dung chính'.")

#     new_article_type.perform_tag_operations()
#     time.sleep(1)

#     # Click "Tạo mới" để đảm bảo đang ở đúng trang
#     new_article_type.click_new_article_type_button()
#     time.sleep(1)

#     # **Bước 1**: Click vào tab "Thông tin chung"
#     result_tab_info = new_article_type.click_tab_general_information()
#     assert result_tab_info, "Không thể nhấn vào tab 'Thông tin chung'."
#     test_logger.info("Đã nhấn vào tab 'Thông tin chung'.")

#     # **Bước 2**: Kiểm tra giá trị của LABEL_STATUS thông qua `is_displayed_new_article_type`
#     label_status_correct = is_displayed_new_article_type.is_label_status_displayed()
#     assert label_status_correct, "Tab 'Thông tin chung' không đúng hoặc không xuất hiện!"
#     test_logger.info("Tab 'Thông tin chung' hiển thị đúng.")

#     # **Bước 3**: Click vào tab "Nội dung chính"
#     result_tab_main = new_article_type.click_tab_main_content()
#     assert result_tab_main, "Không thể nhấn vào tab 'Nội dung chính'."
#     test_logger.info("Đã nhấn vào tab 'Nội dung chính'.")

#     # **Bước 4**: Kiểm tra giá trị của LABEL_ARTICLE_TYPE thông qua `is_displayed_new_article_type`
#     label_article_correct = is_displayed_new_article_type.is_label_article_type_correct()
#     assert label_article_correct, "Tab 'Nội dung chính' không đúng hoặc không xuất hiện!"
#     test_logger.info("Tab 'Nội dung chính' hiển thị đúng.")

#     # Kết quả mong đợi
#     expected_result = "Tab 'Thông tin chung' và 'Nội dung chính' hoạt động đúng."
#     actual_result = expected_result if (label_status_correct and label_article_correct) else "Một trong các bước kiểm tra không đạt yêu cầu."

#     # Kiểm tra kết quả
#     if label_status_correct and label_article_correct:
#         test_logger.info(f"Test Case 4 PASS: test_click_tabs_and_check_labels | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 4 FAIL: test_click_tabs_and_check_labels | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 5: Click tab 'English'
# def test_click_tab_english_and_check_translate_button(new_article_type, is_displayed_new_article_type):
#     test_logger.info("Bắt đầu Test Case 5: Kiểm tra tab 'English' và nút 'Dịch nội dung'.")

#     # Bước 1: Thực hiện các thao tác trước khi kiểm tra
#     new_article_type.perform_tag_operations()
#     time.sleep(1)

#     # Bước 2: Click vào nút "Tạo mới" để đảm bảo đang ở đúng trang
#     new_article_type.click_new_article_type_button()
#     time.sleep(1)
#     test_logger.info("Đã nhấn vào nút 'Tạo mới'.")

#     # Bước 3: Click vào tab "English"
#     result_tab_english = new_article_type.click_tab_english()
#     assert result_tab_english, "Không thể nhấn vào tab 'English'."
#     test_logger.info("Đã nhấn vào tab 'English'.")

#     # Bước 4: Kiểm tra xem nút "Dịch nội dung" có xuất hiện không
#     is_translate_visible = is_displayed_new_article_type.is_translate_button_displayed()
#     assert is_translate_visible, "Nút 'Dịch nội dung' không xuất hiện!"
#     test_logger.info("Nút 'Dịch nội dung' xuất hiện đúng.")

#     # Kết quả mong đợi
#     expected_result = "Tab 'English' hoạt động và nút 'Dịch nội dung' hiển thị đúng."
#     actual_result = expected_result if is_translate_visible else "Nút 'Dịch nội dung' không hiển thị."

#     # Kiểm tra kết quả
#     if is_translate_visible:
#         test_logger.info(f"Test Case 5 PASS: test_click_tab_english_and_check_translate_button | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 5 FAIL: test_click_tab_english_and_check_translate_button | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 6: Click tab 'Tieng Viet'
# def test_click_tabs_english_vietnamese_and_check_labels(new_article_type, is_displayed_new_article_type):
#     test_logger.info("Bắt đầu Test Case 6: Kiểm tra tab 'Tiếng Việt'.")

#     new_article_type.perform_tag_operations()
#     time.sleep(1)

#     # Click "Tạo mới" để đảm bảo đang ở đúng trang
#     new_article_type.click_new_article_type_button()
#     time.sleep(1)

#     # **Bước 1**: Click vào tab "Tiếng Anh"
#     result_tab_english = new_article_type.click_tab_english()
#     assert result_tab_english, "Không thể nhấn vào tab 'Tiếng Anh'."
#     test_logger.info("Đã nhấn vào tab 'Tiếng Anh'.")

#     # **Bước 2**: Kiểm tra nút "Dịch nội dung"
#     translate_button_displayed = is_displayed_new_article_type.is_translate_button_displayed()
#     assert translate_button_displayed, "Nút 'Dịch nội dung' không xuất hiện!"
#     test_logger.info("Nút 'Dịch nội dung' hiển thị đúng.")

#     # **Bước 3**: Click vào tab "Tiếng Việt"
#     result_tab_vietnamese = new_article_type.click_tab_tieng_viet()
#     assert result_tab_vietnamese, "Không thể nhấn vào tab 'Tiếng Việt'."
#     test_logger.info("Đã nhấn vào tab 'Tiếng Việt'.")

#     # **Bước 4**: Kiểm tra nhãn "Loại bài viết*"
#     label_article_correct = is_displayed_new_article_type.is_label_article_type_correct()
#     assert label_article_correct, "Tab 'Tiếng Việt' không hiển thị đúng!"
#     test_logger.info("Tab 'Tiếng Việt' hiển thị đúng.")

#     # Kết quả mong đợi
#     expected_result = "Tab 'Tiếng Việt' hoạt động đúng."
#     actual_result = expected_result if (translate_button_displayed and label_article_correct) else "Một trong các bước kiểm tra không đạt yêu cầu."

#     # Kiểm tra kết quả
#     if translate_button_displayed and label_article_correct:
#         test_logger.info(f"Test Case 6 PASS: test_click_tabs_english_vietnamese_and_check_labels | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 6 FAIL: test_click_tabs_english_vietnamese_and_check_labels | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 7: Click nut 'Luu' khi chua nhap Loai bai viet
# def test_click_save_and_check_error_message(new_article_type, is_displayed_new_article_type):
#     test_logger.info("Bắt đầu Test Case 7: Click 'Tạo Mới' -> Click 'Lưu' -> Kiểm tra lỗi 'Vui lòng nhập loại bài viết'.")

#     new_article_type.perform_tag_operations()
#     time.sleep(1)

#     # Click "Tạo mới" để đảm bảo đang ở đúng trang
#     new_article_type.click_new_article_type_button()
#     time.sleep(1)

#     # **Bước 1**: Nhấn nút "Lưu" mà không nhập dữ liệu
#     new_article_type.click_save_button()
#     time.sleep(1)
#     test_logger.info("Đã nhấn vào nút 'Lưu' mà không nhập dữ liệu.")

#     # **Bước 2**: Kiểm tra thông báo lỗi "Vui lòng nhập loại bài viết"
#     error_message_displayed = is_displayed_new_article_type.is_please_field_type_article_displayed()
#     assert error_message_displayed, "Thông báo lỗi 'Vui lòng nhập loại bài viết' không xuất hiện!"
    
#     test_logger.info("Thông báo lỗi 'Vui lòng nhập loại bài viết' đã xuất hiện như mong đợi.")

#     # Kết quả mong đợi
#     expected_result = "Thông báo lỗi 'Vui lòng nhập loại bài viết' xuất hiện đúng."
#     actual_result = expected_result if error_message_displayed else "Thông báo lỗi không xuất hiện."

#     # Kiểm tra kết quả
#     if error_message_displayed:
#         test_logger.info(f"Test Case 7 PASS: test_click_save_and_check_error_message | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 7 FAIL: test_click_save_and_check_error_message | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 8: Click nút "Lưu và Tiếp Tục Cập Nhật" khi chưa nhập Loại bài viết
# def test_click_save_and_continue_and_check_error_message(new_article_type, is_displayed_new_article_type):
#     test_logger.info("Bắt đầu Test Case 8: Click 'Tạo Mới' -> Click 'Lưu và Tiếp Tục Cập Nhật' -> Kiểm tra lỗi 'Vui lòng nhập loại bài viết'.")

#     new_article_type.perform_tag_operations()
#     time.sleep(1)

#     # Click "Tạo mới" để đảm bảo đang ở đúng trang
#     new_article_type.click_new_article_type_button()
#     time.sleep(1)

#     # **Bước 1**: Nhấn nút "Lưu và Tiếp Tục Cập Nhật" mà không nhập dữ liệu
#     new_article_type.click_save_and_continue_button()
#     time.sleep(1)
#     test_logger.info("Đã nhấn vào nút 'Lưu và Tiếp Tục Cập Nhật' mà không nhập dữ liệu.")

#     # **Bước 2**: Kiểm tra thông báo lỗi "Vui lòng nhập loại bài viết"
#     error_message_displayed = is_displayed_new_article_type.is_please_field_type_article_displayed()
#     assert error_message_displayed, "Thông báo lỗi 'Vui lòng nhập loại bài viết' không xuất hiện!"

#     test_logger.info("Thông báo lỗi 'Vui lòng nhập loại bài viết' đã xuất hiện như mong đợi.")

#     # Kết quả mong đợi
#     expected_result = "Thông báo lỗi 'Vui lòng nhập loại bài viết' xuất hiện đúng."
#     actual_result = expected_result if error_message_displayed else "Thông báo lỗi không xuất hiện."

#     # Kiểm tra kết quả
#     if error_message_displayed:
#         test_logger.info(f"Test Case 8 PASS: test_click_save_and_continue_and_check_error_message | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 8 FAIL: test_click_save_and_continue_and_check_error_message | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test case 9: Click nut 'Luu' khi khong nhap loai bai viet o tab 'English'
# def test_translate_and_save_without_article_type(new_article_type, is_displayed_new_article_type):
#     test_logger.info("Bắt đầu Test Case 9.")

#     new_article_type.perform_tag_operations()
#     time.sleep(1)

#     # **Bước 1**: Click "Tạo mới"
#     new_article_type.click_new_article_type_button()
#     time.sleep(1)

#     # **Bước 2**: Chuyển sang tab tiếng Anh
#     new_article_type.click_tab_english()
#     time.sleep(1)
#     test_logger.info("Đã chuyển sang tab tiếng Anh.")

#     # **Bước 3**: Click nút "Dịch nội dung"
#     new_article_type.click_translate_button()
#     time.sleep(1)
#     test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")

#     # **Bước 4**: Click nút "Lưu" mà không nhập loại bài viết
#     new_article_type.click_save_button()
#     time.sleep(1)
#     test_logger.info("Đã nhấn vào nút 'Lưu' mà không nhập loại bài viết.")

#     # **Bước 5**: Kiểm tra thông báo lỗi "Vui lòng nhập loại bài viết"
#     error_message_displayed = is_displayed_new_article_type.is_please_field_type_article_displayed()
#     assert error_message_displayed, "Thông báo lỗi 'Vui lòng nhập loại bài viết' không xuất hiện!"

#     test_logger.info("Thông báo lỗi 'Vui lòng nhập loại bài viết' đã xuất hiện như mong đợi.")

#     # **Kết quả mong đợi**
#     expected_result = "Thông báo lỗi 'Vui lòng nhập loại bài viết' xuất hiện đúng."
#     actual_result = expected_result if error_message_displayed else "Thông báo lỗi không xuất hiện."

#     # **Kiểm tra kết quả**
#     if error_message_displayed:
#         test_logger.info(f"Test Case 9 PASS: test_translate_and_save_without_article_type | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 9 FAIL: test_translate_and_save_without_article_type | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 10: Click nut 'Luu va tiep tuc cap nhat' o tab 'English' khi chua nhap loai bai viet
# def test_translate_and_save_continue_without_article_type(new_article_type, is_displayed_new_article_type):
#     test_logger.info("Bắt đầu Test Case 10: Tạo mới -> Click tab tiếng Anh -> Click 'Dịch nội dung' -> Click 'Lưu và Tiếp tục cập nhật' -> Kiểm tra lỗi.")

#     new_article_type.perform_tag_operations()
#     time.sleep(1)

#     # **Bước 1**: Click "Tạo mới"
#     new_article_type.click_new_article_type_button()
#     time.sleep(1)

#     # **Bước 2**: Chuyển sang tab tiếng Anh
#     new_article_type.click_tab_english()
#     time.sleep(1)
#     test_logger.info("Đã chuyển sang tab tiếng Anh.")

#     # **Bước 3**: Click nút "Dịch nội dung"
#     new_article_type.click_translate_button()
#     time.sleep(1)
#     test_logger.info("Đã nhấn vào nút 'Dịch nội dung'.")

#     # **Bước 4**: Click nút "Lưu và Tiếp tục cập nhật" mà không nhập loại bài viết
#     new_article_type.click_save_and_continue_button()
#     time.sleep(1)
#     test_logger.info("Đã nhấn vào nút 'Lưu và Tiếp tục cập nhật' mà không nhập loại bài viết.")

#     # **Bước 5**: Kiểm tra thông báo lỗi "Vui lòng nhập loại bài viết"
#     error_message_displayed = is_displayed_new_article_type.is_please_field_type_article_displayed()
#     assert error_message_displayed, "Thông báo lỗi 'Vui lòng nhập loại bài viết' không xuất hiện!"

#     test_logger.info("Thông báo lỗi 'Vui lòng nhập loại bài viết' đã xuất hiện như mong đợi.")

#     # **Kết quả mong đợi**
#     expected_result = "Thông báo lỗi 'Vui lòng nhập loại bài viết' xuất hiện đúng."
#     actual_result = expected_result if error_message_displayed else "Thông báo lỗi không xuất hiện."

#     # **Kiểm tra kết quả**
#     if error_message_displayed:
#         test_logger.info(f"Test Case 10 PASS: test_translate_and_save_continue_without_article_type | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 10 FAIL: test_translate_and_save_continue_without_article_type | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 11: Nhập loại bài viết o tab 'Tiếng Việt'
# def test_enter_vi_article_type_and_verify(new_article_type, enter_field_new_article_type, get_field_new_article_type):
#     test_logger.info("Bắt đầu Test Case 11: Nhập loại bài viết tiếng Việt -> Kiểm tra dữ liệu.")

#     new_article_type.perform_tag_operations()
#     time.sleep(1)

#     # **Bước 1**: Click "Tạo mới" để vào trang nhập liệu
#     new_article_type.click_new_article_type_button()
#     time.sleep(1)

#     # **Bước 2**: Nhập loại bài viết vào ô tiếng Việt
#     expected_text = "Bài viết thử nghiệm"
#     enter_field_new_article_type.enter_vi_article_type(expected_text)
#     time.sleep(1)

#     # **Bước 3**: Lấy giá trị đã nhập để kiểm tra
#     actual_text = get_field_new_article_type.get_vi_article_type_value()

#    # **Kết quả mong đợi**
#     expected_result = f"Giá trị '{expected_text}' hiển thị đúng trong ô nhập liệu."
#     actual_result = expected_result if actual_text == expected_text else f"Giá trị hiển thị không đúng: '{actual_text}'"

#     # **Kiểm tra kết quả**
#     if actual_text == expected_text:
#         test_logger.info(f"Test Case 11 PASS: test_enter_vi_article_type_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 11 FAIL: test_enter_vi_article_type_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 12: Nhập đường dẫn o tab 'Tiếng Việt'     
# def test_enter_vi_article_link_and_verify(new_article_type,  enter_field_new_article_type, get_field_new_article_type):
#     test_logger.info("Bắt đầu Test Case 12: Nhập đường dẫn tiếng Việt -> Kiểm tra dữ liệu.")

#     new_article_type.perform_tag_operations()
#     time.sleep(1)

#     # **Bước 1**: Click "Tạo mới" để vào trang nhập liệu
#     new_article_type.click_new_article_type_button()
#     time.sleep(1)

#     # **Bước 2**: Nhập đường dẫn vào ô tiếng Việt
#     expected_link = "bai-viet-thu-nghiem"
#     enter_field_new_article_type.enter_vi_article_link(expected_link)
#     time.sleep(1)

#     # **Bước 3**: Lấy giá trị đã nhập để kiểm tra
#     actual_link = get_field_new_article_type.get_vi_article_link_value()

#     # **Kết quả mong đợi**
#     expected_result = f"Giá trị '{expected_link}' hiển thị đúng trong ô nhập liệu."
#     actual_result = expected_result if actual_link == expected_link else f"Giá trị hiển thị không đúng: '{actual_link}'"

#     # **Kiểm tra kết quả**
#     if actual_link == expected_link:
#         test_logger.info(f"Test Case 12 PASS: test_enter_vi_article_link_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 12 FAIL: test_enter_vi_article_link_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 13: Nhập 'Từ khóa meta' o tab 'Tiếng Việt'
# def test_enter_vi_meta_keyword_and_verify(new_article_type, enter_field_new_article_type, get_field_new_article_type):
#     test_logger.info("Bắt đầu Test Case 13: Nhập 'Từ khóa meta' tiếng Việt -> Kiểm tra dữ liệu.")

#     new_article_type.perform_tag_operations()
#     time.sleep(1)

#     # **Bước 1**: Click "Tạo mới" để vào trang nhập liệu
#     new_article_type.click_new_article_type_button()
#     time.sleep(1)

#     # **Bước 2**: Nhập "Từ khóa meta" vào ô tiếng Việt
#     expected_keyword = "tin-tuc, cong-nghe, review"
#     enter_field_new_article_type.enter_vi_meta_keyword(expected_keyword)
#     time.sleep(1)

#     # **Bước 3**: Lấy giá trị đã nhập để kiểm tra
#     actual_keyword = get_field_new_article_type.get_vi_meta_keyword_value()

#     # **Kết quả mong đợi**
#     expected_result = f"Giá trị '{expected_keyword}' hiển thị đúng trong ô nhập liệu."
#     actual_result = expected_result if actual_keyword == expected_keyword else f"Giá trị hiển thị không đúng: '{actual_keyword}'"

#     # **Kiểm tra kết quả**
#     if actual_keyword == expected_keyword:
#         test_logger.info(f"Test Case 13 PASS: test_enter_vi_meta_keyword_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 13 FAIL: test_enter_vi_meta_keyword_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 14: Nhập 'Mô tả' o tab 'Tiếng Việt'
# def test_enter_vi_description_and_verify(new_article_type, enter_field_new_article_type, get_field_new_article_type):
#     test_logger.info("Bắt đầu Test Case 14: Nhập 'Mô tả' tiếng Việt -> Kiểm tra dữ liệu.")

#     new_article_type.perform_tag_operations()
#     time.sleep(1)

#     # **Bước 1**: Click "Tạo mới" để vào trang nhập liệu
#     new_article_type.click_new_article_type_button()
#     time.sleep(1)

#     # **Bước 2**: Nhập nội dung vào ô "Mô tả" tiếng Việt
#     expected_description = "Đây là mô tả thử nghiệm cho bài viết mới."
#     enter_field_new_article_type.enter_vi_description(expected_description)
#     time.sleep(1)

#     # **Bước 3**: Lấy giá trị đã nhập để kiểm tra
#     actual_description = get_field_new_article_type.get_vi_description_value()

#     # **Kết quả mong đợi**
#     expected_result = f"Giá trị '{expected_description}' hiển thị đúng trong ô nhập liệu."
#     actual_result = expected_result if actual_description == expected_description else f"Giá trị hiển thị không đúng: '{actual_description}'"

#     # **Kiểm tra kết quả**
#     if actual_description == expected_description:
#         test_logger.info(f"Test Case 14 PASS: test_enter_vi_description_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 14 FAIL: test_enter_vi_description_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 15: Nhập 'Mô tả Meta' o tab 'Tiếng Việt'
# def test_enter_vi_meta_description_and_verify(new_article_type, enter_field_new_article_type, get_field_new_article_type):
#     test_logger.info("Bắt đầu Test Case 15: Nhập 'Meta Description' tiếng Việt -> Kiểm tra dữ liệu.")

#     new_article_type.perform_tag_operations()
#     time.sleep(1)

#     # **Bước 1**: Click "Tạo mới" để vào trang nhập liệu
#     new_article_type.click_new_article_type_button()
#     time.sleep(1)

#     # **Bước 2**: Nhập nội dung vào ô "Meta Description" tiếng Việt
#     expected_meta_description = "Đây là Meta Description thử nghiệm."
#     enter_field_new_article_type.enter_vi_meta_description(expected_meta_description)
#     time.sleep(1)

#     # **Bước 3**: Lấy giá trị đã nhập để kiểm tra
#     actual_meta_description = get_field_new_article_type.get_vi_meta_description_value()

#     # **Kết quả mong đợi**
#     expected_result = f"Giá trị '{expected_meta_description}' hiển thị đúng trong ô nhập liệu."
#     actual_result = expected_result if actual_meta_description == expected_meta_description else f"Giá trị hiển thị không đúng: '{actual_meta_description}'"

#     # **Kiểm tra kết quả**
#     if actual_meta_description == expected_meta_description:
#         test_logger.info(f"Test Case 15 PASS: test_enter_vi_meta_description_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 15 FAIL: test_enter_vi_meta_description_and_verify | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test case 16: Click field 'Upload image'
# def test_click_meta_image_and_check_popup(new_article_type, meta_image_new_article_type, is_displayed_new_article_type):
#     test_logger.info("Bắt đầu Test Case 16: Click vào hình ảnh -> Kiểm tra popup tải lên ảnh xuất hiện.")

#     new_article_type.perform_tag_operations()
#     time.sleep(1)

#     # **Bước 1**: Click "Tạo mới" để vào trang nhập liệu
#     new_article_type.click_new_article_type_button()
#     time.sleep(1)

#     # **Bước 2**: Click vào trường hình ảnh (sử dụng hàm `click_vi_meta_image`)
#     meta_image_new_article_type.click_meta_image()
#     time.sleep(1)
#     test_logger.info("Đã click vào hình ảnh để mở popup tải lên.")

#     # **Bước 3**: Kiểm tra popup có xuất hiện không
#     popup_displayed = is_displayed_new_article_type.is_popup_upload_image_displayed()

#     # **Kết quả mong đợi**
#     expected_result = "Popup tải lên ảnh hiển thị đúng."
#     actual_result = expected_result if popup_displayed else "Popup tải lên ảnh không xuất hiện."

#     # **Kiểm tra kết quả**
#     if popup_displayed:
#         test_logger.info(f"Test Case 16 PASS: test_click_vi_meta_image_and_check_popup | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 16 FAIL: test_click_vi_meta_image_and_check_popup | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test case 17: Click field 'Upload image'
# def test_click_upload_image_and_check_popup(new_article_type, meta_image_new_article_type, is_displayed_new_article_type):
#     test_logger.info("Bắt đầu Test Case 17: Click vào hình ảnh -> Kiểm tra popup tải lên ảnh xuất hiện.")

#     new_article_type.perform_tag_operations()
#     time.sleep(1)

#     # **Bước 1**: Click "Tạo mới" để vào trang nhập liệu
#     new_article_type.click_new_article_type_button()
#     time.sleep(1)

#     # **Bước 2**: Click vào trường hình ảnh (sử dụng hàm `click_vi_meta_image`)
#     meta_image_new_article_type.click_button_upload_image()
#     time.sleep(1)

#     # **Bước 3**: Kiểm tra popup có xuất hiện không
#     popup_displayed = is_displayed_new_article_type.is_popup_upload_image_displayed()

#     # **Kết quả mong đợi**
#     expected_result = "Popup tải lên ảnh hiển thị đúng."
#     actual_result = expected_result if popup_displayed else "Popup tải lên ảnh không xuất hiện."

#     # **Kiểm tra kết quả**
#     if popup_displayed:
#         test_logger.info(f"Test Case 17 PASS: test_click_vi_meta_image_and_check_popup | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 17 FAIL: test_click_vi_meta_image_and_check_popup | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"
    
# # Test Case 18: Upload ảnh và kiểm tra ảnh có hiển thị không
# def test_upload_image_and_check_display(new_article_type, meta_image_new_article_type, is_displayed_new_article_type):
#     test_logger.info("Bắt đầu Test Case 18: Click tab Browser -> Chọn ảnh -> Click Upload -> Kiểm tra ảnh hiển thị.")

#     new_article_type.perform_tag_operations()
#     time.sleep(1)

#     # **Bước 1**: Click "Tạo mới" để vào trang nhập liệu
#     new_article_type.click_new_article_type_button()
#     time.sleep(1)

#     # **Bước 2**: Click vào trường hình ảnh
#     meta_image_new_article_type.click_button_upload_image()
#     time.sleep(1)

#     # **Bước 3**: Kiểm tra popup có xuất hiện không
#     popup_displayed = is_displayed_new_article_type.is_popup_upload_image_displayed()
#     assert popup_displayed, "Popup tải lên ảnh không xuất hiện!"

#     # **Bước 4**: Click tab "Browser"
#     meta_image_new_article_type.click_tab_browser()
#     time.sleep(1)

#     # **Bước 5**: Chọn ảnh đầu tiên
#     meta_image_new_article_type.click_first_image()
#     time.sleep(1)

#     # **Bước 6**: Click nút "Upload"
#     meta_image_new_article_type.click_button_upload()
#     time.sleep(2)  # Đợi ảnh tải lên

#     # **Bước 7**: Kiểm tra ảnh đã hiển thị
#     image_displayed = is_displayed_new_article_type.is_uploaded_image_displayed()
    
#     # **Kết quả mong đợi**
#     expected_result = "Ảnh hiển thị đúng sau khi tải lên."
#     actual_result = expected_result if image_displayed else "Ảnh không hiển thị sau khi tải lên."

#     # **Kiểm tra kết quả**
#     if image_displayed:
#         test_logger.info(f"Test Case 18 PASS: test_upload_image_and_check_display | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 18 FAIL: test_upload_image_and_check_display | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test case 19: Kiểm tra trạng thái nút 'Xóa ảnh' trước và sau khi tải ảnh, sau do click nut xoa anh
# def test_check_delete_button_before_and_after_upload(new_article_type, meta_image_new_article_type, is_displayed_new_article_type):
#     test_logger.info("Bắt đầu Test Case 19: Kiểm tra trạng thái nút 'Xóa ảnh' trước và sau khi tải ảnh, sau đó click nút xóa ảnh.")

#     new_article_type.perform_tag_operations()
#     time.sleep(1)
#     new_article_type.click_new_article_type_button()
#     time.sleep(1)

#     # **Bước 1**: Click vào trường hình ảnh
#     meta_image_new_article_type.click_button_upload_image()

#     # **Bước 2**: Kiểm tra popup có xuất hiện không
#     popup_displayed = is_displayed_new_article_type.is_popup_upload_image_displayed()
#     assert popup_displayed, "Popup tải lên ảnh không xuất hiện!"

#     # **Bước 3**: Click tab "Browser"
#     meta_image_new_article_type.click_tab_browser()

#     # **Bước 4**: Chọn ảnh đầu tiên
#     meta_image_new_article_type.click_first_image()

#     # **Bước 5**: Click nút "Upload"
#     meta_image_new_article_type.click_button_upload()

#     # **Bước 6**: Kiểm tra nút 'Xóa ảnh' sau khi upload
#     is_displayed_new_article_type.is_delete_image_button_displayed()

#     # **Bước 7**: Click nút 'Xóa ảnh'
#     meta_image_new_article_type.click_button_delete_image()

#     # **Bước 8**: Kiểm tra nút 'Xóa ảnh' sau khi xóa ảnh
#     delete_button_after_delete = not is_displayed_new_article_type.is_delete_image_button_displayed()

#     # **Bước 9**: Kiểm tra kết quả
#     expected_result = "Nút 'Xóa ảnh' ẩn đi sau khi xóa ảnh."
#     actual_result = expected_result if delete_button_after_delete else "LỖI: Nút 'Xóa ảnh' chưa ẩn đi sau khi xóa ảnh!"

#     if delete_button_after_delete:
#         test_logger.info(f"Test Case 19 PASS: test_check_delete_button_before_and_after_upload | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 19 FAIL: test_check_delete_button_before_and_after_upload | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"


# # Test Case 20: Không chọn ảnh và click 'Upload', kiểm tra nút 'Xóa ảnh
# def test_upload_without_selecting_image(new_article_type, meta_image_new_article_type, is_displayed_new_article_type):
#     test_logger.info("Bắt đầu Test Case 20: Không chọn ảnh và click 'Upload', kiểm tra nút 'Xóa ảnh'.")

#     new_article_type.perform_tag_operations()
#     time.sleep(1)
#     new_article_type.click_new_article_type_button()
#     time.sleep(1)

#     # **Bước 1**: Click vào trường hình ảnh
#     meta_image_new_article_type.click_button_upload_image()

#     # **Bước 2**: Kiểm tra popup có xuất hiện không
#     popup_displayed = is_displayed_new_article_type.is_popup_upload_image_displayed()
#     assert popup_displayed, "Popup tải lên ảnh không xuất hiện!"

#     # **Bước 3**: Click nút 'Upload' mà không chọn ảnh
#     meta_image_new_article_type.click_button_upload()

#     # **Bước 4**: Kiểm tra nút 'Xóa ảnh' sau khi click 'Upload'
#     delete_button_after_upload = not is_displayed_new_article_type.is_delete_image_button_displayed()

#     # **Bước 5**: Kiểm tra kết quả
#     expected_result = "Nút 'Xóa ảnh' không xuất hiện sau khi click 'Upload' mà không chọn ảnh."
#     actual_result = expected_result if delete_button_after_upload else "Nút 'Xóa ảnh' xuất hiện sau khi click 'Upload' mà không chọn ảnh."

#     if delete_button_after_upload:
#         test_logger.info(f"Test Case 20 PASS: test_upload_without_selecting_image | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 20 FAIL: test_upload_without_selecting_image | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"


# def test_vi_article_type_255_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
#     test_logger.info("Bắt đầu Test Case 21: Nhập 255 ký tự vào ô 'Loại bài viết' (Tiếng Việt) và kiểm tra thông báo lỗi.")

#     new_article_type.perform_tag_operations()
#     time.sleep(1)
    
#     # **Bước 1**: Click "Tạo mới" để vào trang nhập liệu
#     new_article_type.click_new_article_type_button()
#     time.sleep(1)

#     # **Bước 2**: Nhập 255 ký tự vào ô 'Loại bài viết' (Tiếng Việt)
#     long_text = "A" * 255  # Tạo chuỗi 255 ký tự
#     enter_field_new_article_type.enter_vi_article_type(long_text)
#     time.sleep(2)

#     # **Bước 3**: Kiểm tra xem thông báo lỗi có xuất hiện không
#     error_displayed = validation_new_article_type.is_max_type_error_displayed()

#     # **Bước 4**: Kiểm tra kết quả
#     expected_result = "Thông báo lỗi xuất hiện: 'Vui lòng nhập Loại bài viết không quá 254 ký tự'."
#     actual_result = expected_result if error_displayed else "Thông báo lỗi không xuất hiện!"

#     if error_displayed:
#         test_logger.info(f"Test Case 21 PASS: test_vi_article_type_255_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 21 FAIL: test_vi_article_type_255_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 22: Nhập dữ liệu vào ô 'Loại bài viết' (Tiếng Việt) và sau đó xóa, kiểm tra thông báo lỗi.
# def test_vi_article_type_clear_and_check_error(new_article_type, enter_field_new_article_type, validation_new_article_type):
#     test_logger.info("Bắt đầu Test Case 22: Nhập dữ liệu vào ô 'Loại bài viết' (Tiếng Việt) và sau đó xóa, kiểm tra thông báo lỗi.")

#     new_article_type.perform_tag_operations()
#     time.sleep(1)
    
#     # **Bước 1**: Click "Tạo mới" để vào trang nhập liệu
#     new_article_type.click_new_article_type_button()
#     time.sleep(1)

#     # **Bước 4**: Nhập nội dung vào ô 'Loại bài viết'
#     test_text = "Bài viết test"
#     enter_field_new_article_type.enter_vi_article_type(test_text)
#     time.sleep(1)

#     # **Bước 5**: Xóa nội dung đã nhập bằng hàm mới
#     enter_field_new_article_type.clear_vi_article_type()
#     time.sleep(2)

#     # **Bước 6**: Kiểm tra xem thông báo lỗi có xuất hiện không
#     error_displayed = validation_new_article_type.is_field_error_displayed()

#     # **Bước 7**: Kiểm tra kết quả
#     expected_result = "Thông báo lỗi xuất hiện: 'Trường này không được để trống'."
#     actual_result = expected_result if error_displayed else "Thông báo lỗi không xuất hiện!"

#     if error_displayed:
#         test_logger.info(f"Test Case 22 PASS: test_vi_article_type_clear_and_check_error | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 22 FAIL: test_vi_article_type_clear_and_check_error | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test case Test Case 22: Nhập 255 ký tự vào ô 'Duong dan' (Tiếng Việt)
# def test_vi_article_link_255_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
#     test_logger.info("Bắt đầu Test Case 22: Nhập 255 ký tự vào ô 'Duong dan' (Tiếng Việt) và kiểm tra thông báo lỗi.")

#     new_article_type.perform_tag_operations()
#     time.sleep(1)
#     new_article_type.click_new_article_type_button()
#     time.sleep(1)

#     # **Bước 1**: Nhập 255 ký tự vào ô 'Liên kết bài viết' (Tiếng Việt)
#     long_text = "A" * 255
#     enter_field_new_article_type.enter_vi_article_link(long_text)
#     time.sleep(2)

#     # **Bước 2**: Kiểm tra xem thông báo lỗi có xuất hiện không
#     error_displayed = validation_new_article_type.is_max_link_error_displayed()

#     # **Kiểm tra kết quả**
#     expected_result = "Thông báo lỗi xuất hiện: 'Vui lòng nhập Duong dan không quá 254 ký tự'."
#     actual_result = expected_result if error_displayed else "Thông báo lỗi không xuất hiện!"

#     if error_displayed:
#         test_logger.info(f"Test Case 22 PASS: test_vi_article_link_255_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 22 FAIL: test_vi_article_link_255_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 23: Nhập 255 ký tự vào ô 'Mô tả ngắn' (Tiếng Việt)
# def test_vi_short_description_255_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
#     test_logger.info("Bắt đầu Test Case 23: Nhập 255 ký tự vào ô 'Mô tả ngắn' (Tiếng Việt) và kiểm tra thông báo lỗi.")

#     new_article_type.perform_tag_operations()
#     time.sleep(1)
#     new_article_type.click_new_article_type_button()
#     time.sleep(1)

#     # **Bước 1**: Nhập 255 ký tự vào ô 'Mô tả ngắn' (Tiếng Việt)
#     long_text = "A" * 255
#     enter_field_new_article_type.enter_vi_description(long_text)
#     time.sleep(2)

#     # **Bước 2**: Kiểm tra xem thông báo lỗi có xuất hiện không
#     error_displayed = validation_new_article_type.is_max_short_description_error_displayed()

#     # **Kiểm tra kết quả**
#     expected_result = "Thông báo lỗi xuất hiện: 'Vui lòng nhập Mô tả ngắn không quá 254 ký tự'."
#     actual_result = expected_result if error_displayed else "Thông báo lỗi không xuất hiện!"

#     if error_displayed:
#         test_logger.info(f"Test Case 23 PASS: test_vi_short_description_255_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 23 FAIL: test_vi_short_description_255_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test case 24: Nhập 101 ký tự vào ô 'Meta Keyword' (Tiếng Việt)
# def test_vi_meta_keyword_101_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
#     test_logger.info("Bắt đầu Test Case 24: Nhập 101 ký tự vào ô 'Meta Keyword' (Tiếng Việt) và kiểm tra thông báo lỗi.")

#     new_article_type.perform_tag_operations()
#     time.sleep(1)
#     new_article_type.click_new_article_type_button()
#     time.sleep(1)

#     # **Bước 1**: Nhập 101 ký tự vào ô 'Meta Keyword' (Tiếng Việt)
#     long_text = "A" * 101
#     enter_field_new_article_type.enter_vi_meta_keyword(long_text)
#     time.sleep(2)

#     # **Bước 2**: Kiểm tra xem thông báo lỗi có xuất hiện không
#     error_displayed = validation_new_article_type.is_meta_keyword_error_displayed()

#     # **Kiểm tra kết quả**
#     expected_result = "Thông báo lỗi xuất hiện: 'Vui lòng nhập Meta Keyword không quá 100 ký tự'."
#     actual_result = expected_result if error_displayed else "Thông báo lỗi không xuất hiện!"

#     if error_displayed:
#         test_logger.info(f"Test Case 24 PASS: test_vi_meta_keyword_101_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 24 FAIL: test_vi_meta_keyword_101_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# def test_vi_meta_description_501_chars(new_article_type, enter_field_new_article_type, validation_new_article_type):
#     test_logger.info("Bắt đầu Test Case 25: Nhập 501 ký tự vào ô 'Meta Description' (Tiếng Việt) và kiểm tra thông báo lỗi.")

#     new_article_type.perform_tag_operations()
#     time.sleep(1)
#     new_article_type.click_new_article_type_button()
#     time.sleep(1)

#     # **Bước 1**: Nhập 501 ký tự vào ô 'Meta Description' (Tiếng Việt)
#     long_text = "A" * 501
#     enter_field_new_article_type.enter_vi_meta_description(long_text)
#     time.sleep(2)

#     # **Bước 2**: Kiểm tra xem thông báo lỗi có xuất hiện không
#     error_displayed = validation_new_article_type.is_meta_description_error_displayed()

#     # **Kiểm tra kết quả**
#     expected_result = "Thông báo lỗi xuất hiện: 'Vui lòng nhập Meta Description không quá 300 ký tự'."
#     actual_result = expected_result if error_displayed else "Thông báo lỗi không xuất hiện!"

#     if error_displayed:
#         test_logger.info(f"Test Case 25 PASS: test_vi_meta_description_501_chars | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 25 FAIL: test_vi_meta_description_501_chars | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"
