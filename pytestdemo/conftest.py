import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):

    # chrome driver
    # -- Chrome
    # service_obj = Service("/Users/MRF/Downloads/Compressed/chromedriver-win64/chromedriver.exe")
    # driver = webdriver.Chrome(service=service_obj)
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(4)
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        request.cls.driver = driver
        yield
        driver.close()

