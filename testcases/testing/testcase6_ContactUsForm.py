from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

def contactus_form(name,email,subject,msg):
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

    # step 4. Click on 'Contact Us' button
    homepage.go_to_contactus()

    # step 5. Verify 'GET IN TOUCH' is visible
