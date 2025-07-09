from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager as edge_chromium
from config.config import Config

def get_driver():
    if Config.BROWSER.lower() == "edge":
        options = webdriver.EdgeOptions()
        if Config.HEADLESS:
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Edge(service=EdgeService(edge_chromium().install()), options=options)
    
    
    else:
        raise ValueError(f"Unsupported browser: {Config.BROWSER}")
    
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    return driver