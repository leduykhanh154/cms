import pytest
import logging
import time
from utils.login import Login
from pages.pagev2 import PageV2
from utils.driver_setup import get_driver
from locators.locator_pagev2 import LocatorPageV2
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

 
@pytest.fixture(scope="function")
def setup_driver():
    driver = get_driver()
    login_page = Login(driver)
    login_success = login_page.login()
    if not login_success:
        pytest.fail("Không thể đăng nhập!")
    yield driver
    driver.quit()

@pytest.fixture
def pagev2(setup_driver):
    return PageV2(setup_driver)

def log_success(message):
    print(f"{message}")
    logging.info(message)

# Test Case 1: Verify khi không nhập Tiêu đề trang -> Hệ thống hiển thị thông báo lỗi Vui lòng nhập tiêu đề trang
def test_empty_page_title(pagev2, setup_driver):
    pagev2.perform_tag_operations()
    pagev2.click_create_new_button()
    pagev2.enter_page_title("")
    pagev2.click_save_button()
    error_message = pagev2.check_title_error_message()
    if error_message == "Vui lòng nhập tiêu đề trang":
        logging.info("Test Case 1 PASS: Hiển thị đúng thông báo lỗi khi không nhập tiêu đề trang.")
    else:
        logging.error(f"Test Case 1 FAILED: Không hiển thị hoặc hiển thị sai thông báo lỗi: {error_message}")
        assert False, "Thông báo lỗi không đúng hoặc không xuất hiện!"

# Test Case 2: Verify khi nhập Tiêu đề trang -> Hệ thống lưu thành công và chuyển hướng về trang danh sách
def test_save_page_and_check_in_list(pagev2, setup_driver):
    pagev2.perform_tag_operations()
    valid_title = "Trang kiểm thử"
    pagev2.enter_page_title(valid_title)
    pagev2.click_save_button()
    expected_url = "https://mpire-cms-demo.mpire.asia/cms/admin-page-v2?page=1"
    WebDriverWait(setup_driver, 10).until(EC.url_to_be(expected_url))
    if pagev2.is_page_title_in_list(valid_title):
        logging.info("Test Case 2 PASS: Lưu trang thành công và hiển thị trong danh sách.")
    else:
        logging.error("Test Case 2 FAILED: Tiêu đề trang không xuất hiện trong danh sách sau khi lưu!")
        assert False, "Tiêu đề trang không xuất hiện trong danh sách!"

# Test Case 3: Verify khi nhấn nút Thêm section -> Hệ thống hiển thị pop-up Thêm section
def test_add_section_popup_displayed(setup_driver, pagev2):
    pagev2.perform_tag_operations()
    pagev2.click_add_section_button()   
    popup_element = None
    try:
        popup_element = WebDriverWait(setup_driver, 5).until(
            EC.visibility_of_element_located(LocatorPageV2.ADD_SECTION_POPUP)
        )
    except Exception as e:
        logging.error(f"ERROR: Pop-up không xuất hiện! {e}", exc_info=True)
    if popup_element and popup_element.is_displayed():
        logging.info("Test Case 3 PASS: Pop-up thêm section hiển thị thành công.")
    else:
        logging.error("Test Case 3 FAILED: Pop-up không hiển thị sau khi nhấn 'Thêm section'.")
        assert False, "Pop-up không hiển thị sau khi nhấn 'Thêm section'."

# Test Case 4: Verify sau khi thêm section News -> Hệ thống hiển thị section News bên ngoài Danh sách section
def test_add_news_section_and_verify_display(setup_driver, pagev2):
    pagev2.perform_tag_operations()
    pagev2.click_add_section_button()
    pagev2.is_add_section_popup_displayed()
    pagev2.click_section_news_checkbox()
    pagev2.click_add_button()
    news_section_element = WebDriverWait(setup_driver, 10).until(
        EC.visibility_of_element_located(LocatorPageV2.NEWS_SECTION)
    )

    if news_section_element and news_section_element.is_displayed():
        logging.info("Test Case 4 PASS: Section 'News' đã được thêm thành công và hiển thị trong danh sách.")
    else:
        logging.error("Test Case 4 PASS: Section 'News' không hiển thị trong danh sách.")
        assert False, "Section 'News' không hiển thị sau khi thêm!"

# Test Case 5: Verify khi không nhập Tiêu đề tin tức -> Hệ thống hiển thị thông báo lỗi Vui lòng nhập tiêu đề tin tức
def test_news_section_title_validation(setup_driver, pagev2):
    pagev2.click_content_menu()
    pagev2.click_page_v2_menu()
    assert pagev2.click_create_new_button()
    assert pagev2.click_add_section_button()
    assert pagev2.is_add_section_popup_displayed()
    assert pagev2.click_section_news_checkbox()
    assert pagev2.click_add_button()
    news_section_element = pagev2.is_news_section_displayed()
    assert news_section_element is not None
    assert pagev2.click_save_button()
    error_message = pagev2.get_news_section_error_message(news_section_element)
    if error_message == "Vui lòng nhập tiêu đề tin tức":
        logging.info("PASS: Hiển thị đúng thông báo lỗi: Vui lòng nhập tiêu đề tin tức.")
    else:
        logging.error(f"FAILED: Không hiển thị hoặc hiển thị sai thông báo lỗi: {error_message}")
        assert False, "Không tìm thấy hoặc thông báo lỗi không đúng."

