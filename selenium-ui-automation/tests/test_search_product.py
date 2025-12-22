import allure

@allure.feature("Search")
class TestSearchProduct:

    @allure.title("Search for product and verify relevant results are displayed")
    def test_search_product(self, home):
        product_search = "Men Tshirt"
        product = home.click_product_tab()
        assert product.is_cases_test_title_visible(), "All Products title is not visible"
        product.search_product(product_search)
        product.search_product_click()
        assert product.is_cases_test_title_visible(), "Searched Products title is not visible"
        assert product.is_products_related_to_search_are_visible(), "Displayed products do not match the search query"