from selenium.webdriver.common.by import By


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR,"a[href*='shop']")
    name = (By.XPATH, "//input[@name='name']")
    email = (By.XPATH, "//input[@name='email']")
    success_alert = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    products = (By.XPATH, "//div[@class='card h-100']")

    def shop_items(self):
        return self.driver.find_element(*Homepage.shop)

    def get_name(self):
        return self.driver.find_element(*Homepage.name)

    def get_email(self):
        return  self.driver.find_element(*Homepage.email)

    def get_success_alert(self):
        return self.driver.find_element(*Homepage.success_alert)

    def get_products(self):
        return self.driver.find_elements(*Homepage.products)
