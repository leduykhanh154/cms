import time
import pytest
from utils.login import Login
from utils.logger import LoggerConfig
from utils.driver_setup import get_driver
from pages.article_type.article_type import ArticleTypeBase
from pages.article_type.enter_field_article_type import EnterFieldArticleType
from pages.article_type.is_displayed_article_type import IsDisplayedArticleType
from pages.article_type.popup_article_type import PopupArticleType
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
def article_type(setup_driver):
    return ArticleTypeBase(setup_driver)

@pytest.fixture
def enter_field_article_type(setup_driver):
    return EnterFieldArticleType(setup_driver)

@pytest.fixture
def is_displayed_article_type(setup_driver):
    return IsDisplayedArticleType(setup_driver)

@pytest.fixture
def popup_article_type(setup_driver):
    return PopupArticleType(setup_driver)

# Test Case 1: Click 'Trang chủ' trên breadcrumb -> Chuyển hướng về trang chủ.
def test_click_breadcrumb_home(article_type):
    test_logger.info("Bắt đầu Test Case 1: Verify khi nhấn vào breadcrumb 'Trang chủ' -> Hệ thống điều hướng về trang chủ thành công.")
    article_type.perform_tag_operations()
    result = article_type.click_breadcrumb_home()
    expected_result = "Hệ thống điều hướng thành công đến trang 'Trang chủ'."
    actual_result = expected_result if result else "Hệ thống không điều hướng đến trang 'Trang chủ'."
    if result:
        test_logger.info(f"Test Case 1 PASS: test_click_breadcrumb_home | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 1 FAIL: test_click_breadcrumb_home | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 2: Click "Tạo mới loại bài viết" -> Chuyển hướng về trang tạo mới.
def test_click_create_new_article_type(article_type):
    test_logger.info("Bắt đầu Test Case 2: Verify khi nhấn vào nút 'Tạo mới loại bài viết' -> Hệ thống điều hướng về trang tạo mới thành công.")
    article_type.perform_tag_operations()
    time.sleep(1)
    result = article_type.click_new_article_type_button()
    expected_result = "Hệ thống điều hướng thành công đến trang 'Tạo mới loại bài viết'."
    actual_result = expected_result if result else "Hệ thống không điều hướng đến trang 'Tạo mới loại bài viết'."
    if result:
        test_logger.info(f"Test Case 2 PASS: test_click_create_new_article_type | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 2 FAIL: test_click_create_new_article_type | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 3: Click dropdown 'Trang thai'
def test_click_status_dropdown(article_type):
    test_logger.info("Bắt đầu Test Case 3: Verify khi nhấn vào dropdown 'Status'.")
    article_type.perform_tag_operations()
    time.sleep(1)
    result = article_type.click_dropdown_status()
    expected_result = "Dropdown 'Status' được nhấn thành công."
    actual_result = expected_result if result else "Không thể nhấn vào dropdown 'Status'."
    if result:
        test_logger.info(f"Test Case 3 PASS: test_click_status_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 3 FAIL: test_click_status_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 4: Click datepicker 'Tu ngay'
def test_click_datepicker_from(article_type):
    test_logger.info("Bắt đầu Test Case 4: Verify khi nhấn vào Datepicker 'Từ ngày'.")
    article_type.perform_tag_operations()
    time.sleep(1)
    result = article_type.click_datepicker_from()
    expected_result = "Datepicker 'Từ ngày' được nhấn thành công."
    actual_result = expected_result if result else "Không thể nhấn vào Datepicker 'Từ ngày'."
    if result:
        test_logger.info(f"Test Case 4 PASS: test_click_datepicker_from | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 4 FAIL: test_click_datepicker_from | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 5: Click vào Datepicker 'Đến ngày'
def test_click_datepicker_to(article_type):
    test_logger.info("Bắt đầu Test Case 5: Verify khi nhấn vào Datepicker 'Đến ngày'.")
    article_type.perform_tag_operations()
    time.sleep(1)
    result = article_type.click_datepicker_to()
    expected_result = "Datepicker 'Đến ngày' được nhấn thành công."
    actual_result = expected_result if result else "Không thể nhấn vào Datepicker 'Đến ngày'."
    if result:
        test_logger.info(f"Test Case 5 PASS: test_click_datepicker_to | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 5 FAIL: test_click_datepicker_to | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 6: Click vào Dropdown 'Loại bai viet cap cha'
def test_click_dropdown_father_type(article_type):
    test_logger.info("Bắt đầu Test Case 6: Verify khi nhấn vào Dropdown 'Loại cha'.")
    article_type.perform_tag_operations()
    time.sleep(1)
    result = article_type.click_dropdown_father_type()
    expected_result = "Dropdown 'Loại cha' được nhấn thành công."
    actual_result = expected_result if result else "Không thể nhấn vào Dropdown 'Loại cha'."
    if result:
        test_logger.info(f"Test Case 6 PASS: test_click_dropdown_father_type | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 6 FAIL: test_click_dropdown_father_type | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 7: Click vào nút 'Reset'
def test_click_reset_button(article_type):
    test_logger.info("Bắt đầu Test Case 7: Verify khi nhấn vào nút 'Tai lai'.")
    article_type.perform_tag_operations()
    time.sleep(1)
    result = article_type.click_reset_button()
    expected_result = "Nút 'Tai lai' được nhấn thành công."
    actual_result = expected_result if result else "Không thể nhấn vào nút 'Tai lai'."
    if result:
        test_logger.info(f"Test Case 7 PASS: test_click_reset_button | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 7 FAIL: test_click_reset_button | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 8: Click vào dropdown phân trang 'Split'
def test_click_pagination_dropdown(article_type):
    test_logger.info("Bắt đầu Test Case 8: Verify khi nhấn vào dropdown 'Phân trang'.")
    article_type.perform_tag_operations()
    time.sleep(1)
    result = article_type.click_pagination_dropdown()
    expected_result = "Dropdown 'Phân trang' được nhấn thành công."
    actual_result = expected_result if result else "Không thể nhấn vào dropdown 'Phân trang' được nhấn thành công."
    if result:
        test_logger.info(f"Test Case 8 PASS: test_click_pagination_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 8 FAIL: test_click_pagination_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 9: Click vào nút 'Thao tác' (Operate Button)
def test_click_operate_button(article_type):
    test_logger.info("Bắt đầu Test Case 9: Verify khi nhấn vào nút 'Thao tác'.")
    article_type.perform_tag_operations()
    time.sleep(1)
    result = article_type.click_operate_button()
    expected_result = "Nút 'Thao tác' được nhấn thành công."
    actual_result = expected_result if result else "Không thể nhấn vào nút 'Thao tác'."
    if result:
        test_logger.info(f"Test Case 9 PASS: test_click_operate_button | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 9 FAIL: test_click_operate_button | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 10: Nhập dữ liệu vào ô tìm kiếm
def test_enter_search_keyword(article_type, enter_field_article_type):
    test_logger.info("Bắt đầu Test Case 10: Verify có thể nhập từ khóa vào ô tìm kiếm.")
    article_type.perform_tag_operations()
    time.sleep(1)
    keyword = "Test Article"
    result = enter_field_article_type.enter_search_keyword(keyword)
    expected_result = f"Đã nhập '{keyword}' vào ô tìm kiếm và thực hiện tìm kiếm."
    actual_result = expected_result if result else "Không thể nhập dữ liệu vào ô tìm kiếm."
    if result:
        test_logger.info(f"Test Case 10 PASS: test_enter_search_keyword | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 10 FAIL: test_enter_search_keyword | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 11: Chọn tất cả mục bằng checkbox "Select All"
def test_click_select_all_checkbox(article_type):
    test_logger.info("Bắt đầu Test Case 11: Verify có thể nhấn vào checkbox 'Select All'.")
    article_type.perform_tag_operations()
    time.sleep(1)
    result = article_type.click_select_all_checkbox()
    expected_result = "Đã nhấn vào checkbox 'Select All'."
    actual_result = expected_result if result else "Không thể nhấn vào checkbox 'Select All'."
    if result:
        test_logger.info(f"Test Case 11 PASS: test_click_select_all_checkbox | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 11 FAIL: test_click_select_all_checkbox | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 12: Chọn mục đầu tiên bằng checkbox "Select First"
def test_click_select_first_checkbox(article_type, is_displayed_article_type):
    test_logger.info("Bắt đầu Test Case 12: Verify có thể nhấn vào checkbox 'Select First'.")
    article_type.perform_tag_operations()
    time.sleep(1)
    result = article_type.click_select_first_checkbox()
    assert result, "Không thể nhấn vào checkbox 'Select First'."
    test_logger.info("Đã nhấn vào checkbox 'Select First'.")
    expected_selected_text = "1"
    selected_correct = is_displayed_article_type.is_selected_line_correct(expected_selected_text)
    assert selected_correct, f"Nội dung '{expected_selected_text}' không hiển thị đúng."
    test_logger.info(f"Hệ thống hiển thị chính xác '{expected_selected_text}'.")
    expected_result = f"Đã chọn mục đầu tiên và hiển thị đúng '{expected_selected_text}'"
    actual_result = expected_result if selected_correct else "Hệ thống không hiển thị đúng"
    if selected_correct:
        test_logger.info(f"Test Case 12 PASS: test_click_select_first_checkbox | Expected: {expected_result} dòng được chọn. | Actual: {actual_result} dòng được chọn. | Status: PASS")
    else:
        test_logger.error(f"Test Case 12 FAIL: test_click_select_first_checkbox | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 13: Nhấn vào liên kết đầu tiên và kiểm tra text trên trang đích
def test_click_first_link(article_type, is_displayed_article_type):
    test_logger.info("Bắt đầu Test Case 13: Kiểm tra liên kết đầu tiên và sự xuất hiện của text trên trang đích.")
    article_type.perform_tag_operations()
    first_link_text = article_type.get_first_link_text()
    assert first_link_text, "Không thể lấy text của liên kết đầu tiên hoặc text rỗng."
    test_logger.info(f"Text của liên kết đầu tiên: '{first_link_text}'.")
    link_result = article_type.click_first_link()
    assert link_result, "Không thể nhấn vào liên kết đầu tiên."
    test_logger.info("Đã nhấn vào liên kết đầu tiên thành công.")
    time.sleep(2) 
    text_found = is_displayed_article_type.is_text_displayed_on_page(first_link_text)
    assert text_found, f"Không tìm thấy '{first_link_text}' trên trang đích."
    test_logger.info(f"Text '{first_link_text}' hiển thị đúng trên trang đích.")
    expected_result = f"Text '{first_link_text}' hiển thị đúng trên trang."
    actual_result = expected_result if text_found else f"Text '{first_link_text}' không hiển thị đúng."
    if text_found:
        test_logger.info(f"Test Case 13 PASS: test_click_first_link | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 13 FAIL: test_click_first_link | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 14: Nhấn vào nút menu đầu tiên
def test_click_first_menu_button(article_type):
    test_logger.info("Bắt đầu Test Case 14: Verify có thể nhấn vào nút menu đầu tiên.")
    article_type.perform_tag_operations()
    time.sleep(1)
    result = article_type.click_first_menu_button()
    expected_result = "Hệ thống đã nhấn vào nút menu đầu tiên thành công."
    actual_result = expected_result if result else "Không thể nhấn vào nút menu đầu tiên."
    if result:
        test_logger.info(f"Test Case PASS 14: test_click_first_menu_button | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case FAIL 14: test_click_first_menu_button | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 15: Click vào nút 'Thao tác' rồi nhấn 'Xóa' khi chua chon loai bai viet
def test_click_operate_and_delete_without_selection(article_type, is_displayed_article_type):
    test_logger.info("Bắt đầu Test Case 15: Nhấn 'Thao tác' -> Nhấn 'Xóa' khi chưa chọn loại bài viết -> Kiểm tra cảnh báo 'Vui lòng chọn Loại bài viết để xóa.'.")
    article_type.perform_tag_operations()
    time.sleep(1)
    operate_result = article_type.click_operate_button()
    assert operate_result, "Không thể nhấn vào nút 'Thao tác'."
    test_logger.info("Đã nhấn vào nút 'Thao tác'.")
    time.sleep(1)
    delete_result = article_type.click_delete_button()
    assert delete_result, "Không thể nhấn vào nút 'Xóa'."
    test_logger.info("Đã nhấn vào nút 'Xóa'.")
    time.sleep(1)
    expected_warning_text = "Vui lòng chọn Loại bài viết để xóa."
    warning_displayed = is_displayed_article_type.is_warning_displayed()
    warning_text_correct = is_displayed_article_type.is_warning_text_correct(expected_warning_text)
    expected_result = f"Hệ thống hiển thị cảnh báo: '{expected_warning_text}'."
    actual_result = "Hệ thống hiển thị đúng cảnh báo." if warning_text_correct else "Cảnh báo không đúng."
    if warning_displayed and warning_text_correct:
        test_logger.info(f"Test Case 15 PASS: test_click_operate_and_delete_without_selection | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 15 FAIL: test_click_operate_and_delete_without_selection | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 16: Click vào nút 'Thao tác' rồi nhấn 'Xóa' khi da chon loai bai viet
def test_select_and_delete_article_type(article_type, is_displayed_article_type):
    test_logger.info("Bắt đầu Test Case 16: Chọn bài viết -> Nhấn 'Thao tác' -> Nhấn 'Xóa' -> Kiểm tra cảnh báo 'Bạn có chắc chắn ?'.")
    article_type.perform_tag_operations()
    time.sleep(1)
    select_result = article_type.click_select_first_checkbox()
    assert select_result, "Không thể chọn bài viết đầu tiên."
    test_logger.info("Đã chọn bài viết đầu tiên thành công.")
    time.sleep(1)
    operate_result = article_type.click_operate_button()
    assert operate_result, "Không thể nhấn vào nút 'Thao tác'."
    test_logger.info("Đã nhấn vào nút 'Thao tác'.")
    time.sleep(1)
    delete_result = article_type.click_delete_button()
    assert delete_result, "Không thể nhấn vào nút 'Xóa'."
    test_logger.info("Đã nhấn vào nút 'Xóa'.")
    time.sleep(1)
    expected_warning_text = "Bạn có chắc chắn ?"
    warning_displayed = is_displayed_article_type.is_warning_displayed()
    warning_text_correct = is_displayed_article_type.is_warning_text_correct(expected_warning_text)
    expected_result = f"Hệ thống hiển thị cảnh báo: '{expected_warning_text}'."
    actual_result = "Hệ thống hiển thị đúng cảnh báo." if warning_text_correct else "Cảnh báo không đúng."
    if warning_displayed and warning_text_correct:
        test_logger.info(f"Test Case 16 PASS: test_select_and_delete_article_type | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 16 FAIL: test_select_and_delete_article_type | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 17: Click icon '...' doc sau do click menu-item 'Chi tiet'
def test_click_menu_and_detail_button(article_type):
    test_logger.info("Bắt đầu Test Case 17: Verify có thể nhấn vào icon '...' rồi chọn menu-item 'Chi tiết'.")
    article_type.perform_tag_operations()
    time.sleep(1)
    menu_result = article_type.click_first_menu_button()
    assert menu_result, "Không thể nhấn vào icon '...'."
    test_logger.info("Đã nhấn vào icon '...' thành công.")
    time.sleep(1)
    detail_result = article_type.click_detail_button()
    assert detail_result, "Không thể nhấn vào menu-item 'Chi tiết'."
    test_logger.info("Đã nhấn vào menu-item 'Chi tiết' thành công.")
    
    # Chỉ kiểm tra một phần URL
    expected_partial_url = "cms/category/update/"
    actual_url_correct = article_type.verify_path_of_current_url(expected_partial_url)
    
    expected_result = f"Hệ thống đã nhấn vào 'Chi tiết' và chuyển hướng đến trang do '{expected_partial_url}'."
    actual_result = expected_result if actual_url_correct else f"Chuyển hướng sai hoac khong chuyen huong."
    
    if actual_url_correct:
        test_logger.info(f"Test Case 17 PASS: test_click_menu_and_detail_button | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 17 FAIL: test_click_menu_and_detail_button | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 18: Click icon '...' rồi click nút 'Xóa'
def test_click_menu_and_delete_button(article_type, is_displayed_article_type):
    test_logger.info("Bắt đầu Test Case 18: Verify có thể nhấn vào icon '...' rồi chọn nút 'Xóa'.")
    article_type.perform_tag_operations()
    time.sleep(1)
    menu_result = article_type.click_first_menu_button()
    assert menu_result, "Không thể nhấn vào icon '...'."
    test_logger.info("Đã nhấn vào icon '...' thành công.")
    time.sleep(1)
    delete_result = article_type.click_item_delete_button()
    assert delete_result, "Không thể nhấn vào nút 'Xóa'."
    test_logger.info("Đã nhấn vào nút 'Xóa' thành công.")
    expected_warning_text = "Bạn có chắc chắn ?"
    warning_displayed = is_displayed_article_type.is_warning_displayed()
    warning_text_correct = is_displayed_article_type.is_warning_text_correct(expected_warning_text)
    expected_result = f"Hệ thống hiển thị cảnh báo: '{expected_warning_text}' khi nhấn 'Xóa'."
    actual_result = "Hệ thống hiển thị đúng cảnh báo." if warning_text_correct else "Cảnh báo không đúng."
    if warning_displayed and warning_text_correct:
        test_logger.info(f"Test Case 18 PASS: test_click_menu_and_delete_button | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 18 FAIL: test_click_menu_and_delete_button | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 19: Click nut 'Thao tac' rồi click nút 'Xóa', Click 'Khong
def test_select_and_cancel_delete(article_type, is_displayed_article_type, popup_article_type):
    test_logger.info("Bắt đầu Test Case 19: Chọn bài viết -> Nhấn 'Thao tác' -> Nhấn 'Xóa' -> Nhấn 'No'.")
    article_type.perform_tag_operations()
    old_text = article_type.get_first_link_text()
    assert old_text, "Không thể lấy text của bài viết đầu tiên trước khi xóa."
    select_result = article_type.click_select_first_checkbox()
    assert select_result, "Không thể chọn bài viết đầu tiên."
    test_logger.info("Đã chọn bài viết đầu tiên.")
    operate_result = article_type.click_operate_button()
    assert operate_result, "Không thể nhấn vào nút 'Thao tác'."
    test_logger.info("Đã nhấn vào nút 'Thao tác'.")
    time.sleep(1)
    delete_result = article_type.click_delete_button()
    assert delete_result, "Không thể nhấn vào nút 'Xóa'."
    test_logger.info("Đã nhấn vào nút 'Xóa'.")
    time.sleep(1)
    expected_warning_text = "Bạn có chắc chắn ?"
    warning_displayed = is_displayed_article_type.is_warning_text_correct(expected_warning_text)
    assert warning_displayed, "Hộp thoại cảnh báo không hiển thị hoặc sai nội dung."
    test_logger.info("Hộp thoại cảnh báo hiển thị đúng.")
    no_button_clicked = popup_article_type.click_no_button()
    assert no_button_clicked, "Không thể nhấn vào nút 'No'."
    test_logger.info("Đã nhấn vào nút 'No'.")
    popup_closed = is_displayed_article_type.is_warning_popup_closed(expected_warning_text)
    assert popup_closed, "Hộp thoại cảnh báo không đóng sau khi nhấn 'No'."
    test_logger.info("Hộp thoại cảnh báo đã đóng sau khi nhấn 'No'.")
    new_text = article_type.get_first_link_text()
    assert old_text == new_text, "Tiêu đề bài viết đầu tiên đã thay đổi sau khi nhấn 'No'."
    test_logger.info("Bài viết đầu tiên không thay đổi sau khi hủy xóa.")
    expected_result = "Popup da dong, loai bai viet van con."
    actual_result = expected_result if popup_closed and (old_text == new_text) else "Kết quả không đúng, kiểm tra lại."
    if popup_closed and (old_text == new_text):
        test_logger.info(f"Test Case 19 PASS: test_select_and_cancel_delete | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 19 FAIL: test_select_and_cancel_delete | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 20: click thao tac -> click nut xoa -> click co
def test_select_and_confirm_delete(article_type, is_displayed_article_type, popup_article_type):
    test_logger.info("Bắt đầu Test Case 20: Chọn bài viết -> Nhấn 'Thao tác' -> Nhấn 'Xóa' -> Nhấn 'Có'.")
    article_type.perform_tag_operations()
    old_text = article_type.get_first_link_text()
    assert old_text, "Không thể lấy text của bài viết đầu tiên trước khi xóa."
    select_result = article_type.click_select_first_checkbox()
    assert select_result, "Không thể chọn bài viết đầu tiên."
    test_logger.info("Đã chọn bài viết đầu tiên.")
    operate_result = article_type.click_operate_button()
    assert operate_result, "Không thể nhấn vào nút 'Thao tác'."
    test_logger.info("Đã nhấn vào nút 'Thao tác'.")
    time.sleep(1)
    delete_result = article_type.click_delete_button()
    assert delete_result, "Không thể nhấn vào nút 'Xóa'."
    test_logger.info("Đã nhấn vào nút 'Xóa'.")
    time.sleep(1)
    expected_warning_text = "Bạn có chắc chắn ?"
    warning_displayed = is_displayed_article_type.is_warning_text_correct(expected_warning_text)
    assert warning_displayed, "Hộp thoại cảnh báo không hiển thị hoặc sai nội dung."
    test_logger.info("Hộp thoại cảnh báo hiển thị đúng.")
    yes_button_clicked = popup_article_type.click_yes_button()
    assert yes_button_clicked, "Không thể nhấn vào nút 'Có'."
    test_logger.info("Đã nhấn vào nút 'Có'.")
    popup_closed = is_displayed_article_type.is_warning_popup_closed(expected_warning_text)
    assert popup_closed, "Hộp thoại cảnh báo không đóng sau khi nhấn 'Có'."
    test_logger.info("Hộp thoại cảnh báo đã đóng sau khi nhấn 'Có'.")
    time.sleep(5)
    new_text = article_type.get_first_link_text()
    article_deleted = new_text != old_text 
    expected_result = "Bài viết đã bị xóa."
    actual_result = expected_result if article_deleted else "Bài viết không bị xóa, kiểm tra lại."
    if popup_closed and article_deleted:
        test_logger.info(f"Test Case 20 PASS: test_select_and_confirm_delete | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 20 FAIL: test_select_and_confirm_delete | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 21: Chọn bài viết -> Nhấn 'Thao tác' -> Nhấn 'Xóa' -> Nhấn 'No'.
def test_click_and_cancel_delete(article_type, is_displayed_article_type, popup_article_type):
    test_logger.info("Bắt đầu Test Case 21: Chọn bài viết -> Nhấn 'Thao tác' -> Nhấn 'Xóa' -> Nhấn 'No'.")
    article_type.perform_tag_operations()
    old_text = article_type.get_first_link_text()
    assert old_text, "Không thể lấy text của bài viết đầu tiên trước khi xóa."

    # Click vào icon '...' để mở menu và chọn 'Xóa'
    menu_result = article_type.click_first_menu_button()
    assert menu_result, "Không thể nhấn vào icon '...'."
    test_logger.info("Đã nhấn vào icon '...' thành công.")
    time.sleep(1)
    delete_result = article_type.click_item_delete_button()
    assert delete_result, "Không thể nhấn vào nút 'Xóa'."
    test_logger.info("Đã nhấn vào nút 'Xóa' thành công.")
    time.sleep(1)

    expected_warning_text = "Bạn có chắc chắn ?"
    warning_displayed = is_displayed_article_type.is_warning_text_correct(expected_warning_text)
    assert warning_displayed, "Hộp thoại cảnh báo không hiển thị hoặc sai nội dung."
    test_logger.info("Hộp thoại cảnh báo hiển thị đúng.")
    
    no_button_clicked = popup_article_type.click_no_button()
    assert no_button_clicked, "Không thể nhấn vào nút 'No'."
    test_logger.info("Đã nhấn vào nút 'No'.")
    
    popup_closed = is_displayed_article_type.is_warning_popup_closed(expected_warning_text)
    assert popup_closed, "Hộp thoại cảnh báo không đóng sau khi nhấn 'No'."
    test_logger.info("Hộp thoại cảnh báo đã đóng sau khi nhấn 'No'.")
    
    new_text = article_type.get_first_link_text()
    assert old_text == new_text, "Tiêu đề bài viết đầu tiên đã thay đổi sau khi nhấn 'No'."
    test_logger.info("Bài viết đầu tiên không thay đổi sau khi hủy xóa.")

    expected_result = "Popup da dong, loai bai viet van con."
    actual_result = expected_result if popup_closed and (old_text == new_text) else "Kết quả không đúng, kiểm tra lại."
    
    if popup_closed and (old_text == new_text):
        test_logger.info(f"Test Case 21 PASS: test_click_and_cancel_delete | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 21 FAIL: test_click_and_cancel_delete | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 22: Chọn bài viết -> Nhấn 'Thao tác' -> Nhấn 'Xóa' -> Nhấn 'Có'.
def test_click_and_confirm_delete(article_type, is_displayed_article_type, popup_article_type):
    test_logger.info("Bắt đầu Test Case 22: Chọn bài viết -> Nhấn 'Thao tác' -> Nhấn 'Xóa' -> Nhấn 'Có'.")
    article_type.perform_tag_operations()
    old_text = article_type.get_first_link_text()
    assert old_text, "Không thể lấy text của bài viết đầu tiên trước khi xóa."

    # Click vào icon '...' để mở menu và chọn 'Xóa'
    menu_result = article_type.click_first_menu_button()
    assert menu_result, "Không thể nhấn vào icon '...'."
    test_logger.info("Đã nhấn vào icon '...' thành công.")
    time.sleep(1)
    delete_result = article_type.click_item_delete_button()
    assert delete_result, "Không thể nhấn vào nút 'Xóa'."
    test_logger.info("Đã nhấn vào nút 'Xóa' thành công.")
    time.sleep(1)

    expected_warning_text = "Bạn có chắc chắn ?"
    warning_displayed = is_displayed_article_type.is_warning_text_correct(expected_warning_text)
    assert warning_displayed, "Hộp thoại cảnh báo không hiển thị hoặc sai nội dung."
    test_logger.info("Hộp thoại cảnh báo hiển thị đúng.")
    
    yes_button_clicked = popup_article_type.click_yes_button()
    assert yes_button_clicked, "Không thể nhấn vào nút 'Có'."
    test_logger.info("Đã nhấn vào nút 'Có'.")
    
    popup_closed = is_displayed_article_type.is_warning_popup_closed(expected_warning_text)
    assert popup_closed, "Hộp thoại cảnh báo không đóng sau khi nhấn 'Có'."
    test_logger.info("Hộp thoại cảnh báo đã đóng sau khi nhấn 'Có'.")
    
    time.sleep(5)  # Đợi quá trình xóa hoàn tất và cập nhật lại UI
    new_text = article_type.get_first_link_text()
    article_deleted = new_text != old_text 
    expected_result = "Bài viết đã bị xóa."
    actual_result = expected_result if article_deleted else "Bài viết không bị xóa, kiểm tra lại."
    
    if popup_closed and article_deleted:
        test_logger.info(f"Test Case 22 PASS: test_click_and_confirm_delete | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 22 FAIL: test_click_and_confirm_delete | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"



