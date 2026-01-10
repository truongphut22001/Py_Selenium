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

    # Radio button
    driver.find_elements(By.CSS_SELECTOR, ".radioButton")[2].click()
    assert driver.find_elements(By.CSS_SELECTOR, ".radioButton")[2].is_selected()

    # "Hide" button
    assert driver.find_element(By.ID, "displayed-text").is_displayed()

    driver.find_element(By.ID, "hide-textbox").click()
    # driver.find_element(By.ID, "show-textbox").click()
    assert not driver.find_element(By.ID, "displayed-text").is_displayed()


    time.sleep(3)
finally:
    driver.quit()