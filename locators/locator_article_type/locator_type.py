from selenium.webdriver.common.by import By

class LocatorArticleType:
    # Menu
    CONTENT_MENU = (By.XPATH, "//*[@id='left-menu']/ul/li[1]/a")
    ARTICLE_MENU = (By.XPATH, "//*[@id='left-menu']/ul/li[1]/ul/li[2]/a")
    ARTICLE_TYPE_MENU= (By.XPATH, '//*[@id="left-menu"]/ul/li[1]/ul/li[2]/ul/li[3]/a')
    
    # Breadcrumb
    BREADCRUMB_HOME = (By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div/nav/ol/li[1]/a')
    BREADCRUMB_TYPE_LIST = (By.XPATH, '//*[@id="app-container"]/main/div/div/div/nav/ol/li[2]/a')

    # Status
    DROPDOWN_STATUS = (By.XPATH, '//*[@id="mpire-filters-form"]/div[1]/div[1]/div/div/span')
    ITEM_ACTIVE = (By.XPATH, '//*[@id="select2-select-status-result-oyms-1"]')
    ITEM_PROCESSING = (By.XPATH, '//*[@id="select2-select-status-result-lw57-2"]')
    
    # From Date
    DATEPICKER_FROM = (By.XPATH, '//*[@id="mpire-filters-form"]/div[1]/div[2]/div/div[1]')
    
    # To Date
    DATEPICKER_TO = (By.XPATH, '//*[@id="mpire-filters-form"]/div[1]/div[2]/div/div[2]')
    
    # Father type
    DROPDOWN_FATHER_TYPE = (By.XPATH, '//*[@id="mpire-filters-form"]/div[1]/div[3]/div/div/span')
    SEARCHBAR_FATHER_TYPE = (By.XPATH, '//*[@id="app-container"]/span/span/span[1]/input')
    ALL_FATHER_TYPE = (By.XPATH, '//*[@id="select2-category_id-result-ogr9-0"]')
    FIRST_FATHER_TYPE = (By.XPATH, '//*[@id="select2-category_id-result-ljr2-673451b5e69e1"]')
    SECOND_FATHER_TYPE = (By.XPATH, '//*[@id="select2-category_id-result-1g4t-67345ab3e3570"]')
    THIRD_FATHER_TYPE = (By.XPATH, '//*[@id="select2-category_id-result-h5ar-672d94557669f"]')
    
    # Split
    DROPDOWN_SPLIT = (By.XPATH, '//*[@id="table-category-list_wrapper"]/div[1]/div[1]/div/label/select')
    
    # Button
    NEW_TYPE_BUTTON = (By.XPATH, "//*[@id='app-container']/main/div/div[2]/div[2]/div/a")
    RESET_BUTTON = (By.XPATH, '//*[@id="mpire-filters-form"]/div[2]/a')
    OPERATE_BUTTON = (By.XPATH, '//*[@id="dropdownMenuButton"]')
    DELETE_BUTTON = (By.XPATH, '//*[@id="app-container"]/main/div/div[3]/div[2]/div/div/div/div/div[1]/div/div/a')
    
    # Selected line
    SELECTED_LINE = (By.XPATH, '//*[@id="count"]')
    
    # Searchbar
    SEARCHBAR = (By.XPATH, '//*[@id="dt-search-0"]')
    
    # Checkbox
    SELECT_ALL = (By.XPATH, '//*[@id="table-category-list"]/thead/tr/th[1]/span[1]/span/input')
    SELECT_FIRST = (By.XPATH, '//*[@id="checkbox67ef62b07e389"]')
    
    # Link
    FIRST_LINK = (By.XPATH, '//*[@id="table-category-list"]/tbody/tr[1]/td[2]/a')
    
    # First menu item 
    FIRST_MENU_BUTTON = (By.XPATH, '//*[@id="dropdownMenuLink13"]')
    DETAIL_BUTTON = (By.XPATH, '//*[@id="table-category-list"]/tbody/tr[1]/td[8]/div/div/a[1]')
    DELETE2_BUTTON = (By.XPATH, '//*[@id="table-category-list"]/tbody/tr[1]/td[8]/div/div/a[2]')
    
    # Warning
    POPUP_WARNING = (By.XPATH, '//*[@id="app-container"]/div[3]/div')
    WARNING_TEXT = (By.XPATH, '//*[@id="swal2-title"]')
    YES_BUTTON = (By.XPATH, '//*[@id="app-container"]/div[3]/div/div[3]/button[1]')
    NO_BUTTON = (By.XPATH, '//*[@id="app-container"]/div[3]/div/div[3]/button[3]')

    # Title
    ARTICLE_TYPE_TITLE = (By.XPATH, '//*[@id="languages[vi][title]"]')
    
    # Create date
    FIRST_CREATE_DATE = (By.XPATH, '//*[@id="table-category-list"]/tbody/tr[1]/td[6]')