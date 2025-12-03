from selenium.webdriver.common.by import By
from testcases.bases.base_page import BasePage

class LoginPage(BasePage):
    # LOCATORS login page
    SIGNUP_HEADER = (By.XPATH,"//div[@class='signup-form']//h2")
    SIGNUP_NAMEBOX = (By.XPATH,"//input[@data-qa='signup-name']")
    SIGNUP_EMAILBOX = (By.XPATH,"//input[@data-qa='signup-email']")
    SIGNUP_BTN = (By.XPATH,"//button[@data-qa='signup-button']")

    # ACTIONS at login page
    def open_login_page(self):
        self.driver.get('https://automationexercise.com/login')

    def get_signup_text(self):
        signup_text = self.get_text(self.SIGNUP_HEADER)
        if signup_text == "New User Signup!":
            test_result = 'PASS'
        else:
            test_result = 'FAIL'
        print(f"Verify 'New User Signup!' is visible: {test_result}")

    def signup(self, username, email):
        self.type(self.SIGNUP_NAMEBOX, username)
        self.type(self.SIGNUP_EMAILBOX, email)

    def submit_signup(self):
        self.click(self.SIGNUP_BTN)


