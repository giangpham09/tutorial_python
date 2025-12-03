from selenium.webdriver.common.by import By

# FIXME: xoá bỏ import không liên quan
# from basic_exercises.basicPython import result1
from testcases.bases.base_page import BasePage

class DeleteAccountPage(BasePage):
    TITLE=(By.XPATH,"//h2[@class='title text-center']")
    BTN=(By.XPATH,"//a[@class='btn btn-primary']")

    def get_title(self):
        title=self.get_text(self.TITLE)
        if title=='ACCOUNT DELETED!':
            result='PASS'
        else:
            result='FAIL'
        print(f"Verify that 'ACCOUNT DELETED!' is visible: {result}")
    def deleted_confirm(self):
        self.click(self.BTN)