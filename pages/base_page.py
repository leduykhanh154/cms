import time
import pytest
import logging
import datetime
from utils.login import Login
from utils.driver_setup import get_driver
from pages.articles.article import Article
from pages.articles.select import SelectArticle
from pages.articles.enterfield import EnterFieldArticle
from pages.articles.validation import ArticleValidation
from selenium.webdriver.support import expected_conditions as EC

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

# Test Case 3: Verify khi không nhập Tiêu đề - Tiếng Việt -> Hệ thống hiển thị thống báo lỗi 'Vui lòng nhập Tiêu đề'
def test_empty_article_title_vi(article, enter_field, validation):
    article.perform_tag_operations()
    article.click_create_new_button()
    enter_field.enter_title_vi("")
    article.click_save_button()
    error_message = validation.is_title_vi_error_displayed()
    if error_message:
        logging.info("Test Case 3 PASS: Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Tiêu đề'")
    else:
        logging.error("Test Case 3 FAIL: Hệ thống không hiển thị thông báo lỗi 'Vui lòng nhập Tiêu đề'")
        assert False, "Lỗi: Không hiển thị thông báo 'Vui lòng nhập Tiêu đề'"

# Test Case 4: Verify khi nhập Tiêu đề - Tiếng Việt -> Hệ thống ẩn đi thông báo lỗi 'Vui lòng nhập Tiêu đề'
def test_title_vi_error_disappears(article, enter_field, validation):
    article.perform_tag_operations()
    article.click_create_new_button()
    enter_field.enter_title_vi("")
    article.click_save_button()
    validation.is_title_vi_error_displayed()
    enter_field.enter_title_vi("Tiêu đề bài viết")
    if not validation.is_title_vi_error_displayed():
        logging.info("Test Case 4 PASS: Thông báo lỗi bị ẩn sau khi nhập Tiêu đề")
    else:
        logging.error("Test Case 4 FAIL: Thông báo lỗi vẫn còn sau khi nhập tiêu đề!")
        assert False, "Lỗi: Thông báo lỗi vẫn còn sau khi nhập tiêu đề."

# Test Case 5: Verify khi nhập Tiêu đề - Tiếng Việt hơn 250 ký tự -> Hệ thống hiển thị thông báo lỗi 'Tiêu đề không được vượt quá 250 ký tự'
def test_title_vi_max_length_error(article, enter_field, validation):
    article.perform_tag_operations()
    article.click_create_new_button()
    long_title = "A" * 251
    enter_field.enter_title_vi(long_title)
    article.click_save_button()
    if validation.is_title_vi_max_length_error_displayed():
        logging.info("Test Case 5 PASS: Hệ thống hiển thị lỗi khi tiêu đề vượt quá 250 ký tự.")
    else:
        logging.error("Test Case 5 FAIL: Hệ thống không hiển thị lỗi khi tiêu đề quá dài!")
        assert False, "Lỗi: Không hiển thị thông báo 'Tiêu đề không được vượt quá 250 ký tự'."

# Test Case 6: Verify khi giảm số ký tự trong Tiêu đề - Tiếng Việt xuống <= 250 -> Hệ thống ẩn đi thông báo lỗi 'Vui lòng nhập Tiêu đề không quá 250 ký tự'
def test_title_vi_max_length_error_disappears(article, enter_field, validation):
    article.perform_tag_operations()
    article.click_create_new_button()
    long_title = "A" * 251
    enter_field.enter_title_vi(long_title)
    article.click_save_button()
    assert validation.is_title_vi_max_length_error_displayed(), "Lỗi: Không hiển thị thông báo 'Vui lòng nhập Tiêu đề không quá 250 ký tự'"
    short_title = "A" * 250 
    enter_field.enter_title_vi(short_title)
    if not validation.is_title_vi_max_length_error_displayed():
        logging.info("Test Case 6 PASS: Thông báo lỗi bị ẩn sau khi giảm số ký tự xuống <= 250.")
    else:
        logging.error("Test Case 6 FAIL: Thông báo lỗi vẫn còn dù tiêu đề đã giảm xuống <= 250 ký tự!")
        assert False, "Lỗi: Thông báo lỗi vẫn còn dù tiêu đề đã giảm xuống <= 250 ký tự."

