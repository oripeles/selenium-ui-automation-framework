from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from utilities.config import EXPLICIT_WAIT
from utilities.waits import Waits


class BasePage:
    def __init__(self, driver, timeout: int = EXPLICIT_WAIT):
        self.driver = driver
        self.waits = Waits(driver, timeout)

    def click(self, locator):
        self.waits.clickable(locator).click()

    def handle_alert(self):
        if self.waits.alert_present():
            self.driver.switch_to.alert.accept()
            return True
        return False

    def is_visible(self, locator) -> bool:
        try:
            self.waits.visible(locator)
            return True
        except AssertionError:
            return False

    def get_text(self, locator):
        return self.waits.visible(locator).text.strip()

    def enter_text(self, locator, text):
        element = self.waits.visible(locator)
        element.clear()
        element.send_keys(text)

    def select_by_value(self, locator, value):
        el = self.waits.clickable(locator)
        Select(el).select_by_value(str(value))

    def select_by_text(self, locator, text):
        el = self.waits.clickable(locator)
        Select(el).select_by_visible_text(str(text))

    def js_click(self, locator):
        el = self.waits.visible(locator)
        try:
            self.driver.execute_script("arguments[0].click();", el)
        except Exception as e:
            raise AssertionError(f"JS click failed on {locator}: {str(e)}")

    def get_value(self, locator):
        return self.waits.present(locator).get_attribute("value")

    def normalize_text(self, text: str) -> str:
        return "".join(text.split()).lower()

    def texts_equal(self, locator_expected, locator_actual) -> bool:
        expected = self.normalize_text(self.get_value(locator_expected))
        actual = self.normalize_text(self.get_text(locator_actual))
        return expected == actual

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def hover(self, locator):
        el = self.waits.visible(locator)
        ActionChains(self.driver).move_to_element(el).perform()
        return el

    def count_after_wait(self, locator, min_count=1) -> int:
        self.waits.wait.until(lambda d: len(d.find_elements(*locator)) >= min_count)
        return len(self.driver.find_elements(*locator))

