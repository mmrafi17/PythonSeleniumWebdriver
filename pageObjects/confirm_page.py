from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country = (By.CSS_SELECTOR, "#country")
    linkTextCountry = (By.LINK_TEXT, 'Indonesia')
    radioButton = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submitButton = (By.CSS_SELECTOR, "input[type='submit']")
    anAlert = (By.CLASS_NAME, "alert-success")

    def get_country_cards(self):
        return self.driver.find_element(*ConfirmPage.country)

    def link_text(self):
        return self.driver.find_element(*ConfirmPage.linkTextCountry)

    def radio_country_button(self):
        return self.driver.find_element(*ConfirmPage.radioButton)

    def get_submit_button(self):
        return self.driver.find_element(*ConfirmPage.submitButton)

    def get_alert(self):
        return self.driver.find_element(*ConfirmPage.anAlert)