# Test Case 7: Verify khi không nhập Tiêu đề - Enlish -> Hệ thống hiển thị thống báo lỗi 'Vui lòng nhập Tiêu đề'
def test_empty_article_title_en(article, enter_field, validation):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_en_tab()
    article.click_translate_content_button()
    enter_field.enter_title_en("")
    article.click_save_button()
    error_message = validation.is_title_en_error_displayed()
    if error_message:
        logging.info("Test Case 7 PASS: Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Tiêu đề'")
    else:
        logging.error("Test Case 7 FAIL: Hệ thống không hiển thị thông báo lỗi 'Vui lòng nhập Tiêu đề'")
        assert False, "Lỗi: Không hiển thị thông báo 'Vui lòng nhập Tiêu đề'"

# Test Case 8: Verify khi nhập Tiêu đề - Enlish -> Hệ thống ẩn đi thông báo lỗi 'Vui lòng nhập Tiêu đề'
def test_title_en_error_disappears(article, enter_field, validation):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_en_tab()
    article.click_translate_content_button()
    enter_field.enter_title_en("")
    article.click_save_button()
    validation.is_title_en_error_displayed()
    enter_field.enter_title_en("Article Title")
    if not validation.is_title_en_error_displayed():
        logging.info("Test Case 8 PASS: Thông báo lỗi bị ẩn sau khi nhập Tiêu đề")
    else:
        logging.error("Test Case 8 FAIL: Thông báo lỗi vẫn còn sau khi nhập tiêu đề!")
        assert False, "Lỗi: Thông báo lỗi vẫn còn sau khi nhập tiêu đề."

# Test Case 9: Verify khi nhập Tiêu đề - Enlish hơn 250 ký tự -> Hệ thống hiển thị thông báo lỗi 'Tiêu đề không được vượt quá 250 ký tự'
def test_title_en_max_length_error(article, enter_field, validation):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_en_tab()
    article.click_translate_content_button()
    long_title = "A" * 251
    enter_field.enter_title_en(long_title)
    article.click_save_button()
    if validation.is_title_en_max_length_error_displayed():
        logging.info("Test Case 9 PASS: Hệ thống hiển thị lỗi khi tiêu đề vượt quá 250 ký tự.")
    else:
        logging.error("Test Case 9 FAIL: Hệ thống không hiển thị lỗi khi tiêu đề quá dài!")
        assert False, "Lỗi: Không hiển thị thông báo 'Tiêu đề không được vượt quá 250 ký tự'."

# Test Case 10: Verify khi giảm số ký tự trong Tiêu đề - Enlish xuống <= 250 -> Hệ thống ẩn đi thông báo lỗi 'Vui lòng nhập Tiêu đề không quá 250 ký tự'
def test_title_en_max_length_error_disappears(article, enter_field, validation):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_en_tab()
    article.click_translate_content_button()
    long_title = "A" * 251
    enter_field.enter_title_en(long_title)
    article.click_save_button()
    assert validation.is_title_en_max_length_error_displayed(), "Lỗi: Không hiển thị thông báo 'Vui lòng nhập Tiêu đề không quá 250 ký tự'"
    short_title = "A" * 250 
    enter_field.enter_title_en(short_title)
    if not validation.is_title_en_max_length_error_displayed():
        logging.info("Test Case 10 PASS: Thông báo lỗi bị ẩn sau khi giảm số ký tự xuống <= 250.")
    else:
        logging.error("Test Case 10 FAIL: Thông báo lỗi vẫn còn dù tiêu đề đã giảm xuống <= 250 ký tự!")
        assert False, "Lỗi: Thông báo lỗi vẫn còn dù tiêu đề đã giảm xuống <= 250 ký tự."

# Test Case 11: Verify khi nhập Mô tả ngắn - Tiếng Việt hơn 1000 ký tự -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Mô tả ngắn không quá 1000 ký tự'
def test_short_description_vi_max_length_error(article, enter_field, validation):
    article.perform_tag_operations()
    article.click_create_new_button()
    long_title = "A" * 1002
    enter_field.enter_short_description_vi(long_title)
    article.click_save_button()
    if validation.is_short_description_vi_max_lenght_error_displayed():
        logging.info("Test Case 11 PASS: Hệ thống hiển thị lỗi khi mô tả ngắn vượt quá 1000 ký tự.")
    else:
        logging.error("Test Case 11 FAIL: Hệ thống không hiển thị lỗi khi mô tả ngắn quá dài!")
        assert False, "Lỗi: Không hiển thị thông báo 'Vui lòng nhập Mô tả ngắn không quá 1000 ký tự'."
    
