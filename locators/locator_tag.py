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
    

    TAG_NAME_ERROR_MESSAGE = (By.XPATH, '//*[@id="tabs-listTag"]/div/div[2]/div/div/div')



    # BUTTONS
    ADD_KEYWORD_BUTTON = (By.XPATH, '//*[@id="btnCreateKeyword"]')
    SAVE_BUTTON = (By.XPATH, '//*[@id="formKeyword"]/div[3]/div/button')


    # POP-UP
    ADD_KEYWORD_POPUP = (By.XPATH, '//*[@id="formKeyword"]/div[1]')


    # Input
    TAG_NAME_INPUT = (By.CSS_SELECTOR, "#name")


