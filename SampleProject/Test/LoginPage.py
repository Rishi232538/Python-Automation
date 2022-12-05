import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver

from SampleProject.Pages.Login_Test import Login_Test


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
        cls.driver.maximize_window()

    def test_login_valid(self):
         driver = self.driver;
         login = Login_Test(driver)
         login.enter_the_email("admin@yourstore.com")
         login.enter_the_password("admin")
         login.click_the_loginbutton()


    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completed")