# Test Case 1.2: Verify khi không nhập Tiêu đề trang bam luu va tiep tuc cap nhat -> Hệ thống hiển thị thông báo lỗi Vui lòng nhập tiêu đề trang
def test_empty_page_title_2(pagev2, setup_driver):
    pagev2.perform_tag_operations()
    pagev2.enter_page_title("")
    pagev2.click_save_and_continue_button()
    error_message = pagev2.check_title_error_message()
    if error_message == "Vui lòng nhập tiêu đề trang":
        logging.info("Test Case 1.2 PASS: Hiển thị đúng thông báo lỗi khi không nhập tiêu đề trang.")
    else:
        logging.error(f"Test Case 1.2 FAILED: Không hiển thị hoặc hiển thị sai thông báo lỗi: {error_message}")
        assert False, "Thông báo lỗi không đúng hoặc không xuất hiện!"

# (Error) Test Case 2.2: Verify khi nhập Tiêu đề trang bam luu va tiep tuc cap nhat -> Hệ thống lưu thành công và chuyển hướng về trang danh sách
def test_save_page_and_check_in_list_2(pagev2, setup_driver):
    pagev2.perform_tag_operations()
    valid_title = "Trang kiểm thử"
    pagev2.enter_page_title(valid_title)
    pagev2.click_save_and_continue_button()
    try:
        # Chờ tối đa 5 giây để tìm kiếm 'Chỉnh sửa trang' trên toàn bộ trang
        WebDriverWait(setup_driver, 5).until(
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div/nav/ol/li[3]'), "Chỉnh sửa trang")
        )
        logging.info("Test Case 2.2 PASS: 'Chỉnh sửa trang' xuất hiện trên trang sau khi lưu.")
    except TimeoutException:
        logging.error("Test Case 2.2 FAILED: 'Chỉnh sửa trang' không xuất hiện trên trang sau khi lưu!")
        assert False, "'Chỉnh sửa trang' không xuất hiện trên trang!"

# Test Case 3.2: Verify section News -> section News hien thi trong popup Them section
def test_section_news_present(setup_driver, pagev2):
    pagev2.perform_tag_operations()
    pagev2.click_add_section_button()
    pagev2.is_add_section_popup_displayed()
    if pagev2.is_section_news_present():
        logging.info("Test Case 3.2 PASS: Section 'News' đã hiển thị trong popup 'Thêm section'.")
    else:
        logging.error("Test Case 3.2 FAILED: Section 'News' KHÔNG hiển thị trong popup 'Thêm section'!")
    

# Test Case 3.3: Verify Add_button is disable -> He thong enable Add_button trong popup Them section
def test_add_button_disable(setup_driver, pagev2):
    pagev2.perform_tag_operations()
    pagev2.click_add_section_button()
    pagev2.is_add_section_popup_displayed()

    # Lấy phần tử nút "Add"
    add_button = WebDriverWait(setup_driver, 10).until(
        EC.presence_of_element_located(LocatorPageV2.ADD_BUTTON)
    )

    # Kiểm tra trạng thái của nút
    if add_button.is_enabled():
        logging.error("Test Case 3.3 FAILED: Nút 'Add' có thể click, đáng lẽ phải bị vô hiệu hóa.")
        assert False, "Nút 'Add' có thể click, testcase failed."
    else:
        logging.info("Test Case 3.3 PASS: Nút 'Add' bị vô hiệu hóa như mong đợi.")
        assert True

# Test Case 3.4: Verify Add_button is enable -> He thong enable Add_button trong popup Them section
def test_add_button_enable(setup_driver, pagev2):
    pagev2.perform_tag_operations()
    pagev2.click_add_section_button()
    pagev2.is_add_section_popup_displayed()
    pagev2.click_section_news_checkbox()
    
    # Lấy phần tử nút "Add"
    add_button = WebDriverWait(setup_driver, 10).until(
        EC.presence_of_element_located(LocatorPageV2.ADD_BUTTON)
    )

    # Kiểm tra trạng thái của nút
    if add_button.is_enabled():
        logging.info("Test Case 3.4 PASS: Nút 'Add' bị vô hiệu hóa như mong đợi.")
        assert True
    else:
        logging.error("Test Case 3.4 FAILED: Nút 'Add' có thể click, đáng lẽ phải bị vô hiệu hóa.")
        assert False, "Nút 'Add' có thể click, testcase failed."
    
