import time
import pytest
from utils.login import Login
from utils.logger import LoggerConfig
from utils.driver_setup import get_driver
from pages.location.new_location.new_location_base import NewLocationBase
from pages.location.new_location.enter_new_location import EnterNewLocation
from pages.location.new_location.get_field_new_location import GetFieldNewLocation
from pages.location.new_location.is_displayed_new_location import IsDisplayedNewLocation
from pages.location.new_location.image_new_location import ImageNewLocation
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
def new_location_base(setup_driver):
    return NewLocationBase(setup_driver)

@pytest.fixture
def enter_new_location(setup_driver):
    return EnterNewLocation(setup_driver)

@pytest.fixture
def get_field_new_location(setup_driver):
    return GetFieldNewLocation(setup_driver)

@pytest.fixture
def is_displayed_new_location(setup_driver):
    return IsDisplayedNewLocation(setup_driver)

@pytest.fixture
def image_new_location(setup_driver):
    return ImageNewLocation(setup_driver)

# # Test Case 1: Verify khi nhấn nút 'Tạo mới' -> Hệ thống điều hướng đến trang 'Tạo mới chi nhánh'.
# def test_click_create_button(new_location_base):
#     test_logger.info("Bắt đầu Test Case 1: Verify khi nhấn nút 'Tạo mới'.")
#     new_location_base.perform_tag_operations()
#     result = new_location_base.click_create_button()
#     expected_result = "Hệ thống điều hướng đến trang 'Tạo mới chi nhánh'."
#     actual_result = expected_result if result else "Hệ thống không điều hướng đến trang 'Tạo mới chi nhánh'."
#     if result:
#         test_logger.info(f"Test Case 1 PASS: test_click_create_button | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 1 FAIL: test_click_create_button | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 2: Verify khi nhập Tên chi nhánh ở tab Tiếng Việt -> Hệ thống hiển thị thông tin vừa nhập
# def test_enter_vi_location_name(new_location_base, enter_new_location, get_field_new_location):
#     test_logger.info("Bắt đầu Test Case 2: Verify khi nhập Tên chi nhánh ở tab Tiếng Việt.")
#     new_location_base.perform_tag_operations()
#     new_location_base.click_create_button()
#     name = "Tp. Hồ Chí Minh"
#     enter_new_location.enter_name(name)
#     result = get_field_new_location.get_name()
#     expected_result = "Hệ thống hiển thị thông tin vừa nhập."
#     actual_result = expected_result if result == "Tp. Hồ Chí Minh" else "Hệ thống không hiển thị thông tin vừa nhập."
#     if result:
#         test_logger.info(f"Test Case 2 PASS: test_enter_vi_location_name | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 2 FAIL: test_enter_vi_location_name | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 3: Verify khi nhập Địa chỉ chi nhánh ở tab Tiếng Việt -> Hệ thống hiển thị thông tin vừa nhập
# def test_enter_vi_location_address(new_location_base, enter_new_location, get_field_new_location):
#     test_logger.info("Bắt đầu Test Case 3: Verify khi nhập Địa chỉ chi nhánh ở tab Tiếng Việt.")
#     new_location_base.perform_tag_operations()
#     new_location_base.click_create_button()
#     address = "Quận 2"
#     enter_new_location.enter_address(address)
#     result = get_field_new_location.get_address()
#     expected_result = "Hệ thống hiển thị thông tin vừa nhập."
#     actual_result = expected_result if result == "Quận 2" else "Hệ thống không hiển thị thông tin vừa nhập."
#     if result:
#         test_logger.info(f"Test Case 3 PASS: test_enter_vi_location_address | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 3 FAIL: test_enter_vi_location_address | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 4: Verify khi nhập Nội dung chi nhánh ở tab Tiếng Việt -> Hệ thống hiển thị thông tin vừa nhập
# def test_enter_vi_location_content(new_location_base, enter_new_location, get_field_new_location):
#     test_logger.info("Bắt đầu Test Case 4: Verify khi nhập Địa chỉ chi nhánh ở tab Tiếng Việt.")
#     new_location_base.perform_tag_operations()
#     new_location_base.click_create_button()
#     content = "31D, An Phú 2"
#     enter_new_location.enter_content(content)
#     result = get_field_new_location.get_content()
#     expected_result = "Hệ thống hiển thị thông tin vừa nhập."
#     actual_result = expected_result if result == "31D, An Phú 2" else "Hệ thống không hiển thị thông tin vừa nhập."
#     if result:
#         test_logger.info(f"Test Case 4 PASS: test_enter_vi_location_content | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 4 FAIL: test_enter_vi_location_content | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"        

