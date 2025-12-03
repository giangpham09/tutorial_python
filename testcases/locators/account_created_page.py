from selenium.webdriver.common.by import By
from testcases.bases.base_page import BasePage

class AccountCreatedPage(BasePage):
    TITLE=(By.XPATH,"//h2[@class='title text-center']")
    BTN=(By.XPATH,"//a[@class='btn btn-primary']")

    def get_title(self):
        self.scroll(self.TITLE)

        title=self.get_text(self.TITLE)
        if title == 'ACCOUNT CREATED!':
            result='PASS'
        else:
            result='FAIL'
        print(f"Verify that 'ACCOUNT CREATED!' is visible: {result}")

    def submit(self):
        self.click(self.BTN)