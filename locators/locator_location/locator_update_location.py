from selenium.webdriver.common.by import By

class LocatorUpdateLocation:
    # MENU
    CONTENT_MENU = (By.XPATH, "//*[@id='left-menu']/ul/li[1]/a")
    LOCATION_MENU = (By.XPATH, '//*[@id="left-menu"]/ul/li[1]/ul/li[5]/a')
    
    # LOCATION LIST
    FIRST_MENU_BUTTON = (By.XPATH, '//*[@id="dropdownMenuLink13"]')
    FIRST_DETAIL_MENU_ITEM = (By.XPATH, '//*[@id="table-dealer-list"]/tbody/tr[1]/td[9]/div/div/a[1]')
    FIRST_LOCATION_NAME = (By.XPATH, '//*[@id="table-dealer-list"]/tbody/tr[1]/td[2]/a')
    
    # BUTTON
    CANCEL_BUTTON = (By.XPATH, '//*[@id="mpireValidateForm"]/div[1]/div[2]/div/div/a')
    SAVE_BUTTON = (By. XPATH, '//*[@id="mpireValidateForm"]/div[1]/div[2]/div/div/button[1]')
    SAVE_AND_CONTINUE_BUTTON = (By.XPATH, '//*[@id="mpireValidateForm"]/div[1]/div[2]/div/div/button[2]')
    TRANSLATE_BUTTON = (By.XPATH, '//*[@id="en-content"]/button')
    
    # TAB
    MAIN_CONTENT_TAB = (By.XPATH, '//*[@id="showTranslate"]')
    GENERAL_INFORMATION_TAB = (By.XPATH, '//*[@id="MainTab"]')
    TIENG_VIET_TAB = (By.XPATH, '//*[@id="vi-tab"]')
    ENGLISH_TAB = (By.XPATH, '//*[@id="en-tab"]')
    
    # TEXT-INPUT
    NAME_TEXT_INPUT = (By.XPATH, '//*[@id="name"]')
    ADDRESS_TEXT_INPUT = (By.XPATH, '//*[@id="address"]')
    PHONE_TEXT_INPUT = (By.XPATH, '//*[@id="phone"]')
    FAX_TEXT_INPUT = (By.XPATH, '//*[@id="fax"]')
    LONGITUDE_TEXT_INPUT = (By.XPATH, '//*[@id="longitude"]')
    LATITUDE_TEXT_INPUT = (By.XPATH, '//*[@id="latitude"]')
    EMAIL_TEXT_INPUT = (By.XPATH, '//*[@id="email"]')
    SORT_ORDER_TEXT_INPUT = (By.XPATH, '//*[@id="ordering"]')
    
    # TEXT-AREA
    CONTENT_TEXT_AREA = (By.XPATH, '//*[@id="cke_1_contents"]/iframe')
    
    # DROPDOWN 
    PROVINCE_DROPDOWN = (By.XPATH, '//*[@id="select2-select-province-container"]')
    FIRST_PROVINCE_ITEM = (By.XPATH, '//*[@id="app-container"]/span/span/span[2]/ul/li[2]')
    DISTRICT_DROPDOWN = (By.XPATH, '//*[@id="select2-select-district-container"]')
    FIRST_DISTRICT_ITEM = (By.XPATH, '//*[@id="app-container"]/span/span/span[2]/ul/li[2]')
    STATUS_DROPDOWN = (By.XPATH, '//*[@id="select2-status-container"]')
    ACTIVE_STATUS = (By.XPATH, '//*[@id="app-container"]/span/span/span[2]/ul/li[1]')
    PROCESSING_STATUS = (By.XPATH, '//*[@id="app-container"]/span/span/span[2]/ul/li[2]')
    
    # IMAGE
    IMAGE_FIELD = (By.XPATH, '//*[@id="image-id_upload"]/div/div[1]/a')
    UPLOAD_IMAGE_POPUP = (By.XPATH, '//*[@id="image-id_upload-ModalUploadImage"]/div/div')
    UPLOAD_IMAGE_BUTTON = (By.XPATH, '//*[@id="image-id_upload"]/div/div[2]/a[1]')
    DELETE_IMAGE_BUTTON = (By.XPATH, '//*[@id="image-id_upload"]/div/div[2]/a[2]')
    UPLOAD_IMAGE_POPUP = (By.XPATH, '//*[@id="image-id_upload-ModalUploadImage"]/div/div')
    UPLOAD_BUTTON = (By.XPATH, '//*[@id="btn-choose-version"]')
    BROWSER_TAB = (By.XPATH, '//*[@id="browse-tab"]')
    FIRST_IMAGE = (By.XPATH, '//*[@id="file-listing"]/div[1]/div')