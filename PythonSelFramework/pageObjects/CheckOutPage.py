from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cards = (By.CSS_SELECTOR, "div[class='card h-100']")
    # buttonAddCO = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")
    buttonPrimary = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")
    buttonCheckout = (By.CSS_SELECTOR, "button[class='btn btn-success']")

    def getCards(self):
        return self.driver.find_elements(*CheckOutPage.cards)

    def getButtonPrimaryCO(self):
        return self.driver.find_element(*CheckOutPage.buttonPrimary)

    def getButtonCheckout(self):
        self.driver.find_element(*CheckOutPage.buttonCheckout).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
