import allure

@allure.feature("Cart")
class TestRemoveProductsFromCart:

    @allure.title("Remove product from cart successfully")
    def test_remove_products_from_cart(self, home):
        product = home.click_product_tab()
        product.add_first_product_to_cart()
        product.continue_shopping()
        cart = product.open_cart()
        cart.click_delete()
        assert cart.is_cart_empty(), "Product was not removed from the cart"