# Test Case 6: Verify khi click icon rename -> Hệ thống hiển thị pop-up Chỉnh sửa tên section
def test_rename_section_popup_display(setup_driver, pagev2):
    pagev2.perform_tag_operations()
    pagev2.add_news_section()
    news_section_element = pagev2.is_news_section_displayed()
    assert news_section_element is not None
    pagev2.click_rename_section()
    popup_displayed = pagev2.is_rename_popup_displayed()
    
    if popup_displayed:
        logging.info("Test Case 6 PASS: Pop-up Rename hiển thị thành công.")
    else:
        logging.error("Test Case 6 FAILED: Pop-up Rename không hiển thị.")
        assert False, "Pop-up Rename không hiển thị."

# Test Case 7.1.1: Verify click icon Dong tren pop-up Chinh sua ten section -> He thong dong pop-up  
def test_click_icon_close_rename_section_popup(setup_driver, pagev2):
    try:
        logging.info("Bắt đầu Test Case 7.1.1: Verify click icon Đóng trên pop-up Chỉnh sửa tên section")

        # Bước 1: Thực hiện thao tác để hiển thị pop-up Rename
        pagev2.perform_tag_operations()
        pagev2.add_news_section()
        assert pagev2.is_news_section_displayed(), "Section News không hiển thị!"

        pagev2.click_rename_section()
        assert pagev2.is_rename_popup_displayed(), "Pop-up Rename không hiển thị!"

        # Bước 2: Nhấn nút đóng pop-up
        pagev2.click_icon_close_rename()
        time.sleep(1)  # Đợi UI cập nhật

        # Bước 3: Kiểm tra pop-up đã đóng
        if pagev2.is_rename_popup_closed():
            logging.info("Test Case 7.1.1 PASS: Đóng pop-up Rename thành công.")
        else:
            logging.error("Test Case 7.1.1 FAILED: Pop-up Rename vẫn hiển thị sau khi đóng!")
            assert False, "Pop-up Rename vẫn hiển thị!"

    except Exception as e:
        logging.error("Test Case 7.1.1 FAILED: Lỗi xảy ra - %s", e, exc_info=True)
        raise

# Test Case 7.1.2: Verify click nut Dong tren pop-up Chinh sua ten section -> He thong dong pop-up  
def test_click_button_close_rename_section_popup(setup_driver, pagev2):
    try:
        logging.info("Bắt đầu Test Case 7.1.2: Verify click icon Đóng trên pop-up Chỉnh sửa tên section")

        # Bước 1: Thực hiện thao tác để hiển thị pop-up Rename
        pagev2.perform_tag_operations()
        pagev2.add_news_section()
        assert pagev2.is_news_section_displayed(), "Section News không hiển thị!"

        pagev2.click_rename_section()
        assert pagev2.is_rename_popup_displayed(), "Pop-up Rename không hiển thị!"

        # Bước 2: Nhấn nút đóng pop-up
        pagev2.click_button_close_rename()
        time.sleep(1)  # Đợi UI cập nhật

        # Bước 3: Kiểm tra pop-up đã đóng
        if pagev2.is_rename_popup_closed():
            logging.info("Test Case 7.1.2 PASS: Đóng pop-up Rename thành công.")
        else:
            logging.error("Test Case 7.1.2 FAILED: Pop-up Rename vẫn hiển thị sau khi đóng!")
            assert False, "Pop-up Rename vẫn hiển thị!"

    except Exception as e:
        logging.error("Test Case 7 FAILED: Lỗi xảy ra - %s", e, exc_info=True)
        raise

# Test Case 7.2.1: Nhap ten moi cho section -> hien thi ten duoc nhap
def test_rename_section_input(setup_driver, pagev2):
    pagev2.perform_tag_operations()
    pagev2.add_news_section()
    
    # Mở pop-up Rename
    pagev2.click_rename_section()
    assert pagev2.is_rename_popup_displayed(), "Pop-up Rename không hiển thị!"

    # Nhập và kiểm tra nội dung text input Rename
    new_name = "Tên mới cho Section"
    pagev2.enter_and_verify_rename_text(new_name)

    logging.info("Test Case: Nhập và xác nhận nội dung Rename thành công.")

