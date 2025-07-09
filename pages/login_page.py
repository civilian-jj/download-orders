from pages.base_page import BasePage
from config.config import Config
from config.constants import Constants


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_locator = Config.LOGIN_USERNAME_LOCATOR
        self.password_locator = Config.LOGIN_PASSWORD_LOCATOR
        self.login_button_locator = Config.LOGIN_BUTTON_LOCATOR

    def login(self, username, password):
        self.send_keys(self.username_locator, username)
        self.send_keys(self.password_locator, password)
        self.click(self.login_button_locator)

    def is_login_page_visible(self):
        return self.is_element_visible(self.username_locator) and self.is_element_visible(self.password_locator)