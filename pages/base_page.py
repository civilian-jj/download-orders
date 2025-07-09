import selenium
from utils import logger
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, locator):
        try:
            element = self.wait.until(selenium.webdriver.support.expected_conditions.element_to_be_clickable(locator))
            element.click()
            logger.info(f"Clicked on element: {locator}")
        except Exception as e:
            logger.error(f"Failed to click on element {locator}: {e}")
            raise

    def send_keys(self, locator, text):
        try:
            element = self.wait.until(selenium.webdriver.support.expected_conditions.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            logger.info(f"Sent keys '{text}' to element: {locator}")
        except Exception as e:
            logger.error(f"Failed to send keys to element {locator}: {e}")
            raise

    def is_element_visible(self, locator, timeout=10):
        try:
            self.wait = selenium.webdriver.support.ui.WebDriverWait(self.driver, timeout)
            element = self.wait.until(selenium.webdriver.support.expected_conditions.visibility_of_element_located(locator))
            logger.info(f"Element {locator} is visible")
            return True
        except selenium.common.exceptions.TimeoutException:
            logger.warning(f"Element {locator} is not visible after {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"Error checking visibility of element {locator}: {e}")
            raise