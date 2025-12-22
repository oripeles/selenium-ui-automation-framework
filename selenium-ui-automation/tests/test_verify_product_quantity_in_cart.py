import allure

@allure.feature("Cart")
class TestVerifyProductQuantityInCart:

    @allure.title("Add product with specific quantity and verify it appears in cart")
    def test_verify_product_quantity_in_cart(self, home):
        qty = "4"
        product = home.click_view_product()
        product.set_quantity(qty)
        product.click_add_to_cart()
        product.click_continue_shopping()
        cart = home.go_to_cart()
        assert cart.is_product_displayed(), "Product is not displayed in cart"

