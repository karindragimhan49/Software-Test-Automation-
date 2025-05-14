from selenium.webdriver.common.by import By
from driver_setup import create_chrome_driver
import os, time

try:
    os.makedirs("screenshots", exist_ok=True)
    driver = create_chrome_driver()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    assert "Your Cart" in driver.page_source and "Remove" not in driver.page_source
    print(" TC06 - Invalid Cart Test Passed (Empty Cart)")
    driver.save_screenshot("screenshots/tc06_invalid_cart.png")
except Exception as e:
    print(" TC06 - Invalid Cart Test Failed")
    print("Error:", e)
    driver.save_screenshot("screenshots/tc06_invalid_cart_error.png")
finally:
    driver.quit()