# Test Case 7.2.2 : Verify Nhap ten moi nhung click icon Dong -> He thong dong pop-up va ten khong duoc cap nhat
def test_rename_section_cancel(setup_driver, pagev2):
    try:
        logging.info("Bắt đầu Test Case 7.2.2: Nhập tên nhưng đóng pop-up trước khi lưu")

        # Bước 1: Thực hiện thao tác để hiển thị pop-up Rename
        pagev2.perform_tag_operations()
        pagev2.add_news_section()
        assert pagev2.is_news_section_displayed(), "Section News không hiển thị!"

        # Lấy tên section ban đầu
        original_name = pagev2.get_section_name()

        # Bước 2: Mở pop-up Rename và nhập tên mới
        pagev2.click_rename_section()
        assert pagev2.is_rename_popup_displayed(), "Pop-up Rename không hiển thị!"

       # Nhập và kiểm tra nội dung text input Rename
        new_name = "Tên mới cho Section"
        pagev2.enter_and_verify_rename_text(new_name)

        logging.info("Test Case: Nhập và xác nhận nội dung Rename thành công.")

        # Bước 3: Đóng pop-up mà không nhấn nút Lưu
        pagev2.click_icon_close_rename()
        time.sleep(1)  # Đợi UI cập nhật

        # Kiểm tra pop-up đã đóng
        assert pagev2.is_rename_popup_closed(), "Pop-up Rename vẫn hiển thị sau khi đóng!"

        # Bước 4: Kiểm tra tên section **không thay đổi**
        updated_name = pagev2.get_section_name()
        assert updated_name == original_name, f"Tên section đã thay đổi thành '{updated_name}', mong đợi '{original_name}'"

        logging.info("Test Case 7.2.2 PASS: Tên section không bị thay đổi khi đóng pop-up trước khi lưu.")

    except Exception as e:
        logging.error("Test Case 7.2.2 FAILED: Lỗi xảy ra - %s", e, exc_info=True)
        raise

# Test Case 7.2.3 : Verify Nhap ten moi nhung click nut Dong -> He thong dong pop-up va ten khong duoc cap nhat
def test_rename_section_cancel(setup_driver, pagev2):
    try:
        logging.info("Bắt đầu Test Case 7.2.3: Nhập tên nhưng đóng pop-up trước khi lưu")

        # Bước 1: Thực hiện thao tác để hiển thị pop-up Rename
        pagev2.perform_tag_operations()
        pagev2.add_news_section()
        assert pagev2.is_news_section_displayed(), "Section News không hiển thị!"

        # Lấy tên section ban đầu
        original_name = pagev2.get_section_name()

        # Bước 2: Mở pop-up Rename và nhập tên mới
        pagev2.click_rename_section()
        assert pagev2.is_rename_popup_displayed(), "Pop-up Rename không hiển thị!"

       # Nhập và kiểm tra nội dung text input Rename
        new_name = "Tên mới cho Section"
        pagev2.enter_and_verify_rename_text(new_name)

        logging.info("Test Case: Nhập và xác nhận nội dung Rename thành công.")

        # Bước 3: Đóng pop-up mà không nhấn nút Lưu
        pagev2.click_button_close_rename()
        time.sleep(1)  # Đợi UI cập nhật

        # Kiểm tra pop-up đã đóng
        assert pagev2.is_rename_popup_closed(), "Pop-up Rename vẫn hiển thị sau khi đóng!"

        # Bước 4: Kiểm tra tên section **không thay đổi**
        updated_name = pagev2.get_section_name()
        assert updated_name == original_name, f"Tên section đã thay đổi thành '{updated_name}', mong đợi '{original_name}'"

        logging.info("Test Case 7.2.3 PASS: Tên section không bị thay đổi khi đóng pop-up trước khi lưu.")

    except Exception as e:
        logging.error("Test Case 7.2.3 FAILED: Lỗi xảy ra - %s", e, exc_info=True)
        raise

# Test Case 7.2.4: Verify nhập tên mới và click nút Lưu -> Hệ thống lưu và hiển thị tên section mới
def test_rename_section_and_check_name(setup_driver, pagev2):
    try:
        logging.info("Bắt đầu Test Case 7.2.4: Nhập tên mới, lưu và kiểm tra tên section")

        # Bước 1: Hiển thị pop-up Rename
        pagev2.perform_tag_operations()
        pagev2.add_news_section()
        assert pagev2.is_news_section_displayed(), "Section News không hiển thị!"

        pagev2.click_rename_section()
        assert pagev2.is_rename_popup_displayed(), "Pop-up Rename không hiển thị!"

        # Bước 2: Nhập tên mới và lưu
        expected_name = "Tên mới cho Section"
        pagev2.enter_and_verify_rename_text(expected_name)
        pagev2.click_save_rename()

        # Bước 3: Kiểm tra pop-up đã đóng
        assert pagev2.is_rename_popup_closed(), "Pop-up Rename vẫn còn hiển thị sau khi nhấn Lưu!"

        # Bước 4: Chờ 3 giây để UI cập nhật trước khi tìm kiếm
        time.sleep(3)

        # Bước 5: Kiểm tra xem tên mới có hiển thị trên trang không
        assert pagev2.search_text_on_page(expected_name), f"Từ khóa '{expected_name}' không tìm thấy trên trang!"

        logging.info("Test Case 7.2.4 PASS: Tên section đã cập nhật thành công và hiển thị trên trang.")

    except Exception as e:
        logging.error("Test Case 7.2.4 FAILED: Lỗi xảy ra - %s", e, exc_info=True)
        raise

