from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Dropdown_Test():

    def __init__(self, driver):
        self.driver = driver

        self.CLick_the_Dropdown_xpath = "//*[text()='Drop-Down']"
        self.Select_the_fruitname_id = "fruits"
        self.Select_the_superhero_id = "superheros"

    def Click_on_the_Dropdown(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.CLick_the_Dropdown_xpath).click()

    def Select_the_apple_using_visible_Text(self):
        Dropdown1 =  self.driver.find_element(By.ID, self.Select_the_fruitname_id)
        First_dropdown = Select(Dropdown1)
        First_dropdown.select_by_visible_text("Apple")

    def Select_the_superhero(self):
        Dropdown2 = self.driver.find_element(By.ID, self.Select_the_superhero_id)
        Second_dropdown = Select(Dropdown2)
        Second_dropdown.select_by_visible_text("Ant-Man")
        Second_dropdown.select_by_visible_text("Aquaman")
        Second_dropdown.select_by_visible_text("The Avengers")

