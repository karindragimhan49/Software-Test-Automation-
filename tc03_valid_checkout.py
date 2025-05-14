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

    # Add to cart
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    # Checkout form
    driver.find_element(By.ID, "first-name").send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    time.sleep(1)
    
    # Finish checkout
    driver.find_element(By.ID, "finish").click()
    time.sleep(2)

    # Assert order confirmation
    assert "THANK YOU FOR YOUR ORDER" in driver.page_source.upper()

    print(" TC03 - Valid Checkout Test Passed")
    driver.save_screenshot("screenshots/tc03_valid_checkout.png")

except Exception as e:
    print(" TC03 - Valid Checkout Test Failed")
    print("Error:", e)
    driver.save_screenshot("screenshots/tc03_valid_checkout_error.png")
    print("\n=== Page Source Preview ===")
    print(driver.page_source[:1000])  # Only print first 1000 chars to avoid clutter

finally:
    driver.quit()