# Test Case 8.1: Verify click icon Collapse -> Hệ thống thu gọn form Section News
def test_collapse_section(setup_driver, pagev2):
    try:
        logging.info("Bắt đầu Test Case 8.1: Click icon Collapse để thu gọn Section News")

        # Bước 1: Hiển thị section News nếu chưa có
        pagev2.perform_tag_operations()
        pagev2.add_news_section()
        assert pagev2.is_news_section_displayed(), "Section News không hiển thị!"

        # Bước 2: Click icon collapse
        pagev2.click_collapse_section()
        time.sleep(2)  # Đợi UI cập nhật

        # Bước 3: Kiểm tra section đã thu gọn
        assert pagev2.is_section_collapsed(), "Section News không được thu gọn sau khi click icon Collapse!"

        logging.info("Test Case 8.1 PASS: Hệ thống đã thu gọn Section News thành công.")

    except Exception as e:
        logging.error("Test Case 8.1 FAILED: Lỗi xảy ra - %s", e, exc_info=True)
        raise

# Test Case 8.2: Verify click icon Expand -> Hệ thống mở rộng lại Section News
def test_expand_section(setup_driver, pagev2):
    try:
        logging.info("Bắt đầu Test Case 8.2: Click icon Expand để mở rộng lại Section News")

        # Bước 1: Hiển thị section News nếu chưa có
        pagev2.perform_tag_operations()
        pagev2.add_news_section()
        assert pagev2.is_news_section_displayed(), "Section News không hiển thị!"

        # Bước 2: Click icon collapse để thu gọn section
        pagev2.click_collapse_section()
        time.sleep(2)
        assert pagev2.is_section_collapsed(), "Section News chưa được thu gọn!"

        # Bước 3: Click icon expand để mở rộng lại section
        pagev2.click_expand_section()
        time.sleep(2)

        # Bước 4: Kiểm tra section đã hiển thị lại
        assert pagev2.is_news_section_displayed(), "Section News không được mở rộng lại sau khi click icon Expand!"

        logging.info("Test Case 8.2 PASS: Hệ thống đã mở rộng lại Section News thành công.")

    except Exception as e:
        logging.error("Test Case 8.2 FAILED: Lỗi xảy ra - %s", e, exc_info=True)
        raise

# Test Case 9.1: Click icon '...' doc -> He thong hien thi cac menu-item
def test_click_menu_icon_display_items(setup_driver, pagev2):
    try:
        logging.info("Bắt đầu Test Case 9.1: Click icon '...' để hiển thị menu-item")

        # Bước 1: Đảm bảo Section News hiển thị
        pagev2.perform_tag_operations()
        pagev2.add_news_section()
        assert pagev2.is_news_section_displayed(), "Section News không hiển thị!"

        # Bước 2: Click vào icon '...' (menu)
        pagev2.click_menu_icon()
        time.sleep(2)  # Đợi menu hiển thị

        # Bước 3: Kiểm tra các menu-item Delete & Duplicate có hiển thị không
        assert pagev2.is_delete_button_displayed(), "Nút Delete không hiển thị trong menu!"
        assert pagev2.is_duplicate_button_displayed(), "Nút Duplicate không hiển thị trong menu!"

        logging.info("Test Case 9.1 PASS: Hệ thống hiển thị đầy đủ menu-item sau khi click icon '...'.")
    
    except Exception as e:
        logging.error("Test Case 9.1 FAILED: Lỗi xảy ra - %s", e, exc_info=True)
        raise

# Test Case 9.2.1: Click menu-item Xoa -> He thong hien thi pop-up Confirm
def test_check_delete_confirmation_popup(setup_driver, pagev2):
    try:
        logging.info("Bắt đầu Test Case 9.2.1: Kiểm tra pop-up xác nhận khi click Xóa")

        # Bước 1: Đảm bảo Section News hiển thị
        pagev2.perform_tag_operations()
        pagev2.add_news_section()
        assert pagev2.is_news_section_displayed(), "Section News không hiển thị!"

        # Bước 2: Click vào icon '...' (menu)
        pagev2.click_menu_icon()
        time.sleep(1)  # Đợi menu hiển thị

        # Bước 3: Click vào menu-item Xóa
        pagev2.click_delete_button()
        time.sleep(1)  # Đợi pop-up hiển thị

        # Bước 4: Kiểm tra pop-up xác nhận có hiển thị không
        assert pagev2.is_delete_confirmation_popup_displayed(), "Pop-up xác nhận xóa không hiển thị!"

        logging.info("Test Case 9.2.1 PASS: Pop-up xác nhận hiển thị đúng khi click Xóa.")

    except Exception as e:
        logging.error("Test Case 9.2.1 FAILED: Lỗi xảy ra - %s", e, exc_info=True)
        raise

