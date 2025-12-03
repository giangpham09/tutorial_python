class Elements:
    def homepage(self):
        BANNER = "//div[@class='carousel-inner']"
        SIGNUP_BTN = "//a[@href='/login']"

    def login_page(self):
        SIGNUP_HEADER = "//div[@class='signup-form']"
        SIGNUP_NAMEBOX = "//input[@data-qa='signup-name']"
        SIGNUP_EMAILBOX = "//input[@data-qa='signup-email']"
        SIGNUP_BTN = "//button[@data-qa='signup-button']"

    def signup_page(self):
        HEADER = "//h2[@class='title text-center']"
        RADIO_MR = "//label[@for='id_gender1']"
        RADIO_MRS = "//label[@for='id_gender2']"
        NAMEBOX = "//input[@id='name']"
        EMAILBOX = "//input[@id='email']"
        PWBOX = "//input[@id='password']"
        DOB_DAY = "//select[@id='days']"
        DOB_MONTH = "//select[@id='months']"
        DOB_YEAR = "//select[@id='years']"
        CHECKBOX_1 = "//input[@name='newsletter']"
        CHECKBOX_2 = "//input[@name='optin']"
        FIRSTNAME = "//input[@id='first_name']"
        LASTNAME = "//input[@id='last_name']"
        COMPANY = "//input[@id='company']"
        ADDRESS_1 = "//input[@id='address1']"
        ADDRESS_2 = "//input[@id='address2']"
        COUNTRY = "//select[@id='country']"
        STATE = "//input[@name='optin']"
        CITY = "//input[@name='optin']"
        ZIPCODE = "//input[@id='zipcode']"
        PHONE = "//input[@id='mobile_number']"
        CREAT_BTN = "//button[@class='btn btn-default']"

    def account_created_page(self):
        HEADER = "//h2[@class='title text-center']"
        BUTTON = "//a[@data-qa='continue-button']"
        LOGGED_USERNAME = "//i[@class='fa fa-user']"
        DEL_BTN =  "//a[@href='/delete_account']"
        LOGGED_USERNAME = "//i[@class='fa fa-user']"
        LOGGED_USERNAME = "//i[@class='fa fa-user']"

    def deleted_page(self):
        HEADER = "//h2[@class='title text-center']"
        BUTTON = "//a[@data-qa='continue-button']"




