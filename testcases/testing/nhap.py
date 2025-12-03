import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get('https://automationexercise.com/')
wait = WebDriverWait(driver,10)
a=(By.XPATH,"//div[@class='carousel-inner']//h2")
b= wait.until(EC.visibility_of_element_located(a)).text
print(b)
time.sleep(3)