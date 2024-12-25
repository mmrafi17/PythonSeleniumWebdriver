from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href$='/angularpractice/shop']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.XPATH, "//input[@type='checkbox']")
    dropdown = (By.ID, "exampleFormControlSelect1")
    textarea = (By.XPATH, "//input[@type='text']")
    checkboxstatus = (By.CSS_SELECTOR, "#inlineRadio1")
    submitbutton = (By.XPATH, "//input[@type='submit']")

    def getShop(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckOutPage(self.driver)
        return checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.dropdown)

    def getTextArea(self):
        return self.driver.find_element(*HomePage.textarea)

    def getStatus(self):
        return self.driver.find_element(*HomePage.checkboxstatus)

    def submitButton(self):
        return self.driver.find_element(*HomePage.submitbutton)
