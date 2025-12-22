import allure

@allure.feature("Products")
class TestVerifyAllProductsDetail:

    @allure.title("Verify product details page is accessible from all products list")
    def test_verify_all_products_detail(self, home):
        product = home.click_product_tab()
        assert product.is_cases_test_title_visible(), "All Products title is not visible"
        assert product.is_view_product_visible(), "View Product button is not visible for products"
        product.click_product_view()
