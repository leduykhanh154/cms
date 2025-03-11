from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--force-device-scale-factor=0.67")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
