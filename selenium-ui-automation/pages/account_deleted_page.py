from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AccountDeletedPage(BasePage):
    ACCOUNT_DELETED_TITLE = (By.XPATH, "//*[text()='Account Deleted!']")
    DELETED_ACCOUNT_BUTTON = (By.XPATH, "//*[@data-qa='continue-button']")

    def is_account_deleted_title_visible(self) -> bool:
        return self.is_visible(self.ACCOUNT_DELETED_TITLE)

    def click_deleted_account_button(self):
        self.click(self.DELETED_ACCOUNT_BUTTON)


