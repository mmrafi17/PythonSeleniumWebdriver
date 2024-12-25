from selenium.webdriver.common.by import By
from pageObjects.home_page import Homepage
from utilities.BaseClass import BaseClass

class Testhomepage(BaseClass):

    def testcase1(self):
        #  //a[contains(@href,'shop')]    a[href*='shop']
        homepage = Homepage(self.driver)
        homepage.get_name().send_keys('Majin Buu')
        homepage.get_email().send_keys('majinbuu123@gmail.com')
        # self.driver.find_element(By.XPATH, "//input[@name='name']").send_keys('Majin Buu')
        # self.driver.find_element(By.XPATH, "").send_keys('Majinbuu@gmail.com')
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        success_alert = homepage.get_success_alert().text
        print(success_alert)
        assert "Success!" in success_alert

