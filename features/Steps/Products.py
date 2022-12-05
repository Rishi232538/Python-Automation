from behave import *
from selenium import webdriver

from SampleProject.Pages.Login_Test import Login_Test
from SampleProject.Pages.Products_Test import Products_Test


@given(u'User login into application')
def setUpClass(cls):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    cls.driver = webdriver.Chrome(options=options)
    cls.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    cls.driver.maximize_window()
    driver = cls.driver;
    login = Login_Test(driver)
    login.enter_the_email("admin@yourstore.com")
    login.enter_the_password("admin")
    login.click_the_loginbutton()


@when(u'User clicks on Catalog Section')
def step_impl(self):
    driver = self.driver;
    product = Products_Test(driver)
    product.click_the_Catelog()


@when(u'User clicks on Product Section')
def step_impl(self):
    driver = self.driver;
    product = Products_Test(driver)
    product.Click_on_the_Products()


@when(u'User enter the product name, SKU')
def step_impl(self):
    driver = self.driver;
    product = Products_Test(driver)
    product.enter_the_productname("Build your own computer")
    product.enter_the_sku("COMP_CUST")

@then(u'User clicks on SearchButton')
def step_impl(self):
    driver = self.driver;
    product = Products_Test(driver)
    product.Click_on_the_SearchButton()











