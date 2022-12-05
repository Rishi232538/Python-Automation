from behave import *
from selenium import webdriver

from SampleProject.Pages.Dropdown_Test import Dropdown_Test


@given(u'Select the fruit')
def step_impl(self):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    self.driver = webdriver.Chrome(options=options)
    self.driver.get("https://letcode.in/test")
    self.driver.maximize_window()
    self.driver.implicitly_wait(20)


@when(u'User needs to select the super hero')
def step_impl(self):
    driver = self.driver
    DP = Dropdown_Test(driver)
    DP.Click_on_the_Dropdown()
    DP.Select_the_apple_using_visible_Text()


@when(u'User needs to select the programming language')
def step_impl(self):
    driver = self.driver
    DP = Dropdown_Test(driver)
    DP.Select_the_superhero()
