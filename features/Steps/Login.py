from behave import *
from selenium import webdriver
from webdriver_manager.core import driver

from SampleProject.Pages.Login_Test import Login_Test



@given(u'User login into the application')
def setUpClass(cls):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    cls.driver = webdriver.Chrome(options=options)
    cls.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    cls.driver.maximize_window()


@when(u'User enter the Email')
def test_login_valid(self):
    driver = self.driver;
    login = Login_Test(driver)
    login.enter_the_email("admin@yourstore.com")


@when(u'User enter the password')
def step_impl(self):
    driver = self.driver;
    login = Login_Test(driver)
    login.enter_the_password("admin")


@then(u'User click the login')
def step_impl(self):
    driver = self.driver;
    login = Login_Test(driver)
    login.click_the_loginbutton()



