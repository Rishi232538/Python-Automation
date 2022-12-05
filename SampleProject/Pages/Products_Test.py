import self as self
from selenium.webdriver.common.by import By


class Products_Test():

    def __init__(self, driver):
        self.driver = driver

        self.Catelog_Xpath = "(//i[@class='right fas fa-angle-left '])[1]"
        self.Products_Xpath = "//*[text()=' Products']"
        self.Product_name_id = "SearchProductName"
        self.SKU_id = "GoDirectlyToSku"
        self.Search_Button_id = "search-products"

    def click_the_Catelog(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.Catelog_Xpath).click()

    def Click_on_the_Products(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.Products_Xpath).click()

    def enter_the_productname(self, element):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, self.Product_name_id).send_keys(element)

    def enter_the_sku(self, element):
        self.driver.find_element(By.ID, self.SKU_id).send_keys(element)

    def Click_on_the_SearchButton(self):
        self.driver.find_element(By.ID, self.Search_Button_id).click()
