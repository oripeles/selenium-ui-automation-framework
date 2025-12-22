import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage
from utilities.json_loader import load_json

BASE_URL = "https://www.automationexercise.com/"
@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(3)
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




