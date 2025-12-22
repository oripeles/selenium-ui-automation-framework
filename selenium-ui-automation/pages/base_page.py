from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait, Select

class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Element not visible: {locator}")

    def wait_for_clickable(self, locator):
        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise AssertionError(f"Element not clickable: {locator}")

    def click(self, locator):
        self.wait_for_clickable(locator).click()

    def handle_alert(self):
        try:
            self.wait.until(EC.alert_is_present())
            self.driver.switch_to.alert.accept()
            return True
        except TimeoutException:
            return False


    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def get_text(self, locator):
        return self.wait_for_visible(locator).text.strip()

    def enter_text(self, locator, text):
        element = self.wait_for_visible(locator)
        element.clear()
        element.send_keys(text)

    def select_by_value(self, locator, value):
        el = self.wait_for_clickable(locator)
        Select(el).select_by_value(str(value))

    def select_by_text(self, locator, text):
        el = self.wait_for_clickable(locator)
        Select(el).select_by_visible_text(str(text))

    def js_click(self, locator):
        el = self.wait_for_visible(locator)
        try:
            self.driver.execute_script("arguments[0].click();", el)
        except Exception as e:
            raise AssertionError(f"JS click failed on {locator}: {str(e)}")

    def get_value(self, locator):
        try:
            el = self.wait.until(EC.presence_of_element_located(locator))
            return el.get_attribute("value")
        except TimeoutException:
            raise AssertionError(f"Element not present (get_value): {locator}")

    def normalize_text(self, text: str) -> str:
        return "".join(text.split()).lower()

    def texts_equal(self, locator_expected, locator_actual) -> bool:
        expected = self.normalize_text(self.get_value(locator_expected))
        actual = self.normalize_text(self.get_text(locator_actual))
        return expected == actual

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def hover(self, locator):
        el = self.wait_for_visible(locator)
        ActionChains(self.driver).move_to_element(el).perform()
        return el

    def count_after_wait(self, locator, min_count=1) -> int:
        self.wait.until(lambda d: len(d.find_elements(*locator)) >= min_count)
        return len(self.driver.find_elements(*locator))

