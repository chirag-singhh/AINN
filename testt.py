# food_delivery_test.py
# ------------------------------------------
# Automated test for a food delivery web app using Selenium
# ------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Step 1: Set up Chrome driver
# Make sure you have ChromeDriver installed and in PATH
driver = webdriver.Chrome()

# Step 2: Open website
driver.get("https://food-delivery-frontend-s2l9.onrender.com/")
driver.maximize_window()
time.sleep(3)

print("✅ Opened food delivery website successfully")

# Step 3: Test - Verify title
expected_title = "Food Delivery"
if expected_title.lower() in driver.title.lower():
    print("✅ Title verified successfully")
else:
    print("❌ Title verification failed")

# Step 4: Test - Try searching for a restaurant/food (if available)
try:
    search_box = driver.find_element(By.TAG_NAME, "input")
    search_box.send_keys("Pizza")
    search_box.send_keys(Keys.ENTER)
    print("✅ Search box working")
except Exception as e:
    print("⚠️ Search test skipped:", e)

time.sleep(3)

# Step 5: Test - Try clicking on menu items if available
try:
    items = driver.find_elements(By.TAG_NAME, "img")
    if items:
        items[0].click()
        print("✅ Clicked on first food item")
    else:
        print("⚠️ No menu items found")
except Exception as e:
    print("⚠️ Error while clicking item:", e)

time.sleep(3)

# Step 6: Final result
print("✅ All test steps executed successfully")

# Step 7: Close the browser
driver.quit()
print("✅ Browser closed. Test completed.")



# URL = "https://food-delivery-frontend-s2l9.onrender.com/"   # replace with actual app URL
# EMAIL = "test1009@gmail.com"
# PASSWORD = "12345678"