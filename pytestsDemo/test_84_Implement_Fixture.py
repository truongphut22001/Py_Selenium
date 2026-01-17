import json
import time
from asyncio import wait
from tokenize import tabsize

import openpyxl
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v141.dom_storage import Item
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.LoginPage import LoginPage


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
test_data_path = "C:\\Users\\Phu\\Desktop\\Py_Selenium\\data\\test_84_Implement_Fixture.json"
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize("test_item", test_list)
def test_e2e(browserInstance, test_item):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    login = LoginPage(driver);
    login.get_title()
    shop_page =  login.login(test_item["userEmail"], test_item["passWord"])
    shop_page.add_product_to_cart(test_item["productName"])
    checkout_page = shop_page.goToCart()
    checkout_page.click_checkout()
    checkout_page.enter_delivery_address("India")
    checkout_page.validate_order()