# # Lỗi không tìm được phần tử
# # Test Case 5: Verify khi nhập Tên chi nhánh ở tab English -> Hệ thống hiển thị thông tin vừa nhập
# def test_enter_en_location_name(new_location_base, enter_new_location, get_field_new_location):
#     test_logger.info("Bắt đầu Test Case 2: Verify khi nhập Tên chi nhánh ở tab English.")
#     new_location_base.perform_tag_operations()
#     new_location_base.click_create_button()
#     new_location_base.click_english_tab()
#     new_location_base.click_translate_button()
#     time.sleep(0.5)
#     name = "Ho Chi Minh City"
#     enter_new_location.enter_name(name)
#     result = get_field_new_location.get_name()
#     expected_result = "Hệ thống hiển thị thông tin vừa nhập."
#     actual_result = expected_result if result == "Ho Chi Minh City" else "Hệ thống không hiển thị thông tin vừa nhập."
#     if result:
#         test_logger.info(f"Test Case 5 PASS: test_enter_en_location_name | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 5 FAIL: test_enter_en_location_name | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Lỗi không tìm được phần tử
# # Test Case 6: Verify khi nhập Địa chỉ chi nhánh ở tab English -> Hệ thống hiển thị thông tin vừa nhập
# def test_enter_en_location_address(new_location_base, enter_new_location, get_field_new_location):
#     test_logger.info("Bắt đầu Test Case 3: Verify khi nhập Địa chỉ chi nhánh ở tab English.")
#     new_location_base.perform_tag_operations()
#     new_location_base.click_create_button()
#     new_location_base.click_english_tab()
#     new_location_base.click_translate_button()
#     time.sleep(0.5)
#     address = "2 District"
#     enter_new_location.enter_address(address)
#     result = get_field_new_location.get_address()
#     expected_result = "Hệ thống hiển thị thông tin vừa nhập."
#     actual_result = expected_result if result == "2 District" else "Hệ thống không hiển thị thông tin vừa nhập."
#     if result:
#         test_logger.info(f"Test Case 6 PASS: test_enter_en_location_address | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 6 FAIL: test_enter_en_location_address | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Lỗi không tìm được phần tử
# # Test Case 7: Verify khi nhập Nội dung chi nhánh ở tab English -> Hệ thống hiển thị thông tin vừa nhập
# def test_enter_en_location_content(new_location_base, enter_new_location, get_field_new_location):
#     test_logger.info("Bắt đầu Test Case 4: Verify khi nhập Địa chỉ chi nhánh ở tab English.")
#     new_location_base.perform_tag_operations()
#     new_location_base.click_create_button()
#     content = "31D, An Phu 2"
#     enter_new_location.enter_content(content)
#     result = get_field_new_location.get_content()
#     expected_result = "Hệ thống hiển thị thông tin vừa nhập."
#     actual_result = expected_result if result == "31D, An Phu 2" else "Hệ thống không hiển thị thông tin vừa nhập."
#     if result:
#         test_logger.info(f"Test Case 7 PASS: test_enter_en_location_content | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 7 FAIL: test_enter_en_location_content | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"           

