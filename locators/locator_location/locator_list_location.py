from selenium.webdriver.common.by import By

class LocatorListLocation:
    # MENU
    CONTENT_MENU = (By.XPATH, "//*[@id='left-menu']/ul/li[1]/a")
    LOCATION_MENU = (By.XPATH, '//*[@id="left-menu"]/ul/li[1]/ul/li[5]/a')
    
    # BREADCRUMB
    HOME_BREADCRUMB = (By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div/nav/ol/li[1]/a')
    
    # BUTTON
    CREATE_BUTTON = (By.XPATH, '//*[@id="app-container"]/main/div/div[2]/div[2]/div/a')
    RELOAD_BUTTON = (By.XPATH, '//*[@id="mpire-filters-form"]/div[2]/a')
    OPERATE_BUTTON = (By.XPATH, '//*[@id="dropdownMenuButton"]')
    DELETE_BUTTON = (By.XPATH, '//*[@id="app-container"]/main/div/div[3]/div[2]/div/div/div/div/div[1]/div/div/a')
    
    # DROPDOWN
    PROVINCE_DROPDOWN = (By.XPATH, '//*[@id="select2-select-province-container"]')
    FIRST_ITEM_PROVINCE = (By.XPATH, '//*[@id="app-container"]/span/span/span[2]/ul/li[2]')
    DISTRICT_DROPDOWN = (By.XPATH, '//*[@id="select2-select-district-container"]')
    FIRST_ITEM_DISTRICT = (By.XPATH, '//*[@id="app-container"]/span/span/span[2]/ul/li[2]')
    STATUS_DROPDOWN = (By.XPATH, '//*[@id="select2-select-status-container"]')
    ACTIVE_STATUS = (By.XPATH, '//*[@id="app-container"]/span/span/span[2]/ul/li[2]')
    PROCESSING_STATUS = (By.XPATH, '//*[@id="app-container"]/span/span/span[2]/ul/li[3]')
    PAGINATION_DROPDOWN = (By.XPATH, '//*[@id="table-dealer-list_wrapper"]/div[1]/div[1]/div/label/select')
    FIRST_PAGINATION_ITEM = (By.XPATH, '//*[@id="table-dealer-list_wrapper"]/div[1]/div[1]/div/label/select/option[1]')
    
    # DATEPICKER
    FROM_DATE_DATEPICKER = (By.XPATH, '//*[@id="from_date"]')
    TO_DATE_DAYEPICKER = (By.XPATH, '//*[@id="to_date"]')
    
    # TEXT
    SELECTED_NUMBER = (By.XPATH, '//*[@id="count"]')
    
    # SEARCHBAR
    LOCATION_SEARCHBAR = (By.XPATH, '//*[@id="dt-search-0"]')
    
    # CHECKBOX
    SELECT_ALL_CHECKBOX = (By.XPATH, '//*[@id="table-dealer-list"]/thead/tr/th[1]/span[1]/span/input')
    SELECT_FIRST_CHECKBOX = (By.XPATH, '//*[@id="checkbox67f8cc107222e"]')
    
    # LOCATION NAME
    FIRST_LOCATION_NAME = (By.XPATH, '//*[@id="table-dealer-list"]/tbody/tr[1]/td[2]/a')
    
    # MENU ITEM
    FIRST_MENU_BUTTON = (By.XPATH, '//*[@id="dropdownMenuLink13"]')
    FIRST_DETAIL_MENU_ITEM = (By.XPATH, '//*[@id="table-dealer-list"]/tbody/tr[1]/td[9]/div/div/a[1]')
    FIRST_DELETE_MENU_ITEM = (By.XPATH, '//*[@id="table-dealer-list"]/tbody/tr[1]/td[9]/div/div/a[2]')
    
    # POPUP
    WARNING_POPUP = (By.XPATH, '//*[@id="app-container"]/div[3]/div')
    WARNING_TEXT = (By.XPATH, '//*[@id="swal2-title"]')
    YES_BUTTON = (By.XPATH, '//*[@id="app-container"]/div[3]/div/div[3]/button[1]')
    NO_BUTTON = (By.XPATH, '//*[@id="app-container"]/div[3]/div/div[3]/button[3]')
    
    