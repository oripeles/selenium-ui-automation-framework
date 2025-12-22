import allure

@allure.feature("Categories")
class TestViewCategoryProducts:

    @allure.title("View products in Women > Dress category")
    def test_view_women_category_products(self, home):
        assert home.is_left_sidebar_visible(), "Categories sidebar is not visible"
        home.click_women_category()
        home.click_dress_category()
        assert home.is_women_category_title_visible(), "Women category title is not visible"

    @allure.title("View products in Men > Shirt category")
    def test_view_men_category_products(self, home):
        assert home.is_left_sidebar_visible(), "Categories sidebar is not visible"
        home.click_men_category()
        home.click_shirt_category()
        assert home.is_men_category_title_visible(), "Men category title is not visible"