# # Test Case 8: Verify khi nhấn dropdown 'Tỉnh/Thành phố' và chọn Tỉnh/Thành phố đầu tiên -> Hệ thống hiển thị Tỉnh/Thành phố được chọn.
# def test_click_province_dropdown_and_choose_province(new_location_base, is_displayed_new_location):
#     test_logger.info("Bắt đầu Test Case 8: Verify khi nhấn dropdown 'Tỉnh/Thành phố' và chọn Tỉnh/Thành phố đầu tiên.")
#     new_location_base.perform_tag_operations()
#     new_location_base.click_create_button()
#     new_location_base.click_general_information_tab()
#     new_location_base.click_province_dropdown()
#     new_location_base.click_first_item_province()
#     time.sleep(1)
#     expected_text = 'An Giang'
#     result = is_displayed_new_location.is_text_displayed_in_province_dropdown(expected_text)
#     expected_result = "Hệ thống hiển thị Tỉnh/Thành phố được chọn."
#     actual_result = expected_result if result else "Hệ thống không hiển thị Tỉnh/Thành phố được chọn."
#     if result:
#         test_logger.info(f"Test Case 8 PASS: test_click_province_dropdown_and_choose_province | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 8 FAIL: test_click_province_dropdown_and_choose_province | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# # Test Case 9: Verify khi nhấn dropdown 'Huyện/Quận' khi chưa chọn Tỉnh/Thành phố -> Hệ thống mở dropdown chỉ có giá trị mặc định.
# def test_click_district_dropdown(new_location_base, is_displayed_new_location):
#     test_logger.info("Bắt đầu Test Case 9: Verify khi nhấn dropdown 'Huyện/Quận' khi chưa chọn Tỉnh/Thành phố.")
#     new_location_base.perform_tag_operations()
#     new_location_base.click_create_button()
#     new_location_base.click_general_information_tab()
#     new_location_base.click_district_dropdown()
#     result = is_displayed_new_location.is_first_district_item_not_present()
#     expected_result = "Hệ thống mở dropdown chỉ có giá trị mặc định."
#     actual_result = expected_result if result else "Hệ thống hiện thị Huyện/Quận tương ứng của Tỉnh/Thành phố."
#     if result:
#         test_logger.info(f"Test Case 9 PASS: test_click_district_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 9 FAIL: test_click_district_dropdown | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"    
        
# # Test Case 10: Verify khi nhấn dropdown 'Huyện/Quận' sau khi chọn Tỉnh/Thành phố -> Hệ thống mở dropdown chỉ có giá trị mặc định.
# def test_click_district_dropdown_after_choose_province(new_location_base, is_displayed_new_location):
#     test_logger.info("Bắt đầu Test Case 10: Verify khi nhấn dropdown 'Huyện/Quận' khi chưa chọn Tỉnh/Thành phố.")
#     new_location_base.perform_tag_operations()
#     new_location_base.click_create_button()
#     new_location_base.click_general_information_tab()
#     new_location_base.click_province_dropdown()
#     new_location_base.click_first_item_province()
#     new_location_base.click_district_dropdown()
#     expected_text = "Long Xuyên"
#     result = is_displayed_new_location.is_text_displayed_in_first_district_item(expected_text)
#     expected_result = "Hệ thống hiện thị Huyện/Quận tương ứng của Tỉnh/Thành phố."
#     actual_result = expected_result if result else "Hệ thống mở dropdown chỉ có giá trị mặc định."
#     if result:
#         test_logger.info(f"Test Case 10 PASS: test_click_district_dropdown_after_choose_province | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 10 FAIL: test_click_district_dropdown_after_choose_province | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"              

# # Test Case 11: Verify khi nhấn dropdown 'Huyện/Quận' và chọn Huyện/Quận đầu tiên -> Hệ thống hiển thị Huyện/Quận được chọn
# def test_click_district_dropdown_and_choose_district(new_location_base, is_displayed_new_location):
#     test_logger.info("Bắt đầu Test Case 11: Verify khi nhấn dropdown 'Huyện/Quận'và chọn Huyện/Quận đầu tiên.")
#     new_location_base.perform_tag_operations()
#     new_location_base.click_create_button()
#     new_location_base.click_general_information_tab()
#     new_location_base.click_province_dropdown()
#     new_location_base.click_first_item_province()
#     new_location_base.click_district_dropdown()
#     new_location_base.click_first_item_district()
#     expected_text = "Long Xuyên"
#     result = is_displayed_new_location.is_text_displayed_in_district_dropdown(expected_text)
#     expected_result = "Hệ thống hiển thị Huyện/Quận được chọn."
#     actual_result = expected_result if result else "Hệ thống không hiển thị Huyện/Quận được chọn."
#     if result:
#         test_logger.info(f"Test Case 11 PASS: test_click_district_dropdown_and_choose_district | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 11 FAIL: test_click_district_dropdown_and_choose_district | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"  

