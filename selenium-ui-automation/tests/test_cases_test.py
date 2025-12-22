import allure

@allure.feature("Test Cases")
class TestCasesTest:

    @allure.title("Verify test cases page is accessible and title is visible")
    def test_cases_test(self, home):
        cases = home.click_test_cases_tab()
        assert cases.is_case_test_title_visible(), "Test cases title is not visible"
