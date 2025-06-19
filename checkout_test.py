from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup Chrome driver
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Step 1: Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Step 2: Add items to cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

# Step 3: Proceed to Checkout
driver.find_element(By.ID, "checkout").click()

# Step 4: Fill checkout form
driver.find_element(By.ID, "first-name").send_keys("John")
driver.find_element(By.ID, "last-name").send_keys("Doe")
driver.find_element(By.ID, "postal-code").send_keys("12345")
driver.find_element(By.ID, "continue").click()

# Step 5: Finish checkout
driver.find_element(By.ID, "finish").click()

# Step 6: Validate success message
success_msg = driver.find_element(By.CLASS_NAME, "complete-header").text
assert "THANK YOU FOR YOUR ORDER" in success_msg

print("✅ Test Passed: Order completed successfully!")

# Close browser
driver.quit()
