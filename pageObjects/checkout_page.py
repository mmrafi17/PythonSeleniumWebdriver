from selenium.webdriver.common.by import By

from pageObjects.confirm_page import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cards = (By.CSS_SELECTOR, "div[class='card h-100']")
    # buttonAddCO = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")
    buttonPrimary = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")
    buttonCheckout = (By.CSS_SELECTOR, "button[class='btn btn-success']")

    def get_cards(self):
        return self.driver.find_elements(*CheckoutPage.cards)

    def get_button_primary_co(self):
        return self.driver.find_element(*CheckoutPage.buttonPrimary)

    def get_button_checkout(self):
        self.driver.find_element(*CheckoutPage.buttonCheckout).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
