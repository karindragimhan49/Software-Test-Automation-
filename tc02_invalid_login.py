from selenium.webdriver.common.by import By
from driver_setup import create_chrome_driver
import os, time

try:
    os.makedirs("screenshots", exist_ok=True)
    driver = create_chrome_driver()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("wrong_pass")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)
    assert "Epic sadface" in driver.page_source
    print(" TC02 - Invalid Login Test Passed")

    driver.save_screenshot("screenshots/tc02_invalid_login.png")
except Exception as e:
    print(" TC02 - Invalid Login Test Failed")
    print("Error:", e)
    driver.save_screenshot("screenshots/tc02_invalid_login_error.png")
finally:
    driver.quit()
