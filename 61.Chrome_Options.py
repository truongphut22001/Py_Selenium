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
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--lang=vi")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)


service = Service("D:/OneDrive/Learning/Python_Selenium/chromedriver-win64/chromedriver.exe")
try:
    driver = webdriver.Chrome(
        service=service,
        options=chrome_options
    )
    driver.implicitly_wait(3)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    driver.find_element(By.CSS_SELECTOR, "th:nth-child(1)").click()
    Select(driver.find_element(By.ID, "page-menu")).select_by_visible_text("20")
    actual_sorted_ascending = []
    veggies_list = driver.find_elements(By.CSS_SELECTOR, "tbody tr td:nth-child(1)")
    for item in veggies_list:
        actual_sorted_ascending.append(item.text)
    expected_sorted_ascending = actual_sorted_ascending.copy()
    expected_sorted_ascending.sort()
    assert actual_sorted_ascending  == expected_sorted_ascending

finally:
    driver.quit()