from selenium.webdriver.common.by import By

class LocatorEditFAQ:

    CONTENT_MENU = (By.XPATH, "//*[@id='left-menu']/ul/li[1]/a")
    FAQ_MENU = (By.XPATH, '//*[@id="left-menu"]/ul/li[1]/ul/li[6]/a')

    # Trang Danh sách câu hỏi
    HOME_PAGE = (By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div/nav/ol/li[1]/a')

    # BUTTON
    CREATE_NEW_BUTTON = (By.XPATH, '//*[@id="app-container"]/main/div/div[2]/div[2]/div/a')
    SAVE_CONTINUE_BUTTON = (By.XPATH, '//*[@id="mpireValidateForm"]/div[1]/div[2]/div/div/button[2]')
    OPERATION_BUTTON = (By.XPATH, '//*[@id="dropdownMenuButton"]')

    # Chỉnh sửa FAQ
    # Thẻ A
    EDIT_FIRST_LINE = (By.XPATH, '//*[@id="table-career-field-list"]/tbody/tr[1]/td[2]/a')

    # TAB
    GENERAL_INFO_TAB = (By.XPATH, '//*[@id="MainTab"]')

    # FIELD HIỂN THỊ - VI
    SELECT_SHOW = (By.XPATH, '//*[@id="select2-status-container"]')
    SELECT_VALUE_NOT = (By.XPATH, '//*[@id="app-container"]/span/span/span[2]/ul/li[2]')
    SELECT_VALUE_HAS = (By.XPATH, '//*[@id="app-container"]/span/span/span[2]/ul/li[1]')

    # FIELD CÂU HỎI - VI
    FAQ_INPUT_VI = (By.XPATH, '//*[@id="cke_1_contents"]/iframe')
    CHECK_FAQ_INPUT_VI = (By.XPATH, '//*[@id="cke_1_contents"]')
    FAQ_ERROR_MESSAGE_VI = (By.XPATH, '//*[@id="vi-content"]/div/div[3]/div/div[2]/div')

    # FIELD CÂU TRẢ LỜI - VI
    ANSWER_INPUT_VI = (By.XPATH, '//*[@id="cke_2_contents"]/iframe')
    ANSWER_ERROR_MESSAGE_VI = (By.XPATH, '//*[@id="vi-content"]/div/div[4]/div/div[2]/div')

    # FIELD LOẠI CÂU HỎI - VI
    SELECT_QUESTION_TYPE = (By.XPATH, '//*[@id="select2-faq_type_id-container"]')
    SELECT_VALUE_PROCEDURE = (By.XPATH, '//*[@id="app-container"]/span/span/span[2]/ul/li[2]')
    SELECT_VALUE_OTHER_SERVICE = (By.XPATH, '//*[@id="app-container"]/span/span/span[2]/ul/li[3]')
    SELECT_VALUE_PILOTAGE_SERVICE = (By.XPATH, '//*[@id="app-container"]/span/span/span[2]/ul/li[4]')

    # FIELD THỨ TỰ SẮP XẾP - VI
    SORT_ORDER_INPUT_VI = (By.XPATH, '//*[@id="ordering"]')
    CHECK_SORT_ORDER_INPUT_VI = (By.XPATH, '//*[@id="showSettingTab"]/div/div[3]/div')

    # FIELD TRẠNG THÁI - VI
    SELECT_STATUS = (By.XPATH, '//*[@id="showSettingTab"]/div/div[5]/div/span/span[1]/span')
    SELECT_VALUE_PENDING = (By.XPATH, '//*[@id="app-container"]/span/span/span[2]/ul/li[2]')
    SELECT_VALUE_ACTIVATE = (By.XPATH, '//*[@id="app-container"]/span/span/span[2]/ul/li[1]')

    # FIELD NGÀY ĐĂNG - VI
    SELECT_POSTED_DATE = (By.XPATH, '//*[@id="public_date"]')
    SELECT_14APR = (By.XPATH, '//*[@id="showSettingTab"]/div/div[4]/div/div[1]/div/ul/li[1]/div/div[1]/table/tbody/tr[3]/td[2]')
    SELECT_VALUE_ACTIVATE = (By.XPATH, '//*[@id="app-container"]/span/span/span[2]/ul/li[1]')