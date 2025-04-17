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
            pytest.fail("Không thể đăng nhập!")
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

# # Test Case 1: Verify khi click Tên của chi nhánh đầu tiên -> Hệ thống chuyển hướng đến trang chỉnh sửa chi nhánh đầu tiên
# def test_click_first_location_name(update_location_base, is_displayed_update_location):
#     test_logger.info("Bắt đầu Test Case 1: Verify khi click Tên của chi nhánh đầu tiên.")
#     update_location_base.perform_tag_operations()
#     update_location_base.click_first_name()
#     expected_url = "https://mpire-cms-demo.mpire.asia/cms/dealer/edit"
#     result = is_displayed_update_location.verify_path_of_current_url(expected_url)
#     expected_result = f"Hệ thống chuyển hướng đến trang chỉnh sửa."
#     actual_result = expected_result if result else f"Hệ thống không chuyển hướng đến trang chỉnh sửa."
#     if result:
#         test_logger.info(f"Test Case 1 PASS: test_click_first_location_name | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 1 FAIL: test_click_first_location_name | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"

# # Test Case 2: Verify khi click nút '...' của chi nhánh đầu tiên và chọn Chi tiết -> Hệ thống chuyển hướng đến trang chỉnh sửa chi nhánh đầu tiên
# def test_click_first_menu_button_choose_detail(update_location_base, is_displayed_update_location):
#     test_logger.info("Bắt đầu Test Case 2: Verify khi click nút '...' của chi nhánh đầu tiên và chọn Chi tiết.")
#     update_location_base.perform_tag_operations()
#     update_location_base.click_first_menu_button()
#     update_location_base.click_first_detail_menu_item()
#     expected_url = "https://mpire-cms-demo.mpire.asia/cms/dealer/edit"
#     result = is_displayed_update_location.verify_path_of_current_url(expected_url)
#     expected_result = f"Hệ thống chuyển hướng đến trang chỉnh sửa."
#     actual_result = expected_result if result else f"Hệ thống không chuyển hướng đến trang chỉnh sửa."
#     if result:
#         test_logger.info(f"Test Case 2 PASS: test_click_first_menu_button_choose_detail | Expected: {expected_result} | Actual: {actual_result} | Status: PASS")
#     else:
#         test_logger.error(f"Test Case 2 FAIL: test_click_first_menu_button_choose_detail | Expected: {expected_result} | Actual: {actual_result} | Status: FAIL")
#         assert False, f"Expected: {expected_result} | Actual: {actual_result}"
        
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