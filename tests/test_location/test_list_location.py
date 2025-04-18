import time
import pytest
from utils.login import Login
from utils.logger import LoggerConfig
from utils.driver_setup import get_driver
from pages.location.list_location.list_location_base import ListLocationBase
from pages.location.list_location.is_displayed_list_location import IsDisplayedListLocation
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
def list_location_base(setup_driver):
    return ListLocationBase(setup_driver)

@pytest.fixture
def is_displayed_list_location(setup_driver):
    return IsDisplayedListLocation(setup_driver)

# Test Case 1: Verify khi nhấn nút 'Tạo mới' -> Hệ thống điều hướng đến trang 'Tạo mới chi nhánh'.
def test_click_create_button(list_location_base):
    test_logger.info("Bắt đầu Test Case 1: Verify khi nhấn nút 'Tạo mới'.")
    list_location_base.perform_tag_operations()
    result = list_location_base.click_create_button()
    expected_result = "Hệ thống điều hướng đến trang 'Tạo mới chi nhánh'."
    actual_result = expected_result if result else "Hệ thống không điều hướng đến trang 'Tạo mới chi nhánh'."
    if result:
        test_logger.info(f"Test Case 1 PASS: test_click_create_button | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 1 FAIL: test_click_create_button | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 2: Verify khi nhấn dropdown 'Tỉnh/Thành phố' và chọn Tỉnh/Thành phố đầu tiên -> Hệ thống hiển thị Tỉnh/Thành phố được chọn.
def test_click_province_dropdown_and_choose_province(list_location_base, is_displayed_list_location):
    test_logger.info("Bắt đầu Test Case 2: Verify khi nhấn dropdown 'Tỉnh/Thành phố' và chọn Tỉnh/Thành phố đầu tiên.")
    list_location_base.perform_tag_operations()
    list_location_base.click_province_dropdown()
    list_location_base.click_first_item_province()
    time.sleep(1)
    expected_text = 'An Giang'
    result = is_displayed_list_location.is_text_displayed_in_province_dropdown(expected_text)
    expected_result = "Hệ thống hiển thị Tỉnh/Thành phố được chọn."
    actual_result = expected_result if result else "Hệ thống không hiển thị Tỉnh/Thành phố được chọn."
    if result:
        test_logger.info(f"Test Case 2 PASS: test_click_province_dropdown_and_choose_province | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 2 FAIL: test_click_province_dropdown_and_choose_province | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# Test Case 3: Verify khi nhấn dropdown 'Huyện/Quận' khi chưa chọn Tỉnh/Thành phố -> Hệ thống mở dropdown chỉ có giá trị mặc định.
def test_click_district_dropdown(list_location_base, is_displayed_list_location):
    test_logger.info("Bắt đầu Test Case 3: Verify khi nhấn dropdown 'Huyện/Quận' khi chưa chọn Tỉnh/Thành phố.")
    list_location_base.perform_tag_operations()
    list_location_base.click_district_dropdown()
    result = is_displayed_list_location.is_first_district_item_not_present()
    expected_result = "Hệ thống mở dropdown chỉ có giá trị mặc định."
    actual_result = expected_result if result else "Hệ thống hiện thị Huyện/Quận tương ứng của Tỉnh/Thành phố."
    if result:
        test_logger.info(f"Test Case 3 PASS: test_click_district_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 3 FAIL: test_click_district_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"    
        
# Test Case 4: Verify khi nhấn dropdown 'Huyện/Quận' sau khi chọn Tỉnh/Thành phố -> Hệ thống mở dropdown chỉ có giá trị mặc định.
def test_click_district_dropdown_after_choose_province(list_location_base, is_displayed_list_location):
    test_logger.info("Bắt đầu Test Case 4: Verify khi nhấn dropdown 'Huyện/Quận' khi chưa chọn Tỉnh/Thành phố.")
    list_location_base.perform_tag_operations()
    list_location_base.click_province_dropdown()
    list_location_base.click_first_item_province()
    list_location_base.click_district_dropdown()
    expected_text = "Long Xuyên"
    result = is_displayed_list_location.is_text_displayed_in_first_district_item(expected_text)
    expected_result = "Hệ thống hiện thị Huyện/Quận tương ứng của Tỉnh/Thành phố."
    actual_result = expected_result if result else "Hệ thống mở dropdown chỉ có giá trị mặc định."
    if result:
        test_logger.info(f"Test Case 4 PASS: test_click_district_dropdown_after_choose_province | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 4 FAIL: test_click_district_dropdown_after_choose_province | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"              

# Test Case 5: Verify khi nhấn dropdown 'Huyện/Quận' và chọn Huyện/Quận đầu tiên -> Hệ thống hiển thị Huyện/Quận được chọn
def test_click_district_dropdown_and_choose_district(list_location_base, is_displayed_list_location):
    test_logger.info("Bắt đầu Test Case 5: Verify khi nhấn dropdown 'Huyện/Quận'và chọn Huyện/Quận đầu tiên.")
    list_location_base.perform_tag_operations()
    list_location_base.click_province_dropdown()
    list_location_base.click_first_item_province()
    list_location_base.click_district_dropdown()
    list_location_base.click_first_item_district()
    expected_text = "Long Xuyên"
    result = is_displayed_list_location.is_text_displayed_in_district_dropdown(expected_text)
    expected_result = "Hệ thống hiển thị Huyện/Quận được chọn."
    actual_result = expected_result if result else "Hệ thống không hiển thị Huyện/Quận được chọn."
    if result:
        test_logger.info(f"Test Case 5 PASS: test_click_district_dropdown_and_choose_district | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 5 FAIL: test_click_district_dropdown_and_choose_district | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"  
        
# Test Case 6: Verify click dropdown 'Status' và chọn trạng thái 'Kích hoạt' -> Hệ thống đóng dropdown, hiển thị trạng thái được chọn.
def test_click_status_dropdown_and_choose_active(list_location_base, is_displayed_list_location):
    test_logger.info("Bắt đầu Test Case 6:  Verify click dropdown 'Status' và chọn trạng thái 'Kích hoạt'.")
    list_location_base.perform_tag_operations()
    list_location_base.click_status_dropdown()
    list_location_base.click_active_status()
    expected_text = "Kích hoạt"
    result = is_displayed_list_location.is_text_displayed_in_status_dropdown(expected_text)
    expected_result = "Hệ thống đóng dropdown, hiển thị trạng thái được chọn."
    actual_result = expected_result if result else "Hệ thống không hiển thị trạng thái được chọn."
    if result:
        test_logger.info(f"Test Case 6 PASS: test_click_status_dropdown_and_choose_active | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 6 FAIL: test_click_status_dropdown_and_choose_active | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"         

# Test Case 7: Verify click dropdown 'Status' và chọn trạng thái 'Chờ xử lý' -> Hệ thống đóng dropdown, hiển thị trạng thái được chọn.
def test_click_status_dropdown_and_choose_processing(list_location_base, is_displayed_list_location):
    test_logger.info("Bắt đầu Test Case 7:  Verify click dropdown 'Status' và chọn trạng thái 'Chờ xử lý'.")
    list_location_base.perform_tag_operations()
    list_location_base.click_status_dropdown()
    list_location_base.click_processing_status()
    expected_text = "Chờ xử lý"
    result = is_displayed_list_location.is_text_displayed_in_status_dropdown(expected_text)
    expected_result = "Hệ thống đóng dropdown, hiển thị trạng thái được chọn."
    actual_result = expected_result if result else "Hệ thống không hiển thị trạng thái được chọn."
    if result:
        test_logger.info(f"Test Case 7 PASS: test_click_status_dropdown_and_choose_processing | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 7 FAIL: test_click_status_dropdown_and_choose_processing | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"   

# Test Case 8: Verify click nút 'Tải lại' -> Hệ thống đặt lại các bộ lọc.
def test_click_reload_button_after_select(list_location_base, is_displayed_list_location):
    test_logger.info("Bắt đầu Test Case 8:  Verify click nút 'Tải lại'.")
    list_location_base.perform_tag_operations()
    list_location_base.click_province_dropdown()
    list_location_base.click_first_item_province()
    list_location_base.click_district_dropdown()
    list_location_base.click_first_item_district()
    list_location_base.click_reload_button()
    time.sleep(1)
    expected_text = "An Giang"
    expected_text_2 = "Long Xuyên"
    result = is_displayed_list_location.is_text_not_displayed_in_province_dropdown(expected_text)
    result_2 = is_displayed_list_location.is_text_not_displayed_in_district_dropdown(expected_text_2)
    expected_result = "Hệ thống đặt lại các bộ lọc."
    actual_result = expected_result if result and result_2 else "Hệ thống không đặt lại các bộ lọc."
    if result:
        test_logger.info(f"Test Case 8 PASS: test_click_reload_button_after_select | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 8 FAIL: test_click_reload_button_after_select | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"         

# Test Case 9: Verify click dropdown 'Phân trang' và chọn Số trang -> Hệ thống đóng dropdown, hiển thị Số trang được chọn.
def test_click_pagination_dropdown_and_choose_number_of_page(list_location_base, is_displayed_list_location):
    test_logger.info("Bắt đầu Test Case 9:  Verify click dropdown 'Status' và chọn trạng thái 'Chờ xử lý'.")
    list_location_base.perform_tag_operations()
    list_location_base.click_pagination_dropdown()
    list_location_base.click_first_pagination_item()
    expected_text = "2/TRANG"
    result = is_displayed_list_location.is_text_displayed_in_pagination_dropdown(expected_text)
    expected_result = "Hệ thống đóng dropdown, hiển thị trạng thái được chọn."
    actual_result = expected_result if result else "Hệ thống không hiển thị trạng thái được chọn."
    if result:
        test_logger.info(f"Test Case 9 PASS: test_click_pagination_dropdown_and_choose_number_of_page | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 9 FAIL: test_click_pagination_dropdown_and_choose_number_of_page | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}" 

# Test Case 10: Verify khi nhấn nút 'Thao tác' và chọn 'Xóa' khi không chọn Chi nhánh -> Hệ thống hiển thị popup thông báo 'Vui lòng chọn Chi nhánh để xóa.'.
def test_click_create_button(list_location_base, is_displayed_list_location):
    test_logger.info("Bắt đầu Test Case 10: Verify khi nhấn nút 'Thao tác' và chọn 'Xóa' khi không chọn Chi nhánh.")
    list_location_base.perform_tag_operations()
    list_location_base.click_operate_button()
    list_location_base.click_delete_button()
    is_displayed_list_location.is_warning_displayed()
    expected_text ="Vui lòng chọn Chi nhánh để xóa."
    result = is_displayed_list_location.is_warning_text_correct(expected_text)
    expected_result = "Popup hiển thị đúng nội dung."
    actual_result = expected_result if result else "Popup không hiển thị đúng nội dung."
    if result:
        test_logger.info(f"Test Case 10 PASS: test_click_create_button | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 10 FAIL: test_click_create_button | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 11: Verify khi nhập từ khóa vào thanh tìm kiếm -> Từ khóa tìm kiếm được nhập và hiển thị.
def test_enter_search_keyword(list_location_base):
    test_logger.info("Bắt đầu Test Case 11: Verify khi nhập từ khóa vào thanh tìm kiếm.")
    list_location_base.perform_tag_operations()
    keyword = "Long Xuyên"
    result = list_location_base.enter_search_keyword(keyword)
    expected_result = "Từ khóa tìm kiếm được nhập và hiển thị."
    actual_result = expected_result if result else "Từ khóa tìm kiếm không được nhập hoặc hiển thị."
    if result:
        test_logger.info(f"Test Case 11 PASS: test_enter_search_keyword | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 11 FAIL: test_enter_search_keyword | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# Test Case 12: Verify khi click chọn checkbox và click nút 'Thao tác', chọn 'Xóa' -> Hiển thị popup 'Xác nhận xóa'
def test_click_delete_button_after_click_checkbox(list_location_base, is_displayed_list_location):
    test_logger.info("Bắt đầu Test Case 12: Verify khi click chọn checkbox và click nút 'Thao tác', chọn 'Xóa'.")
    list_location_base.perform_tag_operations()
    list_location_base.click_select_all_checkbox()
    list_location_base.click_operate_button()
    list_location_base.click_delete_button()
    is_displayed_list_location.is_warning_displayed()
    expected_text = "Bạn có chắc chắn ?"
    result = is_displayed_list_location.is_warning_text_correct(expected_text)
    expected_result = "Hiển thị popup 'Xác nhận xóa' với đúng nội dung."
    actual_result = expected_result if result else "Không Hiển thị popup 'Xác nhận xóa' hoặc nội dung hiển thị sai."
    if result:
        test_logger.info(f"Test Case 12 PASS: test_click_delete_button_after_click_checkbox | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 12 FAIL: test_click_delete_button_after_click_checkbox | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"        

# Test Case 13: Verify khi click Tên của chi nhánh đầu tiên -> Hệ thống chuyển hướng đến trang chỉnh sửa chi nhánh đầu tiên
def test_click_first_location_name(list_location_base, is_displayed_list_location):
    test_logger.info("Bắt đầu Test Case 13: Verify khi click Tên của chi nhánh đầu tiên.")
    list_location_base.perform_tag_operations()
    list_location_base.click_first_name()
    expected_url = "https://mpire-cms-demo.mpire.asia/cms/dealer/edit"
    result = is_displayed_list_location.verify_path_of_current_url(expected_url)
    expected_result = f"Hệ thống chuyển hướng đến trang chỉnh sửa."
    actual_result = expected_result if result else f"Hệ thống không chuyển hướng đến trang chỉnh sửa."
    if result:
        test_logger.info(f"Test Case 13 PASS: test_click_first_location_name | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 13 FAIL: test_click_first_location_name | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 14: Verify khi click nút '...' của chi nhánh đầu tiên và chọn Chi tiết -> Hệ thống chuyển hướng đến trang chỉnh sửa chi nhánh đầu tiên
def test_click_first_menu_button_choose_detail(list_location_base, is_displayed_list_location):
    test_logger.info("Bắt đầu Test Case 14: Verify khi click nút '...' của chi nhánh đầu tiên và chọn Chi tiết.")
    list_location_base.perform_tag_operations()
    list_location_base.click_first_menu_button()
    list_location_base.click_first_detail_menu_item()
    expected_url = "https://mpire-cms-demo.mpire.asia/cms/dealer/edit"
    result = is_displayed_list_location.verify_path_of_current_url(expected_url)
    expected_result = f"Hệ thống chuyển hướng đến trang chỉnh sửa."
    actual_result = expected_result if result else f"Hệ thống không chuyển hướng đến trang chỉnh sửa."
    if result:
        test_logger.info(f"Test Case 14 PASS: test_click_first_menu_button_choose_detail | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 14 FAIL: test_click_first_menu_button_choose_detail | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 15: Verify khi click nút '...' của chi nhánh đầu tiên và chọn Xóa -> Hệ thống hiển thị popup 'Xác nhận' với đúng nội dung
def test_click_first_menu_button_choose_delete(list_location_base, is_displayed_list_location):
    test_logger.info("Bắt đầu Test Case 15: Verify khi click nút '...' của chi nhánh đầu tiên và chọn Xóa.")
    list_location_base.perform_tag_operations()
    list_location_base.click_first_menu_button()
    list_location_base.click_first_delete_menu_item()
    is_displayed_list_location.is_warning_displayed()
    expected_text = "Bạn có chắc chắn ?"
    result = is_displayed_list_location.is_warning_text_correct(expected_text)
    expected_result = f"Hệ thống hiển thị popup 'Xác nhận' với đúng nội dung."
    actual_result = expected_result if result else f"Hệ thống không hiển thị popup 'Xác nhận' hoặc không đúng nội dung."
    if result:
        test_logger.info(f"Test Case 15 PASS: test_click_first_menu_button_choose_delete | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 15 FAIL: test_click_first_menu_button_choose_delete | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"     

# Test Case 16: Verify khi click chọn Có trong popup 'Xác nhận' -> Hệ thống xóa Chi nhánh
def test_click_yes_in_popup_confirm(list_location_base, is_displayed_list_location):
    test_logger.info("Bắt đầu Test Case 16: Verify khi click chọn Có trong popup 'Xác nhận'.")
    list_location_base.perform_tag_operations()
    list_location_base.click_first_menu_button()
    list_location_base.click_first_delete_menu_item()
    is_displayed_list_location.is_warning_displayed()
    list_location_base.click_button_yes_in_popup()
    time.sleep(0.5)
    expected_text = "1 Chi nhánh đã chọn được xóa thành công."
    result = is_displayed_list_location.is_warning_text_correct(expected_text)
    expected_result = f" Hệ thống xóa Chi nhánh thành công, hiển thị thông báo."
    actual_result = expected_result if result else f"Hệ thống không thể popup Chi nhánh"
    if result:
        test_logger.info(f"Test Case 16 PASS: test_click_yes_in_popup_confirm | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 16 FAIL: test_click_yes_in_popup_confirm | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"             

# Test Case 17: Verify khi click chọn Không trong popup 'Xác nhận' -> Hệ thống hủy xóa Chi nhánh, đóng popup
def test_click_no_in_popup_confirm(list_location_base, is_displayed_list_location):
    test_logger.info("Bắt đầu Test Case 17: Verify khi click chọn Không trong popup 'Xác nhận'.")
    list_location_base.perform_tag_operations()
    list_location_base.click_first_menu_button()
    list_location_base.click_first_delete_menu_item()
    is_displayed_list_location.is_warning_displayed()
    time.sleep(1)
    result = list_location_base.click_button_no_in_popup()
    expected_result = f" Hệ thống hủy xóa Chi nhánh, đóng popup."
    actual_result = expected_result if result else f"Hệ thống không hủy xóa Chi nhánh, hoặc không đóng popup"
    if result:
        test_logger.info(f"Test Case 17 PASS: test_click_no_in_popup_confirm | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 17 FAIL: test_click_no_in_popup_confirm | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"          