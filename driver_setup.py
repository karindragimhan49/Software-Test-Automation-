from selenium import webdriver
import os

def create_chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--start-maximized")

    # Explicitly set the path to chromedriver if needed
    chromedriver_path = os.path.join(os.getcwd(), "chromedriver.exe")
    return webdriver.Chrome(executable_path=chromedriver_path, options=options)
