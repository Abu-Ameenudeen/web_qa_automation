from pages.login_page import LoginPage
from utils.config import CONFIG
import time

def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.load()

    creds = CONFIG["valid_user"]
    login_page.login(creds["username"], creds["password"])

    time.sleep(2)
    assert "inventory" in driver.current_url
