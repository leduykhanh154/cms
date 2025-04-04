from selenium.webdriver.common.by import By

class LocatorCreateFAQ:

    CONTENT_MENU = (By.XPATH, "//*[@id='left-menu']/ul/li[1]/a")
    FAQ_MENU = (By.XPATH, '//*[@id="left-menu"]/ul/li[1]/ul/li[6]/a')

    # Trang Danh sách câu hỏi
    HOME_PAGE = (By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div/nav/ol/li[1]/a')

    # BUTTON
    CREATE_NEW_BUTTON = (By.XPATH, '//*[@id="app-container"]/main/div/div[2]/div[2]/div/a')
    OPERATION_BUTTON = (By.XPATH, '//*[@id="dropdownMenuButton"]')

    # Tạo mới FAQ
    # SELECT
    SELECT_SHOW = (By.XPATH, '//*[@id="select2-status-container"]')
    SELECT_VALUE_NOT = (By.XPATH, '//*[@id="app-container"]/span/span/span[2]/ul/li[2]')
    SELECT_VALUE_HAS = (By.XPATH, '//*[@id="app-container"]/span/span/span[2]/ul/li[1]')
    SELECT_VALUE_VISIBLE = (By.XPATH, '//*[@id="select2-status-container"]')
    SELECT_QUESTION_TYPE = (By.XPATH, '//*[@id="select2-faq_type_id-container"]')
    
    # DROPDOWN
    DROPDOWN_VISIBLE = (By.XPATH, '//*[@id="app-container"]/span/span')

    # FIELD CÂU HỎI - VI
    FAQ_INPUT_VI = (By.XPATH, '//*[@id="cke_1_contents"]/iframe')
    FAQ_ERROR_MESSAGE_VI = (By.XPATH, '//*[@id="vi-content"]/div/div[3]/div/div[2]/div')

    # FIELD CÂU TRẢ LỜI - VI
    ANSWER_INPUT_VI = (By.XPATH, '//*[@id="cke_2_contents"]/iframe')
    ANSWER_ERROR_MESSAGE_VI = (By.XPATH, '//*[@id="vi-content"]/div/div[4]/div/div[2]/div')

    # BUTTON
    SAVE_BUTTON = (By.CSS_SELECTOR, '#mpireValidateForm > div.row.page-header > div.col-6.d-flex.justify-content-end > div > div > button:nth-child(1)')

    # TAB
    GENERAL_INFO_TAB = (By.XPATH, '//*[@id="MainTab"]')
    GENERAL_INFO_TAB_DISPLAYED = (By.XPATH, '//*[@id="mpireValidateForm"]/div[2]/div/div/div/div[2]')

    # Field Loại câu hỏi* - Tab Thông tin chung
    SELECT_VALUE_PROCEDURE = (By.XPATH, '//*[@id="app-container"]/span/span/span[2]/ul/li[2]')

    
