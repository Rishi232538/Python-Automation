from behave import *
from selenium import webdriver

from SampleProject.Pages.Alert_Test import alert_text


@given(u'User enter into the application for alert')
def step_impl(self):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    self.driver = webdriver.Chrome(options=options)
    self.driver.get("https://letcode.in/test")
    self.driver.maximize_window()
    self.driver.implicitly_wait(20)


@when(u'User clicks on Dialog in Alert')
def step_impl(self):
    driver= self.driver
    Alert_Test =alert_text(driver)
    Alert_Test.User_click_on_Dialog()


@when(u'User clicks on the prompt Alert')
def step_impl(self):
    driver = self.driver
    Alert_Test = alert_text(driver)
    Alert_Test.User_clicks_on_the_Prompt_Alert()
