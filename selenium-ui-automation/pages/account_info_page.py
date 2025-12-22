from selenium.webdriver.common.by import By
from pages.account_created_page import AccountCreatedPage
from pages.base_page import BasePage

class AccountInfoPage(BasePage):
    ENTER_ACCOUNT_INFO_TITLE = (By.XPATH, "//*[text()='Enter Account Information']")
    TITLE_MR = (By.ID, "id_gender1")
    TITLE_MRS = (By.ID, "id_gender2")
    PASSWORD_INPUT = (By.ID, "password")
    DAYS_SELECT = (By.ID, "days")
    MONTHS_SELECT = (By.ID, "months")
    YEARS_SELECT = (By.ID, "years")
    NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    OPTIN_CHECKBOX = (By.ID, "optin")
    FIRST_NAME_INPUT = (By.ID, "first_name")
    LAST_NAME_INPUT = (By.ID, "last_name")
    COMPANY_INPUT = (By.ID, "company")
    ADDRESS1_INPUT = (By.ID, "address1")
    ADDRESS2_INPUT = (By.ID, "address2")
    COUNTRY_SELECT = (By.ID, "country")
    STATE_INPUT = (By.ID, "state")
    CITY_INPUT = (By.ID, "city")
    ZIPCODE_INPUT = (By.ID, "zipcode")
    MOBILE_INPUT = (By.ID, "mobile_number")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//*[@data-qa='create-account']")

    def is_account_info_title_visible(self) -> bool:
        return self.is_visible(self.ENTER_ACCOUNT_INFO_TITLE)

    def select_title(self, title):
        if title == "Mr":
            self.click(self.TITLE_MR)
        elif title == "Mrs":
            self.click(self.TITLE_MRS)
        else:
            raise ValueError("Title must be 'Mr' or 'Mrs'")

    def fill_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def select_date(self, day, month, year):
        self.select_by_value(self.DAYS_SELECT, day)
        self.select_by_text(self.MONTHS_SELECT, month)
        self.select_by_value(self.YEARS_SELECT, year)

    def select_newsletter(self):
        self.js_click(self.NEWSLETTER_CHECKBOX)

    def select_optin(self):
        self.js_click(self.OPTIN_CHECKBOX)

    def fill_details(self, first, last, company, addr1, addr2, country, state, city, zipcode, mobile):
        self.enter_text(self.FIRST_NAME_INPUT, first)
        self.enter_text(self.LAST_NAME_INPUT, last)
        self.enter_text(self.COMPANY_INPUT, company)
        self.enter_text(self.ADDRESS1_INPUT, addr1)
        self.enter_text(self.ADDRESS2_INPUT, addr2)
        self.select_by_text(self.COUNTRY_SELECT, country)
        self.enter_text(self.STATE_INPUT, state)
        self.enter_text(self.CITY_INPUT, city)
        self.enter_text(self.ZIPCODE_INPUT, zipcode)
        self.enter_text(self.MOBILE_INPUT, mobile)

    def click_create_account_button(self):
        self.js_click(self.CREATE_ACCOUNT_BUTTON)
        return AccountCreatedPage(self.driver)

