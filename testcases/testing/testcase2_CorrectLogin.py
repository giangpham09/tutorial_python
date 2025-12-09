import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from testcases.locators.delete_account_page import DeleteAccountPage
from testcases.locators.home_page import HomePage
from testcases.locators.login_page import LoginPage
from testcases.locators.register_page import RegisterPage
from testcases.locators.account_created_page import AccountCreatedPage
from testcases.locators.logged_in_page import LoggedInPage


def get_driver():
    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

def correct_login(username,email,password):
    # step 1. Launch browser
    driver=get_driver()

    # 2. Navigate to url 'http://automationexercise.com'
    home_page=HomePage(driver)
    home_page.open_homepage()

    # 3. Verify that home page is visible successfully
    result_step3=home_page.get_banner()
    if result_step3=='FAIL':
        print("Step 3: FAIL -> Dừng lại, không chạy các step sau")
        return

    # step 4. Click on 'Signup / Login' button
    home_page.go_to_login()

    # step 5. Verify 'Login to your account' is visible
    login_page=LoginPage(driver)
    result_step5=login_page.get_login_text()
    if result_step5=='FAIL':
        print(f"Step 5: FAIL -> Dừng lại, không chạy các step sau")
        return

    # step 6. Enter correct email address and password
    # 6.1: đăng ký tài khoản
    login_page.signup(username,email)
    login_page.submit_signup()
    register_page=RegisterPage(driver)
    register_page.select_female()
    register_page.input_textbox(username,password)
    register_page.select_day('19')
    register_page.select_month('April')
    register_page.select_year('2000')
    register_page.input_info('giang', 'pham', 'abc', '123abc', 'ewk323', 'AC', 'HN', '12345', '01234')
    register_page.select_country('Israel')
    register_page.submit_register()

    account_created_page=AccountCreatedPage(driver)
    account_created_page.submit()

    home_page.go_to_logout()

    # 6.2: login vào tài khoản mới đăng ký
    login_page.login(email,password)

    # step 7. Click 'login' button
    login_page.submit_login()

    # step 8. Verify that 'Logged in as username' is visible
    logged_in_page=LoggedInPage(driver)
    result_step8=logged_in_page.get_logged_tag(username)
    if result_step8=='FAIL':
        print(f"Step 8: FAIL -> Dừng lại, không chạy các step sau")
        return

    # step 9. Click 'Delete Account' button
    logged_in_page.delete_account()

    # step 10. Verify that 'ACCOUNT DELETED!' is visible
    delete_page=DeleteAccountPage(driver)
    result_step10=delete_page.get_title()
    if result_step10=='FAIL':
        print(f'Step 10: FAIL -> Dừng lại, không chạy các step sau')
        return

correct_login(f'newtest{random.randint(1,99)}',f'newtest{random.randint(1,99)}+1@mail.com','abcd1234')
correct_login(f'ftest{random.randint(1,99)}',f'fnewtest{random.randint(1,99)}+1@mail.com','abcd1234')
