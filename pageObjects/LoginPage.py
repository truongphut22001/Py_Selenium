from selenium.webdriver.common.bidi.browser import Browser
from selenium.webdriver.common.by import By

from pageObjects.ShopPage import ShopPage
from utils.Browser_Utils import Browser_Utils


class LoginPage(Browser_Utils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.term_checkbox = (By.ID, "terms")
        self.sign_in_button = (By.ID, "signInBtn")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.term_checkbox).click()
        self.driver.find_element(*self.sign_in_button).click()
        return ShopPage(self.driver)
