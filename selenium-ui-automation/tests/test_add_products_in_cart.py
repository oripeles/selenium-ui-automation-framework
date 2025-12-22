import pytest
import allure

@allure.feature("Cart")
class TestAddProductsInCart:

    @pytest.mark.smoke
    @allure.title("Add two products to cart and verify price and quantity")
    def test_add_products_in_cart(self, home):
        expected_first_price = "Rs. 500"
        expected_second_price = "Rs. 400"
        expected_first_qty = "1"
        expected_second_qty = "1"
        product = home.click_product_tab()
        product.add_first_product_to_cart()
        product.continue_shopping()
        product.add_second_product()
        product.continue_shopping()
        cart = product.open_cart()
        assert cart.get_first_product_price() == expected_first_price, "Wrong price for first product"
        assert cart.get_second_product_price() == expected_second_price, "Wrong price for second product"
        assert cart.get_first_product_quantity() == expected_first_qty, "Wrong quantity for first product"
        assert cart.get_second_product_quantity() == expected_second_qty, "Wrong quantity for second product"

