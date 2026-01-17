from typing import Self

from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage
from utils.Browser_Utils import Browser_Utils


class ShopPage(Browser_Utils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_link = (By.CSS_SELECTOR, "a[href*='shop']")
        self.phone_card = (By.CSS_SELECTOR, "app-card-list app-card")
        self.checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def add_product_to_cart(self, productname):
        self.driver.find_element(*self.shop_link).click()
        phone_list = self.driver.find_elements(*self.phone_card)
        for phone in phone_list:
            if phone.find_element(By.CSS_SELECTOR, "h4.card-title a").text == productname:
                phone.find_element(By.CSS_SELECTOR, ".card-footer button").click()
                break

    def goToCart(self):
        self.driver.find_element(*self.checkout_button).click()
        return CheckoutPage(self.driver)