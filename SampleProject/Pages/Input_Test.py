from _ast import Assert

from selenium.webdriver.common.by import By
from selenium import webdriver


class Input_Test():

    def __init__(self, driver):
        self.driver = driver

        self.clicks_on_the_Edit_xpath = "//*[text()='Edit']"
        self.Enter_the_Full_Name_id = "fullName"
        self.Append_a_text_to_add_id = "join"
        self.inside_the_textbox_id = "getMe"
        self.clear_the_Text_id = "clearMe"
        self.confirm_the_Text_id = "dontwrite"


    def User_clicks_the_Edit_in_inputSection(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.clicks_on_the_Edit_xpath).click()


    def Enter_your_full_name(self, element):
        self.driver.find_element(By.ID, self.Enter_the_Full_Name_id).send_keys(element)

    def Append_a_text_to_add(self, element):
        self.driver.find_element(By.ID, self.Append_a_text_to_add_id).send_keys(element)

    def inside_the_textbox_id(self):
        GetText =self.driver.find_element(By.ID, self.inside_the_textbox_id).get_attribute("value")
        print(GetText)

    def Clear_the_Text(self):
        self.driver.find_element(By.ID, self.clear_the_Text_id).clear()

    def confirm_the_Text(self):
        Actual_Result = self.driver.find_element(By.ID, self.confirm_the_Text_id)
        Expected_Result = "This text is readonly"

        Assert(Actual_Result,Expected_Result)


