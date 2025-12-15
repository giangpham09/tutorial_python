from my_project_apply_pytest.pages.home_page import HomePage

def test_contact_us_flow(driver):

    # FIXME: do đã dùng pytest fixture (conftest.py @pytest.fixture() driver)
    #  nên biến driver scope này nhận giá trị bằng driver ở conftest.py dòng `yield driver`
    #   không cần gán/khởi tạo lại driver.
    #   -> điểm hay khi dùng pytest: fixture: pytest tự truyền driver vào đoạn `test_contact_us_flow(driver)`
    #   không cần phải import thêm hay gì cả

    # step 1. Launch browser
    driver=driver()

    # step 2. Navigate to url 'http://automationexercise.com'
    driver.get('http://automationexercise.com')

    # step 3. Verify that home page is visible successfully
    homepage=HomePage(driver)
    # FIXME: chưa truyền locator vào get_text() -> chạy bị lỗi
    result_step3=homepage.get_banner()
    if result_step3!='PASS':
        return 'Step 3: FAIL, quit flow!'

    # step 4. Click on 'Contact Us' button
    homepage.go_to_contactus()

    # step 5. Verify 'GET IN TOUCH' is visible
    # step 6. Enter name, email, subject and message
    # step 7. Upload file
    # step 8. Click 'Submit' button
    # step 9. Click OK button
    # step 10. Verify success message 'Success! Your details have been submitted successfully.' is visible
    # step 11. Click 'Home' button and verify that landed to home page successfully