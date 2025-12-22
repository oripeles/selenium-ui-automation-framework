import os
import allure

@allure.feature("Login")
class TestLogoutUser:

    @allure.title("Logout successfully and return to login page")
    def test_logout_user(self, home, existing_user):
        password = os.getenv("USER_PASSWORD")
        email = existing_user["email"]
        login_page = home.click_login_tab()
        assert login_page.is_login_title_visible(), "Login page title is not visible"
        login_page.enter_email_and_password(email, password)
        login_page.click_login_button()
        home.click_logout_tab()
        assert login_page.is_login_title_visible(), "Login page title is not visible after logout"
