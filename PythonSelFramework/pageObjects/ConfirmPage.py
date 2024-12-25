from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country = (By.CSS_SELECTOR, "#country")
    linkTextCountry = (By.LINK_TEXT, 'Indonesia')
    radioButton = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submitButton = (By.CSS_SELECTOR, "input[type='submit']")
    anAlert = (By.CLASS_NAME, "alert-success")

    def getCountryCards(self):
        return self.driver.find_element(*ConfirmPage.country)

    def linkText(self):
        return self.driver.find_element(*ConfirmPage.linkTextCountry)

    def radioCountryButton(self):
        return self.driver.find_element(*ConfirmPage.radioButton)

    def getSubmitButton(self):
        return self.driver.find_element(*ConfirmPage.submitButton)

    def getAlert(self):
        return self.driver.find_element(*ConfirmPage.anAlert)
