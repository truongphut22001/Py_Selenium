import pytest
import time
from asyncio import wait
from tokenize import tabsize

import openpyxl
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v141.dom_storage import Item
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="class")
def setup():
    print("Before Class")
    yield
    print("After Class")

@pytest.fixture()
def dataLoad():
    print("Data Parameter")
    return ["PHU", "Truong", "TEST"]

@pytest.fixture(params=[("chrome","PHU1","vip"),
                        ("firefox","PHu2","vip2"),
                        ("IE", "phu3", "vip3")])
def cross_browser(request):
    return request.param


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--ignore-certificate-errors")
        service = ChromeService("D:/OneDrive/Learning/Python_Selenium/chromedriver-win64/chromedriver.exe")
        driver = webdriver.Chrome(
            service=service,
            options=chrome_options
        )
    elif browser_name == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--start-maximized")
        firefox_options.add_argument("--ignore-certificate-errors")
        service = FirefoxService("D:/OneDrive/Learning/Python_Selenium/geckodriver-v0.35.0-win64/geckodriver.exe")
        driver = webdriver.Firefox(service=service)
    driver.implicitly_wait(3)
    yield driver
    driver.quit()