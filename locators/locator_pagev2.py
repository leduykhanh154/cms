from selenium.webdriver.common.by import By

class LocatorPageV2:
    # Menu navigation
    CONTENT_MENU = (By.XPATH, "//*[@id='left-menu']/ul/li[1]/a")
    MENU_PAGE_V2 = (By.XPATH, "//*[@id='left-menu']/ul/li[1]/ul/li[10]/a")

    # URLs
    PAGE_V2_LIST_URL = "https://mpire-cms-demo.mpire.asia/cms/admin-page-v2?page=1"
    PAGE_V2_CREATE_URL = "https://mpire-cms-demo.mpire.asia/cms/admin-page-v2/create"

    # Buttons
    CREATE_NEW_BUTTON = (By.XPATH, "//*[@id='app-container']/main/div/div[2]/div[2]/div/a")
    ADD_SECTION_BUTTON = (By.XPATH, "//*[@id='accordionParent']/div[2]/div[1]/div[2]/button[5]")
    ADD_BUTTON = (By.XPATH, '//*[@id="app-container"]/div[12]/div/div/div[3]/button[2]')
    SAVE_BUTTON = (By.XPATH, '//*[@id="sticky-header"]/div[2]/div/div/div/button[1]')
    SAVE_AND_CONTINUE_BUTTON = (By.XPATH, '//*[@id="sticky-header"]/div[2]/div/div/div/button[2]')

    # Inputs
    PAGE_TITLE_INPUT = (By.ID, "root_content_title-vi")
    URL_KEY_INPUT = (By.XPATH, '//*[@id="root_content_url_key-vi"]')

    # Error messages
    TITLE_ERROR_MESSAGE = (By.XPATH, "//*[@id='root_content_title__error-0']")

    # Section-related locators
    SECTION_NEWS = (By.ID, "news")
    ADD_SECTION_POPUP = (By.XPATH, '//*[@id="app-container"]/div[12]/div/div') 
    NEWS_SECTION = (By.XPATH, '//*[@id="accordionParent"]/div[2]/div[2]') 
    NEWS_SECTION_DISPLAY = (By.XPATH, '//*[@id="accordionParent"]/div[2]/div[2]/div[1]/div/div[1]/li/div/div')  
    SECTION_LIST = (By.XPATH, '//*[@id="accordionParent"]/div[2]/div[2]/div[1]/div')  
    NEWS_SECTION_ERROR = (By.XPATH, ".//div[starts-with(@id, 'root_') and contains(@id, '_title__error')]")  

    # Page list
    PAGE_LIST_WRAPPER = (By.XPATH, '//*[@id="page-v2-list_wrapper"]/div[2]')