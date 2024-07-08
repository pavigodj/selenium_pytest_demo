import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="firefox", help="my option: chrome or firefox"
    )

@pytest.fixture(scope="class")
def driverSetUp(request):
    browserName = request.config.getoption("browser")
    print(browserName)
    if browserName == "firefox":
        options_obj = webdriver.FirefoxOptions()
        #certfication error handling, maximizing screen, making browser headless
        options_obj.add_argument("--ignore-certification-errors")
        service_obj = Service("/Users/bavi/Downloads/geckodriver 3")
        driver = webdriver.Firefox(service=service_obj, options=options_obj)
    elif browserName == "chrome":
        options_obj = Options()
        options_obj.add_argument('--headless=new')
        #certfication error handling, maximizing screen, making browser headless
        options_obj.add_argument("--ignore-certification-errors")
        driver = webdriver.Chrome(options=options_obj)                                  
    request.cls.driver = driver
    # driver.get("https://opencart.abstracta.us/")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def driverSetUp_2(request):
    browserName = request.config.getoption("browser")
    print(browserName)
    if browserName == "firefox":
        options_obj = webdriver.FirefoxOptions()
        #certfication error handling, maximizing screen, making browser headless
        options_obj.add_argument("--ignore-certification-errors")
        service_obj = Service("/Users/bavi/Downloads/geckodriver 3")
        driver = webdriver.Firefox(service=service_obj, options=options_obj)
    elif browserName == "chrome":
        options_obj = Options()
        options_obj.add_argument('--headless=new')
        #certfication error handling, maximizing screen, making browser headless
        options_obj.add_argument("--ignore-certification-errors")
        driver = webdriver.Chrome(options=options_obj)                                  
    request.cls.driver = driver
    # driver.get("https://opencart.abstracta.us/")
    driver.maximize_window()
    yield driver
    driver.quit()

