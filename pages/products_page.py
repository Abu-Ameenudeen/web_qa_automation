from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def add_item_to_cart(self):
        self.driver.find_element(*self.add_to_cart_btn).click()

    def get_cart_count(self):
        # Wait until the cart badge is visible
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.cart_badge)
        )
        return element.text