# Test Case 9.2.2 Click icon Close tren pop-up Confirm
def test_click_close_confirm_popup(setup_driver, pagev2):
    try:
        logging.info("Bắt đầu Test Case 9.2.2: Click icon 'X' để đóng pop-up xác nhận xóa.")

        # Bước 1: Đảm bảo Section News hiển thị
        pagev2.perform_tag_operations()
        pagev2.add_news_section()
        assert pagev2.is_news_section_displayed(), "Section News không hiển thị!"

        # Bước 2: Click vào icon '...' (menu)
        pagev2.click_menu_icon()
        time.sleep(1)  # Đợi menu hiển thị

        # Bước 3: Click vào menu-item Xóa
        pagev2.click_delete_button()
        time.sleep(1)  # Đợi pop-up xác nhận hiển thị

        # Bước 4: Kiểm tra pop-up xác nhận có hiển thị không
        assert pagev2.is_delete_confirmation_popup_displayed(), "Pop-up xác nhận xóa không hiển thị!"

        # Bước 5: Click icon 'X' để đóng pop-up
        pagev2.click_close_confirm_popup()
        time.sleep(1)  # Đợi pop-up đóng

        # Bước 6: Kiểm tra Section News vẫn còn trên giao diện
        assert pagev2.is_news_section_displayed(), "Section News đã bị xóa sau khi đóng pop-up xác nhận!"

        logging.info("Test Case 9.2.2 PASS: Pop-up xác nhận đã đóng, Section News vẫn còn.")

    except Exception as e:
        logging.error("Test Case 9.2.2 FAILED: Lỗi xảy ra - %s", e, exc_info=True)
        raise


# Test Case 9.2.3: Click nut Yes trong pop-up Confirm  -> He thong xoa section
def test_click_delete_section(setup_driver, pagev2):
    try:
        logging.info("Bắt đầu Test Case 9.2.3: Click menu-item Xóa để xóa Section News")

        # Bước 1: Đảm bảo Section News hiển thị
        pagev2.perform_tag_operations()
        pagev2.add_news_section()
        assert pagev2.is_news_section_displayed(), "Section News không hiển thị!"

        # Bước 2: Click vào icon '...' (menu)
        pagev2.click_menu_icon()
        time.sleep(1)  # Đợi menu hiển thị

        # Bước 3: Click vào menu-item Xóa
        pagev2.click_delete_button()
        time.sleep(1)  # Đợi pop-up xác nhận hiển thị

        # Bước 4: Kiểm tra pop-up xác nhận có hiển thị không
        assert pagev2.is_delete_confirmation_popup_displayed(), "Pop-up xác nhận xóa không hiển thị!"

        # Bước 5: Click nút xác nhận Xóa trên pop-up
        pagev2.confirm_delete_section()
        time.sleep(2)  # Đợi hệ thống xử lý xóa

        # Bước 6: Kiểm tra Section đã bị xóa bằng hàm is_section_news_deleted()
        assert pagev2.is_section_news_deleted(), "Section News vẫn còn sau khi xác nhận xóa!"

        logging.info("Test Case 9.2.3 PASS: Section đã được xóa thành công.")

    except Exception as e:
        logging.error("Test Case 9.2.3 FAILED: Lỗi xảy ra - %s", e, exc_info=True)
        raise

# Test Case 9.2.4: Click nut No trong pop-up Confirm -> He thong huy xoa section
def test_cancel_delete_section(setup_driver, pagev2):
    try:
        logging.info("Bắt đầu Test Case 9.2.4: Click nút 'No' để hủy xóa Section News.")

        # Bước 1: Đảm bảo Section News hiển thị
        pagev2.perform_tag_operations()
        pagev2.add_news_section()
        assert pagev2.is_news_section_displayed(), "Section News không hiển thị!"

        # Bước 2: Click vào icon '...' (menu)
        pagev2.click_menu_icon()
        time.sleep(1)  # Đợi menu hiển thị

        # Bước 3: Click vào menu-item Xóa
        pagev2.click_delete_button()
        time.sleep(1)  # Đợi pop-up xác nhận hiển thị

        # Bước 4: Kiểm tra pop-up xác nhận có hiển thị không
        assert pagev2.is_delete_confirmation_popup_displayed(), "Pop-up xác nhận xóa không hiển thị!"

        # Bước 5: Click nút 'No' để hủy xóa
        pagev2.cancel_delete_section()
        time.sleep(1)  # Đợi pop-up đóng

        # Bước 6: Kiểm tra Section News vẫn còn trên giao diện
        assert pagev2.is_news_section_displayed(), "Section News đã bị xóa sau khi hủy xác nhận!"

        logging.info("Test Case 9.2.4 PASS: Pop-up xác nhận đã đóng, Section News vẫn còn.")

    except Exception as e:
        logging.error("Test Case 9.2.4 FAILED: Lỗi xảy ra - %s", e, exc_info=True)
        raise

