from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import time

def test_logout(driver):  # driver from fixture
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    time.sleep(2)
    inventory_page = InventoryPage(driver)
    inventory_page.logout()

    time.sleep(1)
    assert "saucedemo.com" in driver.current_url and "login" in driver.page_source
