import time
from asyncio import wait
from tokenize import tabsize

import openpyxl
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v141.dom_storage import Item
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")
# chrome_options.add_argument("headless")
# chrome_options.add_argument("--window-size=1920,1080")
# chrome_options.add_argument("--disable-notifications")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--lang=vi")
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_experimental_option("useAutomationExtension", False)

service = Service("D:/OneDrive/Learning/Python_Selenium/chromedriver-win64/chromedriver.exe")
try:
    driver = webdriver.Chrome(
        service=service,
        options=chrome_options
    )
    driver.implicitly_wait(3)

    excel_file_obj = openpyxl.load_workbook("data.xlsx")
    username = excel_file_obj["Sheet1"]["A2"].value
    password = excel_file_obj["Sheet1"]["B2"].value

    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "signInBtn").click()

finally:
    driver.quit()