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

    def add_to_cart_by_name(self,name):
        card = (By.XPATH, f"//*[@class='product-image-wrapper'][.//p[normalize-space()='{name}']]")
        add_btn = (
            By.XPATH,
            f"//div[contains(@class,'overlay-content')]//p[normalize-space()='{name}']/following-sibling::a[contains(@class,'add-to-cart')]"
        )
        self.hover(card)
        self.click(add_btn)

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BTN)

    def open_cart(self):
        self.click(self.VIEW_CART_TOP)
        return CartPage(self.driver)

    def is_products_related_to_search_are_visible(self) -> bool:
        return self.texts_equal(self.SEARCH_PRODUCT, self.VIEW_PRODUCT_RESULT)



