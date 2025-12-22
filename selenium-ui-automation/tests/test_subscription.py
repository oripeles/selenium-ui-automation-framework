import allure

@allure.feature("Subscription")
class TestSubscription:

    @allure.title("Subscribe successfully from home page")
    def test_subscription_from_home_page(self, home, existing_user):
        email = existing_user["email"]
        home.scroll_down()
        assert home.is_subscription_title_visible(),  "Subscription title is not visible"
        home.subscribe(email)
        assert home.is_subscription_success_visible(), "Subscription success message is not visible"