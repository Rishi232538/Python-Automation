from telnetlib import EC

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Button_Test():

    def __init__(self, driver):
        self.driver = driver

        self.click_the_button_section_xpath = "//*[text()='Click']"

        self.Click_on_the_GoToHome_xpath = "//*[text()='Goto Home']"
        self.Find_the_X_Y_Coordinate_xpath = "//*[text()='Find Location']"
        self.color_of_the_button_xpath = "//*[text()='What is my color?']"
        self.Height_and_Width_of_button_xpath = "//*[text()='How tall & fat I am?']"
        self.confirm_the_button_xpath = "//*[text()='Disabled']"
        self.click_and_hold_xpath = "//*[text()='Button Hold!']"


    def Click_on_the_clickButton(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, self.click_the_button_section_xpath).click()

    def Click_on_the_GoToHome(self):
        self.driver.find_element(By.XPATH, self.Click_on_the_GoToHome_xpath).click()
        self.driver.back()

    def Get_the_Position(self):
        self.driver.find_element(By.XPATH, self.Find_the_X_Y_Coordinate_xpath).click()
        Element = self.driver.find_element(By.XPATH, self.Find_the_X_Y_Coordinate_xpath)
        Location = Element.location
        size = Element.location

        print(Location)
        print(size)

    def Color_of_the_button(self):
        Color = self.driver.find_element(By.XPATH, self.color_of_the_button_xpath).value_of_css_property('background-color')
        print(Color)
        

    def Confirm_the_button(self):
        Text = self.driver.find_element(By.XPATH, self.confirm_the_button_xpath)
        a = Text.is_enabled()
        print(a)


    def Click_and_hold(self):
        action = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH, self.click_and_hold_xpath)
        action.click_and_hold(element)
        action.perform()







