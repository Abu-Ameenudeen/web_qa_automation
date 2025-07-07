from pages.login_page import LoginPage
import time

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("invalid_user", "wrong_pass")

    time.sleep(1)
    error_text = login_page.get_error_message()

    assert "Username and password do not match" in error_text
