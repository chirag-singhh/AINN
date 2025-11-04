# pip install selenium webdriver-manager

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

def run_login_test(test_id, username, password):
    """
    This function automates a login test case.
    It now checks for a success URL *or* an error message.
    """
    print(f"--- Running {test_id}: {username} / {password} ---")
    driver = None
    
    try:
        # --- 1. Setup ---
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        
        # --- 2. Go to the Page ---
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()
        time.sleep(1)

        # --- 3. Find Elements ---
        user_field = driver.find_element(By.ID, "username")
        pass_field = driver.find_element(By.ID, "password")
        submit_button = driver.find_element(By.ID, "submit")

        # --- 4. Perform Actions (The Test Case) ---
        user_field.send_keys(username)
        pass_field.send_keys(password)
        time.sleep(1)
        submit_button.click()
        
        # --- 5. Verify Result (Assertion) ---
        time.sleep(2)
        
        # Check for success URL first
        current_url = driver.current_url
        if "logged-in-successfully" in current_url:
            print(f"Test Case {test_id}: PASSED")
            print("Login was successful.")
            return "Yes"
        
        # If no success, check for an error message
        try:
            error_message = driver.find_element(By.ID, "error")
            if error_message.is_displayed():
                print(f"Test Case {test_id}: FAILED (as expected)")
                print(f"Found error message: {error_message.text}")
                # For a real test, you would check if this error is *correct*
                # For this experiment, finding the error proves the login *failed*.
                # If TC-002 *didn't* produce an error, that would be a bug.
                return "No" # The login was not achieved
        except NoSuchElementException:
            # No success URL and no error message
            print(f"Test Case {test_id}: FAILED")
            print("Login failed. No success URL and no error message found.")
            return "No"

    except Exception as e:
        print(f"An error occurred: {e}")
        return "No"
        
    finally:
        # --- 6. Cleanup ---
        if driver:
            driver.quit()
            print("Browser closed.")

# --- This is where the experiment runs ---
if __name__ == "__main__":
    
    # We are testing TC-002 from our Excel sheet
    test_case_id = "TC-002"
    test_username = "student"
    test_password = "wrongpassword" # This is the invalid data
    
    # Run the test
    result = run_login_test(test_case_id, test_username, test_password)
    
    print("\n--- Experiment Complete ---")
    print(f"Test Case {test_case_id} Achieved (Login): {result}")
    print("You can now update your 'TestCases.xlsx' file with this result.")