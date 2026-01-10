import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

service = Service("D:/OneDrive/Learning/Python_Selenium/chromedriver-win64/chromedriver.exe")
try:
    driver = webdriver.Chrome(
        service=service,
        options=chrome_options
    )
    # driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    print(driver.title)
    print(driver.current_url)
    email_textBox = driver.find_element(By.NAME, "email")
    email_textBox.send_keys("chungoc0110a2@gmail.com")
    pw_textBox = driver.find_element(By.ID, "exampleInputPassword1")
    pw_textBox.send_keys("Hamy")
    chkBox = driver.find_element(By.ID, "exampleCheck1");
    chkBox.click()

    driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("PHU")

    driver.find_element(By.XPATH, "//input[@value='Submit']").click()
    messsage = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
    assert "Success" in messsage

    driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
    driver.find_element(By.XPATH, "(//input[@name='name'])[2]").send_keys("TriPRocip")
    driver.find_element(By.XPATH, "(//input[@name='name'])[2]").clear()

    time.sleep(5)
finally:
    driver.quit()