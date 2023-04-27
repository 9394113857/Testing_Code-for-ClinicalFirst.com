from selenium import webdriver

import time
import unittest


class testing_clinicalfirst_dev(unittest.TestCase):

    def setUp(self):
        # initializing the browser window
        driver_path = "D:\\Training Session\\Downloads\\chromedriver_win32\\chromedriver.exe"

        self.driver = webdriver.Chrome(
            executable_path = driver_path)
        self.driver.get("https://clinicalfirst.com/dev/2/")


        # self.driver = webdriver.Chrome(
        #     executable_path="C:\\Users\\raghu\\Downloads\\chromedriver_win32\\chromedriver.exe")
        # self.driver.get("https://clinicalfirst.com/dev/2/") # Initial code



        # for maximizing browser window

        self.driver.maximize_window()

    def test_login_logout(self):
        # Path for login button
        self.driver.find_element_by_class_name("hidden-xs").click()
        self.driver.find_element_by_link_text("Login").click()

        # login to the clinicalfirst
        self.driver.find_element_by_name("email").send_keys("saikrishnasanagapalli@gmail.com")

        self.driver.find_element_by_name("password").send_keys("saikrishna12@#")

        self.driver.find_element_by_xpath("//*[@id='content']/div/div[2]/div/form/input").click()
        time.sleep(3)

        # my account
        # self.driver.find_element_by_xpath('//*[@id="my_account"]/a/span[1]').click()
        # self.driver.find_element_by_link_text('My Account').click()
        # time.sleep(3)

        self.driver.find_element_by_link_text('Edit your account information').click()
        time.sleep(3)

        # my acc
        # edit information
        self.driver.find_element_by_name('firstname').clear()
        time.sleep(3)

        self.driver.find_element_by_name('firstname').send_keys('saikrishna')

        self.driver.find_element_by_name('telephone').clear()
        time.sleep(2)
        self.driver.find_element_by_name('telephone').send_keys('9246718057')

        # coutinue
        self.driver.find_element_by_xpath('//*[@id="content"]/form/div/div[2]/input').click()
        time.sleep(2)

        # change password
        self.driver.find_element_by_link_text('Change your password').click()
        self.driver.find_element_by_name('password').send_keys('saikrishna12@#')
        self.driver.find_element_by_name('confirm').send_keys('saikrishna12@#')
        time.sleep(2)
        # countiune
        self.driver.find_element_by_xpath('//*[@id="content"]/form/div/div[2]/input').click()
        time.sleep(2)

        # edit prescription
        self.driver.find_element_by_link_text('Modify your prescriptions').click()
        time.sleep(2)
        self.driver.find_element_by_link_text('Account').click()
        time.sleep(2)

        # Modify your address book entries
        self.driver.find_element_by_link_text('Modify your address book entries').click()
        time.sleep(2)
        # self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/table/tbody/tr/td[2]/a[1]').click()
        self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/a').click()
        # deatials
        self.driver.find_element_by_id('input-firstname').send_keys('saikrishna')
        self.driver.find_element_by_id("input-lastname").send_keys('sanagapalli')
        self.driver.find_element_by_id("input-address-1").send_keys('15-12-18,Janda chetu bazar,tenali')
        self.driver.find_element_by_id("input-city").send_keys('Tenali')
        self.driver.find_element_by_id("input-postcode").send_keys('522201')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="input-country"]')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="input-zone"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="input-zone"]/option[3]').click()
        time.sleep(2)
        # countiune
        self.driver.find_element_by_xpath('//*[@id="content"]/form/div/div[2]/input').click()
        time.sleep(2)
        # account
        self.driver.find_element_by_link_text('Account').click()
        time.sleep(2)

        # Modify your wish list
        self.driver.find_element_by_link_text('Modify your wish list').click()
        time.sleep(2)
        # countiune
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div/a').click()
        time.sleep(2)

        # Logout from CLinicalfirst
        self.driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div/div[2]/ul[2]/li[2]/a').click()
        time.sleep(3)

    def tearDown(self):
        time.sleep(3)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()