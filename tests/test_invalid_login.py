from pages.login_page import LoginPage
from utils.config import CONFIG
import time

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()

    creds = CONFIG["invalid_user"]
    login_page.login(creds["username"], creds["password"])

    time.sleep(1)
    error_text = login_page.get_error_message()

    assert "Username and password do not match" in error_text
