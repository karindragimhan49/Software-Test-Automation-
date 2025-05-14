from selenium.webdriver.common.by import By
from driver_setup import create_chrome_driver
import os, time

try:
    os.makedirs("screenshots", exist_ok=True)
    driver = create_chrome_driver()
    driver.get("https://www.saucedemo.com/")

    assert driver.find_element(By.ID, "user-name")
    assert driver.find_element(By.ID, "password")
    assert driver.find_element(By.ID, "login-button")

    print(" TC07 - Valid UI Elements Test Passed")
    driver.save_screenshot("screenshots/tc07_valid_ui_elements.png")
except Exception as e:
    print(" TC07 - Valid UI Elements Test Failed")
    print("Error:", e)
    driver.save_screenshot("screenshots/tc07_valid_ui_elements_error.png")
finally:
    driver.quit()