# Test Case 12: Verify khi nhập lại Mô tả ngắn - Tiếng Việt < 100 ký tự -> Hệ thống ẩn đi thông báo lỗi 'Vui lòng nhập Mô tả ngắn không quá 100 ký tự'
def test_short_description_vi_max_length_error_disappears(article, enter_field, validation):
    article.perform_tag_operations()
    article.click_create_new_button()
    long_title = "A" * 1002
    enter_field.enter_short_description_vi(long_title)
    article.click_save_button()
    assert validation.is_short_description_vi_max_lenght_error_displayed(), "Lỗi: Không hiển thị thông báo 'Hệ thống hiển thị lỗi khi mô tả ngắn vượt quá 1000 ký tự.'"
    short_title = "A" * 999
    enter_field.enter_short_description_vi(short_title)
    if not validation.is_short_description_vi_max_lenght_error_displayed():
        logging.info("Test Case 12 PASS: Thông báo lỗi bị ẩn sau khi giảm số ký tự xuống <= 1000.")
    else:
        logging.error("Test Case 12 FAIL: Thông báo lỗi vẫn còn dù tiêu đề đã giảm xuống <= 1000 ký tự!")
        assert False, "Lỗi: Thông báo lỗi vẫn còn dù tiêu đề đã giảm xuống <= 1000 ký tự."

# Test Case 13: Verify khi nhập Mô tả ngắn - English hơn 1000 ký tự -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Mô tả ngắn không quá 1000 ký tự'
def test_short_description_vi_max_length_error(article, enter_field, validation):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_en_tab()
    article.click_translate_content_button()
    long_title = "A" * 1002
    enter_field.enter_short_description_en(long_title)
    article.click_save_button()
    if validation.is_short_description_en_max_lenght_error_displayed():
        logging.info("Test Case 13 PASS: Hệ thống hiển thị lỗi khi mô tả ngắn vượt quá 1000 ký tự.")
    else:
        logging.error("Test Case 13 FAIL: Hệ thống không hiển thị lỗi khi mô tả ngắn quá dài!")
        assert False, "Lỗi: Không hiển thị thông báo 'Vui lòng nhập Mô tả ngắn không quá 1000 ký tự'."

# Test Case 14: Verify khi nhập lại Mô tả ngắn - English < 100 ký tự -> Hệ thống ẩn đi thông báo lỗi 'Vui lòng nhập Mô tả ngắn không quá 100 ký tự'
def test_short_description_vi_max_length_error_disappears(article, enter_field, validation):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_en_tab()
    article.click_translate_content_button()
    long_title = "A" * 1002
    enter_field.enter_short_description_en(long_title)
    article.click_save_button()
    assert validation.is_short_description_en_max_lenght_error_displayed(), "Lỗi: Không hiển thị thông báo 'Hệ thống hiển thị lỗi khi mô tả ngắn vượt quá 1000 ký tự.'"
    short_title = "A" * 999
    enter_field.enter_short_description_en(short_title)
    if not validation.is_short_description_en_max_lenght_error_displayed():
        logging.info("Test Case 14 PASS: Thông báo lỗi bị ẩn sau khi giảm số ký tự xuống <= 1000.")
    else:
        logging.error("Test Case 14 FAIL: Thông báo lỗi vẫn còn dù tiêu đề đã giảm xuống <= 1000 ký tự!")
        assert False, "Lỗi: Thông báo lỗi vẫn còn dù tiêu đề đã giảm xuống <= 1000 ký tự."

# Test Case 15: Verify khi không nhập Nội dung - Tiếng Việt -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Nội dung'
def test_empty_article_content_vi(article, enter_field, validation):
    article.perform_tag_operations()
    article.click_create_new_button()
    enter_field.enter_title_vi("Tiêu đề bài viết")
    enter_field.enter_content_vi("")
    article.click_save_button()
    error_message = validation.is_content_vi_error_displayed()
    if error_message:
        logging.info("Test Case 15 PASS: Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Nội dung'")
    else:
        logging.error("Test Case 15 FAIL: Hệ thống không hiển thị thông báo lỗi 'Vui lòng nhập Nội dung'")
        assert False, "Lỗi: Không hiển thị thông báo 'Vui lòng nhập Nội dung'."

# Test Case 16: Verify khi nhập dữ liệu vào field Nội dung - Tiếng Việt -> Hệ thống không hiển thị thông báo lỗi 'Vui lòng nhập Nội dung'
def test_content_vi_error_disappears(article, enter_field, validation):
    article.perform_tag_operations()
    article.click_create_new_button()
    enter_field.enter_title_vi("Tiêu đề bài viết")
    enter_field.enter_content_vi("")
    article.click_save_button()
    validation.is_content_vi_error_displayed()
    enter_field.enter_content_vi("Nội dung bài viết")
    error_message_after_input = validation.is_content_vi_error_displayed()
    if not error_message_after_input:
        logging.info("Test Case 16 PASS: Thông báo lỗi bị ẩn sau khi nhập Nội dung")
    else:
        logging.error("Test Case 16 FAIL: Thông báo lỗi vẫn còn sau khi nhập Nội dung!")
        assert False, "Lỗi: Thông báo lỗi vẫn còn sau khi nhập Nội dung."

