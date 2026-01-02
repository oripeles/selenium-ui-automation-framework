import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from utilities.json_loader import load_json
from utilities.config import BASE_URL, HEADLESS, IMPLICIT_WAIT

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    if HEADLESS:
        options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(IMPLICIT_WAIT)
    yield driver
    driver.quit()

@pytest.fixture
def home(driver):
    driver.get(BASE_URL)
    home = HomePage(driver)
    assert home.is_home_page_visible(), "Home page not active or visible"
    return home

@pytest.fixture(scope="session")
def user_data():
    return load_json("user_data")

@pytest.fixture
def existing_user(user_data):
    return user_data["existing_user"]

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            allure.attach(

                driver.get_screenshot_as_png(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            allure.attach(
                driver.current_url,
                name="Current URL",
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                driver.page_source,
                name="Page Source",
                attachment_type=allure.attachment_type.HTML
            )




