from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Waits:
    def __init__(self, driver, timeout: int):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def visible(self, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise AssertionError(f"Element not visible: {locator}")

    def clickable(self, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            raise AssertionError(f"Element not clickable: {locator}")

    def present(self, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            raise AssertionError(f"Element not present: {locator}")

    def alert_present(self) -> bool:
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.alert_is_present())
            return True
        except TimeoutException:
            return False


