from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ViewProductPage(BasePage):
    QUANTITY_INPUT = (By.ID, "quantity")
    ADD_TO_CART = (By.CLASS_NAME, "cart")
    CONTINUE_SHOPPING = (By.XPATH, "//button[text()='Continue Shopping']")

    def set_quantity(self, amount):
        self.enter_text(self.QUANTITY_INPUT, amount)

    def click_add_to_cart(self):
        self.click(self.ADD_TO_CART)

    def click_continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING)
