from selenium.webdriver.common.by import By
from driver_setup import create_chrome_driver
import time
import os

driver = None  # declare driver here so it's accessible in finally

try:
    os.makedirs("screenshots", exist_ok=True)
    driver = create_chrome_driver()
    driver.get("https://www.saucedemo.com/")

    # Enter valid credentials
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    assert "Products" in driver.page_source
    print(" TC01 - Valid Login Test Passed")
    driver.save_screenshot("screenshots/tc01_valid_login.png")

except Exception as e:
    print(" TC01 - Valid Login Test Failed")
    print("Error:", e)
    if driver:
        driver.save_screenshot("screenshots/tc01_valid_login_error.png")

finally:
    if driver:
        driver.quit()
