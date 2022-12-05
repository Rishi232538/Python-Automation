from behave import  *
from selenium import webdriver

from SampleProject.Pages.Button_Test import Button_Test


@given(u'User enter into the Application')
def step_impl(self):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    self.driver = webdriver.Chrome(options=options)
    self.driver.get("https://letcode.in/test")
    self.driver.maximize_window()
    self.driver.implicitly_wait(20)


@when(u'User clicks on the Button section')
def step_impl(self):
    driver = self.driver
    Button_Section = Button_Test(driver)
    Button_Section.Click_on_the_clickButton()


@when(u'User clicks on the Go_To_Button')
def step_impl(self):
    driver = self.driver
    Button_Section = Button_Test(driver)
    Button_Section.Click_on_the_GoToHome()



@when(u'Get the X and Y co-ordinates in Find Location')
def step_impl(self):
    driver = self.driver
    Button_Section = Button_Test(driver)
    Button_Section.Get_the_Position()


@when(u'System will show the color of the button')
def step_impl(self):
    driver = self.driver
    Button_Section = Button_Test(driver)
    Button_Section.Color_of_the_button()


@when(u'Confirm button is disabled')
def step_impl(self):
    driver = self.driver
    Button_section = Button_Test(driver)
    Button_section.Confirm_the_button()


@then(u'User hold the Button')
def step_impl(self):
    driver = self.driver
    Button_section = Button_Test(driver)
    Button_section.Click_and_hold()