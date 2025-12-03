import random
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from testcases.locators.account_created_page import AccountCreatedPage
from testcases.locators.delete_account_page import DeleteAccountPage
from testcases.locators.home_page import HomePage
from testcases.locators.logged_in_page import LoggedInPage
from testcases.locators.login_page import LoginPage
from testcases.locators.register_page import RegisterPage


def get_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

def register_user():
    # step 1. Launch browser
    driver = get_driver()

    # step 2. Navigate to url 'http://automationexercise.com'
    homepage = HomePage(driver)
    homepage.open_homepage()

    # step 3. Verify that home page is visible successfully
    homepage.get_banner()

    # step 4. Click on 'Signup / Login' button
    homepage.go_to_login()

    # step 5. Verify 'New User Signup!' is visible
    login_page = LoginPage(driver)
    login_page.get_signup_text()

    # step 6. Enter name and email address
    username = 'testname'
    email = f'test{random.randint(1,100)}+1@mail.com'
    login_page.signup(username,email)

    # step 7. Click 'Signup' button
    login_page.submit_signup()

    # step 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
    register_page = RegisterPage(driver)
    register_page.get_title()

    # step 9. Fill details: Title, Name, Email, Password, Date of birth
    register_page.select_female()
    register_page.input_textbox(name=username,password='abcd1234')
    register_page.select_day('10')
    register_page.select_month('April')
    register_page.select_year('2000')

    # step 10. Select checkbox 'Sign up for our newsletter!'
    register_page.select_checkbox1()

    # step 11. Select checkbox 'Receive special offers from our partners!'
    register_page.select_checkbox2()

    # step 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    register_page.input_info('giang','pham','abc','123abc','ewk323','AC','HN','12345','01234')
    register_page.select_country('Israel')

    # step 13. Click 'Create Account button'
    register_page.submit_register()

    # step 14. Verify that 'ACCOUNT CREATED!' is visible
    created_page=AccountCreatedPage(driver)
    created_page.get_title()

    # step 15. Click 'Continue' button
    created_page.submit()

    # step 16. Verify that 'Logged in as username' is visible
    logged_in_page=LoggedInPage(driver)
    logged_in_page.get_logged_tag(username)

    # step 17. Click 'Delete Account' button
    logged_in_page.delete_account()

    # step 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    delete_page=DeleteAccountPage(driver)
    delete_page.get_title()
    delete_page.deleted_confirm()




    time.sleep(2)

print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
register_user()