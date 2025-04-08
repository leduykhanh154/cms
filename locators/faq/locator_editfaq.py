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

    # SELECT HIỂN THỊ - VI
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
    
