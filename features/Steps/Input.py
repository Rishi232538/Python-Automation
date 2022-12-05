
from behave import *
from selenium import webdriver
from SampleProject.Pages.Input_Test import Input_Test
from features.Chromedriver.Driver import Driver


@given(u'User enter into the letcode.in')
def step_impl(self):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    self.driver = webdriver.Chrome(options=options)
    self.driver.get("https://letcode.in/test")
    self.driver.maximize_window()
    self.driver.implicitly_wait(20)


@when(u'User clicks on the edit in input section')
def step_impl(self):
    driver = self.driver;
    Inputtest = Input_Test(driver)
    Inputtest.User_clicks_the_Edit_in_inputSection()


@when(u'User enter the full name')
def step_impl(self):
    driver = self.driver;
    Inputtest = Input_Test(driver)
    Inputtest.Enter_your_full_name("Rishi Ramanathan")


@when(u'User needs to clear the text')
def step_impl(self):
    driver = self.driver;
    Inputtest = Input_Test(driver)
    Inputtest.Clear_the_Text()


@when(u'User needs to confirm the text')
def step_impl(self):
    driver = self.driver;
    Inputtest = Input_Test(driver)
    Inputtest.confirm_the_Text()
