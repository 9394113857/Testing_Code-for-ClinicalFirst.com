# ============================================================
# Import required Selenium and Python libraries
# ============================================================

from selenium import webdriver
import time
import unittest


# ============================================================
# Test Class Definition
# ============================================================

class ClinicalFirstAutomationTest(unittest.TestCase):
    """
    Automation test class for ClinicalFirst application
    Using Python + Selenium + unittest framework

    Type: End-to-End UI Automation Test
    Framework: unittest (built-in Python test framework)
    """

    # ========================================================
    # setUp() Method
    # ========================================================

    def setUp(self):
        """
        This method runs BEFORE every test case.

        Purpose:
        - Initialize browser
        - Launch application
        - Prepare test environment
        """

        # Path to ChromeDriver executable
        driver_path = "D:\\Training Session\\Downloads\\chromedriver_win32\\chromedriver.exe"

        # Launch Chrome browser
        self.driver = webdriver.Chrome(executable_path=driver_path)

        # Open ClinicalFirst DEV environment
        self.driver.get("https://clinicalfirst.com/dev/2/")

        # Maximize browser window
        self.driver.maximize_window()

        # ===== Stage Status =====
        # Browser: OPENED
        # Application: LOADED
        # Session: STARTED


    # ========================================================
    # Test Case Method
    # ========================================================

    def test_login_and_account_workflow(self):
        """
        Test Case Flow:

        1. Login to application
        2. Edit account details
        3. Change password
        4. Update address book
        5. Access wishlist
        6. Logout

        Type: End-to-End Functional UI Test
        """

        # ----------------------------------------------------
        # STEP 1: Navigate to Login Page
        # ----------------------------------------------------

        self.driver.find_element_by_class_name("hidden-xs").click()
        self.driver.find_element_by_link_text("Login").click()

        # ----------------------------------------------------
        # STEP 2: Enter Login Credentials
        # ----------------------------------------------------

        self.driver.find_element_by_name("email").send_keys("saikrishnasanagapalli@gmail.com")
        self.driver.find_element_by_name("password").send_keys("saikrishna12@#")

        # Submit login form
        self.driver.find_element_by_xpath(
            "//*[@id='content']/div/div[2]/div/form/input"
        ).click()

        time.sleep(3)

        # ===== Stage Status =====
        # Login: SUCCESSFUL
        # User Session: ACTIVE


        # ----------------------------------------------------
        # STEP 3: Edit Account Information
        # ----------------------------------------------------

        self.driver.find_element_by_link_text("Edit your account information").click()
        time.sleep(2)

        # Update First Name
        self.driver.find_element_by_name("firstname").clear()
        self.driver.find_element_by_name("firstname").send_keys("saikrishna")

        # Update Telephone
        self.driver.find_element_by_name("telephone").clear()
        self.driver.find_element_by_name("telephone").send_keys("9246718057")

        # Save changes
        self.driver.find_element_by_xpath(
            "//*[@id='content']/form/div/div[2]/input"
        ).click()

        time.sleep(2)


        # ----------------------------------------------------
        # STEP 4: Change Password
        # ----------------------------------------------------

        self.driver.find_element_by_link_text("Change your password").click()

        self.driver.find_element_by_name("password").send_keys("saikrishna12@#")
        self.driver.find_element_by_name("confirm").send_keys("saikrishna12@#")

        # Save new password
        self.driver.find_element_by_xpath(
            "//*[@id='content']/form/div/div[2]/input"
        ).click()

        time.sleep(2)


        # ----------------------------------------------------
        # STEP 5: Modify Address Book
        # ----------------------------------------------------

        self.driver.find_element_by_link_text("Modify your address book entries").click()
        time.sleep(2)

        # Add new address
        self.driver.find_element_by_xpath(
            "//*[@id='content']/div[2]/div[2]/a"
        ).click()

        # Fill address details
        self.driver.find_element_by_id("input-firstname").send_keys("saikrishna")
        self.driver.find_element_by_id("input-lastname").send_keys("sanagapalli")
        self.driver.find_element_by_id("input-address-1").send_keys(
            "15-12-18, Janda chetu bazar, Tenali"
        )
        self.driver.find_element_by_id("input-city").send_keys("Tenali")
        self.driver.find_element_by_id("input-postcode").send_keys("522201")

        # Select State
        self.driver.find_element_by_id("input-zone").click()
        time.sleep(1)

        self.driver.find_element_by_xpath(
            "//*[@id='input-zone']/option[3]"
        ).click()

        # Save address
        self.driver.find_element_by_xpath(
            "//*[@id='content']/form/div/div[2]/input"
        ).click()

        time.sleep(2)


        # ----------------------------------------------------
        # STEP 6: Access Wishlist
        # ----------------------------------------------------

        self.driver.find_element_by_link_text("Modify your wish list").click()
        time.sleep(2)

        # Return to account page
        self.driver.find_element_by_xpath(
            "//*[@id='content']/div/div/a"
        ).click()

        time.sleep(2)


        # ----------------------------------------------------
        # STEP 7: Logout
        # ----------------------------------------------------

        self.driver.find_element_by_xpath(
            "//*[@id='header']/div[1]/div/div/div[2]/ul[2]/li[2]/a"
        ).click()

        time.sleep(3)

        # ===== Stage Status =====
        # User Session: TERMINATED
        # Workflow: COMPLETED SUCCESSFULLY


    # ========================================================
    # tearDown() Method
    # ========================================================

    def tearDown(self):
        """
        This method runs AFTER every test case.

        Purpose:
        - Close browser
        - End session
        - Clean up resources
        """

        self.driver.close()

        # ===== Final Stage Status =====
        # Browser: CLOSED
        # Session: ENDED
        # Test Execution: FINISHED


# ============================================================
# Test Execution Entry Point
# ============================================================

if __name__ == "__main__":
    unittest.main()



# ============================================================
# ================== STRUCTURE EXPLANATION ==================
# ============================================================

# 1. What Opens First?
#    - Python execution starts
#    - unittest framework initializes
#    - setUp() method runs
#    - Browser launches
#    - Application loads

# 2. What Runs Next?
#    - test_login_and_account_workflow()
#    - Executes complete user journey
#    - Login → Edit → Password → Address → Wishlist → Logout

# 3. What Closes?
#    - tearDown() method runs
#    - Browser closes
#    - Session destroyed

# 4. What Type of Automation is This?
#    - UI Automation
#    - Functional Testing
#    - End-to-End Testing
#    - Regression Testing (if added to suite)

# 5. Framework Type?
#    - unittest-based automation framework
#    - Linear test design (not POM)
#    - Single test case structure
#    - Hardcoded test data
#    - No reporting layer
#    - No external configuration

# 6. Improvements for Production-Level Framework:
#    1. Use Page Object Model (POM)
#    2. Replace time.sleep() with WebDriverWait
#    3. Remove hardcoded credentials
#    4. Add logging
#    5. Add HTML reporting
#    6. Integrate with CI/CD (Jenkins)
#    7. Use webdriver-manager
#    8. Add exception handling

# 7. Final Verdict:
#    This is a Basic End-to-End Selenium UI Automation Script
#    built using Python and unittest framework.
#    It validates real-world user account workflows.