# # Test Case 12: Verify khi nhập Số điện thoại ở tab 'Thông tin chung' -> Hệ thống hiển thị thông tin vừa nhập
# def test_enter_phone_number(new_location_base, enter_new_location, get_field_new_location):
#     test_logger.info("Bắt đầu Test Case 12: Verify khi nhập Số điện thoại ở tab 'Thông tin chung'.")
#     new_location_base.perform_tag_operations()
#     new_location_base.click_create_button()
#     new_location_base.click_general_information_tab()
#     phone_number = "0392963132"
#     enter_new_location.enter_phone(phone_number)
#     result = get_field_new_location.get_phone()
#     expected_result = "Hệ thống hiển thị thông tin vừa nhập."
#     actual_result = expected_result if result == "0392963132" else "Hệ thống không hiển thị thông tin vừa nhập."
#     if result:
#         test_logger.info(f"Test Case 12 PASS: test_enter_phone_number | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 12 FAIL: test_enter_phone_number | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
# # Test Case 13: Verify khi nhập FAX ở tab 'Thông tin chung' -> Hệ thống hiển thị thông tin vừa nhập
# def test_enter_fax(new_location_base, enter_new_location, get_field_new_location):
#     test_logger.info("Bắt đầu Test Case 13: Verify khi nhập FAX ở tab 'Thông tin chung'.")
#     new_location_base.perform_tag_operations()
#     new_location_base.click_create_button()
#     new_location_base.click_general_information_tab()
#     fax = "0212"
#     enter_new_location.enter_fax(fax)
#     result = get_field_new_location.get_fax()
#     expected_result = "Hệ thống hiển thị thông tin vừa nhập."
#     actual_result = expected_result if result == "0212" else "Hệ thống không hiển thị thông tin vừa nhập."
#     if result:
#         test_logger.info(f"Test Case 13 PASS: test_enter_fax | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 13 FAIL: test_enter_fax | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"        
        
