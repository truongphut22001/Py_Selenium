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

    name = "Phu"
    driver.find_element(By.ID, "name").send_keys(name)
    driver.find_element(By.ID, "alertbtn").click()
    alert_popup = driver.switch_to.alert
    alert_text =  alert_popup.text
    assert name in alert_text
    alert_popup.accept()
    # alert_popup.dismiss()
    time.sleep(3)
finally:
    driver.quit()