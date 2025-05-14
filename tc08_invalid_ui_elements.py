from selenium.webdriver.common.by import By
from driver_setup import create_chrome_driver
import os, time

try:
    os.makedirs("screenshots", exist_ok=True)
    driver = create_chrome_driver()
    driver.get("https://www.saucedemo.com/")

    missing_element = driver.find_elements(By.ID, "non-existent-element")
    assert not missing_element

    print(" TC08 - Invalid UI Elements Test Passed (Element not found as expected)")
    driver.save_screenshot("screenshots/tc08_invalid_ui_elements.png")
except Exception as e:
    print(" TC08 - Invalid UI Elements Test Failed")
    print("Error:", e)
    driver.save_screenshot("screenshots/tc08_invalid_ui_elements_error.png")
finally:
    driver.quit()