# # Test Case 14: Verify khi nhập Kinh độ ở tab 'Thông tin chung' -> Hệ thống hiển thị thông tin vừa nhập
# def test_enter_longitude(new_location_base, enter_new_location, get_field_new_location):
#     test_logger.info("Bắt đầu Test Case 14: Verify khi nhập Kinh độ ở tab 'Thông tin chung'.")
#     new_location_base.perform_tag_operations()
#     new_location_base.click_create_button()
#     new_location_base.click_general_information_tab()
#     longitude = "105.123456"
#     enter_new_location.enter_longitude(longitude)
#     result = get_field_new_location.get_longitude()
#     expected_result = "Hệ thống hiển thị thông tin vừa nhập."
#     actual_result = expected_result if result == longitude else "Hệ thống không hiển thị thông tin vừa nhập."
#     if result == longitude:
#         test_logger.info(f"Test Case 14 PASS: test_enter_longitude | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 14 FAIL: test_enter_longitude | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 15: Verify khi nhập Vĩ độ ở tab 'Thông tin chung' -> Hệ thống hiển thị thông tin vừa nhập
# def test_enter_latitude(new_location_base, enter_new_location, get_field_new_location):
#     test_logger.info("Bắt đầu Test Case 15: Verify khi nhập Vĩ độ ở tab 'Thông tin chung'.")
#     new_location_base.perform_tag_operations()
#     new_location_base.click_create_button()
#     new_location_base.click_general_information_tab()
#     latitude = "21.028511"
#     enter_new_location.enter_latitude(latitude)
#     result = get_field_new_location.get_latitude()
#     expected_result = "Hệ thống hiển thị thông tin vừa nhập."
#     actual_result = expected_result if result == latitude else "Hệ thống không hiển thị thông tin vừa nhập."
#     if result == latitude:
#         test_logger.info(f"Test Case 15 PASS: test_enter_latitude | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 15 FAIL: test_enter_latitude | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 16: Verify khi nhập Email ở tab 'Thông tin chung' -> Hệ thống hiển thị thông tin vừa nhập
# def test_enter_email(new_location_base, enter_new_location, get_field_new_location):
#     test_logger.info("Bắt đầu Test Case 16: Verify khi nhập Email ở tab 'Thông tin chung'.")
#     new_location_base.perform_tag_operations()
#     new_location_base.click_create_button()
#     new_location_base.click_general_information_tab()
#     email = "example@domain.com"
#     enter_new_location.enter_email(email)
#     result = get_field_new_location.get_email()
#     expected_result = "Hệ thống hiển thị thông tin vừa nhập."
#     actual_result = expected_result if result == email else "Hệ thống không hiển thị thông tin vừa nhập."
#     if result == email:
#         test_logger.info(f"Test Case 16 PASS: test_enter_email | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 16 FAIL: test_enter_email | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 17: Verify khi nhập Giá trị sắp xếp ở tab 'Thông tin chung' -> Hệ thống hiển thị thông tin vừa nhập
# def test_enter_sort_order(new_location_base, enter_new_location, get_field_new_location):
#     test_logger.info("Bắt đầu Test Case 17: Verify khi nhập Giá trị sắp xếp ở tab 'Thông tin chung'.")
#     new_location_base.perform_tag_operations()
#     new_location_base.click_create_button()
#     new_location_base.click_general_information_tab()
#     sort_value = "5"
#     enter_new_location.enter_sort_order(sort_value)
#     result = get_field_new_location.get_sort_order()
#     expected_result = "Hệ thống hiển thị thông tin vừa nhập."
#     actual_result = expected_result if result == sort_value else "Hệ thống không hiển thị thông tin vừa nhập."
#     if result == sort_value:
#         test_logger.info(f"Test Case 17 PASS: test_enter_sort_order | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 17 FAIL: test_enter_sort_order | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 18: Verify click dropdown 'Status' và chọn trạng thái 'Kích hoạt' -> Hệ thống đóng dropdown, hiển thị trạng thái được chọn.
# def test_click_status_dropdown_and_choose_active(new_location_base, is_displayed_new_location):
#     test_logger.info("Bắt đầu Test Case 18:  Verify click dropdown 'Status' và chọn trạng thái 'Kích hoạt'.")
#     new_location_base.perform_tag_operations()
#     new_location_base.click_create_button()
#     new_location_base.click_general_information_tab()    
#     new_location_base.click_status_dropdown()
#     new_location_base.click_active_status()
#     expected_text = "Kích hoạt"
#     result = is_displayed_new_location.is_text_displayed_in_status_dropdown(expected_text)
#     expected_result = "Hệ thống đóng dropdown, hiển thị trạng thái được chọn."
#     actual_result = expected_result if result else "Hệ thống không hiển thị trạng thái được chọn."
#     if result:
#         test_logger.info(f"Test Case 18 PASS: test_click_status_dropdown_and_choose_active | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 18 FAIL: test_click_status_dropdown_and_choose_active | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"         