# Test Case 17: Verify khi không nhập Nội dung - English -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Nội dung'
def test_empty_article_content_en(article, enter_field, validation):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_en_tab()
    article.click_translate_content_button()
    enter_field.enter_title_en("Article Title")
    enter_field.enter_content_en("")
    article.click_save_button()
    error_message = validation.is_content_en_error_displayed()
    if error_message:
        logging.info("Test Case 17 PASS: Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Nội dung'")
    else:
        logging.error("Test Case 17 FAIL: Hệ thống không hiển thị thông báo lỗi 'Vui lòng nhập Nội dung'")
        assert False, "Lỗi: Không hiển thị thông báo 'Vui lòng nhập Nội dung'."

# Test Case 18: Verify khi nhập dữ liệu vào field Nội dung - Tiếng Việt -> Hệ thống không hiển thị thông báo lỗi 'Vui lòng nhập Nội dung'
def test_content_en_error_disappears(article, enter_field, validation):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_en_tab()
    article.click_translate_content_button()
    enter_field.enter_title_en("Article Title")
    enter_field.enter_content_en("")
    article.click_save_button()
    validation.is_content_en_error_displayed()
    enter_field.enter_content_en("Article Content")
    error_message_after_input = validation.is_content_en_error_displayed()
    if not error_message_after_input:
        logging.info("Test Case 18 PASS: Thông báo lỗi bị ẩn sau khi nhập Nội dung")
    else:
        logging.error("Test Case 18 FAIL: Thông báo lỗi vẫn còn sau khi nhập Nội dung!")
        assert False, "Lỗi: Thông báo lỗi vẫn còn sau khi nhập Nội dung."

# Test Case 19: Verify khi không chọn 'Loại bài viết' -> Hệ thống hiển thị thông báo lỗi 'Vui lòng nhập Loại bài viết'
def test_article_type_error(article, enter_field, validation):
    article.perform_tag_operations()
    article.click_create_new_button()
    enter_field.enter_title_vi("Tiêu đề bài viết")
    enter_field.enter_content_vi("Nội dung bài viết")
    article.click_save_button()
    article.click_tab_general_info()
    error_message = validation.is_article_type_error_displayed()
    if error_message:
        logging.info("Test Case 19 PASS: Hệ thống hiển thị đúng thông báo lỗi khi không chọn loại bài viết.")
    else:
        logging.error("Test Case 19 FAIL: Hệ thống KHÔNG hiển thị lỗi khi không chọn loại bài viết!")
        assert False, "Lỗi: Không hiển thị thông báo 'Vui lòng nhập Loại bài viết'."

# Test Case 20: Verify khi click vào dropdown 'Loại bài viết' -> Hệ thống mở dropdown 'Loại bài viết'
def test_open_article_type_dropdown(article, select):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_tab_general_info()
    select.click_select()
    if select.is_dropdown_visible():
        logging.info("Test Case 20 PASS: Hệ thống mở dropdown 'Loại bài viết' thành công!")
    else:
        logging.error("Test Case 20 FAIL: Hệ thống không mở dropdown 'Loại bài viết'!")
        assert False, "Lỗi: Dropdown không mở."
    
# Test Case 21: Verify khi chọn 'Loại bài viết' từ dropdown -> Hệ thống hiển thị đúng giá trị đã chọn và ẩn đi thông báo lỗi
def test_select_article_type_from_dropdown(article, select):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_tab_general_info()
    select.click_select()
    select.select_article_type("Tin tức chuyên ngành")
    if select.is_selected_article_type_displayed("Tin tức chuyên ngành"):
        logging.info("Test Case 21 PASS: Loại bài viết đã chọn hiển thị đúng.")
    else:
        logging.error(f"Test Case 21 FAIL: Loại bài viết đã chọn không đúng. Expected: 'Tin tức chuyên ngành'")
        assert False, "Lỗi: Loại bài viết hiển thị không đúng."

