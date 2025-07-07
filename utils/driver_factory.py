from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

def get_driver():
    driver_path = os.path.join(os.getcwd(), "drivers", "chromedriver.exe")
    service = Service(executable_path=driver_path)
    options = webdriver.ChromeOptions()

    # Suppress the password manager popup
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=service, options=options)
    return driver
