from selenium.webdriver.common.by import By
from testcases.bases.base_page import BasePage

class LoggedInPage(BasePage):

    LOGGED_TAG=(By.XPATH,"//a[contains(text(),'Logged in as')]")
    DEL_BTN=(By.XPATH,"//a[@href='/delete_account']")

    def get_logged_tag(self,username):
        tag=self.get_text(self.LOGGED_TAG)
        if not tag:
            return 'FAIL'
        if tag==f'Logged in as {username}':
            result='PASS'
        else:
            result='FAIL'
        print(f"Verify that 'Logged in as {username}' is visible: {result}")

    def delete_account(self):
        self.click(self.DEL_BTN)