# Test Case 9.3: Click menu-item Duplicate -> Hệ thống tạo bản sao của Section News
def test_duplicate_section(setup_driver, pagev2):
    try:
        logging.info("Bắt đầu Test Case 9.3: Click menu-item 'Duplicate' để tạo bản sao Section News")

        # Bước 1: Đảm bảo Section News hiển thị
        pagev2.perform_tag_operations()
        pagev2.add_news_section()
        assert pagev2.is_news_section_displayed(), "Section News không hiển thị!"

        # Bước 2: Click vào icon '...' (menu)
        pagev2.click_menu_icon()
        time.sleep(1)  # Đợi menu hiển thị

        # Bước 3: Click vào menu-item Duplicate
        pagev2.click_duplicate_button()
        time.sleep(2)  # Đợi hệ thống xử lý sao chép

        # Bước 4: Kiểm tra xem Section News đã được nhân bản hay chưa
        assert pagev2.search_text_on_page('Copy of News')

        logging.info("Test Case 9.3 PASS: Hệ thống đã tạo bản sao Section News thành công.")

    except Exception as e:
        logging.error("Test Case 9.3 FAILED: Lỗi xảy ra - %s", e, exc_info=True)
        raise

# # Test Case 7: Verify khi không nhập "Số bài viết hiển thị trên slide" & button "Lưu" -> Hệ thống hiển thị thông báo lỗi: "Vui lòng nhập số bài viết hiển thị trên slide"
# def test_numberdisplay_button_section_validation(setup_driver, pagev2):
#     try: 
#         pagev2.click_content_menu()
#         pagev2.click_page_v2_menu()
#         assert pagev2.click_create_new_button()
#         assert pagev2.click_add_section_button()
#         assert pagev2.is_add_section_popup_displayed()
#         assert pagev2.click_section_news_checkbox()
#         assert pagev2.click_add_button()
#         news_section_element = pagev2.is_news_section_displayed()
#         assert news_section_element is not None
#         assert pagev2.click_save_button()
#         error_message = "Vui lòng nhập số bài viết hiển thị trên slide"
#         assert pagev2.search_text_on_page(error_message)
#         logging.info("Test Case 6 PASS: Hiển thị đúng thông báo lỗi: Vui lòng nhập số bài viết hiển thị trên slide")
#     except Exception as e:
#         logging.error(f"Test Case 6 FAILED: Không hiển thị hoặc hiển thị sai thông báo lỗi: {error_message}")
#         assert False, "Không tìm thấy hoặc thông báo lỗi không đúng."

# # Test Case 8: Verify khi không nhập "Số bài viết hiển thị trên slide" & button "Lưu và Tiếp tục cập nhật" -> Hệ thống hiển thị thông báo lỗi: "Vui lòng nhập số bài viết hiển thị trên slide"
# def test_numberdisplay_continue_button_section_validation(setup_driver, pagev2):
#     try: 
#         pagev2.click_content_menu()
#         pagev2.click_page_v2_menu()
#         assert pagev2.click_create_new_button()
#         assert pagev2.click_add_section_button()
#         assert pagev2.is_add_section_popup_displayed()
#         assert pagev2.click_section_news_checkbox()
#         assert pagev2.click_add_button()
#         news_section_element = pagev2.is_news_section_displayed()
#         assert news_section_element is not None
#         assert pagev2.click_save_and_continue_button()
#         error_message = "Vui lòng nhập số bài viết hiển thị trên slide"
#         assert pagev2.search_text_on_page(error_message)
#         logging.info("Test Case 7 PASS: Hiển thị đúng thông báo lỗi: Vui lòng nhập số bài viết hiển thị trên slide")
#     except Exception as e:
#         logging.error(f"Test Case 7 FAILED: Không hiển thị hoặc hiển thị sai thông báo lỗi: {error_message}")
#         assert False, "Không tìm thấy hoặc thông báo lỗi không đúng."

# # Test Case 9: Verify khi không nhập Tiêu đề trang, nhấn Lưu và tiếp tục cập nhật -> Hệ thống hiển thị thông báo lỗi Vui lòng nhập tiêu đề trang
# def test_empty_page_title_button_continue(pagev2, setup_driver):
#     pagev2.perform_tag_operations()
#     pagev2.click_create_new_button()
#     pagev2.enter_page_title("")
#     pagev2.click_save_and_continue_button()
#     error_message = pagev2.check_title_error_message()
#     if error_message == "Vui lòng nhập tiêu đề trang":
#         logging.info("Test Case 8 PASS: Hiển thị đúng thông báo lỗi: Vui lòng nhập tiêu đề trang.")
#     else:
#         logging.error(f"Test Case 8 FAILED: Không hiển thị hoặc hiển thị sai thông báo lỗi: {error_message}")
#         assert False, "Thông báo lỗi không đúng hoặc không xuất hiện!"   
   

