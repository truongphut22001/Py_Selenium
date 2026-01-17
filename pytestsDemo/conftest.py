import os

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
driver = None

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
    global driver
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

# @pytest.hookimpl( hookwrapper=True )
# def pytest_runtest_makereport(item):
#     """
#         Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#         :param item:
#         """
#     pytest_html = item.config.pluginmanager.getplugin( 'html' )
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr( report, 'extra', [] )
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr( report, 'wasxfail' )
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             reports_dir = os.path.join( os.path.dirname( __file__ ), 'reports' )
#             file_name = os.path.join( reports_dir, report.nodeid.replace( "::", "_" ) + ".png" )
#             print( "file name is " + file_name )
#             _capture_screenshot( file_name )
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append( pytest_html.extras.html( html ) )
#         report.extras = extra
#
#
# def _capture_screenshot(file_name):
#     driver.get_screenshot_as_file(file_name)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
            if not os.path.exists(reports_dir):  # Tạo folder reports nếu chưa có
                os.makedirs(reports_dir)

            # Làm sạch nodeid: Chỉ lấy tên test chính, bỏ thư mục cha (pytestsDemo/), thay :: và [ ] bằng _
            # Ví dụ: từ "pytestsDemo/test_84_Implement_Fixture.py::test_e2e[test_item1]" → "test_e2e_test_item1"
            parts = report.nodeid.split("::")
            test_file = parts[0].split("/")[-1].replace(".py", "") if len(
                parts) > 0 else ""  # Lấy tên file test (bỏ .py)
            test_name = "_".join(parts[1:]) if len(parts) > 1 else report.nodeid
            test_name = test_name.replace("[", "_").replace("]", "").replace("-", "_")  # Làm sạch dấu ngoặc và -
            clean_nodeid = f"{test_file}_{test_name}" if test_file else test_name

            file_name = os.path.join(reports_dir, clean_nodeid + ".png")

            print("file name is " + file_name)
            _capture_screenshot(file_name)
            if os.path.exists(file_name):  # Kiểm tra file tồn tại trước khi embed
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra  # Sửa nếu code gốc là extras


def _capture_screenshot(file_name):
    global driver  # Giả sử driver là global từ fixture
    if driver is not None:
        try:
            driver.get_screenshot_as_file(file_name)
            print(f"Đã chụp screenshot thành công: {file_name}")
        except Exception as e:
            print(f"Lỗi chụp screenshot: {e}")
    else:
        print("Driver is None, không chụp được.")