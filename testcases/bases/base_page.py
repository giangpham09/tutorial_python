from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def click(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator)).click()

    def type(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).text
        except TimeoutException:
            print("get_text: Chờ mãi không thấy locator xuất hiện")
            return None

    def scroll(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*locator))
