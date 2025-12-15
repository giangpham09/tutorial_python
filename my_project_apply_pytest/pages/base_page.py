from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

class Actions:
    def __init__(self,driver:webdriver):
        self.driver=driver
        self.wait = WebDriverWait(driver, 10)

    def type(self,locator:tuple,text:str):
        element=self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def click(self,locator:tuple):
        self.wait.until(EC.visibility_of_element_located(locator)).click()

    def get_text(self,locator:tuple):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).text
        except TimeoutException:
            print('Cannot find the locator')
            return None

    def scroll(self,locator:tuple):
        self.driver.execute_script('arguments[0].scrollIntoView();', self.driver.find_element(*locator))