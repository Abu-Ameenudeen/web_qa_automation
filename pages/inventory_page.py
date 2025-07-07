from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")

    def logout(self):
        self.driver.find_element(*self.menu_button).click()

        # ⏳ Wait for the logout link to be clickable (max 5 sec)
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.logout_link)
        ).click()
