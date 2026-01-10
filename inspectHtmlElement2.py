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
    driver.get("https://rahulshettyacademy.com/client")

    # Sử dụng Partial Link Text để tìm element nằm trong 1 thẻ anchor có text contain "Forgot"
    driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot").click()

    # Sử dụng XPath, ghi theo đường dẫn từ cha -> con
    driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")

    # Su dung CSS selector như lúc code css
    driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("password@gmail.com")

    # Sử dụng XPath, ghi theo đường dẫn từ cha -> con
    driver.find_element(By.XPATH, "//form/div[3]/input").send_keys("password@gmail.com")

    # Sử dụng XPath, tìm button có text là "Save New Password"
    driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
    time.sleep(5)
finally:
    driver.quit()