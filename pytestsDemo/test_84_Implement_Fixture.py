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

# chrome_options = Options()
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--ignore-certificate-errors")
# chrome_options.add_argument("headless")
# chrome_options.add_argument("--window-size=1920,1080")
# chrome_options.add_argument("--disable-notifications")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--lang=vi")
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_experimental_option("useAutomationExtension", False)

def test_e2e(browserInstance):
    try:
        driver = browserInstance

        driver.get("https://rahulshettyacademy.com/loginpagePractise/")
        driver.find_element(By.ID, "username").send_keys("rahulshettyacademy")
        driver.find_element(By.ID, "password").send_keys("learning")
        driver.find_element(By.ID, "terms").click()
        driver.find_element(By.ID, "signInBtn").click()

        driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        phone_list = driver.find_elements(By.CSS_SELECTOR, "app-card-list app-card")
        for phone in phone_list:
            if phone.find_element(By.CSS_SELECTOR, "h4.card-title a").text == "Blackberry":
                phone.find_element(By.CSS_SELECTOR, ".card-footer button").click()
                break
        driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
        driver.find_element(By.ID, "country").send_keys("Ind")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "India")))
        driver.find_element(By.LINK_TEXT, "India").click()
        driver.find_element(By.CSS_SELECTOR, ".checkbox.checkbox-primary").click()
        driver.find_element(By.CSS_SELECTOR, "input[value='Purchase']").click()
        assert "Success! Thank you! Your order will be delivered in next few weeks" in driver.find_element(
            By.CSS_SELECTOR, ".alert-success").text
    finally:
        driver.quit()