from selenium.webdriver.common.by import By
from pages.account_deleted_page import AccountDeletedPage
from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.contact_us_form_page import ContactUsFormPage
from pages.login_page import LoginPage
from pages.product_detail_page import  ViewProductPage
from pages.products_page import ProductsPage
from pages.cases_page import CasesPage

class HomePage(BasePage):
    ACTIVE_TAB = (By.XPATH, "//*[@style='color: orange;']")
    CART_BUTTON = (By.XPATH, "//*[@href='/view_cart']")
    VIEW_PRODUCT = (By.XPATH, "//*[@href='/product_details/1']")
    LOGIN_TAB = (By.XPATH, "//*[@href='/login']")
    CONTACT_US_TAB = (By.XPATH, "//*[@href='/contact_us']")
    TEST_CASES_TAB = (By.XPATH, "//*[@href='/test_cases']")
    LOGOUT_TAB = (By.XPATH, "//*[@href='/logout']")
    LOGGED_IN_USER = (By.XPATH, "//*[contains(text(), 'Logged in')]")
    DELETE_ACCOUNT_TAB = (By.LINK_TEXT, "Delete Account")
    PRODUCTS_TAB = (By.XPATH, "//*[@href='/products']")
    SUBSCRIPTION_TITLE = (By.XPATH, "//*[text()='Subscription']")
    LEFT_SIDEBAR = (By.XPATH, "//*[@class='left-sidebar']")
    SUBSCRIPTION_INPUT = (By.ID, "susbscribe_email")
    SUBSCRIPTION_BUTTON = (By.ID, "subscribe")
    SUBSCRIPTION_SUCCESS = (By.XPATH,"//*[normalize-space(text())='You have been successfully subscribed!']")
    WOMEN_CATEGORY = (By.CSS_SELECTOR, "a[href='#Women']")
    DRESS_CATEGORY = (By.XPATH, "//a[normalize-space(text())='Dress']")
    CATEGORY_TITLE_WOMEN = (By.CSS_SELECTOR, "h2.title.text-center")
    MEN_CATEGORY = (By.XPATH, "//a[@href='#Men']")
    SHIRTS_CATEGORY = (By.XPATH, "//a[@href='/category_products/3']")
    CATEGORY_TITLE_MEN = (By.XPATH, "//*[@class='active' and contains(text(),'Men > Tshirts')]")

    def is_home_page_visible(self) -> bool:
        return self.is_visible(self.ACTIVE_TAB)

    def is_logout_visible(self) -> bool:
        return self.is_visible(self.LOGOUT_TAB)

    def is_left_sidebar_visible(self) -> bool:
        return self.is_visible(self.LEFT_SIDEBAR)

    def is_women_category_title_visible(self) -> bool:
        return self.is_visible(self.CATEGORY_TITLE_WOMEN)

    def is_men_category_title_visible(self) -> bool:
        return self.is_visible(self.CATEGORY_TITLE_MEN)

    def is_logged_in_as_visible(self, username: str) -> bool:
        if not self.is_visible(self.LOGGED_IN_USER):
            return False
        return self.get_text(self.LOGGED_IN_USER) == f"Logged in as {username}"

    def click_login_tab(self):
        self.click(self.LOGIN_TAB)
        return LoginPage(self.driver)

    def click_logout_tab(self):
        self.click(self.LOGOUT_TAB)
        return LoginPage(self.driver)

    def click_contact_us_tab(self):
        self.click(self.CONTACT_US_TAB)
        return ContactUsFormPage(self.driver)

    def click_delete_account(self):
        self.click(self.DELETE_ACCOUNT_TAB)
        return AccountDeletedPage(self.driver)

    def click_test_cases_tab(self):
        self.click(self.TEST_CASES_TAB)
        return CasesPage(self.driver)

    def click_product_tab(self):
        self.click(self.PRODUCTS_TAB)
        return ProductsPage(self.driver)

    def click_view_product(self):
        self.js_click(self.VIEW_PRODUCT)
        return ViewProductPage(self.driver)

    def scroll_down(self):
        self.scroll_to_bottom()

    def is_subscription_title_visible(self):
        return self.is_visible(self.SUBSCRIPTION_TITLE)

    def subscribe(self, email):
        self.enter_text(self.SUBSCRIPTION_INPUT, email)
        self.click(self.SUBSCRIPTION_BUTTON)

    def is_subscription_success_visible(self):
        return self.is_visible(self.SUBSCRIPTION_SUCCESS)

    def go_to_cart(self):
        self.click(self.CART_BUTTON)
        return CartPage(self.driver)

    def click_women_category(self):
        self.click(self.WOMEN_CATEGORY)

    def click_dress_category(self):
        self.click(self.DRESS_CATEGORY)

    def click_men_category(self):
        self.click(self.MEN_CATEGORY)

    def click_shirt_category(self):
        self.click(self.SHIRTS_CATEGORY)






