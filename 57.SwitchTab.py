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
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.find_element(By.LINK_TEXT, "Click Here").click()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    assert "New Window" == driver.find_element(By.CSS_SELECTOR, "h3").text
    driver.close()
    driver.switch_to.window(tabs[0])
    assert "Opening a new window" == driver.find_element(By.CSS_SELECTOR, "h3").text

finally:
    driver.quit()