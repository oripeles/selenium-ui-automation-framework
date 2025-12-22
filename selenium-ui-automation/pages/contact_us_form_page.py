from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContactUsFormPage(BasePage):
    GET_IN_TOUCH_TITLE = (By.XPATH,"//*[@class='title text-center']")
    NAME_INPUT = (By.XPATH, "//*[@data-qa='name']")
    EMAIL_INPUT_LOGIN = (By.XPATH, "//*[@type='email']")
    SUBJECT_INPUT = (By.XPATH, "//*[@data-qa='subject']")
    MESSAGE_INPUT = (By.XPATH, "//*[@data-qa='message']")
    SUBMIT_BUTTON = (By.XPATH, "//*[@type='submit']")
    GET_IN_TOUCH_SUCCESS_TITLE = (By.XPATH, "//*[@class='status alert alert-success']")
    HOME_BUTTON = (By.XPATH, "//*[@class='btn btn-success']")

    def is_contact_us_page_visible(self) -> bool:
        return self.is_visible(self.GET_IN_TOUCH_TITLE)

    def is_contact_us_success_visible(self) -> bool:
        return self.is_visible(self.GET_IN_TOUCH_SUCCESS_TITLE)

    def fill_details(self, name, email, subject, message):
        self.enter_text(self.NAME_INPUT, name)
        self.enter_text(self.EMAIL_INPUT_LOGIN, email)
        self.enter_text(self.SUBJECT_INPUT, subject)
        self.enter_text(self.MESSAGE_INPUT, message)

    def click_handle_alert(self):
        self.handle_alert()

    def click_submit(self):
        self.click(self.SUBMIT_BUTTON)

    def click_home(self):
        self.click(self.HOME_BUTTON)
