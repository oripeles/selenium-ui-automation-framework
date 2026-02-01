from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    SUBSCRIPTION_TITLE = (By.XPATH, "//*[text()='Subscription']")
    DELETE_PRODUCT = (By.CSS_SELECTOR, "a.cart_quantity_delete")
    PROCEED_CHECKOUT = (By.XPATH, "//*[text()='Proceed To Checkout']")
    VIEW_PRODUCT = (By.XPATH, "//*[@href='/product_details/1']")
    SUBSCRIPTION_INPUT = (By.ID, "susbscribe_email")
    SUBSCRIPTION_BUTTON = (By.ID, "subscribe")
    SUBSCRIPTION_SUCCESS = (By.XPATH, "//*[contains(text(),'You have been successfully subscribed!')]")
    CART_DESCRIPTION = (By.CSS_SELECTOR, ".cart_description")
    LOGIN_CHECKOUT = (By.XPATH, "//div[@id='checkoutModal']//a[@href='/login']")
    EMPTY_CARD = (By.ID, "empty_cart")

    def scroll_down_to_footer(self):
        self.scroll_to_bottom()

    def is_product_displayed(self) -> bool:
        return self.is_visible(self.VIEW_PRODUCT)

    def is_subscription_title_visible(self) -> bool:
        return self.is_visible(self.SUBSCRIPTION_TITLE)

    def subscribe(self, email):
        self.enter_text(self.SUBSCRIPTION_INPUT, email)
        self.click(self.SUBSCRIPTION_BUTTON)

    def is_subscription_success_visible(self) -> bool:
        return self.is_visible(self.SUBSCRIPTION_SUCCESS)

    def count_products(self):
        return self.count_after_wait(self.CART_DESCRIPTION)

    def get_price_by_product_name(self, name):
        locator = (
            By.XPATH,
            f"//tr[.//td[@class='cart_description']//a[normalize-space()='{name}']]"
            f"//td[@class='cart_price']/p"
        )
        return self.get_text(locator)

    def get_quantity_by_product_name(self, name):
        locator = (
            By.XPATH,
            f"//tr[.//td[@class='cart_description']//a[normalize-space()='{name}']]"
            f"//td[@class='cart_quantity']//button[@class='disabled']"
        )
        return self.get_text(locator)

    def click_checkout(self):
        self.click(self.PROCEED_CHECKOUT)

    def click_login(self):
        self.click(self.LOGIN_CHECKOUT)

    def click_delete(self):
        self.click(self.DELETE_PRODUCT)

    def is_cart_empty(self) -> bool:
        return self.is_visible(self.EMPTY_CARD)



