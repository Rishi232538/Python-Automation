from selenium.webdriver.common.by import By


class Login_Test():

    def __init__(self, driver):
        self.driver = driver

        self.Email_TextBox_Xpath = "//input[@id='Email']"
        self.Password_TextBox_Xpath = "//input[@id='Password']"
        self.Login_Button_Xpath = "//*[text()='Log in']"

    def enter_the_email(self, email):
        self.driver.find_element(By.XPATH, self.Email_TextBox_Xpath).clear()
        self.driver.find_element(By.XPATH, self.Email_TextBox_Xpath).send_keys(email)

    def enter_the_password(self, password):
        self.driver.find_element(By.XPATH, self.Password_TextBox_Xpath).clear()
        self.driver.find_element(By.XPATH, self.Password_TextBox_Xpath).send_keys(password)

    def click_the_loginbutton(self):
        self.driver.find_element(By.XPATH, self.Login_Button_Xpath).click()