# Test Case 22: Verify sau khi nhập đầy đủ thông tin và nhấn nút Lưu -> Hệ thống chuyển hướng về trang Danh sách bài viết
def test_save_article(article, enter_field, select):
    article.perform_tag_operations()
    article.click_create_new_button()
    enter_field.enter_title_vi("Tiêu đề bài viết")
    enter_field.enter_short_description_vi("Mô tả ngắn bài viết")
    enter_field.enter_content_vi("Nội dung bài viết")
    article.click_en_tab()
    article.click_translate_content_button()
    enter_field.enter_title_en("Article Title")
    enter_field.enter_short_description_en("Article Short Description")
    enter_field.enter_content_en("Article Content")
    article.click_tab_general_info()
    select.click_select()
    select.select_article_type("Tin tức chuyên ngành")
    article.click_save_button()
    if article.wait_for_article_to_appear_in_list("Tiêu đề bài viết"):
        logging.info("Test Case 22 PASS: Bài viết hiển thị đúng tên trong danh sách bài viết.")
    else:
        logging.error("Test Case 22 FAIL: Tên bài viết không xuất hiện trong danh sách bài viết.")

# Test Case 23: Verify khi nhấn nút Lưu và tiếp tục chỉnh sửa -> Hệ thống ở lại trang để tiếp tục chỉnh sửa
def test_save_article(article, enter_field, select):
    article.perform_tag_operations()
    article.click_create_new_button()
    enter_field.enter_title_vi("Tiêu đề bài viết")
    enter_field.enter_short_description_vi("Mô tả ngắn bài viết")
    enter_field.enter_content_vi("Nội dung bài viết")
    article.click_en_tab()
    article.click_translate_content_button()
    enter_field.enter_title_en("Article Title")
    enter_field.enter_short_description_en("Article Short Description")
    enter_field.enter_content_en("Article Content")
    article.click_tab_general_info()
    select.click_select()
    select.select_article_type("Tin tức chuyên ngành")
    article.click_save_and_continue_button()
    if article.wait_for_article_to_appear_in_list("Tiêu đề bài viết"):
        logging.info("Test Case 23 PASS: Bài viết hiển thị đúng tên trong danh sách bài viết.")
    else:
        logging.error("Test Case 23 FAIL: Tên bài viết không xuất hiện trong danh sách bài viết.")

# Test Case 24: Verify khi thay đổi giá trị trong dropdown Loại bài viết -> Hệ thống cập nhật lại giá trị Loại bài viết
def test_change_article_type_after_selection(article, select):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_tab_general_info()
    select.click_select()
    select.select_article_type("Tin tức chuyên ngành")
    assert select.is_selected_article_type_displayed("Tin tức chuyên ngành"), "Lỗi: Giá trị 'Loại bài viết' ban đầu không đúng."
    select.click_select()
    select.select_article_type("Lĩnh vực kinh doanh")
    if select.is_selected_article_type_displayed("Lĩnh vực kinh doanh"):
        logging.info("Test Case 24 PASS: Giá trị 'Loại bài viết' được cập nhật chính xác sau khi thay đổi.")
    else:
        logging.error("Test Case 24 FAIL: Giá trị 'Loại bài viết' không cập nhật đúng. Expected: 'Lĩnh vực kinh doanh'")
        assert False, "Lỗi: Giá trị 'Loại bài viết' không cập nhật sau khi thay đổi."

# Test Case 25: Verify khi click vào dropdown 'Trạng thái' -> Hệ thống mở dropdown 'Trạng thái'
def test_open_status_dropdown(article, select):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_tab_general_info()
    select.click_status_dropdown()
    if select.is_status_dropdown_visible():
        logging.info("Test Case 25 PASS: Hệ thống mở dropdown 'Trạng thái' thành công!")
    else:
        logging.error("Test Case 25 FAIL: Hệ thống không mở dropdown 'Trạng thái'!")
        assert False, "Lỗi: Dropdown không mở."

# Test Case 26: Verify khi click chọn giá trị Chờ xử lý -> Hệ thống hiển thị giá trị chờ xử lý lên dropdown Trạng thái
def test_select_status_from_dropdown(article, select):
    article.perform_tag_operations()
    article.click_create_new_button()
    article.click_tab_general_info()
    select.click_status_dropdown()
    select.select_status("Chờ xử lý")
    if select.is_status_selected("Chờ xử lý"):
        logging.info("Test Case 26 PASS: Trạng thái đã chọn hiển thị đúng.")
    else:
        logging.error("Test Case 26 FAIL: Trạng thái đã chọn không đúng. Expected: 'Chờ xử lý'")
        assert False, "Lỗi: Trạng thái hiển thị không đúng."
    
