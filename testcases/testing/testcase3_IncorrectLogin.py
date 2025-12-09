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

def incorrect_login(email,password):
    # step 1. Launch browser
    driver=get_driver()

    # step 2. Navigate to url 'http://automationexercise.com'
    driver.get('http://automationexercise.com')

    # step 3. Verify that home page is visible successfully
    homepage=HomePage(driver)
    result_step3=homepage.get_banner()
    if result_step3=='FAIL':
        print('Step 3: FAIL -> Dừng lại, không chạy các step sau')
        return

    # step 4. Click on 'Signup / Login' button
    homepage.go_to_login()

    # step 5. Verify 'Login to your account' is visible
    login_page=LoginPage(driver)
    result_step5=login_page.get_login_text()
    if result_step5=='FAIL':
        print('Step 5: FAIL -> Dừng lại, không chạy các step sau')
        return

    # step 6. Enter incorrect email address and password
    login_page.login(email,password)

    # step 7. Click 'login' button
    login_page.submit_login()

    # step 8. Verify error 'Your email or password is incorrect!' is visible
    result_step8=login_page.check_login_error1()
    if result_step8=='FAIL':
        print('Step 8: FAIL -> Dừng lại, không chạy các step sau')
        return

# case1: đúng email, sai password
incorrect_login('tester@mail.com','ancewewe')
# case2: tài khoản chưa đăng ký
incorrect_login('tester@tester.com','ancewewe')



