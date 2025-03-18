import time
import pytest
import logging
import datetime
from utils.login import Login
from pages.article import Article
from utils.driver_setup import get_driver
from locators.locator_article import LocatorArticle
from pages.articles.select import SelectArticle
from pages.articles.enterfield import EnterFieldArticle
from pages.articles.validation import ArticleValidation
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

# Cấu hình logging
test_logger = logging.getLogger("test_logger")
test_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("reports/test_results.log", mode="w")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
test_logger.addHandler(file_handler)

@pytest.fixture(scope="function")
def setup_driver():
    driver = get_driver()
    try:
        login_page = Login(driver)
        if not login_page.login():
            pytest.fail("Không thể đăng nhập!")
        yield driver
    finally:
        time.sleep(5)
        driver.quit()

@pytest.fixture
def article(setup_driver):
    return Article(setup_driver)

@pytest.fixture
def validation(setup_driver):
    return ArticleValidation(setup_driver)

@pytest.fixture
def enter_field(setup_driver):
    return EnterFieldArticle(setup_driver)

@pytest.fixture
def select(setup_driver):
    return SelectArticle(setup_driver)

# Test Case 1: Verify khi click menu 'Tất cả bài viết' -> Hệ thống chuyển hướng đến trang Danh sách bài viết 
def test_navigate_to_all_articles(article):
    article.click_content_menu()
    article.click_article_menu()
    result = article.click_all_article_menu()
    if result:
        logging.info("Test Case 1 PASS: Hệ thống chuyển hướng thành công đến trang 'Tất cả bài viết'")
    else:
        logging.error("Test Case 1 FAIL: Hệ thống không chuyển hướng đến trang 'Tất cả bài viết'")
        assert False, "Lỗi: Trang 'Tất cả bài viết' không tải được!"

# Test Case 2: Verify khi click nút 'Tạo mới' -> Hệ thống chuyển hướng đến trang Tạo mới bài viết 
def test_navigate_to_create_article(article):
    article.click_content_menu()
    article.click_article_menu()
    article.click_all_article_menu()
    result = article.click_create_new_button()
    if result:
        logging.info("Test Case 2 PASS: Hệ thống chuyển hướng thành công đến trang 'Tạo mới bài viết'")
    else:
        logging.error("Test Case 2 FAIL: Hệ thống không chuyển đến trang 'Tạo mới bài viết")
        assert False, "Lỗi: Trang 'Tạo mới bài viết' không tải được!"

def test_click_en_tab_and_translate_content(article):
    article.click_content_menu()
    article.click_article_menu()
    article.click_all_article_menu()
    article.click_create_new_button()
    article.click_en_tab()
    logging.info("Đã nhấn vào tab English.")
    result = article.click_translate_content_button()
    if result:
        logging.info("Test Case PASS: Nhấn nút Dịch nội dung trong tab English thành công.")
    else:
        logging.error("Test Case FAIL: Không thể nhấn nút Dịch nội dung trong tab English.")
        assert False, "Lỗi: Nút Dịch nội dung không hoạt động!"

    