# # Test Case 19: Verify click dropdown 'Status' và chọn trạng thái 'Chờ xử lý' -> Hệ thống đóng dropdown, hiển thị trạng thái được chọn.
# def test_click_status_dropdown_and_choose_processing(new_location_base, is_displayed_new_location):
#     test_logger.info("Bắt đầu Test Case 19:  Verify click dropdown 'Status' và chọn trạng thái 'Chờ xử lý'.")
#     new_location_base.perform_tag_operations()
#     new_location_base.click_create_button()
#     new_location_base.click_general_information_tab()    
#     new_location_base.click_status_dropdown()
#     new_location_base.click_processing_status()
#     expected_text = "Chờ xử lý"
#     result = is_displayed_new_location.is_text_displayed_in_status_dropdown(expected_text)
#     expected_result = "Hệ thống đóng dropdown, hiển thị trạng thái được chọn."
#     actual_result = expected_result if result else "Hệ thống không hiển thị trạng thái được chọn."
#     if result:
#         test_logger.info(f"Test Case 19 PASS: test_click_status_dropdown_and_choose_processing | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 19 FAIL: test_click_status_dropdown_and_choose_processing | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"           

# # Test Case 20: Verify click field 'Avatar' -> Hệ thống hiển thị popup 'Upload image'.
# def test_click_field_avatar(new_location_base, is_displayed_new_location, image_new_location):
#     test_logger.info("Bắt đầu Test Case 20:  Verify click field 'Avatar'.")
#     new_location_base.perform_tag_operations()
#     new_location_base.click_create_button()
#     new_location_base.click_general_information_tab()    
#     image_new_location.click_image_field()
#     result = is_displayed_new_location.is_upload_image_popup_displayed()
#     expected_result = "Hệ thống hiển thị popup 'Upload image'."
#     actual_result = expected_result if result else "Hệ thống không hiển thị popup 'Upload image'."
#     if result:
#         test_logger.info(f"Test Case 20 PASS: test_click_field_avatar | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 20 FAIL: test_click_field_avatar | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"  

# # Test Case 21: Verify click field 'Avatar' và click nút 'Upload' -> Hệ thống đóng popup và không hiển thị nút 'Xóa ảnh'.
# def test_click_upload_without_choose_image(new_location_base, is_displayed_new_location, image_new_location):
#     test_logger.info("Bắt đầu Test Case 21:  Verify click field 'Avatar' và click nút 'Upload'.")
#     new_location_base.perform_tag_operations()
#     new_location_base.click_create_button()
#     new_location_base.click_general_information_tab()    
#     image_new_location.click_image_field()
#     is_displayed_new_location.is_upload_image_popup_displayed()
#     image_new_location.click_button_upload()
#     result = is_displayed_new_location.is_delete_image_button_not_displayed()
#     expected_result = "Không hiển thị nút 'Xóa ảnh'."
#     actual_result = expected_result if result else "Hệ thống hiển thị nút 'Xóa ảnh'."
#     if result:
#         test_logger.info(f"Test Case 21 PASS: test_click_field_avatar_and_click_upload | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 21 FAIL: test_click_field_avatar_and_click_upload | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"  

# # Test Case 22: Verify click field 'Avatar', chọn ảnh từ hệ thống và click nút 'Upload' -> Hệ thống đóng popup, hiển thị ảnh được chọn và nút 'Xóa ảnh'.
# def test_click_upload_after_choose_image_from_system(new_location_base, is_displayed_new_location, image_new_location):
#     test_logger.info("Bắt đầu Test Case 22:  Verify click field 'Avatar', chọn ảnh từ hệ thống và click nút 'Upload'.")
#     new_location_base.perform_tag_operations()
#     new_location_base.click_create_button()
#     new_location_base.click_general_information_tab()    
#     image_new_location.click_image_field()
#     is_displayed_new_location.is_upload_image_popup_displayed()
#     image_new_location.click_browser_tab()
#     image_new_location.click_first_image()
#     image_new_location.click_button_upload()
#     result = is_displayed_new_location.is_image_displayed()
#     result_2 = is_displayed_new_location.is_delete_image_button_displayed()
#     expected_result = "Hệ thống đóng popup, hiển thị ảnh được chọn và nút 'Xóa ảnh'."
#     actual_result = expected_result if result and result_2 else "Hệ thống không đóng popup hoặc không hiển thị ảnh được chọn và nút 'Xóa ảnh'."
#     if result:
#         test_logger.info(f"Test Case 22 PASS: test_click_upload_after_choose_image_from_system | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 22 FAIL: test_click_upload_after_choose_image_from_system | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}" 

