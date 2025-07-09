class Config:
    BASE_URL = "https://www.chinawangli.com/"
    BROWSER = "edge" 
    HEADLESS = False
    TIMEOUT = 10
    MAX_RETRIES = 3
    PROXY = None
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 20
    SCREENSHOT_DIR = "screenshots"
    REPORT_DIR = "reports"
    TEST_DATA_FILE = "test_data.json"
    LOGIN_USERNAME_LOCATOR = ("id", "username")
    LOGIN_PASSWORD_LOCATOR = ("id", "password")
    LOGIN_BUTTON_LOCATOR = ("id", "loginButton")
    REG_USERNAME_LOCATOR = ("id", "reg_username")