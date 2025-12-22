import allure

@allure.feature("Subscription")
class TestSubscriptionFromCart:

    @allure.title("Subscribe successfully from cart page")
    def test_subscription_card(self, home, existing_user):
        email = existing_user["email"]
        cart = home.go_to_cart()
        cart.scroll_down_to_footer()
        assert cart.is_subscription_title_visible(), "Subscription title is not visible in cart page"
        cart.subscribe(email)
        assert cart.is_subscription_success_visible(), "Subscription success message is not visible in cart page"