# # Test Case 10: Verify click dropdown "Chọn danh sách theo" ở section "News", Hệ thống mở dropdown 
# def test_list_by_section_displayed(setup_driver, pagev2):
#     pagev2.click_content_menu()
#     pagev2.click_page_v2_menu()
#     assert pagev2.click_create_new_button()
#     assert pagev2.click_add_section_button()
#     assert pagev2.is_add_section_popup_displayed()
#     assert pagev2.click_section_news_checkbox()
#     assert pagev2.click_add_button()
#     news_section_element = pagev2.is_news_section_displayed()
#     assert news_section_element is not None
#     assert pagev2.click_select_list_by()
#     dropdown_list_by_element = pagev2.is_dropdown_list_by_displayed()
#     dropdown_list_by_element = WebDriverWait(setup_driver, 10).until(
#         EC.visibility_of_element_located(LocatorPageV2.DROPDOWN_LIST_BY_DISPLAYED)
#     )

#     if dropdown_list_by_element and dropdown_list_by_element.is_displayed():
#         logging.info("Test Case 9 PASS: Dropdown 'Chọn danh sách theo' đã hiển thị.")
#     else:
#         logging.error("Test Case 9 FAILED: Dropdown 'Chọn danh sách theo' không hiển thị.")
#         assert False, "Dropdown 'Chọn danh sách theo' không hiển thị sau khi click!"

# # Test Case 11: Verify field "Chọn danh sách theo" ở section "News" & chọn "Tùy chọn". Hệ thống hiển thị form 'Danh sách bài viết hiển thị' và nút 'Chọn bài viết'
# def test_list_by_option_section_displayed(setup_driver, pagev2):
#     try:
#         pagev2.click_content_menu()
#         pagev2.click_page_v2_menu()
#         assert pagev2.click_create_new_button()
#         assert pagev2.click_add_section_button()
#         assert pagev2.is_add_section_popup_displayed()
#         assert pagev2.click_section_news_checkbox()
#         assert pagev2.click_add_button()
#         news_section_element = pagev2.is_news_section_displayed()
#         assert news_section_element is not None
#         assert pagev2.click_select_list_by()
#         dropdown_list_by_element = pagev2.is_dropdown_list_by_displayed()
#         assert dropdown_list_by_element is not None
#         assert pagev2.click_select_list_by_option()
#         expected_name = "Danh sách bài viết hiển thị"
#         assert pagev2.search_text_on_page(expected_name)
#         logging.info("Test Case 10 PASS: Section 'Danh sách bài viết hiển thị' đã hiển thị.")
#     except Exception as e:
#         logging.error("Test Case 10 FAILED: Section 'Danh sách bài viết hiển thị' không hiển thị.")
#         assert False, "Section 'Danh sách bài viết hiển thị' không hiển thị sau khi click!"


# # Test Case 12: Verify field "Chọn danh sách theo" ở section "News", chọn "Loại bài viết". Hệ thống hiển thị 2 dropdown "Chọn loại bài viết" & "Sắp xếp"
# def test_list_by_type_article_section_displayed(setup_driver, pagev2):
#     try:
#         pagev2.click_content_menu()
#         pagev2.click_page_v2_menu()
#         assert pagev2.click_create_new_button()
#         assert pagev2.click_add_section_button()
#         assert pagev2.is_add_section_popup_displayed()
#         assert pagev2.click_section_news_checkbox()
#         assert pagev2.click_add_button()
#         news_section_element = pagev2.is_news_section_displayed()
#         assert news_section_element is not None
#         assert pagev2.click_select_list_by()
#         dropdown_list_by_element = pagev2.is_dropdown_list_by_displayed()
#         assert dropdown_list_by_element is not None
#         assert pagev2.click_select_list_by_type_article()
#         expected_name = "Chọn loại bài viết"
#         assert pagev2.search_text_on_page(expected_name)
#         logging.info("Test Case 11 PASS: Dropdown 'Chọn loại bài viết' đã hiển thị.")
#     except Exception as e:
#         logging.error("Test Case 11 FAILED: Dropdown 'Chọn loại bài viết' không hiển thị.")
#         assert False, "Dropdown 'Chọn loại bài viết' không hiển thị sau khi click!"

# Test Case 7: Verify khi nhập chữ vào field nhập số lượng slide -> Hệ thống không nhập dữ liệu chữ
def test_number_of_articles_rejects_text(setup_driver, pagev2):
    pagev2.perform_tag_operations()
    pagev2.add_news_section()
    try:
        assert pagev2.is_news_section_displayed(), "Section News không hiển thị!" 
        invalid_input = "abc"
        pagev2.enter_number_of_articles(invalid_input)
        actual_value = pagev2.get_number_of_articles_value()
        assert actual_value == "" or actual_value.isnumeric(), f"Input không hợp lệ nhưng vẫn giữ giá trị: '{actual_value}'"
        print("Test Case 7 PASS: Nhập chữ vào field số lượng slide không thành công (đúng mong đợi)")
    except Exception as e:
        print(f"Test Case 7 FAIL: Hệ thống vẫn chấp nhận chữ! Lỗi: {str(e)}")
        assert False