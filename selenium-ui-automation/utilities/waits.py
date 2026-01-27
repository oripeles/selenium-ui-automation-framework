from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Waits:
    def __init__(self, driver, timeout: int):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def visible(self, locator,timeout=20):
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Element not visible: {locator}")

    def clickable(self, locator):
        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise AssertionError(f"Element not clickable: {locator}")

    def present(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Element not present: {locator}")

    def alert_present(self) -> bool:
        try:
            self.wait.until(EC.alert_is_present())
            return True
        except TimeoutException:
            return False


