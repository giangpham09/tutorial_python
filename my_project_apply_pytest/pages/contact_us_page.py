from selenium.webdriver.common.by import By
from my_project_apply_pytest.pages.base_page import Actions

class ContactUsPage(Actions):
    # LOCATORS trên contact us page
    HEADER=(By.XPATH,"//div[@class='contact-form']//h2")
    NAME_INPUT=(By.XPATH,"//input[@name='name']")
    EMAIL_INPUT=(By.XPATH,"//input[@name='name']")
    SUBJECT_INPUT=(By.XPATH,"//input[@name='name']")
    MESSAGE_INPUT=(By.XPATH,"//input[@name='name']")
    FILE_UPLOAD=(By.XPATH,"//input[@name='name']")
    SUBMIT_BTN=(By.XPATH,"//input[@name='name']")
    SUCCESS_MSG=(By.XPATH,"//input[@name='name']")

    def get_header(self,locator:tuple):
        header=self.get_text(self.HEADER)
        if not header:
            return 'FAIL'
        if header=='GET IN TOUCH':
            result='PASS'
        else:
            result='FAIL'
        return f"Verify 'GET IN TOUCH' is visible: {result}"

    def input_textbox(self,name:str,email:str,msg:str,file_path:str):
        self.type(self.NAME_INPUT,name)
        self.type(self.EMAIL_INPUT,email)
        self.type(self.MESSAGE_INPUT,msg)
        self.type(self.FILE_UPLOAD,file_path)

    def submit_form(self,locator:tuple):
        self.click(self.SUBMIT_BTN)