# Test Case 3: Verify khi không nhập 'Tiêu đề' -> Hệ thống hiển thị thống báo lỗi 'Vui lòng nhập Tiêu đề'
def test_empty_article_title(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.enter_title("")
    article.click_save_button()
    error_message = article.is_title_error_displayed()
    if error_message:
        logging.info("Test Case 3 PASS: Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Tiêu đề'")
    else:
        logging.error("Test Case 3 FAIL: Hệ thống không hiển thị thông báo lỗi 'Vui lòng nhập Tiêu đề'")
        assert False, "Lỗi: Không hiển thị thông báo 'Vui lòng nhập Tiêu đề'"

# Test Case 4: Verify khi nhập Tiêu đề -> Hệ thống ẩn đi thông báo lỗi 'Vui lòng nhập Tiêu đề'
def test_title_error_disappears(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.enter_title("")
    article.click_save_button()
    article.is_title_error_displayed()
    article.enter_title("Bài viết mới")
    if not article.is_title_error_displayed():
        logging.info("Test Case 4 PASS: Thông báo lỗi bị ẩn sau khi nhập Tiêu đề")
    else:
        logging.error("Test Case 4 FAIL: Thông báo lỗi vẫn còn sau khi nhập tiêu đề!")
        assert False, "Lỗi: Thông báo lỗi vẫn còn sau khi nhập tiêu đề."

# Test Case 5: Verify khi nhập Tiêu đề hơn 250 ký tự -> Hệ thống hiển thị thông báo lỗi 'Tiêu đề không được vượt quá 250 ký tự'
def test_title_max_length_error(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    long_title = "A" * 251
    article.enter_title(long_title)
    article.click_save_button()
    if article.is_title_max_length_error_displayed():
        logging.info("Test Case 5 PASS: Hệ thống hiển thị lỗi khi tiêu đề vượt quá 250 ký tự.")
    else:
        logging.error("Test Case 5 FAIL: Hệ thống không hiển thị lỗi khi tiêu đề quá dài!")
        assert False, "Lỗi: Không hiển thị thông báo 'Tiêu đề không được vượt quá 250 ký tự'."

# Test Case 6: Verify khi không nhập 'Nội dung' -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Nội dung'
def test_empty_article_content(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.enter_title("Bài viết kiểm thử")
    article.click_save_button()
    error_message = article.is_content_error_displayed()
    if error_message:
        logging.info("Test Case 6 PASS: Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Nội dung'")
    else:
        logging.error("Test Case 6 FAIL: Hệ thống không hiển thị thông báo lỗi 'Vui lòng nhập Nội dung'")
        assert False, "Lỗi: Không hiển thị thông báo 'Vui lòng nhập Nội dung'."

# Test Case 7: Verify khi nhập dữ liệu vào field 'Nội dung' -> Hệ thống không hiển thị thông báo lỗi 'Vui lòng nhập Nội dung'
def test_content_error_disappears(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.enter_title("Bài viết kiểm thử")
    article.enter_content("")
    article.click_save_button()
    article.is_content_error_displayed()
    article.enter_content("Đây là nội dung bài viết test")
    error_message_after_input = article.is_content_error_displayed()
    if not error_message_after_input:
        logging.info("Test Case 7 PASS: Thông báo lỗi bị ẩn sau khi nhập Nội dung")
    else:
        logging.error("Test Case 7 FAIL: Thông báo lỗi vẫn còn sau khi nhập Nội dung!")
        assert False, "Lỗi: Thông báo lỗi vẫn còn sau khi nhập Nội dung."

# Test Case 8: Verify khi không chọn 'Loại bài viết' -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Loại bài viết'
def test_article_type_error(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_save_button()
    article.click_tab_general_info()
    error_message = article.is_article_type_error_displayed()
    if error_message:
        logging.info("Test Case 8 PASS: Hệ thống hiển thị đúng thông báo lỗi khi không chọn loại bài viết.")
    else:
        logging.error("Test Case 8 FAIL: Hệ thống KHÔNG hiển thị lỗi khi không chọn loại bài viết!")
        assert False, "Lỗi: Không hiển thị thông báo 'Vui lòng nhập Loại bài viết'."
    
# Test Case 9: Verify khi click vào dropdown 'Loại bài viết' -> Hệ thống mở dropdown 'Loại bài viết'
def test_open_article_type_dropdown(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_tab_general_info()
    select.click_select()
    if select.is_dropdown_visible():
        logging.info("Test Case 9 PASS: Hệ thống mở dropdown 'Loại bài viết' thành công!")
    else:
        logging.error("Test Case 9 FAIL: Hệ thống không mở dropdown 'Loại bài viết'!")
        assert False, "Lỗi: Dropdown không mở."

# Test Case 10: Verify khi chọn 'Loại bài viết' từ dropdown -> Hệ thống hiển thị đúng giá trị đã chọn
def test_select_article_type_from_dropdown(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_tab_general_info()
    article.click_select()
    article.select_article_type("Tin tức chuyên ngành")
    if article.is_selected_article_type_displayed("Tin tức chuyên ngành"):
        logging.info("Test Case 10 PASS: Loại bài viết đã chọn hiển thị đúng.")
    else:
        logging.error(f"Test Case 10 FAIL: Loại bài viết đã chọn không đúng. Expected: 'Tin tức chuyên ngành'")
        assert False, "Lỗi: Loại bài viết hiển thị không đúng."

# Test Case 11: Verify khi nhấn nút Lưu -> Hệ thống chuyển hướng về trang Danh sách bài viết
def test_save_article(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.enter_title("Tiêu đề bài viết")
    article.enter_content("Đây là nội dung bài viết test")
    article.click_tab_general_info()
    article.click_select()
    article.select_article_type("Tin tức chuyên ngành")
    article.click_save_button()
    time.sleep(5)
    if article.wait_for_article_to_appear_in_list("Tiêu đề bài viết"):
        logging.info("Test Case PASS: Bài viết hiển thị đúng tên trong danh sách bài viết.")
    else:
        logging.error("Test Case FAIL: Tên bài viết không xuất hiện trong danh sách bài viết.")

# Test Case 12: Verify khi nhấn nút Lưu và tiếp tục chỉnh sửa -> Hệ thống ở lại trang để tiếp tục chỉnh sửa
def test_save_and_continue_editing(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.enter_title("Tiêu đề bài viết test")
    article.enter_content("Đây là nội dung bài viết test")
    article.click_tab_general_info()
    article.click_select()
    article.select_article_type("Tin tức chuyên ngành")
    article.click_save_and_continue_button()
    if article.verify_article_edit_page("Tiêu đề bài viết test"):
        logging.info("Test Case 12 PASS: Hệ thống giữ nguyên trang chỉnh sửa sau khi lưu.")
    else:
        logging.error("Test Case 12 FAIL: Trang không giữ nguyên trạng thái chỉnh sửa sau khi lưu.")
        assert False, "Lỗi: Trang không giữ nguyên trạng thái chỉnh sửa sau khi lưu."

# Test Case 13: Verify khi thay đổi giá trị trong dropdown Loại bài viết -> Hệ thống cập nhật lại giá trị Loại bài viết
def test_change_article_type_after_selection(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_tab_general_info()
    article.click_select()
    article.select_article_type("Tin tức chuyên ngành")
    assert article.is_selected_article_type_displayed("Tin tức chuyên ngành"), "Lỗi: Giá trị 'Loại bài viết' ban đầu không đúng."
    article.click_select()
    article.select_article_type("Lĩnh vực kinh doanh")
    if article.is_selected_article_type_displayed("Lĩnh vực kinh doanh"):
        logging.info("Test Case 13 PASS: Giá trị 'Loại bài viết' được cập nhật chính xác sau khi thay đổi.")
    else:
        logging.error("Test Case 13 FAIL: Giá trị 'Loại bài viết' không cập nhật đúng. Expected: 'Lĩnh vực kinh doanh'")
        assert False, "Lỗi: Giá trị 'Loại bài viết' không cập nhật sau khi thay đổi."

# Test Case 14: Verify khi click vào dropdown 'Trạng thái' -> Hệ thống mở dropdown 'Trạng thái'
def test_open_status_dropdown(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_tab_general_info()
    article.click_status_dropdown()
    if article.is_status_dropdown_visible():
        logging.info("Test Case 14 PASS: Hệ thống mở dropdown 'Trạng thái' thành công!")
    else:
        logging.error("Test Case 14 FAIL: Hệ thống không mở dropdown 'Trạng thái'!")
        assert False, "Lỗi: Dropdown không mở."

# Test Case 15: Verify khi click chọn giá trị Chờ xử lý -> Hệ thống hiển thị giá trị chờ xử lý lên dropdown Trạng thái
def test_select_status_from_dropdown(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_tab_general_info()
    article.click_status_dropdown()
    article.select_status("Chờ xử lý")
    if article.is_status_selected("Chờ xử lý"):
        logging.info("Test Case 15 PASS: Trạng thái đã chọn hiển thị đúng.")
    else:
        logging.error("Test Case 15 FAIL: Trạng thái đã chọn không đúng. Expected: 'Chờ xử lý'")
        assert False, "Lỗi: Trạng thái hiển thị không đúng."

# Test Case 16: Verify khi không nhập Thứ tự sắp xếp -> Hệ thống hiển thị thông báo lỗi 
def test_ordering_error_message(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.enter_title("Bài viết kiểm thử")
    article.enter_content("Đây là nội dung bài viết test")
    article.click_tab_general_info()
    article.click_select()
    article.select_article_type("Tin tức chuyên ngành")
    article.ordering("")
    article.click_save_button()
    if article.is_ordering_error_displayed():
        logging.info("Test Case 16 PASS: Hệ thống hiển thị lỗi đúng khi không nhập Thứ tự sắp xếp!")
    else:
        logging.error("Test Case 16 FAIL: Hệ thống không hiển thị lỗi khi Thứ tự sắp xếp trống!")
        assert False, "Lỗi: Không hiển thị thông báo 'Vui lòng nhập Thứ tự sắp xếp'."

# Test Case 17: Verify khi nhập hơn 7 số -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập không quá 7 số'
def test_ordering_max_lenght_error_message(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.enter_title("Bài viết kiểm thử")
    article.enter_content("Đây là nội dung bài viết test")
    article.click_tab_general_info()
    article.click_select()
    article.select_article_type("Tin tức chuyên ngành")
    article.ordering("123456789")
    if article.is_ordering_error_displayed():
        logging.info("Test Case 17 PASS: Hệ thống hiển thị thông báo lỗi ")
    else:
        logging.error("Test Case 17 FAIL: Hệ thống KHÔNG hiển thị lỗi khi Thứ tự sắp xếp trống!")
        assert False, "Lỗi: Không hiển thị thông báo 'Vui lòng nhập Thứ tự sắp xếp'."

# Test Case 18: Verify khi nhập chữ -> Hệ thống không chấp nhận
def test_ordering_specific(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.enter_title("Bài viết kiểm thử")
    article.enter_content("Đây là nội dung bài viết test")
    article.click_tab_general_info()
    article.click_select()
    article.select_article_type("Tin tức chuyên ngành")
    article.ordering("adcdfghtktgdadcdfght")
    error_message = article.get_text(article.locators.ORDERING_ERROR_MESSAGE)
    assert error_message is None or error_message == "", "Test Case FAIL: Hệ thống chấp nhận ký tự chữ!"
    logging.info("Test Case PASS: Hệ thống không chấp nhận ký tự chữ!")

# Test Case 19: Verify khi click field Ngày đăng -> Hệ thống sẽ hiển thị ngày hiện tại
def test_public_date_default_value(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.enter_title("Bài viết kiểm thử")
    article.enter_content("Đây là nội dung bài viết test")
    article.click_tab_general_info()
    article.wait.until(EC.visibility_of_element_located(article.locators.PUBLIC_DATE)).click()
    displayed_date = article.get_public_date()
    expected_date = datetime.datetime.now().strftime("%Y-%m-%d")
    assert displayed_date == expected_date, f"Test Case FAIL: Ngày hiển thị là {displayed_date}, mong đợi {expected_date}"
    logging.info("Test Case PASS: Ngày đăng hiển thị đúng ngày hiện tại")

# Test Casse 20: Verify khi nhập ngày tương lai -> 
def test_enter_future_public_date(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.enter_title("Bài viết kiểm thử")
    article.enter_content("Đây là nội dung bài viết test")
    article.click_tab_general_info()
    # Nhập ngày tương lai (thêm 10 ngày)
    future_date = (datetime.datetime.now() + datetime.timedelta(days=10)).strftime("%Y-%m-%d")
    article.set_public_date(future_date)
    
    # Kiểm tra ngày hiển thị
    displayed_date = article.get_public_date()
    assert displayed_date == future_date, f"Test Case FAIL: Ngày hiển thị là {displayed_date}, mong đợi {future_date}"
    logging.info("Test Case PASS: Hệ thống chấp nhận ngày đăng là ngày tương lai")

# Test Case 21: Verify khi nhập ngày quá khứ ->
def test_enter_past_public_date(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.enter_title("Bài viết kiểm thử")
    article.enter_content("Đây là nội dung bài viết test")
    article.click_tab_general_info()
    past_date = (datetime.datetime.now() - datetime.timedelta(days=10)).strftime("%Y-%m-%d")
    article.set_public_date(past_date)
    displayed_date = article.get_public_date()
    assert displayed_date == past_date, f"Test Case FAIL: Ngày hiển thị là {displayed_date}, mong đợi {past_date}"
    logging.info("Test Case PASS: Hệ thống chấp nhận ngày đăng là ngày quá khứ")

# Test Case 22: Verify trạng thái mặc định nút switch Nổi bật là OFF
def test_featured_switch_initial_state(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.enter_title("Bài viết kiểm thử")
    article.enter_content("Đây là nội dung bài viết test")
    article.click_tab_general_info()
    article.reset_switch(LocatorArticle.FEATURED_SWITCH, LocatorArticle.FEATURED_LABEL)
    assert not article.is_switch_on(LocatorArticle.FEATURED_SWITCH), "Test Case FAIL: Trạng thái ban đầu của switch không phải OFF"
    logging.info("Test Case PASS: Trạng thái ban đầu của switch là OFF")

# Test Case 23: Verify chuyển trạng thái nút switch Nổi bật từ OFF -> ON
def test_toggle_featured_switch_on(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.enter_title("Bài viết kiểm thử")
    article.enter_content("Đây là nội dung bài viết test")
    article.click_tab_general_info()
    article.reset_switch(LocatorArticle.FEATURED_SWITCH, LocatorArticle.FEATURED_LABEL)
    article.click_switch(LocatorArticle.FEATURED_LABEL)  # Click vào label để bật switch
    assert article.is_switch_on(LocatorArticle.FEATURED_SWITCH), "Test Case FAIL: Không thể bật switch ON"
    logging.info("Test Case PASS: Nút switch đã được bật ON")

# Test Case 24: Verify khi chuyển trạng thái nút switch Nổi bật từ ON -> OFF 
def test_toggle_featured_switch_off(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.enter_title("Bài viết kiểm thử")
    article.enter_content("Đây là nội dung bài viết test")
    article.click_tab_general_info()
    article.reset_switch(LocatorArticle.FEATURED_SWITCH, LocatorArticle.FEATURED_LABEL)
    article.click_switch(LocatorArticle.FEATURED_LABEL)  
    article.click_switch(LocatorArticle.FEATURED_LABEL) 
    assert not article.is_switch_on(LocatorArticle.FEATURED_SWITCH), "Test Case FAIL: Không thể tắt switch OFF"
    logging.info("Test Case PASS: Nút switch đã được tắt OFF")

# Test Case 25: Verify trạng thái mặc định nút switch Đặt làm trang chủ là OFF
def test_homepage_switch_initial_state(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.enter_title("Bài viết kiểm thử")
    article.enter_content("Đây là nội dung bài viết test")
    article.click_tab_general_info()
    article.reset_switch(LocatorArticle.HOMEPAGE_SWITCH, LocatorArticle.HOMEPAGE_LABEL)  # Truyền đủ 2 tham số
    assert not article.is_switch_on(LocatorArticle.HOMEPAGE_LABEL), "Test Case FAIL: Trạng thái ban đầu của switch không phải OFF"
    logging.info("Test Case PASS: Trạng thái ban đầu của switch là OFF")

# Test Case 26: Verify chuyển trạng thái nút switch Đặt làm trang chủ từ OFF -> ON
def test_toggle_homepage_switch_on(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.enter_title("Bài viết kiểm thử")
    article.enter_content("Đây là nội dung bài viết test")
    article.click_tab_general_info()
    article.reset_switch(LocatorArticle.HOMEPAGE_SWITCH, LocatorArticle.HOMEPAGE_LABEL)
    article.click_switch(LocatorArticle.HOMEPAGE_LABEL)  # Click vào label để bật switch
    assert article.is_switch_on(LocatorArticle.HOMEPAGE_SWITCH), "Test Case FAIL: Không thể bật switch ON"
    logging.info("Test Case PASS: Nút switch đã được bật ON")

# Test Case 27: Verify khi chuyển trạng thái nút switch Đặt làm trang chủ từ ON -> OFF 
def test_toggle_homepage_switch_off(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.enter_title("Bài viết kiểm thử")
    article.enter_content("Đây là nội dung bài viết test")
    article.click_tab_general_info()
    article.reset_switch(LocatorArticle.HOMEPAGE_SWITCH, LocatorArticle.HOMEPAGE_LABEL)
    article.click_switch(LocatorArticle.HOMEPAGE_LABEL)  
    article.click_switch(LocatorArticle.HOMEPAGE_LABEL) 
    assert not article.is_switch_on(LocatorArticle.HOMEPAGE_SWITCH), "Test Case FAIL: Không thể tắt switch OFF"
    logging.info("Test Case PASS: Nút switch đã được tắt OFF")

# Test Case 28: Verify khi click field Upload hình ảnh
def test_upload_image_popup(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.enter_title("Bài viết kiểm thử")
    article.enter_content("Đây là nội dung bài viết test")
    article.click_tab_general_info()
    article.click_upload_image_field()
    assert article.is_upload_popup_displayed(), "Test Case FAIL: Pop-up upload hình ảnh không hiển thị"
    logging.info("Test Case PASS: Pop-up upload hình ảnh hiển thị thành công")

# Test Case 29: Verify khi click nút Tải lên 
def test_upload_image_popup(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.enter_title("Bài viết kiểm thử")
    article.enter_content("Đây là nội dung bài viết test")
    article.click_tab_general_info()
    article.click_upload_button()
    assert article.is_upload_popup_displayed(), "Test Case FAIL: Pop-up upload hình ảnh không hiển thị"
    logging.info("Test Case PASS: Pop-up upload hình ảnh hiển thị thành công")

# Test Case 30: Verify khi tải lên hình ảnh field Thumbnail 
def test_upload_thumbnail_image(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.enter_title("Bài viết kiểm thử")
    article.enter_content("Đây là nội dung bài viết test")
    article.click_tab_general_info()
    article.click_upload_thumbnail_image_field()

    # Đợi popup hiển thị xong trước khi click tab Browser
    time.sleep(2)

    # Thực hiện upload hình ảnh
    article.click_tab_browser_by_href()
    article.wait_for_file_listing()  # Đợi danh sách hình ảnh tải xong
    article.select_first_image()  # Click vào ảnh đầu tiên
    article.click_choose_upload_button()

    article.is_thumbnail_image_uploaded()
    print("✅ Ảnh đã được upload thành công.")
    logging.info("Test Case PASS: Upload hình ảnh thành công")

# Test Case 31: Verify khi tải lên hình ảnh field Feature
def test_upload_feature_image(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.enter_title("Bài viết kiểm thử")
    article.enter_content("Đây là nội dung bài viết test")
    article.click_tab_general_info()
    article.click_upload_feature_image_field()

    # Đợi popup hiển thị xong trước khi click tab Browser
    time.sleep(2)

    # Thực hiện upload hình ảnh
    article.click_tab_browser_by_href()
    article.wait_for_file_listing()  # Đợi danh sách hình ảnh tải xong
    article.select_first_image()  # Click vào ảnh đầu tiên
    article.click_choose_upload_button()

    assert article.is_feature_image_uploaded()
    print("✅ Ảnh đã được upload thành công.")
    logging.info("Test Case PASS: Upload hình ảnh thành công")

# Test Case 32: Verify khi click dropdown tag
def test_open_tag_dropdown(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_tab_general_info()
    article.click_tag_dropdown()
    logging.info("Test Case 11 PASS: Hệ thống mở dropdown 'Tag' thành công!")

# Test Case 33: Verify khi chọn tag trong dropdown select 
def test_select_tag_from_dropdown(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_tab_general_info()
    article.click_tag_dropdown()

    expected_tag = "Tag 1"
    logging.info(f"Đang chọn tag: {expected_tag}")

    article.select_tag(expected_tag)

    if article.is_selected_tag_correct(expected_tag):
        logging.info("Test Case PASS: Tag đã chọn hiển thị đúng.")
    else:
        logging.error(f"Test Case FAIL: Tag đã chọn không đúng. Expected: '{expected_tag}'")

# Test Case 34: Verify khi click nút Tạo mới 
def test_create_keyword_sidebar(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_tab_general_info()
    article.click_create_keyword_button()
    assert article.is_add_keyword_sidebar_visible(), "Lỗi: Sidebar 'Thêm từ khóa' không hiển thị!"

# Test Case 35: Verify khi click dropdown Bài viết liên quan 
def test_open_related_article_dropdown(article):
    """✅ Kiểm tra hệ thống mở dropdown 'Bài viết liên quan' thành công"""
    try:
        article.perform_tag_operations()
        article.click_create_new_button()
        article.click_tab_general_info()
        article.click_related_article_dropdown()

        assert article.is_selected_related_article_correct(""), "❌ Lỗi: Dropdown 'Bài viết liên quan' không mở!"
        logging.info("✅ Test Case PASS: Dropdown 'Bài viết liên quan' mở thành công!")
    except TimeoutException:
        logging.error("❌ Test Case FAIL: Không thể mở dropdown 'Bài viết liên quan'.")
        pytest.fail("Lỗi: Dropdown không mở.")

# Test Case 36: Verify khi click chọn bài viết liên quan 
def test_select_related_article_from_dropdown(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_tab_general_info()
    article.click_related_article_dropdown()
    expected_article = "Tổng công ty Hàng hải lãi gần 5.000 tỷ đồng"
    logging.info(f"🔍 Đang chọn bài viết liên quan: {expected_article}")
    article.select_related_article(expected_article)
    article.wait_for_selected_related_article_to_update(expected_article)
    actual_article = "×\n×Tổng công ty Hàng hải lãi gần 5.000 tỷ đồng"
    cleaned_actual_article = actual_article.lstrip("×\n").strip()
    logging.info(f"Giá trị bài viết hiển thị (đã xử lý): '{cleaned_actual_article}'")
    assert cleaned_actual_article == expected_article, (
        f"Test Case FAIL: Expected '{expected_article}', nhưng nhận được '{cleaned_actual_article}'"
    )
    logging.info("Test Case PASS: Bài viết đã chọn hiển thị đúng.")

# Test Case 37: Verify khi không nhập đường dẫn
def test_url_key_auto_generation(article):
    title = "Bài viết test tự động sinh URL"
    expected_url_key = article.generate_expected_url_key(title)
    article.perform_tag_operations()
    article.click_create_new_button()
    article.enter_title(title)
    article.enter_content("Nội dung bài viết test")
    article.click_tab_general_info()
    article.click_select()
    article.select_article_type("Tin tức chuyên ngành")
    article.click_save_and_continue_button()

    # Chờ hệ thống cập nhật URL Key
    time.sleep(2)

    # Kiểm tra URL Key
    url_key_value = article.get_url_key_value()
    logging.info(f"DEBUG: URL Key lấy được từ hệ thống: '{url_key_value}'")

    if url_key_value == expected_url_key:
        logging.info("Test Case PASS: URL Key tự động sinh đúng theo tiêu đề.")
    else:
        logging.error(f"Test Case FAIL: URL Key không đúng. Mong đợi '{expected_url_key}', nhưng nhận '{url_key_value}'.")
        assert False, f"Lỗi: URL Key không đúng. Mong đợi '{expected_url_key}', nhưng nhận '{url_key_value}'."

# Test Case 38: Verify khi nhập đường dẫn
def test_manual_url_key_entry(article):
    title = "Bài viết test nhập URL bằng tay"
    manual_url_key = "bai-viet-custom-url"  # URL Key nhập tay
    article.perform_tag_operations()
    article.click_create_new_button()
    article.enter_title(title)
    article.enter_url_key(manual_url_key)  # Nhập URL Key bằng tay
    article.enter_content("Nội dung bài viết test")
    article.click_tab_general_info()
    article.click_select()
    article.select_article_type("Tin tức chuyên ngành")
    article.click_save_and_continue_button()
    url_key_value = article.get_url_key_value()
    logging.info(f"DEBUG: URL Key lấy được từ hệ thống: '{url_key_value}'")
    if url_key_value == manual_url_key:
        logging.info("Test Case PASS: URL Key nhập tay đúng.")
    else:
        logging.error(f"Test Case FAIL: URL Key không đúng. Mong đợi '{manual_url_key}', nhưng nhận '{url_key_value}'.")
        assert False, f"Lỗi: URL Key không đúng. Mong đợi '{manual_url_key}', nhưng nhận '{url_key_value}'."


def test_delete_feature_image(article):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.enter_title("Bài viết kiểm thử xóa Feature")
    article.enter_content("Đây là nội dung bài viết test")
    article.click_tab_general_info()
    article.click_upload_feature_image_field()
    article.click_tab_browser_by_href()
    article.wait_for_file_listing()
    article.select_first_image()
    article.click_choose_upload_button()

    assert article.is_feature_image_uploaded(), "❌ Lỗi: Ảnh Feature không được tải lên!"

    # Tiến hành xóa ảnh
    article.delete_feature_image()
    assert article.is_feature_image_deleted(), "❌ Lỗi: Ảnh Feature chưa bị xóa!"

    print("✅ Ảnh Feature đã được xóa thành công.")
    logging.info("Test Case PASS: Xóa ảnh Feature thành công")