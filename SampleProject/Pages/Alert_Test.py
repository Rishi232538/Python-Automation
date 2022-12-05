import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By



class alert_text():

    def __init__(self, driver):
        self.driver= driver

        self.Dialog_xpath = "//*[text() ='Dialog']"
        self.Simple_Alert_xpath = "//*[text() ='Simple Alert']"
        self.COnfirm_alert_xpath = "//*[text() ='Confirm Alert']"

        self.Prompt_Alert_xpath = "//*[text() ='Prompt Alert']"


    def User_click_on_Dialog(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, self.Dialog_xpath).click()


    def User_clicks_on_the_Prompt_Alert(self):
        alert = Alert(self.driver)
        self.driver.find_element(By.XPATH, self.Prompt_Alert_xpath).click()
        alert.send_keys("Rishi")
        alert.accept()




