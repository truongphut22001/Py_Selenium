from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.Browser_Utils import Browser_Utils


class CheckoutPage(Browser_Utils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout_button = (By.CSS_SELECTOR, ".btn-success")
        self.country_input = (By.ID, "country")
        self.term_agree_checkbox = (By.CSS_SELECTOR, ".checkbox.checkbox-primary")
        self.purchase_button = (By.CSS_SELECTOR, "input[value='Purchase']")

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def enter_delivery_address(self, country_name):
        self.driver.find_element(*self.country_input).send_keys(country_name)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, country_name)))
        self.driver.find_element(By.LINK_TEXT, country_name).click()
        self.driver.find_element(*self.term_agree_checkbox).click()
        self.driver.find_element(*self.purchase_button).click()

    def validate_order(self):
        assert "Success! Thank you! Your order will be delivered in next few weeks" in self.driver.find_element(By.CSS_SELECTOR, ".alert-success").text