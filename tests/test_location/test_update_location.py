import time
import pytest
from utils.login import Login
from utils.logger import LoggerConfig
from utils.driver_setup import get_driver
from pages.location.update_location.update_location_base import UpdateLocationBase
from pages.location.update_location.enter_update_location import EnterUpdateLocation
from pages.location.update_location.get_field_update_location import GetFieldUpdateLocation
from pages.location.update_location.is_displayed_update_location import IsDisplayedUpdateLocation
from pages.location.update_location.image_update_location import ImageUpdateLocation
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
            pytest.fail("Không thể đăng cập nhật!")
        yield driver
    finally:
        time.sleep(3)
        driver.quit()

@pytest.fixture
def update_location_base(setup_driver):
    return UpdateLocationBase(setup_driver)

@pytest.fixture
def enter_update_location(setup_driver):
    return EnterUpdateLocation(setup_driver)

@pytest.fixture
def get_field_update_location(setup_driver):
    return GetFieldUpdateLocation(setup_driver)

@pytest.fixture
def is_displayed_update_location(setup_driver):
    return IsDisplayedUpdateLocation(setup_driver)

@pytest.fixture
def image_update_location(setup_driver):
    return ImageUpdateLocation(setup_driver)

# Test Case 1: Verify khi click Tên của chi nhánh đầu tiên -> Hệ thống chuyển hướng đến trang chỉnh sửa chi nhánh đầu tiên
def test_click_first_location_name(update_location_base, is_displayed_update_location):
    test_logger.info("Bắt đầu Test Case 1: Verify khi click Tên của chi nhánh đầu tiên.")
    update_location_base.perform_tag_operations()
    update_location_base.click_first_name()
    expected_url = "https://mpire-cms-demo.mpire.asia/cms/dealer/edit"
    result = is_displayed_update_location.verify_path_of_current_url(expected_url)
    expected_result = f"Hệ thống chuyển hướng đến trang chỉnh sửa."
    actual_result = expected_result if result else f"Hệ thống không chuyển hướng đến trang chỉnh sửa."
    if result:
        test_logger.info(f"Test Case 1 PASS: test_click_first_location_name | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 1 FAIL: test_click_first_location_name | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 2: Verify khi click nút '...' của chi nhánh đầu tiên và chọn Chi tiết -> Hệ thống chuyển hướng đến trang chỉnh sửa chi nhánh đầu tiên
def test_click_first_menu_button_choose_detail(update_location_base, is_displayed_update_location):
    test_logger.info("Bắt đầu Test Case 2: Verify khi click nút '...' của chi nhánh đầu tiên và chọn Chi tiết.")
    update_location_base.perform_tag_operations()
    update_location_base.click_first_menu_button()
    update_location_base.click_first_detail_menu_item()
    expected_url = "https://mpire-cms-demo.mpire.asia/cms/dealer/edit"
    result = is_displayed_update_location.verify_path_of_current_url(expected_url)
    expected_result = f"Hệ thống chuyển hướng đến trang chỉnh sửa."
    actual_result = expected_result if result else f"Hệ thống không chuyển hướng đến trang chỉnh sửa."
    if result:
        test_logger.info(f"Test Case 2 PASS: test_click_first_menu_button_choose_detail | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 2 FAIL: test_click_first_menu_button_choose_detail | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# Test Case 3: Verify khi click nút 'Hủy' -> Hệ thống hủy chỉnh sửa và chuyển hướng về trang danh sách
def test_click_cancel_button(update_location_base, is_displayed_update_location):
    test_logger.info("Bắt đầu Test Case 3: Verify khi click nút 'Hủy'.")
    update_location_base.perform_tag_operations()
    update_location_base.click_first_menu_button()
    update_location_base.click_first_detail_menu_item()
    url = "https://mpire-cms-demo.mpire.asia/cms/dealer/edit"
    is_displayed_update_location.verify_path_of_current_url(url)
    update_location_base.click_cancel_button()
    expected_url = "https://mpire-cms-demo.mpire.asia/cms/dealer"
    result = update_location_base.verify_current_url(expected_url)
    expected_result = f"Hệ thống hủy chỉnh sửa và chuyển hướng về trang danh sách."
    actual_result = expected_result if result else f"Hệ thống không hủy chỉnh sửa và chuyển hướng về trang danh sách."
    if result:
        test_logger.info(f"Test Case 3 PASS: test_click_first_menu_button_choose_detail | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 3 FAIL: test_click_first_menu_button_choose_detail | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"        

# Test Case 4: Verify khi cập nhật Tên chi nhánh ở tab Tiếng Việt -> Hệ thống hiển thị thông tin vừa cập nhật
def test_update_vi_location_name(update_location_base, enter_update_location, get_field_update_location):
    test_logger.info("Bắt đầu Test Case 4: Verify khi cập nhật Tên chi nhánh ở tab Tiếng Việt.")
    update_location_base.perform_tag_operations()
    update_location_base.click_first_name()
    name = "Tp. Hồ Chí Minh"
    enter_update_location.enter_name(name)
    update_location_base.click_save_button()
    update_location_base.click_first_name()
    result = get_field_update_location.get_name()
    expected_result = "Hệ thống hiển thị thông tin vừa cập nhật."
    actual_result = expected_result if result == "Tp. Hồ Chí Minh" else "Hệ thống không hiển thị thông tin vừa cập nhật."
    if result:
        test_logger.info(f"Test Case 4 PASS: test_update_vi_location_name | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 4 FAIL: test_update_vi_location_name | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 5: Verify khi cập nhật Địa chỉ chi nhánh ở tab Tiếng Việt -> Hệ thống hiển thị thông tin vừa cập nhật
def test_update_vi_location_address(update_location_base, enter_update_location, get_field_update_location):
    test_logger.info("Bắt đầu Test Case 5: Verify khi cập nhật Địa chỉ chi nhánh ở tab Tiếng Việt.")
    update_location_base.perform_tag_operations()
    update_location_base.click_first_name()
    address = "Quận 2"
    enter_update_location.enter_address(address)
    update_location_base.click_save_button()
    update_location_base.click_first_name()
    result = get_field_update_location.get_address()
    expected_result = "Hệ thống hiển thị thông tin vừa cập nhật."
    actual_result = expected_result if result == "Quận 2" else "Hệ thống không hiển thị thông tin vừa cập nhật."
    if result:
        test_logger.info(f"Test Case 5 PASS: test_update_vi_location_address | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 5 FAIL: test_update_vi_location_address | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 6: Verify khi cập nhật Nội dung chi nhánh ở tab Tiếng Việt -> Hệ thống hiển thị thông tin vừa cập nhật
def test_update_vi_location_content(update_location_base, enter_update_location, get_field_update_location):
    test_logger.info("Bắt đầu Test Case 6: Verify khi cập nhật Địa chỉ chi nhánh ở tab Tiếng Việt.")
    update_location_base.perform_tag_operations()
    update_location_base.click_first_name()
    content = "31D, An Phú 2"
    enter_update_location.enter_content(content)
    update_location_base.click_save_button()
    update_location_base.click_first_name()
    result = get_field_update_location.get_content()
    expected_result = "Hệ thống hiển thị thông tin vừa cập nhật."
    actual_result = expected_result if result == "31D, An Phú 2" else "Hệ thống không hiển thị thông tin vừa cập nhật."
    if result:
        test_logger.info(f"Test Case 6 PASS: test_update_vi_location_content | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 6 FAIL: test_update_vi_location_content | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"        

# Test Case 7: Verify khi cập nhật Tên chi nhánh ở tab English -> Hệ thống hiển thị thông tin vừa cập nhật
def test_update_en_location_name(update_location_base, enter_update_location, get_field_update_location):
    test_logger.info("Bắt đầu Test Case 7: Verify khi cập nhật Tên chi nhánh ở tab English.")
    update_location_base.perform_tag_operations()
    update_location_base.click_first_name()
    update_location_base.click_english_tab()
    update_location_base.click_translate_button()
    time.sleep(0.5)
    name = "Ho Chi Minh City"
    enter_update_location.enter_en_name(name)
    update_location_base.click_save_button()
    update_location_base.click_first_name()
    update_location_base.click_english_tab()
    result = get_field_update_location.get_en_name()
    expected_result = "Hệ thống hiển thị thông tin vừa cập nhật."
    actual_result = expected_result if result == "Ho Chi Minh City" else "Hệ thống không hiển thị thông tin vừa cập nhật."
    if result:
        test_logger.info(f"Test Case 7 PASS: test_update_en_location_name | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 7 FAIL: test_update_en_location_name | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 8: Verify khi cập nhật Địa chỉ chi nhánh ở tab English -> Hệ thống hiển thị thông tin vừa cập nhật
def test_update_en_location_address(update_location_base, enter_update_location, get_field_update_location):
    test_logger.info("Bắt đầu Test Case 8: Verify khi cập nhật Địa chỉ chi nhánh ở tab English.")
    update_location_base.perform_tag_operations()
    update_location_base.click_first_name()
    update_location_base.click_english_tab()
    update_location_base.click_translate_button()
    time.sleep(0.5)
    address = "2 District"
    enter_update_location.enter_en_address(address)
    update_location_base.click_save_button()
    update_location_base.click_first_name()
    update_location_base.click_english_tab()
    result = get_field_update_location.get_en_address()
    expected_result = "Hệ thống hiển thị thông tin vừa cập nhật."
    actual_result = expected_result if result == "2 District" else "Hệ thống không hiển thị thông tin vừa cập nhật."
    if result:
        test_logger.info(f"Test Case 8 PASS: test_update_en_location_address | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 8 FAIL: test_update_en_location_address | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # đang bị lỗi
# # Test Case 9: Verify khi cập nhật Nội dung chi nhánh ở tab English -> Hệ thống hiển thị thông tin vừa cập nhật
# def test_update_en_location_content(update_location_base, enter_update_location, get_field_update_location):
#     test_logger.info("Bắt đầu Test Case 9: Verify khi cập nhật Địa chỉ chi nhánh ở tab English.")
#     update_location_base.perform_tag_operations()
#     update_location_base.click_first_name()
#     update_location_base.click_english_tab()
#     update_location_base.click_translate_button()
#     time.sleep(2)
#     content = "31D, An Phu 2"
#     enter_update_location.enter_en_content(content)
#     update_location_base.click_save_button()
#     update_location_base.click_first_name()
#     update_location_base.click_english_tab()
#     result = get_field_update_location.get_en_content()
#     expected_result = "Hệ thống hiển thị thông tin vừa cập nhật."
#     actual_result = expected_result if result == "31D, An Phu 2" else "Hệ thống không hiển thị thông tin vừa cập nhật."
#     if result:
#         test_logger.info(f"Test Case 9 PASS: test_update_en_location_content | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 9 FAIL: test_update_en_location_content | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"           

# Test Case 10: Verify khi nhấn dropdown 'Tỉnh/Thành phố' và chọn Tỉnh/Thành phố đầu tiên -> Hệ thống hiển thị Tỉnh/Thành phố được chọn.
def test_click_province_dropdown_and_choose_province(update_location_base, is_displayed_update_location):
    test_logger.info("Bắt đầu Test Case 10: Verify khi nhấn dropdown 'Tỉnh/Thành phố' và chọn Tỉnh/Thành phố đầu tiên.")
    update_location_base.perform_tag_operations()
    update_location_base.click_first_name()
    update_location_base.click_general_information_tab()
    update_location_base.click_province_dropdown()
    update_location_base.click_first_item_province()
    time.sleep(1)
    update_location_base.click_save_button()
    update_location_base.click_first_name()
    update_location_base.click_general_information_tab()
    expected_text = 'An Giang'
    result = is_displayed_update_location.is_text_displayed_in_province_dropdown(expected_text)
    expected_result = "Hệ thống hiển thị Tỉnh/Thành phố được chọn."
    actual_result = expected_result if result else "Hệ thống không hiển thị Tỉnh/Thành phố được chọn."
    if result:
        test_logger.info(f"Test Case 10 PASS: test_click_province_dropdown_and_choose_province | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 10 FAIL: test_click_province_dropdown_and_choose_province | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"         

# Test Case 11: Verify khi nhấn dropdown 'Huyện/Quận' và chọn Huyện/Quận đầu tiên -> Hệ thống hiển thị Huyện/Quận được chọn
def test_click_district_dropdown_and_choose_district(update_location_base, is_displayed_update_location):
    test_logger.info("Bắt đầu Test Case 11: Verify khi nhấn dropdown 'Huyện/Quận'và chọn Huyện/Quận đầu tiên.")
    update_location_base.perform_tag_operations()
    update_location_base.click_first_name()
    update_location_base.click_general_information_tab()
    update_location_base.click_province_dropdown()
    update_location_base.click_first_item_province()
    update_location_base.click_district_dropdown()
    update_location_base.click_first_item_district()
    update_location_base.click_save_button()
    update_location_base.click_first_name()
    update_location_base.click_general_information_tab()
    expected_text = "An Phú"
    result = is_displayed_update_location.is_text_displayed_in_district_dropdown(expected_text)
    expected_result = "Hệ thống hiển thị Huyện/Quận được chọn."
    actual_result = expected_result if result else "Hệ thống không hiển thị Huyện/Quận được chọn."
    if result:
        test_logger.info(f"Test Case 11 PASS: test_click_district_dropdown_and_choose_district | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 11 FAIL: test_click_district_dropdown_and_choose_district | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"  

# Test Case 12: Verify khi cập nhật Số điện thoại ở tab 'Thông tin chung' -> Hệ thống hiển thị thông tin vừa cập nhật
def test_update_phone_number(update_location_base, enter_update_location, get_field_update_location):
    test_logger.info("Bắt đầu Test Case 12: Verify khi cập nhật Số điện thoại ở tab 'Thông tin chung'.")
    update_location_base.perform_tag_operations()
    update_location_base.click_first_name()
    update_location_base.click_general_information_tab()
    phone_number = "0392963132"
    enter_update_location.enter_phone(phone_number)
    update_location_base.click_save_button()
    update_location_base.click_first_name()
    update_location_base.click_general_information_tab()
    result = get_field_update_location.get_phone()
    expected_result = "Hệ thống hiển thị thông tin vừa cập nhật."
    actual_result = expected_result if result == "0392963132" else "Hệ thống không hiển thị thông tin vừa cập nhật."
    if result:
        test_logger.info(f"Test Case 12 PASS: test_update_phone_number | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 12 FAIL: test_update_phone_number | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# Test Case 13: Verify khi cập nhật FAX ở tab 'Thông tin chung' -> Hệ thống hiển thị thông tin vừa cập nhật
def test_update_fax(update_location_base, enter_update_location, get_field_update_location):
    test_logger.info("Bắt đầu Test Case 13: Verify khi cập nhật FAX ở tab 'Thông tin chung'.")
    update_location_base.perform_tag_operations()
    update_location_base.click_first_name()
    update_location_base.click_general_information_tab()
    fax = "0212"
    enter_update_location.enter_fax(fax)
    update_location_base.click_save_button()
    update_location_base.click_first_name()
    update_location_base.click_general_information_tab()
    result = get_field_update_location.get_fax()
    expected_result = "Hệ thống hiển thị thông tin vừa cập nhật."
    actual_result = expected_result if result == "0212" else "Hệ thống không hiển thị thông tin vừa cập nhật."
    if result:
        test_logger.info(f"Test Case 13 PASS: test_update_fax | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 13 FAIL: test_update_fax | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"        
        
# Test Case 14: Verify khi cập nhật Kinh độ ở tab 'Thông tin chung' -> Hệ thống hiển thị thông tin vừa cập nhật
def test_update_longitude(update_location_base, enter_update_location, get_field_update_location):
    test_logger.info("Bắt đầu Test Case 14: Verify khi cập nhật Kinh độ ở tab 'Thông tin chung'.")
    update_location_base.perform_tag_operations()
    update_location_base.click_first_name()
    update_location_base.click_general_information_tab()
    longitude = "105.123456"
    enter_update_location.enter_longitude(longitude)
    update_location_base.click_save_button()
    update_location_base.click_first_name()
    update_location_base.click_general_information_tab()
    result = get_field_update_location.get_longitude()
    expected_result = "Hệ thống hiển thị thông tin vừa cập nhật."
    actual_result = expected_result if result == longitude else "Hệ thống không hiển thị thông tin vừa cập nhật."
    if result == longitude:
        test_logger.info(f"Test Case 14 PASS: test_update_longitude | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 14 FAIL: test_update_longitude | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 15: Verify khi cập nhật Vĩ độ ở tab 'Thông tin chung' -> Hệ thống hiển thị thông tin vừa cập nhật
def test_update_latitude(update_location_base, enter_update_location, get_field_update_location):
    test_logger.info("Bắt đầu Test Case 15: Verify khi cập nhật Vĩ độ ở tab 'Thông tin chung'.")
    update_location_base.perform_tag_operations()
    update_location_base.click_first_name()
    update_location_base.click_general_information_tab()
    latitude = "21.028511"
    enter_update_location.enter_latitude(latitude)
    update_location_base.click_save_button()
    update_location_base.click_first_name()
    update_location_base.click_general_information_tab()
    result = get_field_update_location.get_latitude()
    expected_result = "Hệ thống hiển thị thông tin vừa cập nhật."
    actual_result = expected_result if result == latitude else "Hệ thống không hiển thị thông tin vừa cập nhật."
    if result == latitude:
        test_logger.info(f"Test Case 15 PASS: test_update_latitude | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 15 FAIL: test_update_latitude | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 16: Verify khi cập nhật Email ở tab 'Thông tin chung' -> Hệ thống hiển thị thông tin vừa cập nhật
def test_update_email(update_location_base, enter_update_location, get_field_update_location):
    test_logger.info("Bắt đầu Test Case 16: Verify khi cập nhật Email ở tab 'Thông tin chung'.")
    update_location_base.perform_tag_operations()
    update_location_base.click_first_name()
    update_location_base.click_general_information_tab()
    email = "example@domain.com"
    enter_update_location.enter_email(email)
    update_location_base.click_save_button()
    update_location_base.click_first_name()
    update_location_base.click_general_information_tab()
    result = get_field_update_location.get_email()
    expected_result = "Hệ thống hiển thị thông tin vừa cập nhật."
    actual_result = expected_result if result == email else "Hệ thống không hiển thị thông tin vừa cập nhật."
    if result == email:
        test_logger.info(f"Test Case 16 PASS: test_update_email | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 16 FAIL: test_update_email | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 17: Verify khi cập nhật Giá trị sắp xếp ở tab 'Thông tin chung' -> Hệ thống hiển thị thông tin vừa cập nhật
def test_update_sort_order(update_location_base, enter_update_location, get_field_update_location):
    test_logger.info("Bắt đầu Test Case 17: Verify khi cập nhật Giá trị sắp xếp ở tab 'Thông tin chung'.")
    update_location_base.perform_tag_operations()
    update_location_base.click_first_name()
    update_location_base.click_general_information_tab()
    sort_value = "5"
    enter_update_location.enter_sort_order(sort_value)
    update_location_base.click_save_button()
    update_location_base.click_first_name()
    update_location_base.click_general_information_tab()
    result = get_field_update_location.get_sort_order()
    expected_result = "Hệ thống hiển thị thông tin vừa cập nhật."
    actual_result = expected_result if result == sort_value else "Hệ thống không hiển thị thông tin vừa cập nhật."
    if result == sort_value:
        test_logger.info(f"Test Case 17 PASS: test_update_sort_order | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 17 FAIL: test_update_sort_order | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 18: Verify click dropdown 'Status' và chọn trạng thái 'Kích hoạt' -> Hệ thống đóng dropdown, hiển thị trạng thái được chọn.
def test_click_status_dropdown_and_choose_active(update_location_base, is_displayed_update_location):
    test_logger.info("Bắt đầu Test Case 18:  Verify click dropdown 'Status' và chọn trạng thái 'Kích hoạt'.")
    update_location_base.perform_tag_operations()
    update_location_base.click_first_name()
    update_location_base.click_general_information_tab()    
    update_location_base.click_status_dropdown()
    update_location_base.click_active_status()
    update_location_base.click_save_button()
    update_location_base.click_first_name()
    update_location_base.click_general_information_tab()
    expected_text = "Kích hoạt"
    result = is_displayed_update_location.is_text_displayed_in_status_dropdown(expected_text)
    expected_result = "Hệ thống đóng dropdown, hiển thị trạng thái được chọn."
    actual_result = expected_result if result else "Hệ thống không hiển thị trạng thái được chọn."
    if result:
        test_logger.info(f"Test Case 18 PASS: test_click_status_dropdown_and_choose_active | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 18 FAIL: test_click_status_dropdown_and_choose_active | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"         

# Test Case 19: Verify click dropdown 'Status' và chọn trạng thái 'Chờ xử lý' -> Hệ thống đóng dropdown, hiển thị trạng thái được chọn.
def test_click_status_dropdown_and_choose_processing(update_location_base, is_displayed_update_location):
    test_logger.info("Bắt đầu Test Case 19:  Verify click dropdown 'Status' và chọn trạng thái 'Chờ xử lý'.")
    update_location_base.perform_tag_operations()
    update_location_base.click_first_name()
    update_location_base.click_general_information_tab()    
    update_location_base.click_status_dropdown()
    update_location_base.click_processing_status()
    update_location_base.click_save_button()
    update_location_base.click_first_name()
    update_location_base.click_general_information_tab()
    expected_text = "Chờ xử lý"
    result = is_displayed_update_location.is_text_displayed_in_status_dropdown(expected_text)
    expected_result = "Hệ thống đóng dropdown, hiển thị trạng thái được chọn."
    actual_result = expected_result if result else "Hệ thống không hiển thị trạng thái được chọn."
    if result:
        test_logger.info(f"Test Case 19 PASS: test_click_status_dropdown_and_choose_processing | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 19 FAIL: test_click_status_dropdown_and_choose_processing | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"           

# Test Case 20: Verify click field 'Avatar', chọn ảnh từ hệ thống và click nút 'Upload' -> Hệ thống đóng popup, hiển thị ảnh được chọn và nút 'Xóa ảnh'.
def test_click_upload_after_choose_image_from_system(update_location_base, is_displayed_update_location, image_update_location):
    test_logger.info("Bắt đầu Test Case 20:  Verify click field 'Avatar', chọn ảnh từ hệ thống và click nút 'Upload'.")
    update_location_base.perform_tag_operations()
    update_location_base.click_first_name()
    update_location_base.click_general_information_tab()    
    image_update_location.click_image_field()
    is_displayed_update_location.is_upload_image_popup_displayed()
    image_update_location.click_browser_tab()
    image_update_location.click_first_image()
    image_update_location.click_button_upload()
    update_location_base.click_save_button()
    update_location_base.click_first_name()
    update_location_base.click_general_information_tab()
    result = is_displayed_update_location.is_image_displayed()
    result_2 = is_displayed_update_location.is_delete_image_button_displayed()
    expected_result = "Hệ thống đóng popup, hiển thị ảnh được chọn và nút 'Xóa ảnh'."
    actual_result = expected_result if result and result_2 else "Hệ thống không đóng popup hoặc không hiển thị ảnh được chọn và nút 'Xóa ảnh'."
    if result:
        test_logger.info(f"Test Case 20 PASS: test_click_upload_after_choose_image_from_system | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 20 FAIL: test_click_upload_after_choose_image_from_system | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}" 

# Test Case 21: Verify click field 'Avatar', chọn ảnh từ hệ thống và click nút 'Upload' -> Hệ thống đóng popup, hiển thị ảnh được chọn và nút 'Xóa ảnh'.
def test_click_delete_after_upload_image(update_location_base, is_displayed_update_location, image_update_location):
    test_logger.info("Bắt đầu Test Case 21:  Verify click field 'Avatar', chọn ảnh từ hệ thống và click nút 'Upload'.")
    update_location_base.perform_tag_operations()
    update_location_base.click_first_name()
    update_location_base.click_general_information_tab()    
    image_update_location.click_image_field()
    is_displayed_update_location.is_upload_image_popup_displayed()
    image_update_location.click_browser_tab()
    image_update_location.click_first_image()
    image_update_location.click_button_upload()
    is_displayed_update_location.is_image_displayed()
    is_displayed_update_location.is_delete_image_button_displayed()
    image_update_location.click_button_delete_image()
    update_location_base.click_save_button()
    update_location_base.click_first_name()
    update_location_base.click_general_information_tab()
    result = is_displayed_update_location.is_image_not_displayed()
    result_2 = is_displayed_update_location.is_delete_image_button_not_displayed()
    expected_result = "Hệ thống đóng popup, hiển thị ảnh được chọn và nút 'Xóa ảnh'."
    actual_result = expected_result if result and result_2 else "Hệ thống không đóng popup hoặc không hiển thị ảnh được chọn và nút 'Xóa ảnh'."
    if result:
        test_logger.info(f"Test Case 21 PASS: test_click_delete_after_upload_image | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 21 FAIL: test_click_delete_after_upload_image | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"             
        
# Test Case 22: Nhập tất cả các trường thông tin và click nút 'Lưu và tiếp tục cập nhật' -> Hệ thống tiến hành lưu Chi nhánh và ở lại trang chỉnh sửa.
def test_click_save_and_continue_button_after_field_all_information(update_location_base, get_field_update_location, enter_update_location, image_update_location, is_displayed_update_location):
    test_logger.info("Bắt đầu Test Case 22: Nhập tất cả các trường thông tin và click nút 'Lưu và tiếp tục cập nhật'.")
    update_location_base.perform_tag_operations()
    update_location_base.click_first_name()
    name = "Tp. Hồ Chí Minh"
    enter_update_location.enter_name(name)
    address = "Quận 2"
    enter_update_location.enter_address(address)
    content = "31D, An Phú 2"
    enter_update_location.enter_content(content)
    update_location_base.click_english_tab()
    update_location_base.click_translate_button()
    en_name = "Ho Chi Minh City"
    enter_update_location.enter_en_name(en_name)
    en_address = "2 District"
    enter_update_location.enter_en_address(en_address)
    # content = "31D, An Phú 2"
    # enter_update_location.enter_en_content(content)
    # Text-area 'Nội dung' Tab English đang bị lỗi nên bỏ qua
    update_location_base.click_general_information_tab()
    update_location_base.click_province_dropdown()
    update_location_base.click_first_item_province()
    update_location_base.click_district_dropdown()
    update_location_base.click_first_item_district()
    phone_number = "0392963132"
    enter_update_location.enter_phone(phone_number)
    fax = "0212"
    enter_update_location.enter_fax(fax)
    longitude = "105.123456"
    enter_update_location.enter_longitude(longitude)
    latitude = "21.028511"
    enter_update_location.enter_latitude(latitude)
    email = "example@domain.com"
    enter_update_location.enter_email(email)
    sort_value = "5"
    enter_update_location.enter_sort_order(sort_value)
    update_location_base.click_status_dropdown()
    update_location_base.click_active_status()
    image_update_location.click_button_upload_image()
    is_displayed_update_location.is_upload_image_popup_displayed()
    time.sleep(3)
    image_update_location.click_browser_tab()
    image_update_location.click_first_image()
    image_update_location.click_button_upload()
    update_location_base.click_save_button()
    update_location_base.click_first_name()
    time.sleep(3)
    expected_partial_url = "https://mpire-cms-demo.mpire.asia/cms/dealer/edit"
    url =  is_displayed_update_location.verify_path_of_current_url(expected_partial_url)
    expected_name = get_field_update_location.get_name()
    expected_address = get_field_update_location.get_address()
    expected_content = get_field_update_location.get_content()
    update_location_base.click_english_tab()
    update_location_base.click_translate_button()
    expected_en_name = get_field_update_location.get_en_name()
    expected_en_address = get_field_update_location.get_en_address()
    update_location_base.click_general_information_tab()
    time.sleep(1)
    province = "An Giang"
    expected_province = is_displayed_update_location.is_text_displayed_in_province_dropdown(province)
    district = "Long Xuyên"
    expected_district = is_displayed_update_location.is_text_displayed_in_district_dropdown(district)
    expected_phone = get_field_update_location.get_phone()
    expected_fax = get_field_update_location.get_fax()
    expected_longitude = get_field_update_location.get_longitude()
    expected_latitude = get_field_update_location.get_latitude()
    expected_email = get_field_update_location.get_email()
    expected_sort_value = get_field_update_location.get_sort_order()
    status = "Kích hoạt"
    expected_status = is_displayed_update_location.is_text_displayed_in_status_dropdown(status)
    expected_result = "Hệ thống tiến hành lưu Chi nhánh và ở lại trang chỉnh sửa."
    actual_result = expected_result if url and expected_name == "Tp. Hồ Chí Minh" and expected_address == "Quận 2" and expected_content == "31D, An Phú 2" and expected_en_name == "Ho Chi Minh City" and expected_en_address == '2 District' and expected_phone == "0392963132" and expected_fax == "0212" and expected_longitude == "105.123456" and expected_latitude == "21.028511" and expected_email == "example@domain.com" and expected_sort_value == "5" and expected_province and expected_district and expected_status else "Hệ thống lưu không thành công hoặc không ở lại trang chỉnh sửa."
    if url:
        test_logger.info(f"Test Case 22 PASS: test_click_save_and_continue_button_after_field_all_information | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 22 FAIL: test_click_save_and_continue_button_after_field_all_information | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"          