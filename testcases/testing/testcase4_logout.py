from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from testcases.locators.home_page import HomePage
from testcases.locators.logged_in_page import LoggedInPage
from testcases.locators.login_page import LoginPage

def get_driver():
    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

def logout_user(email, password, username):
    # step 1. Launch browser
    driver=get_driver()

    # step 2. Navigate to url 'http://automationexercise.com'
    driver.get('http://automationexercise.com')

    # step 3. Verify that home page is visible successfully
    homepage=HomePage(driver)
    result_step3 = homepage.get_banner()
    if result_step3 == 'FAIL':
        print('Step 3: FAIL -> Dừng lại, không chạy các step sau')
        return

    # step 4. Click on 'Signup / Login' button
    homepage.go_to_login()

    # step 5. Verify 'Login to your account' is visible
    login_page = LoginPage(driver)
    result_step5 = login_page.get_login_text()
    if result_step5 == 'FAIL':
        print('Step 5: FAIL -> Dừng lại, không chạy các step sau')
        return

    # step 6. Enter correct email address and password
    login_page.login(email, password)

    # step 7. Click 'login' button
    login_page.submit_login()

    # step 8. Verify that 'Logged in as username' is visible
    logged_in_page=LoggedInPage(driver)
    result_step8=logged_in_page.get_logged_tag(username)
    if result_step8 == 'FAIL':
        print('Step 5: FAIL -> Dừng lại, không chạy các step sau')
        return

    # step 9. Click 'Logout' button
    homepage.go_to_logout()

    # step 10. Verify that user is navigated to login page
    url=driver.current_url
    if url=='https://automationexercise.com/login':
        test_result='PASS'
    else:
        test_result='FAIL'
    print(f'Verify that user is navigated to login page: {test_result}')

logout_user('test_undel@example.com','abc1234','test_undel')

