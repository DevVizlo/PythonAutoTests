from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.saucedemo.com/'

    def Visit(self):
        return self.driver.get(self.base_url)

    def FindElement(self, locator):
        return self.driver.findElement(By.CSS_SELECTOR, locator)