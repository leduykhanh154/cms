from selenium.webdriver.common.by import By

class LocatorPageV2:
    CONTENT_MENU = (By.XPATH, "//*[@id='left-menu']/ul/li[1]/a")
    MENU_PAGE_V2 = (By.XPATH, "//*[@id='left-menu']/ul/li[1]/ul/li[10]/a")
    TYPE_ARTICLE_BUTTON = (By.XPATH, '//*[@id="u486rctj29-section"]/div/div/div/div/div/div/div[4]/div/div/div/div/div[1]/button')
    PAGE_V2_LIST_URL = "https://mpire-cms-demo.mpire.asia/cms/admin-page-v2?page=1"
    PAGE_V2_CREATE_URL = "https://mpire-cms-demo.mpire.asia/cms/admin-page-v2/create"
    PAGE_LIST_WRAPPER = (By.XPATH, '//*[@id="page-v2-list_wrapper"]/div[2]')

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
   
   # Selects
    SELECT_LIST_BY = (By.ID, 'react-select-6-input')
    SELECT_LIST_BY_OPTION = (By.XPATH, '//*[@id="react-select-6-option-0"]')
    SELECT_LIST_BY_TYPE_ARTICLE = (By.XPATH, '//*[@id="react-select-6-option-1"]')

    # Section-related locators
    NAME_SECTION = (By.XPATH, '//*[@id="accordionParent"]/div[2]/div[2]/div[1]/div/div[1]/li/div/div/h2/div/div[2]/text()')
    NAME_SECTION_RENAME = (By.XPATH, '//*[@id="accordionParent"]/div[2]/div[2]/div[1]/div/div[1]/li/div/div/h2/div/div[2]/text()')
    SECTION_NEWS = (By.ID, "news")
    NUMBER_SECTION_ERROR = (By.XPATH, '//*[@id="root_uo9rhj0nzz_quantity__error-0"]')
    ADD_SECTION_POPUP = (By.XPATH, '//*[@id="app-container"]/div[12]/div/div')
    NEWS_SECTION = (By.XPATH, '//*[@id="accordionParent"]/div[2]/div[2]') 
    NEWS_SECTION_DISPLAY = (By.XPATH, '//*[@id="accordionParent"]/div[2]/div[2]/div[1]/div/div[1]/li/div/div')  
    SECTION_LIST = (By.XPATH, '//*[@id="accordionParent"]/div[2]/div[2]/div[1]/div')  
    NEWS_SECTION_ERROR = (By.XPATH, ".//div[starts-with(@id, 'root_') and contains(@id, '_title__error')]")  
    NEWS_SECTION_QUANTITY_ERROR = (By.XPATH, "//*[@id='root_bx6h2oef3e_quantity__error']")
    COLLAPSE_SECTION = (By.XPATH, '//*[@id="accordionParent"]/div[2]/div[2]/div[1]/div/div[1]/li/div/div/h2/div/button')
    MENU_SECTION = (By.XPATH, '//*[@id="accordionParent"]/div[2]/div[2]/div[1]/div/div[1]/li/div/div/h2/div/div[3]/button')
    SEARCHBAR_SECTION = (By.XPATH, '//*[@id="dt-search-section"]')
    TYPE_ARTICLE_SELECT_ELEMENT = (By.ID, "react-select-9-input")
    ADD_SECTION_POPUP = (By.XPATH, '//*[@id="app-container"]/div[12]/div/div') 
    NEWS_LIST_POPUP = (By.XPATH, '//*[@id="app-container"]/div[14]/div/div')
    DROPDOWN_LIST_BY_DISPLAYED = (By.CLASS_NAME, 'css-11murdf-menu')
    DROPDOWN_LIST_BY_TYPE_ARTICLE_DISPLAYED = (By.XPATH, '//*[@id="sdqh9emhe6-section"]/div/div/div/div/div/div/div[4]/div/div/div/div/label')
    LIST_BY_OPTION_DISPLAYED = (By.XPATH, '//*[@id="ghd8pmbqdg-section"]/div/div/div/div/div/div/div[4]/div/div/div/div/div[1]/div') 
    
    # Menu item
    DELETE_BUTTON = (By.XPATH, '//*[@id="accordionParent"]/div[2]/div[2]/div[1]/div/div[1]/li/div/div/h2/div/div[3]/div/button[1]')
    DUPLICATE_BUTTON = (By.XPATH, '//*[@id="accordionParent"]/div[2]/div[2]/div[1]/div/div[1]/li/div/div/h2/div/div[3]/div/button[2]')
    
    # Pop-up Confirm Delete
    POPUP_CONFIRM = ( By.XPATH, '//*[@id="app-container"]/div[12]/div/div')
    ICON_CLOSE_CONFIRM = ( By.XPATH, '//*[@id="app-container"]/div[12]/div/div/button')
    BUTTON_YES = ( By.XPATH, '//*[@id="app-container"]/div[12]/div/div/div[3]/button[1]')
    BUTTON_NO = (By.XPATH, '//*[@id="app-container"]/div[12]/div/div/div[3]/button[2]')
    
    # Nút rename của section
    RENAME_SECTION_BUTTON = (By.XPATH, '//*[@id="accordionParent"]/div[2]/div[2]/div[1]/div/div[1]/li/div/div/h2/div/div[2]/button')

    # Popup rename section
    RENAME_SECTION_POPUP = (By.XPATH, '//*[@id="app-container"]/div[14]/div/div')

    ICON_CLOSE = (By.XPATH, '//*[@id="app-container"]/div[14]/div/div/div[1]/button')
    RENAME_TEXT_INPUT = (By.XPATH, '//*[@id="rename-section"]')
    BUTTON_CLOSE = (By.XPATH, '//*[@id="app-container"]/div[14]/div/div/div[3]/button[1]')
    BUTTON_SAVE_RENAME =(By.XPATH, '//*[@id="app-container"]/div[14]/div/div/div[3]/button[2]')

    NUMBER_OF_ARTICLES_INPUT = (By.XPATH, '//*[@id="root_47mwegrft4_quantity-vi"]')
