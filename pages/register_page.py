from selenium.webdriver.common.by import By
from .base_page import BasePage
from config.constants import Constants
from config.config import Config
import time

class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(f"{Config.BASE_URL}/register")
    
    def enter_username(self, username):
        self.send_keys((By.ID, Constants.REG_USERNAME), username)
    
    def enter_email(self, email):
        self.send_keys((By.ID, Constants.REG_EMAIL), email)
    
    def enter_password(self, password):
        self.send_keys((By.ID, Constants.REG_PASSWORD), password)
    
    def enter_confirm_password(self, password):
        self.send_keys((By.ID, Constants.REG_CONFIRM_PASSWORD), password)
    
    def click_register(self):
        self.click((By.ID, Constants.REGISTER_BUTTON))
    
    def register(self, username, email, password):
        self.enter_username(username)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(password)
        self.click_register()
        # 等待注册完成
        time.sleep(1)
    
    def get_success_message(self):
        if self.is_element_visible((By.CLASS_NAME, Constants.SUCCESS_MESSAGE)):
            return self.get_element_text((By.CLASS_NAME, Constants.SUCCESS_MESSAGE))
        return None
    
    def get_error_messages(self):
        errors = []
        error_elements = self.driver.find_elements(By.CLASS_NAME, Constants.ERROR_MESSAGE)
        for element in error_elements:
            if element.is_displayed():
                errors.append(element.text)
        return errors