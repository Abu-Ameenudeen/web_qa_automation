# tests/test_login.py

from utils.driver_factory import get_driver
import time

def test_login_success():
    driver = get_driver()
    driver.get("https://www.saucedemo.com")

    # Input credentials
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("id", "password").send_keys("secret_sauce")
    driver.find_element("id", "login-button").click()

    # Wait and check
    time.sleep(2)
    assert "inventory" in driver.current_url

    driver.quit()
