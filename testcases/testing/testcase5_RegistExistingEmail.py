from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from testcases.locators.home_page import HomePage
from testcases.locators.login_page import LoginPage

def get_driver():
    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

def regist_existing_email(username,email):
    # step 1. Launch browser
    driver=get_driver()

    # step 2. Navigate to url 'http://automationexercise.com'
    driver.get('http://automationexercise.com')

    # step 3. Verify that home page is visible successfully
    homepage = HomePage(driver)
    result_step3 = homepage.get_banner()
    if result_step3 == 'FAIL':
        print('Step 3: FAIL -> Dừng lại, không chạy các step sau')
        return

    # step 4. Click on 'Signup / Login' button
    homepage.go_to_login()

    # step 5. Verify 'New User Signup!' is visible
    login_page = LoginPage(driver)
    result_step5=login_page.get_signup_text()
    if result_step5 == 'FAIL':
        print('Step 5: FAIL -> Dừng lại, không chạy các step sau')
        return

    # step 6. Enter name and already registered email address
    login_page.signup(username,email)

    # step 7. Click 'Signup' button
    login_page.submit_signup()

    # step 8. Verify error 'Email Address already exist!' is visible
    result_step8=login_page.check_signup_error1()
    if result_step8=='FAIL':
        print('Step 8: FAIL -> Dừng lại, không chạy các step sau')
        return

regist_existing_email(email='test_undel@example.com',username='test_undel')