# # Test Case 23: Verify click field 'Avatar', chọn ảnh từ hệ thống và click nút 'Upload' -> Hệ thống đóng popup, hiển thị ảnh được chọn và nút 'Xóa ảnh'.
# def test_click_delete_after_upload_image(new_location_base, is_displayed_new_location, image_new_location):
#     test_logger.info("Bắt đầu Test Case 23:  Verify click field 'Avatar', chọn ảnh từ hệ thống và click nút 'Upload'.")
#     new_location_base.perform_tag_operations()
#     new_location_base.click_create_button()
#     new_location_base.click_general_information_tab()    
#     image_new_location.click_image_field()
#     is_displayed_new_location.is_upload_image_popup_displayed()
#     image_new_location.click_browser_tab()
#     image_new_location.click_first_image()
#     image_new_location.click_button_upload()
#     is_displayed_new_location.is_image_displayed()
#     is_displayed_new_location.is_delete_image_button_displayed()
#     image_new_location.click_button_delete_image()
#     result = is_displayed_new_location.is_image_not_displayed()
#     result_2 = is_displayed_new_location.is_delete_image_button_not_displayed()
#     expected_result = "Hệ thống đóng popup, hiển thị ảnh được chọn và nút 'Xóa ảnh'."
#     actual_result = expected_result if result and result_2 else "Hệ thống không đóng popup hoặc không hiển thị ảnh được chọn và nút 'Xóa ảnh'."
#     if result:
#         test_logger.info(f"Test Case 23 PASS: test_click_delete_after_upload_image | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 23 FAIL: test_click_delete_after_upload_image | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"     

