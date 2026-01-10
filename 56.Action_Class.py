import time
from asyncio import wait

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

service = Service("D:/OneDrive/Learning/Python_Selenium/chromedriver-win64/chromedriver.exe")
try:
    driver = webdriver.Chrome(
        service=service,
        options=chrome_options
    )
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    ActionChains(driver).move_to_element(driver.find_element(By.ID,"mousehover")).perform()
    ActionChains(driver).move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

finally:
    driver.quit()