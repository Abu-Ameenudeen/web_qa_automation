from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

def get_driver():
    driver_path = os.path.join(os.getcwd(), "drivers", "chromedriver.exe")
    service = Service(executable_path=driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maxmized")
    driver = webdriver.Chrome(service=service, options=options)
    return driver