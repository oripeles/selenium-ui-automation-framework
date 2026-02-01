import os
import pytest
import allure

@allure.feature("Login")
class TestLoginValidUser:

    @pytest.mark.smoke
    @allure.title("Login successfully with valid credentials")
    def test_login_valid_user(self, home, existing_user):
        password = os.getenv("USER_PASSWORD")
        email = existing_user["email"]
        login = home.click_login_tab()
        assert login.is_login_title_visible(), "Login page title is not visible"
        login.enter_email_and_password(email, password)
        login.click_login_button()
        assert home.is_logout_visible(), "Logout tab is not visible or text is incorrect"



