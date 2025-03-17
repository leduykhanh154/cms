from selenium.webdriver.common.by import By

class LocatorArticle:
    CONTENT_MENU = (By.XPATH, "//*[@id='left-menu']/ul/li[1]/a")
    ARTICLE_MENU = (By.XPATH, "//*[@id='left-menu']/ul/li[1]/ul/li[2]/a")
    ALL_ARTICLE_MENU = (By.XPATH, "//*[@id='left-menu']/ul/li[1]/ul/li[2]/ul/li[1]")
    ALL_ARTICLE_PAGE = (By.XPATH, "//h1[contains(text(),'Tất cả bài viết')]")

    CREATE_NEW_BUTTON = (By.XPATH, "//*[@id='app-container']/main/div/div[2]/div[2]/div/a")
    CREATE_ARTICLE_PAGE = "https://mpire-cms-demo.mpire.asia/cms/article/create"

    # Tab Tiếng Việt
    VI_TAB = (By.XPATH, "//*[@id='vi-tab']")

    # Tab English
    EN_TAB = (By.XPATH, "//*[@id='en-tab']")

    # Nút Dịch nội dung
    TRANSLATE_CONTENT_BUTTON = (By.XPATH, "//*[@id='en-content']/button")

    # Field Tiêu đề - VI 
    TITLE_INPUT = (By.XPATH, "//*[@id='languages[vi][title]']")
    TITLE_ERROR_MESSAGE = (By.XPATH, "//*[@id='vi-content']/div[1]/div[2]/div/div/div")
    TITLE_MAX_LENGTH_ERROR_LOCATOR = (By.XPATH, "//*[@id='vi-content']/div[1]/div[2]/div/div/div")

    # Field Tiêu đề - EN
    TITLE_EN_INPUT = (By.XPATH, "//*[@id='languages[en][title]']")
    TITLE_EN_ERROR_MESSAGE = (By.XPATH, "//*[@id='en-content']/div[1]/div[2]/div/div")
    TITLE_EN_MAX_LENGTH_ERROR_LOCATOR = (By.XPATH, "//*[@id='en-content']/div[1]/div[2]/div/div")

    # Field Đường dẫn - VI

    # Field Đường dẫn - EN

    # Field Mô tả ngắn - VI
    SHORT_DESCRIPTION_VI_INPUT = (By.XPATH, "//*[@id='languages[vi][short_description]']")
    SHORT_DESCRIPTION_VI_ERROR_MESSAGE = (By.XPATH, "//*[@id='vi-content']/div[1]/div[4]/div/div/div")

    # Field Mô tả ngắn - EN
    SHORT_DESCRIPTION_EN_INPUT = (By.XPATH, "//*[@id='languages[en][short_description]']")
    SHORT_DESCRIPTION_EN_ERROR_MESSAGE = (By.XPATH, "//*[@id='en-content']/div[1]/div[4]/div/div/div" )

    # Field Nội dung 
    CKEDITOR_IFRAME_LOCATOR = (By.XPATH, "//iframe[contains(@title, 'Rich Text Editor')]")
    CKEDITOR_BODY_LOCATOR = (By.TAG_NAME, "body")
    CONTENT_VI_ERROR_MESSAGE = (By.XPATH, "//*[@id='vi-content']/div[1]/div[5]/div/div[2]/div")
    CONTENT_EN_ERROR_MESSAGE = (By.XPATH, "//*[@id='en-content']/div[1]/div[5]/div/div[2]/div")

    # Tab Thông tin chung
    GENERAL_INFO_TAB = (By.ID, "MainTab")

    # Select Loại bài viết
    DROPDOWN_ARTICLE_TYPE = (By.XPATH, '//*[@id="showSettingTab"]/div/div[2]/div/span/span[1]/span')
    DROPDOWN_ARTICLE_TYPE_DISPLAY = (By.XPATH, '//*[@id="showSettingTab"]/div/div[2]/div/span/span[1]') 
    ARTICLE_TYPE_ERROR_MESSAGE = (By.XPATH, "//*[@id='showSettingTab']/div/div[2]/div/div/div")

    # Select Trạng thái 
    DROPDOWN_STATUS = (By.XPATH, "//*[@id='showSettingTab']/div/div[3]/div/span/span[1]/span")
    DROPDOWN_STATUS_OPTION = (By.XPATH, "//li[contains(@class, 'select2-results__option') and text()='{}']")
    DROPDOWN_STATUS_SELECTED = (By.XPATH, "//*[@id='showSettingTab']/div/div[3]/div/span/span[1]/span/span[1]")

    # Field Thứ tự sắp xếp
    ORDERING = (By.XPATH, '//*[@id="ordering"]')
    ORDERING_ERROR_MESSAGE = (By.XPATH, '//*[@id="showSettingTab"]/div/div[5]/div/div')
    ORDERING_MAX_LENGHT_ERROR_MESSAGE = (By.XPATH, '//*[@id="showSettingTab"]/div/div[5]/div/div')

    SAVE_BUTTON = (By.XPATH, '//*[@id="save-article"]/div[1]/div[2]/div/div/button[1]')
    SAVE_AND_CONTINUE_BUTTON = (By.XPATH, '//*[@id="save-article"]/div[1]/div[2]/div/div/button[2]')