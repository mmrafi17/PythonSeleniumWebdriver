import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.home_page import Homepage
from utilities.BaseClass import BaseClass

# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def testcase1(self):
        #  //a[contains(@href,'shop')]    a[href*='shop']
        home_page = Homepage(self.driver)
        home_page.shop_items().click()
        # self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        for product in products:
            product_name = product.find_element(By.XPATH, "div/h4/a").text
            if product_name == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']").click()
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        self.verifylink('India')
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        success_text = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "Success! Thank you!" in success_text

