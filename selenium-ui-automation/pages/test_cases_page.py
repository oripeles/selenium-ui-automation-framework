from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TestCasesPage(BasePage):
    CASES_TITLE = (By.CLASS_NAME, "title")

    def is_case_test_title_visible(self) -> bool:
        return self.is_visible(self.CASES_TITLE)

