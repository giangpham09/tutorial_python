from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from testcases.bases.base_page import BasePage

class RegisterPage(BasePage):
    # LOCATORS register page
    HEADER = (By.XPATH, "//div[@class='login-form']/h2[@class='title text-center']")
    RADIO_MR = (By.XPATH,"//label[@for='id_gender1']")
    RADIO_MRS = (By.XPATH,"//label[@for='id_gender2']")
    NAMEBOX = (By.XPATH,"//input[@id='name']")
    EMAILBOX = (By.XPATH,"//input[@id='email']")
    PWBOX = (By.XPATH,"//input[@id='password']")
    DOB_DAY = (By.XPATH,"//select[@id='days']")
    DOB_MONTH = (By.XPATH,"//select[@id='months']")
    DOB_YEAR = (By.XPATH,"//select[@id='years']")
    CHECKBOX_1 = (By.XPATH,"//input[@name='newsletter']")
    CHECKBOX_2 = (By.XPATH,"//input[@name='optin']")
    FIRSTNAME = (By.XPATH,"//input[@id='first_name']")
    LASTNAME = (By.XPATH,"//input[@id='last_name']")
    COMPANY = (By.XPATH,"//input[@id='company']")
    ADDRESS_1 = (By.XPATH,"//input[@id='address1']")
    ADDRESS_2 = (By.XPATH,"//input[@id='address2']")
    COUNTRY = (By.XPATH,"//select[@id='country']")
    STATE = (By.XPATH,"//input[@name='state']")
    CITY = (By.XPATH,"//input[@name='city']")
    ZIPCODE = (By.XPATH,"//input[@id='zipcode']")
    PHONE = (By.XPATH,"//input[@id='mobile_number']")
    CREATE_BTN = (By.XPATH,"//button[@class='btn btn-default']")

    def get_title(self):
        header =  self.get_text(self.HEADER)
        if header == "ENTER ACCOUNT INFORMATION":
            test_result = 'PASS'
        else:
            test_result = 'FAIL'
        print(f"Verify that 'ENTER ACCOUNT INFORMATION' is visible: {test_result}")

    # Enter Account Information
    def select_male(self):
        self.click(self.RADIO_MR)
    def select_female(self):
        self.click(self.RADIO_MRS)
    def input_textbox(self, name,password):
        self.type(self.NAMEBOX,name)
        # self.type(self.EMAILBOX, email) : field invalid update
        self.type(self.PWBOX, password)
    def select_day(self,value):
        self.scroll(self.DOB_DAY)
        day=self.driver.find_element(*self.DOB_DAY) # dùng *self.DOB_DAY do có 2 tham số truyền vào là By.XPATH và value xpath
        sel=Select(day)
        sel.select_by_visible_text(value)
    def select_month(self,value):
        month=self.driver.find_element(*self.DOB_MONTH)
        sel=Select(month)
        sel.select_by_visible_text(value)
    def select_year(self,value):
        year=self.driver.find_element(*self.DOB_YEAR)
        sel=Select(year)
        sel.select_by_visible_text(value)
    def select_checkbox1(self):
        self.click(self.CHECKBOX_1)
    def select_checkbox2(self):
        self.click(self.CHECKBOX_2)

    # Address Information
    def input_info(self,fname,lname,company,add1,add2,state,city,zipcode,phone):
        self.scroll(self.FIRSTNAME)

        self.type(self.FIRSTNAME,fname)
        self.type(self.LASTNAME,lname)
        self.type(self.COMPANY,company)
        self.type(self.ADDRESS_1,add1)
        self.type(self.ADDRESS_2,add2)

        self.scroll(self.STATE)

        self.type(self.STATE,state)
        self.type(self.CITY,city)
        self.type(self.ZIPCODE,zipcode)
        self.type(self.PHONE,phone)
    def select_country(self,value):
        country=self.driver.find_element(*self.COUNTRY)
        sel=Select(country)
        sel.select_by_visible_text(value)

    def submit_register(self):
        self.click(self.CREATE_BTN)

