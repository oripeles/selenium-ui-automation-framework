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
        first_product_name = "Blue Top"
        second_product_name = "Men Tshirt"
        product = home.click_product_tab()
        product.add_to_cart_by_name(first_product_name)
        product.continue_shopping()
        product.add_to_cart_by_name(second_product_name)
        product.continue_shopping()
        cart = product.open_cart()
        assert cart.get_price_by_product_name(first_product_name) == expected_first_price, "Wrong price for first product"
        assert cart.get_price_by_product_name(second_product_name) == expected_second_price, "Wrong price for second product"
        assert cart.get_quantity_by_product_name(first_product_name) == expected_first_qty, "Wrong quantity for first product"
        assert cart.get_quantity_by_product_name(second_product_name) == expected_second_qty, "Wrong quantity for second product"

