# tests/test_login.py

from utils.driver_factory import get_driver
from pages.login_page import LoginPage
import time

def test_login_success():
    driver = get_driver()
    login_page = LoginPage(driver)

    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    time.sleep(2)
    assert "inventory" in driver.current_url
    driver.quit()
