from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.cart_page import CartPage


class ProductsPage(BasePage):
    CASES_TITLE = (By.CLASS_NAME, "title")
    VIEW_PRODUCT= (By.XPATH, "//*[contains(@href, '/product_details/')]")
    VIEW_PRODUCT_FIRST_BUTTON = (By.XPATH, "//*[@href='/product_details/1']")
    SEARCH_PRODUCT  = (By.ID, "search_product")
    SEARCH_PRODUCT_BUTTON = (By.ID, "submit_search")
    VIEW_PRODUCT_RESULT = (By.CSS_SELECTOR, ".productinfo.text-center p")
    CONTINUE_SHOPPING_BTN = (By.XPATH, "//*[normalize-space()='Continue Shopping']")
    VIEW_CART_TOP = (By.XPATH, "//*[@href='/view_cart']")
    PROD_CARD_1 = (By.XPATH, "(//*[@class='product-image-wrapper'])[1]")
    PROD_CARD_2 = (By.XPATH, "(//*[@class='product-image-wrapper'])[3]")
    ADD_1 = (By.XPATH, "(//*[contains(@class, 'add-to-cart')])[1]")
    ADD_2 = (By.XPATH, "(//*[contains(@class, 'add-to-cart')])[3]")

    def is_cases_test_title_visible(self) -> bool:
        return self.is_visible(self.CASES_TITLE)

    def is_view_product_visible(self) -> bool:
        return self.is_visible(self.VIEW_PRODUCT)

    def click_product_view(self):
        self.js_click(self.VIEW_PRODUCT_FIRST_BUTTON)

    def search_product(self,product):
        self.enter_text(self.SEARCH_PRODUCT,product)

    def search_product_click(self):
        self.click(self.SEARCH_PRODUCT_BUTTON)

    def add_first_product_to_cart(self):
        self.hover(self.PROD_CARD_1)
        self.js_click(self.ADD_1)

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BTN)

    def add_second_product(self):
        self.hover(self.PROD_CARD_2)
        self.js_click(self.ADD_2)

    def open_cart(self):
        self.click(self.VIEW_CART_TOP)
        return CartPage(self.driver)

    def is_products_related_to_search_are_visible(self) -> bool:
        return self.texts_equal(self.SEARCH_PRODUCT, self.VIEW_PRODUCT_RESULT)



