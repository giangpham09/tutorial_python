from selenium.webdriver.common.by import By
from testcases.bases.base_page import BasePage

class HomePage(BasePage):
    # LOCATORS homepage
    TEXT_BANNER = (By.XPATH,"//div[@class='carousel-inner']")
    LOGIN_BTN = (By.XPATH,"//a[@href='/login']")

    # ACTIONS at homepage
    def open_homepage(self):
        self.driver.get('https://automationexercise.com/')

    def get_banner(self):
        banner_text = self.get_text(self.TEXT_BANNER)
        if 'Full-Fledged practice website for Automation Engineers' in banner_text:
            test_result = 'PASS'
        else:
            test_result = 'FAIL'
        print(f'Verify home page is visible successfully: {test_result}')

    def go_to_login(self):
        self.click(self.LOGIN_BTN)






