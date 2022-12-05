from selenium import webdriver


class Driver():

    def __init__(self, driver):
        self.driver = driver

    def Website(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://letcode.in/test")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
