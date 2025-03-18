from selenium.webdriver.common.by import By

class LocatorArticle:
    CONTENT_MENU = (By.XPATH, "//*[@id='left-menu']/ul/li[1]/a")
    ARTICLE_MENU = (By.XPATH, "//*[@id='left-menu']/ul/li[1]/ul/li[2]/a")
    ALL_ARTICLE_MENU = (By.XPATH, "//*[@id='left-menu']/ul/li[1]/ul/li[2]/ul/li[1]")
    ALL_ARTICLE_PAGE = (By.XPATH, "//h1[contains(text(),'Tất cả bài viết')]")

    CREATE_NEW_BUTTON = (By.XPATH, "//*[@id='app-container']/main/div/div[2]/div[2]/div/a")
    CREATE_ARTICLE_PAGE = "https://mpire-cms-demo.mpire.asia/cms/article/create"

    VI_TAB = (By.XPATH, "//*[@id='vi-tab']")
    EN_TAB = (By.XPATH, "//*[@id='en-tab']")

    TRANSLATE_CONTENT_BUTTON = (By.XPATH, "//*[@id='en-content']/button")

    # Field Tiêu đề - VI 
    TITLE_INPUT = (By.XPATH, "//*[@id='languages[vi][title]']")
    TITLE_ERROR_MESSAGE = (By.XPATH, "//*[@id='vi-content']/div[1]/div[2]/div/div/div")
    TITLE_MAX_LENGTH_ERROR_LOCATOR = (By.XPATH, "//*[@id='vi-content']/div[1]/div[2]/div/div/div")

    # Field Tiêu đề - EN
    TITLE_EN_INPUT = (By.XPATH, "//*[@id='languages[en][title]']")
    TITLE_EN_ERROR_MESSAGE = (By.XPATH, "//*[@id='en-content']/div[1]/div[2]/div/div")
    TITLE_EN_MAX_LENGTH_ERROR_LOCATOR = (By.XPATH, "//*[@id='en-content']/div[1]/div[2]/div/div")



    CONTENT_MENU = (By.XPATH, "//*[@id='left-menu']/ul/li[1]/a")
    ARTICLE_MENU = (By.XPATH, "//*[@id='left-menu']/ul/li[1]/ul/li[2]/a")
    ALL_ARTICLE_MENU = (By.XPATH, "//*[@id='left-menu']/ul/li[1]/ul/li[2]/ul/li[1]")
    ALL_ARTICLE_PAGE = (By.XPATH, "//h1[contains(text(),'Tất cả bài viết')]")
    CREATE_NEW_BUTTON = (By.XPATH, "//*[@id='app-container']/main/div/div[2]/div[2]/div/a")
    CREATE_ARTICLE_PAGE = "https://mpire-cms-demo.mpire.asia/cms/article/create"
    
    VI_TAB = (By.XPATH, "//*[@id='vi-tab']")
    EN_TAB = (By.XPATH, "//*[@id='en-tab']")

    TRANSLATE_CONTENT_BUTTON = (By.XPATH, "//*[@id='en-content']/button")
    
    # Field Tiêu đề
    TITLE_INPUT = (By.XPATH, "//*[@id='languages[vi][title]']")
    TITLE_ERROR_MESSAGE = (By.XPATH, "//*[@id='vi-content']/div[1]/div[2]/div/div/div")
    TITLE_MAX_LENGTH_ERROR_LOCATOR = (By.XPATH, "//*[@id='vi-content']/div[1]/div[2]/div/div/div")
    

    # Field Nội dung
    CKEDITOR_IFRAME_LOCATOR = (By.XPATH, "//iframe[contains(@title, 'Rich Text Editor')]")
    CKEDITOR_BODY_LOCATOR = (By.TAG_NAME, "body")
    CONTENT_ERROR_MESSAGE = (By.XPATH, "//*[@id='vi-content']/div[1]/div[5]/div/div[2]/div")

    # Tab Thông tin chung
    GENERAL_INFO_TAB = (By.ID, "MainTab")

    # Dropdown Loại bài viết
    DROPDOWN_ARTICLE_TYPE = (By.XPATH, '//*[@id="showSettingTab"]/div/div[2]/div/span/span[1]/span')
    DROPDOWN_ARTICLE_TYPE_DISPLAY = (By.XPATH, '//*[@id="showSettingTab"]/div/div[2]/div/span/span[1]') 
    ARTICLE_TYPE_ERROR_MESSAGE = (By.XPATH, "//*[@id='showSettingTab']/div/div[2]/div/div/div")

    DROPDOWN_STATUS = (By.XPATH, "//*[@id='showSettingTab']/div/div[3]/div/span/span[1]/span")
    DROPDOWN_STATUS_OPTION = (By.XPATH, "//li[contains(@class, 'select2-results__option') and text()='{}']")  # Tùy chọn bên trong dropdown
    DROPDOWN_STATUS_SELECTED = (By.XPATH, "//*[@id='showSettingTab']/div/div[3]/div/span/span[1]/span/span[1]")  # Giá trị đã chọn

    ARTICLE_LIST_WRAPPER = (By.XPATH, '//*[@id="table-acticle-list_wrapper"]/div[2]')

    SAVE_BUTTON = (By.XPATH, '//*[@id="save-article"]/div[1]/div[2]/div/div/button[1]')
    SAVE_AND_CONTINUE_BUTTON = (By.XPATH, '//*[@id="save-article"]/div[1]/div[2]/div/div/button[2]')

    ORDERING = (By.XPATH, '//*[@id="ordering"]')
    ORDERING_ERROR_MESSAGE = (By.XPATH, '//*[@id="showSettingTab"]/div/div[5]/div/div')
    ORDERING_MAX_LENGHT_ERROR_MESSAGE = (By.XPATH, '//*[@id="showSettingTab"]/div/div[5]/div/div')

    PUBLIC_DATE = (By.ID, "public_date")

    # Locators cho nút "Nổi bật"
    FEATURED_SWITCH = (By.ID, "is_feature")
    FEATURED_LABEL = (By.CSS_SELECTOR, "label[for='is_feature']")  

    # Locators cho nút "Đặt làm trang chủ"
    HOMEPAGE_SWITCH = (By.XPATH, "//*[@id='showSettingTab']/div/div[10]/div/div[1]/input")
    HOMEPAGE_LABEL = (By.XPATH, "//*[@id='showSettingTab']/div/div[10]/div/div[1]/label")


    UPLOAD_THUMBNAIL_IMAGE_FIELD = (By.XPATH, "//*[@id='article-image-id_upload']/div/div[1]/a")
  
    UPLOAD_FEATURE_IMAGE_FIELD = (By.XPATH, '//*[@id="feature-image_upload"]/div/div[1]/a')
    UPLOAD_BUTTON = (By.XPATH, "//*[@id='article-image-id_upload']/div/div[2]/a[1]")

    UPLOAD_IMAGE_POPUP = (By.XPATH, "//*[@id='article-image-id_upload-ModalUploadImage']/div/div")

    BROWSER_TAB = (By.XPATH, "//*[@id='browse-tab']")
    FILE_LISTING = (By.XPATH, "//*[@id='file-listing']//a")
    CHOOSE_UPLOAD_BUTTON = (By.XPATH, "//*[@id='btn-choose-version']")

    DELETE_THUMBNAIL_IMAGE = (By.XPATH, "//*[@id='article-image-id_upload']/div/div[2]/a[2]")
    DELETE_FEATURE_IMAGE = (By.XPATH, '//*[@id="feature-image_upload"]/div/div[2]/a[2]')

    DROPDOWN_SELECT_TAG = (By.XPATH, "//*[@id='showSettingTab']/div/div[4]/div/div[1]/div/span/span[1]/span")
    DROPDOWN_SELECT_TAG_OPTION = (By.XPATH, "//li[contains(@class, 'select2-results__option') and text()='{}']")
    DROPDOWN_TAG_SELECTED = (By.XPATH, "//*[@id='showSettingTab']/div/div[4]/div/div[1]/div/span/span[1]/span/span[1]") 
    SELECTED_TAG_FIELD = (By.XPATH, "//*[@id='select2-article_keyword-result-tc40-676e10ba97097']")

    CREATE_KEYWORD_BUTTON = (By.XPATH, '//*[@id="btnCreateKeyword"]')  
    ADD_KEYWORD_SIDEBAR = (By.XPATH, '//*[@id="modal-AddNewKeyword"]/div[2]')

    RELATED_ARTICLE_DROPDOWN = (By.XPATH, '//*[@id="showSettingTab"]/div/div[13]/div/span/span[1]/span')
    RELATED_ARTICLE_OPTIONS = (By.XPATH, '//ul[@id="select2-relatedArticle-results"]/li')
    SELECTED_RELATED_ARTICLE_FIELD = (By.XPATH, '//*[@id="showSettingTab"]/div/div[13]/div/span')

    URL_KEY_INPUT = (By.XPATH, "//*[@id='languages[vi][url_key]']")


    # Locator cho dropdown loại bài viết (filter)
    FILTER_DROPDOWN_ARTICLE_TYPE = (By.XPATH, '//*[@id="select2-category_id-container"]')
    
    # Locator cho các mục trong dropdown (dựa vào tên loại bài viết) (filter)
    FILTER_ARTICLE_TYPE_OPTION = (By.XPATH, "//ul[@id='select2-category_id-results']//li[contains(text(), '{article_type}')]")
    
    # Locator cho các mục đã được chọn trong dropdown (filter)
    FILTER_SELECTED_ARTICLE_TYPE = (By.XPATH, '//*[@id="select2-category_id-container"]/span')

