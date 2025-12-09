from selenium.webdriver.common.by import By
from testcases.bases.base_page import BasePage

class LoginPage(BasePage):
    # LOCATORS login page
    SIGNUP_HEADER = (By.XPATH,"//div[@class='signup-form']//h2")
    SIGNUP_NAMEBOX = (By.XPATH,"//input[@data-qa='signup-name']")
    SIGNUP_EMAILBOX = (By.XPATH,"//input[@data-qa='signup-email']")
    SIGNUP_BTN = (By.XPATH,"//button[@data-qa='signup-button']")

    LOGIN_HEADER = (By.XPATH,"//div[@class='login-form']//h2")
    LOGIN_EMAILBOX = (By.XPATH,"//input[@data-qa='login-email']")
    LOGIN_PASSWORD = (By.XPATH,"//input[@data-qa='login-password']")
    LOGIN_BTN = (By.XPATH,"//button[@data-qa='login-button']")

    LOGIN_ERROR_MSG1=(By.XPATH,"//p[@style='color: red;']")
    SIGNUP_ERROR_MSG1 = (By.XPATH, "//p[@style='color: red;']")

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

    def get_login_text(self):
        login_text = self.get_text(self.LOGIN_HEADER)
        if login_text == "Login to your account":
            test_result = 'PASS'
        else:
            test_result = 'FAIL'
        print(f"Verify 'Login to your account' is visible: {test_result}")

    def login(self,email,password):
        self.type(self.LOGIN_EMAILBOX, email)
        self.type(self.LOGIN_PASSWORD, password)

    def submit_login(self):
        self.click(self.LOGIN_BTN)

    def check_login_error1(self):
        error1=self.get_text(self.LOGIN_ERROR_MSG1)
        if not error1:
            return 'FAIL'
        if 'Your email or password is incorrect!' in error1:
            test_result = 'PASS'
        else:
            test_result = 'FAIL'
        print(f"Verify error 'Your email or password is incorrect!' is visible: {test_result}")
        return test_result

    def check_signup_error1(self):
        error=self.get_text(self.SIGNUP_ERROR_MSG1)
        if not error:
            return 'FAIL'
        if 'Email Address already exist!' in error:
            test_result = 'PASS'
        else:
            test_result = 'FAIL'
        print(f"Verify error 'Your email or password is incorrect!' is visible: {test_result}")
        return test_result

