from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    chromedriver_path = os.path.join(os.getcwd(), "chromedriver")
    service = Service(chromedriver_path)

    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver
