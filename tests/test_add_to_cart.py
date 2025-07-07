from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import time

def test_add_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    time.sleep(2)
    products_page = ProductsPage(driver)
    products_page.add_item_to_cart()

    time.sleep(1)
    cart_count = products_page.get_cart_count()

    assert cart_count == "1"
