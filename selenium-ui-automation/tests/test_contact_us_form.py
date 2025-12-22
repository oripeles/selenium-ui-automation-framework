import allure

@allure.feature("Contact Us")
class TestContactUsForm:

    @allure.title("Submit contact us form successfully with valid details")
    def test_contact_us_form(self, home, existing_user):
        details_data = {
            "name": "Ori",
            "email": existing_user["email"],
            "subject": "QA Automation",
            "message": "123 Test"
        }
        contact = home.click_contact_us_tab()
        assert contact.is_contact_us_page_visible(), "Contact Us page is not visible"
        contact.fill_details(**details_data)
        contact.click_submit()
        contact.click_handle_alert()
        assert contact.is_contact_us_success_visible(), "Contact Us success page is not visible"
        contact.click_home()