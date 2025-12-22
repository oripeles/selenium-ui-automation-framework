from selenium.webdriver.common.by import By
from pages.account_info_page import AccountInfoPage
from pages.base_page import BasePage

class LoginPage(BasePage):
    NEW_USER_SIGNUP_TITLE = (By.XPATH, "//*[text()='New User Signup!']")
    NEW_USER_LOGIN_TITLE = (By.XPATH, "//*[text()='Login to your account']")
    NAME_INPUT = (By.XPATH, "//*[@type='text']")
    EMAIL_INPUT_LOGIN = (By.XPATH, "//*[@type='email']")
    PASSWORD_INPUT_LOGIN = (By.XPATH, "//*[@type='password']")
    EMAIL_INPUT = (By.XPATH, "//*[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//*[@data-qa='signup-button']")
    LOGIN_BUTTON = (By.XPATH, "//*[@data-qa='login-button']")
    EMAIL_OR_PASSWORD_IS_INCORRECT_TITLE = (By.XPATH, "//*[text()='Your email or password is incorrect!']")
    EMAIL_EXIT_TITLE = (By.XPATH, "//*[text()='Email Address already exist!']")

    def is_signup_title_visible(self) -> bool:
        return self.is_visible(self.NEW_USER_SIGNUP_TITLE)

    def is_login_title_visible(self) -> bool:
        return self.is_visible(self.NEW_USER_LOGIN_TITLE)

    def is_login_incorrect_title_visible(self) -> bool:
        return self.is_visible(self.EMAIL_OR_PASSWORD_IS_INCORRECT_TITLE)

    def is_email_exist_visible(self) -> bool:
        return self.is_visible(self.EMAIL_EXIT_TITLE)

    def enter_name_and_email(self, name, email):
        self.enter_text(self.NAME_INPUT, name)
        self.enter_text(self.EMAIL_INPUT, email)

    def enter_email_and_password(self, email, password):
        self.enter_text(self.EMAIL_INPUT_LOGIN, email)
        self.enter_text(self.PASSWORD_INPUT_LOGIN, password)

    def click_signup_button(self):
        self.click(self.SIGNUP_BUTTON)
        return AccountInfoPage(self.driver)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)