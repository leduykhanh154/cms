from selenium.webdriver.common.by import By

class LocatorNewArticleType:
    # Menu
    CONTENT_MENU = (By.XPATH, "//*[@id='left-menu']/ul/li[1]/a")
    ARTICLE_MENU = (By.XPATH, "//*[@id='left-menu']/ul/li[1]/ul/li[2]/a")
    ARTICLE_TYPE_MENU= (By.XPATH, '//*[@id="left-menu"]/ul/li[1]/ul/li[2]/ul/li[3]/a')
    
    # Breadcrumb
    BREADCRUMB_HOME = (By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div/nav/ol/li[1]/a')
    BREADCRUMB_TYPE_LIST = (By.XPATH, '//*[@id="app-container"]/main/div/div/div/nav/ol/li[2]/a')
    
    # Button
    NEW_TYPE_BUTTON = (By.XPATH, "//*[@id='app-container']/main/div/div[2]/div[2]/div/a")
    SAVE_BUTTON = (By. XPATH, '//*[@id="save-button"]')
    SAVE_AND_CONTINUE_BUTTON = (By.XPATH, '//*[@id="save-category"]/div[1]/div[2]/div/div/button[2]')
    TRANSLATE_BUTTON = (By.XPATH, '//*[@id="en-content"]/button')
    
    # Tab
    TAB_MAIN_CONTENT = (By.XPATH, '//*[@id="showTranslate"]')
    TAB_GENERAL_INFORMATION = (By.XPATH, '//*[@id="MainTab"]')
    TAB_TIENG_VIET = (By.XPATH, '//*[@id="vi-tab"]')
    TAB_ENGLISH = (By.XPATH, '//*[@id="en-tab"]')
    
    # Label
    LABEL_ARTICLE_TYPE = (By.XPATH, '//*[@id="vi-content"]/div[1]/div[2]/div/label')
    LABEL_STATUS = (By.XPATH, '//*[@id="showSettingTab"]/div/div[2]/div/label')
    
    # Error message VI
    VI_ERROR_PLEASE_FIELD_TYPE_ARTICLE = (By.XPATH, '//*[@id="vi-content"]/div[1]/div[2]/div/div/div')
    VI_ERROR_LINK = (By.XPATH, '//*[@id="vi-content"]/div[1]/div[3]/div/div/div')
    VI_ERROR_SHORT_DESCRIPTION = (By.XPATH, '//*[@id="vi-content"]/div[1]/div[4]/div/div/div')
    VI_ERROR_META_KEYWORD = (By.XPATH, '//*[@id="vi-content"]/div[2]/div[2]/div[1]/div/div')
    VI_ERROR_META_DESCRIPTION = (By.XPATH, '//*[@id="vi-content"]/div[2]/div[2]/div[2]/div/div')
    
    # Error message EN
    EN_ERROR_PLEASE_FIELD_TYPE_ARTICLE = (By.XPATH, '//*[@id="en-content"]/div[1]/div[2]/div/div/div')
    EN_ERROR_LINK = (By.XPATH, '//*[@id="en-content"]/div[1]/div[3]/div/div/div')
    EN_ERROR_SHORT_DESCRIPTION = (By.XPATH, '//*[@id="en-content"]/div[1]/div[4]/div/div/div')
    EN_ERROR_META_KEYWORD = (By.XPATH, '//*[@id="en-content"]/div[2]/div[2]/div[1]/div/div')
    EN_ERROR_META_DESCRIPTION = (By.XPATH, '//*[@id="en-content"]/div[2]/div[2]/div[2]/div/div')    
    ERROR_SORT_ORDER = (By.XPATH, '//*[@id="showSettingTab"]/div/div[3]/div/div/div')
    
    # Text
    TEXT_EDIT = (By.XPATH, '//*[@id="save-category"]/div[1]/div[1]')
    
    # Text-input
    VI_TEXT_INPUT_ARTICLE_TYPE =(By.XPATH, '//*[@id="languages[vi][title]"]')
    VI_TEXT_INPUT_LINK = (By.XPATH, '//*[@id="languages[vi][url_key]"]')
    VI_TEXT_INPUT_META_KEYWORD = (By.XPATH, '//*[@id="languages[vi][meta_keyword]"]')
    EN_TEXT_INPUT_ARTICLE_TYPE =(By.XPATH, '//*[@id="languages[en][title]"]')
    EN_TEXT_INPUT_LINK = (By.XPATH, '//*[@id="languages[en][url_key]"]')
    EN_TEXT_INPUT_META_KEYWORD = (By.XPATH, '//*[@id="languages[en][meta_keyword]"]')
    TEXT_INPUT_SORT_ORDER = (By.XPATH, '//*[@id="ordering"]')
    
    # Text-area
    VI_TEXT_AREA_DESCRIPTION = (By.XPATH, '//*[@id="languages[vi][description]"]')
    VI_TEXT_AREA_META_DESCRIPTION = (By.XPATH, '//*[@id="languages[vi][meta_description]"]')
    EN_TEXT_AREA_DESCRIPTION = (By.XPATH, '//*[@id="languages[en][description]"]')
    EN_TEXT_AREA_META_DESCRIPTION = (By.XPATH, '//*[@id="languages[en][meta_description]"]')
    
    # Dropdown
    DROPDOWN_STATUS = (By.XPATH, '//*[@id="showSettingTab"]/div/div[2]/div/span/span[1]/span')
    DROPDOWN_FATHER_TYPE = (By.XPATH, '//*[@id="showSettingTab"]/div/div[4]/div/span/span[1]/span')
    DROPDOWN_BANNER_SET = (By.XPATH, '//*[@id="showSettingTab"]/div/div[5]/div/span/span[1]/span')

    DROPDOWN_ITEM_STATUS_ACTIVE = (By.XPATH, '')
    
    # Meta image VI
    FIELD_IMAGE = (By.XPATH, '//*[@id="languagesvimeta-image_upload"]/div/div[1]/a/img')
    BUTTON_UPLOAD_IMAGE = (By.XPATH, '//*[@id="languagesvimeta-image_upload"]/div/div[2]/a[1]')
    BUTTON_DELETE_IMAGE = (By.XPATH, '//*[@id="languagesvimeta-image_upload"]/div/div[2]/a[2]')
    POPUP_UPLOAD_IMAGE = (By.XPATH, '//*[@id="languagesvimeta-image_upload-ModalUploadImage"]/div/div')
    BUTTON_UPLOAD = (By.XPATH, '//*[@id="btn-choose-version"]')
    TAB_BROWSER = (By.XPATH, '//*[@id="browse-tab"]')
    FIRST_IMAGE = (By.XPATH, '//*[@id="file-listing"]/div[1]/div')

    # Meta image EN
    EN_FIELD_IMAGE = (By.XPATH, '//*[@id="languagesenmeta-image_upload"]/div/div[1]/a/img')
    EN_BUTTON_UPLOAD_IMAGE = (By.XPATH, '//*[@id="languagesenmeta-image_upload"]/div/div[2]/a[1]')
    EN_BUTTON_DELETE_IMAGE = (By.XPATH, '//*[@id="languagesenmeta-image_upload"]/div/div[2]/a[2]')
    EN_POPUP_UPLOAD_IMAGE = (By.XPATH, '//*[@id="languagesenmeta-image_upload-ModalUploadImage"]/div/div')
    
    