from selenium.webdriver.common.by import By
from my_project_apply_pytest.pages.base_page import Actions

class DeleteAccountPage(Actions):
    TITLE=(By.XPATH,"//h2[@class='title text-center']")
    BTN=(By.XPATH,"//a[@class='btn btn-primary']")

    def get_title(self):
        title=self.get_text(self.TITLE)
        if not title:
            return 'FAIL'
        if title=='ACCOUNT DELETED!':
            result='PASS'
        else:
            result='FAIL'
        print(f"Verify that 'ACCOUNT DELETED!' is visible: {result}")
    def deleted_confirm(self):
        self.click(self.BTN)