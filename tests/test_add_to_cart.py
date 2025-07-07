import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.config import CONFIG
import time

@pytest.mark.regression
def test_add_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.load()
    creds = CONFIG["valid_user"]
    login_page.login(creds["username"], creds["password"])
    time.sleep(2)
    products_page = ProductsPage(driver)
    products_page.add_item_to_cart()
    cart_count = products_page.get_cart_count()
    assert cart_count == "1"
