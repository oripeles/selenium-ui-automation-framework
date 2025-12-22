import pytest
import allure
from utilities.json_loader import load_json

@allure.feature("Login")
@allure.title("Login fails with invalid credentials")
@pytest.mark.parametrize(
    "case",
    load_json("invalid_logins")
)
def test_login_invalid_user(home, case):
        login = home.click_login_tab()
        assert login.is_login_title_visible(), "Login to your account title is not visible"
        login.enter_email_and_password(
            case["email"],
            case["password"]
        )
        login.click_login_button()
        assert login.is_login_incorrect_title_visible(), "Incorrect login error message is not visible"