# # Test Case 24: Nhập tất cả các trường thông tin và click nút 'Lưu' -> Hệ thống tiến hành lưu Chi nhánh và chuyển hướng về trang 'Danh sách chi nhánh'.
# def test_click_save_button_after_field_all_information(new_location_base, get_field_new_location, enter_new_location, image_new_location, is_displayed_new_location):
#     test_logger.info("Bắt đầu Test Case 24: Nhập tất cả các trường thông tin và click nút 'Lưu'.")
#     new_location_base.perform_tag_operations()
#     new_location_base.click_create_button()
#     name = "Tp. Hồ Chí Minh"
#     enter_new_location.enter_name(name)
#     address = "Quận 2"
#     enter_new_location.enter_address(address)
#     content = "31D, An Phú 2"
#     enter_new_location.enter_content(content)
#     # Tab English đang bị lỗi nên bỏ qua
#     new_location_base.click_general_information_tab()
#     new_location_base.click_province_dropdown()
#     new_location_base.click_first_item_province()
#     new_location_base.click_district_dropdown()
#     new_location_base.click_first_item_district()
#     phone_number = "0392963132"
#     enter_new_location.enter_phone(phone_number)
#     fax = "0212"
#     enter_new_location.enter_fax(fax)
#     longitude = "105.123456"
#     enter_new_location.enter_longitude(longitude)
#     latitude = "21.028511"
#     enter_new_location.enter_latitude(latitude)
#     email = "example@domain.com"
#     enter_new_location.enter_email(email)
#     sort_value = "5"
#     enter_new_location.enter_sort_order(sort_value)
#     new_location_base.click_status_dropdown()
#     new_location_base.click_active_status()
#     image_new_location.click_button_upload_image()
#     is_displayed_new_location.is_upload_image_popup_displayed()
#     time.sleep(3)
#     image_new_location.click_browser_tab()
#     image_new_location.click_first_image()
#     image_new_location.click_button_upload()
#     new_location_base.click_save_button()
#     time.sleep(1.5)
#     expected_url = "https://mpire-cms-demo.mpire.asia/cms/dealer?page=1"
#     url = new_location_base.verify_current_url(expected_url)
#     expected_name = "Tp. Hồ Chí Minh"
#     result = get_field_new_location.is_first_location_name_matched(expected_name)
#     expected_result = "Hệ thống tiến hành lưu Chi nhánh và chuyển hướng về trang 'Danh sách chi nhánh'."
#     actual_result = expected_result if url and result == "Tp. Hồ Chí Minh" else "Hệ thống lưu không thành công hoặc không chuyyển hướng về trang danh sách hoặc không hiển thị chi nhánh mới lưu trên danh sách."
#     if result:
#         test_logger.info(f"Test Case 24 PASS: test_click_save_button_after_field_all_information | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 24 FAIL: test_click_save_button_after_field_all_information | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# Test Case 25: Nhập tất cả các trường thông tin và click nút 'Lưu và tiếp tục cập nhật' -> Hệ thống tiến hành lưu Chi nhánh và ở lại trang chỉnh sửa.
def test_click_save_and_continue_button_after_field_all_information(new_location_base, get_field_new_location, enter_new_location, image_new_location, is_displayed_new_location):
    test_logger.info("Bắt đầu Test Case 24: Nhập tất cả các trường thông tin và click nút 'Lưu và tiếp tục cập nhật'.")
    new_location_base.perform_tag_operations()
    new_location_base.click_create_button()
    name = "Tp. Hồ Chí Minh"
    enter_new_location.enter_name(name)
    address = "Quận 2"
    enter_new_location.enter_address(address)
    content = "31D, An Phú 2"
    enter_new_location.enter_content(content)
    # Tab English đang bị lỗi nên bỏ qua
    new_location_base.click_general_information_tab()
    new_location_base.click_province_dropdown()
    new_location_base.click_first_item_province()
    new_location_base.click_district_dropdown()
    new_location_base.click_first_item_district()
    phone_number = "0392963132"
    enter_new_location.enter_phone(phone_number)
    fax = "0212"
    enter_new_location.enter_fax(fax)
    longitude = "105.123456"
    enter_new_location.enter_longitude(longitude)
    latitude = "21.028511"
    enter_new_location.enter_latitude(latitude)
    email = "example@domain.com"
    enter_new_location.enter_email(email)
    sort_value = "5"
    enter_new_location.enter_sort_order(sort_value)
    new_location_base.click_status_dropdown()
    new_location_base.click_active_status()
    image_new_location.click_button_upload_image()
    is_displayed_new_location.is_upload_image_popup_displayed()
    time.sleep(3)
    image_new_location.click_browser_tab()
    image_new_location.click_first_image()
    image_new_location.click_button_upload()
    new_location_base.click_save_and_continue_button()
    time.sleep(1.5)
    expected_partial_url = "https://mpire-cms-demo.mpire.asia/cms/dealer/edit"
    url =  is_displayed_new_location.verify_path_of_current_url(expected_partial_url)
    expected_name = get_field_new_location.get_name()
    expected_address = get_field_new_location.get_address()
    expected_content = get_field_new_location.get_content()
    new_location_base.click_general_information_tab()
    province = "An Giang"
    expected_province = is_displayed_new_location.is_text_displayed_in_province_dropdown(province)
    district = "Long Xuyên"
    expected_district = is_displayed_new_location.is_text_displayed_in_district_dropdown(district)
    expected_phone = get_field_new_location.get_phone()
    expected_fax = get_field_new_location.get_fax()
    expected_longitude = get_field_new_location.get_longitude()
    expected_latitude = get_field_new_location.get_latitude()
    expected_email = get_field_new_location.get_email()
    expected_sort_order = get_field_new_location.get_sort_order()
    status = "Kích hoạt"
    expected_status = is_displayed_new_location.is_text_displayed_in_status_dropdown(status)
    expected_result = "Hệ thống tiến hành lưu Chi nhánh và ở lại trang chỉnh sửa."
    actual_result = expected_result if url else "Hệ thống lưu không thành công hoặc không ở lại trang chỉnh sửa."
    if url:
        test_logger.info(f"Test Case 24 PASS: test_click_save_button_after_field_all_information | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
    else:
        test_logger.error(f"Test Case 24 FAIL: test_click_save_button_after_field_all_information | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
        assert False, f"Expected: {expected_result} | Actual: {actual_result}"                          