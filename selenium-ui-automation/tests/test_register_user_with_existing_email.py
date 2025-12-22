import allure

@allure.feature("Registration")
class TestRegisterUserWithExistingEmail:

    @allure.title("Registration fails when using an existing email")
    def test_register_user_with_existing_email(self, home, existing_user):
        email = existing_user["email"]
        name = existing_user["name"]
        login = home.click_login_tab()
        assert login.is_signup_title_visible(), "New User Signup title is not visible"
        login.enter_name_and_email(name, email)
        login.click_signup_button()
        assert login.is_email_exist_visible(), "Email already exists error message is not visible"