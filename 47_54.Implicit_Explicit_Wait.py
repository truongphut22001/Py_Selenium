import time
from asyncio import wait

from selenium import webdriver
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
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
    time.sleep(3)
    item_list = driver.find_elements(By.CSS_SELECTOR, "div.products-wrapper .products .product")
    assert len(item_list) > 0
    expected_item_list = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
    actual_item_list = []
    for item in item_list:
        item_text = item.find_element(By.CSS_SELECTOR, ".product-name").text
        assert "ber" in item_text
        actual_item_list.append(item_text)
        item.find_element(By.CSS_SELECTOR, ".product-action button").click()
    assert actual_item_list == expected_item_list

    driver.find_element(By.CSS_SELECTOR, ".cart-icon img").click()
    driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
    driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
    driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
    WebDriverWait(driver, 10).until( EC.visibility_of_element_located((By.CSS_SELECTOR, ".promoInfo")) )

    cart_items = driver.find_elements(By.CSS_SELECTOR, "#productCartTables td:nth-last-child(1) .amount")
    total_expected = 0
    for item in cart_items:
        item.text
        total_expected += int(item.text)
    total_actual = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
    assert total_expected == total_actual

    discount_percent = int(driver.find_element(By.CSS_SELECTOR, ".discountPerc").text.replace("%", "")) / 100
    total_expected_after_discount = total_expected * (1 - discount_percent)
    total_actual_after_discount = total_actual * (1 - discount_percent)
    assert total_expected_after_discount == total_actual_after_discount

    assert total_actual_after_discount < total_actual

finally:
    driver.quit()