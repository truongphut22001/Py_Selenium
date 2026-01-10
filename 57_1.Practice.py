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
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    mail_text =  driver.find_element(By.CSS_SELECTOR, "p.im-para.red a").text
    user_name_text = mail_text[(mail_text.find("@") + 1) : (mail_text.find(".com"))]
    driver.switch_to.window(tabs[0])
    driver.find_element(By.ID, "username").send_keys(user_name_text)
    driver.find_element(By.ID, "password").send_keys("learning")
    driver.find_element(By.ID, "terms").click()
    driver.find_element(By.ID, "signInBtn").click()
    WebDriverWait(driver, 10).until(EC.title_is("ProtoCommerce"))
    assert "ProtoCommerce" == driver.title

finally:
    driver.quit()