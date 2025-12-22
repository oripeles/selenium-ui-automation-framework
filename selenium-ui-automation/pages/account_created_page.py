from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AccountCreatedPage(BasePage):
    ACCOUNT_CREATED_TITLE = (By.XPATH, "//*[text()='Account Created!']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//*[@data-qa='continue-button']")

    def is_account_created_title_visible(self) -> bool:
        return self.is_visible(self.ACCOUNT_CREATED_TITLE)

    def click_created_account_button(self):
        self.js_click(self.CREATE_ACCOUNT_BUTTON)
