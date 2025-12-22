import os
import allure
from utilities.email_generator import generate_unique_email

@allure.feature("Registration")
class TestRegisterUser:

    @allure.title("Register new user successfully and delete account")
    def test_register_user(self, home, existing_user):
        email = generate_unique_email()
        password = os.getenv("USER_PASSWORD")
        name = existing_user["name"]
        gender = "Mr"
        date_data = {
            "day": 10,
            "month": "January",
            "year": "2000"
        }
        address_data = {
            "first": "Ori",
            "last": "Peles",
            "company": "global",
            "addr1": "123 Test Street",
            "addr2": "Building 4",
            "country": "Israel",
            "state": "Center",
            "city": "Petah Tikva",
            "zipcode": "4950000",
            "mobile": "0501234567"
        }

        login = home.click_login_tab()
        assert login.is_signup_title_visible(), "New User Signup title is not visible"
        login.enter_name_and_email(name, email)
        info = login.click_signup_button()
        assert info.is_account_info_title_visible(), "Enter Account Information title is not visible"
        info.select_title(gender)
        info.fill_password(password)
        info.select_date(**date_data)
        info.select_newsletter()
        info.select_optin()
        info.fill_details(**address_data)
        created = info.click_create_account_button()
        assert created.is_account_created_title_visible(), "Account Created title is not visible"
        created.click_created_account_button()
        assert home.is_logged_in_as_visible(existing_user["name"]), "Wrong logged-in username"
        delete_account =  home.click_delete_account()
        assert delete_account.is_account_deleted_title_visible(),"Account Deleted title is not visible"
        delete_account.click_deleted_account_button()





