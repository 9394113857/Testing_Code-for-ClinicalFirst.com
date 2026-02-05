# Import required Selenium and Python libraries
from selenium import webdriver
import time
import unittest


class ClinicalFirstAutomationTest(unittest.TestCase):
    """
    Automation test class for ClinicalFirst application
    Using Python + Selenium + unittest framework
    """

    def setUp(self):
        """
        This method runs BEFORE every test case.
        Used to initialize browser and launch application.
        """

        # Path to ChromeDriver executable
        driver_path = "D:\\Training Session\\Downloads\\chromedriver_win32\\chromedriver.exe"

        # Launch Chrome browser
        self.driver = webdriver.Chrome(executable_path=driver_path)

        # Open ClinicalFirst DEV environment
        self.driver.get("https://clinicalfirst.com/dev/2/")

        # Maximize browser window
        self.driver.maximize_window()

    def test_login_and_account_workflow(self):
        """
        Test Case:
        - Login to application
        - Edit account details
        - Change password
        - Update address book
        - Access wishlist
        - Logout
        """

        # Click Login menu
        self.driver.find_element_by_class_name("hidden-xs").click()
        self.driver.find_element_by_link_text("Login").click()

        # Enter login credentials
        self.driver.find_element_by_name("email").send_keys("saikrishnasanagapalli@gmail.com")
        self.driver.find_element_by_name("password").send_keys("saikrishna12@#")

        # Submit login form
        self.driver.find_element_by_xpath(
            "//*[@id='content']/div/div[2]/div/form/input"
        ).click()
        time.sleep(3)

        # Navigate to Edit Account Information
        self.driver.find_element_by_link_text("Edit your account information").click()
        time.sleep(2)

        # Update First Name
        self.driver.find_element_by_name("firstname").clear()
        self.driver.find_element_by_name("firstname").send_keys("saikrishna")

        # Update Telephone Number
        self.driver.find_element_by_name("telephone").clear()
        self.driver.find_element_by_name("telephone").send_keys("9246718057")

        # Save account changes
        self.driver.find_element_by_xpath(
            "//*[@id='content']/form/div/div[2]/input"
        ).click()
        time.sleep(2)

        # Change Password
        self.driver.find_element_by_link_text("Change your password").click()
        self.driver.find_element_by_name("password").send_keys("saikrishna12@#")
        self.driver.find_element_by_name("confirm").send_keys("saikrishna12@#")

        # Save new password
        self.driver.find_element_by_xpath(
            "//*[@id='content']/form/div/div[2]/input"
        ).click()
        time.sleep(2)

        # Navigate to Modify Address Book
        self.driver.find_element_by_link_text("Modify your address book entries").click()
        time.sleep(2)

        # Click Add New Address
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

        # Navigate to Wishlist
        self.driver.find_element_by_link_text("Modify your wish list").click()
        time.sleep(2)

        # Return to account page
        self.driver.find_element_by_xpath(
            "//*[@id='content']/div/div/a"
        ).click()
        time.sleep(2)

        # Logout from application
        self.driver.find_element_by_xpath(
            "//*[@id='header']/div[1]/div/div/div[2]/ul[2]/li[2]/a"
        ).click()
        time.sleep(3)

    def tearDown(self):
        """
        This method runs AFTER every test case.
        Used to close the browser.
        """
        self.driver.close()


# Entry point to run the test
if __name__ == "__main__":
    unittest.main()


# 🧠 How to explain this in ONE sentence (remember this)

# This Python Selenium automation script validates end-to-end user workflows like login, account updates, password changes, and logout using the unittest framework.

