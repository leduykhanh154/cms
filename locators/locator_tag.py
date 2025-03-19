from selenium.webdriver.common.by import By

class LocatorTag:
    CONTENT_MENU = (By.XPATH, "//*[@id='left-menu']/ul/li[1]/a")
    ARTICLE_MENU = (By.XPATH, '//*[@id="left-menu"]/ul/li[1]/ul/li[2]/a')
    TAG_MENU = (By.XPATH, '//*[@id="left-menu"]/ul/li[1]/ul/li[2]/ul/li[2]/a')
    HOME_PAGE = (By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div/nav/ol/li[1]/a')
    
    TAG_LIST_URL = "https://mpire-cms-demo.mpire.asia/cms/keyword?page=1"
    HOME_PAGE_URL = "https://mpire-cms-demo.mpire.asia/cms/dashboard"
    PAGE_V2_CREATE_URL = "https://mpire-cms-demo.mpire.asia/cms/admin-page-v2/create"

    PAGE_LIST_WRAPPER = (By.XPATH, '//*[@id="page-v2-list_wrapper"]/div[2]')
    TAG_LIST_WRAPPER = (By.XPATH, '//*[@id="table-keyword-list"]/tbody')
    
    # DROPDOWN
    DROPDOWN_STATUS = (By.XPATH, '//*[@id="mpire-filters-form"]/div[1]/div[1]/div/div')
    DROPDOWN_STATUS_DISPLAY = (By.XPATH, '//*[@id="app-container"]/span/span/span[2]') 
    DROPDOWN_PAGE = (By.XPATH, '//*[@id="table-keyword-list_wrapper"]/div[1]/div[1]/div/label/select')
    DROPDOWN_OPERATION_DISPLAY = (By.XPATH, '//*[@id="app-container"]/main/div/div[4]/div/div/div/div/div[1]/div/div')
    TAG_NAME_ERROR_MESSAGE = (By.XPATH, '//*[@id="tabs-listTag"]/div/div[2]/div/div/div')

    # BUTTONS
    ADD_KEYWORD_BUTTON = (By.XPATH, '//*[@id="btnCreateKeyword"]')
    SAVE_BUTTON = (By.XPATH, '//*[@id="formKeyword"]/div[3]/div/button')
    OPERATION_BUTTON = (By.XPATH, '//*[@id="dropdownMenuButton"]')
    YES_BUTTON = (By.XPATH, '//*[@id="app-container"]/div[3]/div/div[3]/button[1]')
    NO_BUTTON = (By.XPATH, '//*[@id="app-container"]/div[3]/div/div[3]/button[3]')

    
    # POP-UP
    ADD_KEYWORD_POPUP = (By.XPATH, '//*[@id="formKeyword"]/div[1]')
    DELETE_POPUP = (By.XPATH, '//*[@id="app-container"]/div[3]/div')
    EDIT_TAG_POPUP = (By.XPATH, '//*[@id="formKeyword"]/div[1]')

    # Input
    TAG_NAME_INPUT = (By.CSS_SELECTOR, "#name") 
    SEARCH_INPUT = (By.XPATH, '//*[@id="dt-search-0"]')

    # CHECKBOX
    CHECKBOX_FIRST = (By.CLASS_NAME, 'styled.ck.selectable-item')

    # TAG 'A'
    EDIT_TAG_FIRST = (By.XPATH, '//*[@id="table-keyword-list"]/tbody/tr[1]/td[2]/a')