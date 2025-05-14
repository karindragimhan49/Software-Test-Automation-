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

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    # Leave fields empty and continue
    driver.find_element(By.ID, "continue").click()
    time.sleep(1)

    assert "Error" in driver.page_source
    print(" TC04 - Invalid Checkout Test Passed")
    driver.save_screenshot("screenshots/tc04_invalid_checkout.png")
except Exception as e:
    print(" TC04 - Invalid Checkout Test Failed")
    print("Error:", e)
    driver.save_screenshot("screenshots/tc04_invalid_checkout_error.png")
finally:
    driver.quit()
