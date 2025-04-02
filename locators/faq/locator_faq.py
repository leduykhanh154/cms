from selenium.webdriver.common.by import By

class LocatorFAQ:

    CONTENT_MENU = (By.XPATH, "//*[@id='left-menu']/ul/li[1]/a")
    FAQ_MENU = (By.XPATH, '//*[@id="left-menu"]/ul/li[1]/ul/li[6]/a')

    # Trang Danh sách câu hỏi
    HOME_PAGE = (By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div/nav/ol/li[1]/a')

    # BUTTON
    CREATE_NEW_BUTTON = (By.XPATH, '//*[@id="app-container"]/main/div/div[2]/div[2]/div/a')
    OPERATION_BUTTON = (By.XPATH, '//*[@id="dropdownMenuButton"]')

    # DROPDOWN
    DROPDOWN_STATUS = (By.XPATH, '//*[@id="mpire-filters-form"]/div[1]/div[1]/div/div/span')
    DROPDOWN_STATUS_VISIBLE = (By.XPATH, '//*[@id="app-container"]/span/span')
    DROPDOWN_QUESTION_TYPE = (By.XPATH, '//*[@id="mpire-filters-form"]/div[1]/div[2]/div/div/span/span[1]')
    DROPDOWN_QUESTION_TYPE_VISIBLE = (By.XPATH, '//*[@id="app-container"]/span/span')

    # FIELD TÌM KIẾM
    SEARCH_INPUT = (By.XPATH, '//*[@id="dt-search-0"]')

    # WRAPPER
    PAGE_LIST_WRAPPER = (By.XPATH, '//*[@id="table-career-field-list_wrapper"]/div[2]')
    QUESTION_LIST_WRAPPER = (By.XPATH, '//*[@id="table-career-field-list"]/tbody/tr[2]/td[2]/a')
    
    # TAG 'A'
    EDIT_TAG_FIRST = (By.XPATH, '//*[@id="table-career-field-list"]/tbody/tr[1]/td[2]/a')

    # POPUP
    SELECT_QUESTION_POPUP = (By.XPATH, '//*[@id="app-container"]/div[3]/div')
    SECURE_POPUP = (By.XPATH, '//*[@id="app-container"]/div[3]/div')

    # SELECT
    SELECT_DELETE = (By.XPATH, '//*[@id="app-container"]/main/div/div[3]/div[2]/div/div/div/div/div[1]/div/div/a')

    # CHECKBOX
    CHECKBOX_FIRST = (By.XPATH, '//*[@id="table-career-field-list"]/tbody/tr[1]/td[1]/div/input')
 
    #
    # Tạo mới FAQ
    # SELECT
    SELECT_SHOW = (By.XPATH, '//*[@id="select2-status-container"]')
    SELECT_VALUE_NOT = (By.XPATH, '//*[@id="app-container"]/span/span/span[2]/ul/li[2]')
    SELECT_VALUE_HAS = (By.XPATH, '//*[@id="app-container"]/span/span/span[2]/ul/li[1]')
    SELECT_VALUE_VISIBLE = (By.XPATH, '//*[@id="select2-status-container"]')    

    # DROPDOWN
    DROPDOWN_SHOW_VISIBLE = (By.XPATH, '//*[@id="app-container"]/span/span')

    # FIELD CÂU HỎI
    FAQ_INPUT = (By.XPATH, '//*[@id="cke_1_contents"]/iframe/html/body')
    FAQ_ERROR_MESSAGE = (By.XPATH, '//*[@id="vi-content"]/div/div[3]/div/div[2]/div')

    # BUTTON
    SAVE_BUTTON = (By.XPATH, '//*[@id="mpireValidateForm"]/div[1]/div[2]/div/div/button[1]')

    
