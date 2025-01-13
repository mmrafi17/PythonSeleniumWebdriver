import pytest
from selenium.webdriver.common.by import By

from pageObjects.checkout_page import CheckoutPage
from pageObjects.confirm_page import ConfirmPage
from pageObjects.home_page import Homepage
from utilities.BaseClass import BaseClass

# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def testcase1(self):
        home_page = Homepage(self.driver)
        home_page.shop_items().click()
        products = home_page.get_products()

        for product in products:
            product_name = product.find_element(By.XPATH, "div/h4/a").text
            if product_name == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        checkout_page = CheckoutPage(self.driver)
        checkout_page.get_button_primary_co().click()
        checkout_page.get_button_checkout()

        self.driver.find_element(By.ID, "country").send_keys("ind")
        self.verifylink('India')

        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        success_text = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "Success! Thank you!" in success_text
