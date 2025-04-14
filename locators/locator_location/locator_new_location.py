from selenium.webdriver.common.by import By

class LocatorNewLocation:
    # MENU
    CONTENT_MENU = (By.XPATH, "//*[@id='left-menu']/ul/li[1]/a")
    LOCATION_MENU = (By.XPATH, '//*[@id="left-menu"]/ul/li[1]/ul/li[5]/a')
    
    # LOCATION LIST BUTTON
    CREATE_BUTTON = (By.XPATH, '//*[@id="app-container"]/main/div/div[2]/div[2]/div/a')
    
    # BUTTON
    SAVE_BUTTON = (By. XPATH, '//*[@id="save-button"]')
    SAVE_AND_CONTINUE_BUTTON = (By.XPATH, '//*[@id="save-category"]/div[1]/div[2]/div/div/button[2]')
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
    DISTRICT_DROPDOWN = (By.XPATH, '//*[@id="select2-select-district-container"]')
    STATUS_DROPDOWN = (By.XPATH, '//*[@id="select2-status-container"]')
    
    # IMAGE
    IMAGE_FIELD = (By.XPATH, '//*[@id="image-id_upload"]/div/div[1]/a')
    UPLOAD_IMAGE_BUTTON = (By.XPATH, '//*[@id="image-id_upload"]/div/div[2]/a[1]')
    DELETE_IMAGE_BUTTON = (By.XPATH, '//*[@id="image-id_upload"]/div/div[2]/a[2]')
    UPLOAD_IMAGE_POPUP = (By.XPATH, '//*[@id="image-id_upload-ModalUploadImage"]/div/div')
    UPLOAD_BUTTON = (By.XPATH, '//*[@id="btn-choose-version"]')
    BROWSER_TAB = (By.XPATH, '//*[@id="browse-tab"]')
    FIRST_IMAGE = (By.XPATH, '//*[@id="file-listing"]/div[1]/div')