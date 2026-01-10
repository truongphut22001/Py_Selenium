import time
from asyncio import wait
from tokenize import tabsize

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
    driver.implicitly_wait(3)
    driver.get("https://the-internet.herokuapp.com/iframe")
    driver.switch_to.frame("mce_0_ifr")
    driver.find_element(By.ID, "tinymce").clear()
    driver.find_element(By.ID, "tinymce").send_keys("PHUUUUU")
    driver.switch_to.default_content()
    print(driver.find_element(By.CSS_SELECTOR, "h3").text)

finally:
    driver.quit()