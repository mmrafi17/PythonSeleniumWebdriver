import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):

    # chrome driver
    # -- Chrome

    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        service_obj = Service("D:/Automation/chromedriver-win64/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        driver.implicitly_wait(4)
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        request.cls.driver = driver
        yield
        driver.close()

