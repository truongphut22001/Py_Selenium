import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

service = Service("D:/OneDrive/Learning/Python_Selenium/chromedriver-win64/chromedriver.exe")
try:
    driver = webdriver.Chrome(
        service=service,
        options=chrome_options
    )
    driver.get("https://rahulshettyacademy.com/AutomationPractice")
    checkBoxs = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    for checkbox in checkBoxs:
        if checkbox.get_attribute("value") == "option2":
            checkbox.click()
            assert checkbox.is_selected()
            break
    time.sleep(3)
finally:
    driver.quit()