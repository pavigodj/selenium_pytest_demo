import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="firefox", help="my option: chrome or firefox"
    )

@pytest.fixture(scope="class")
def driverSetUp(request):
    # Setup
    browserName = request.config.getoption("browser")
    if browserName == "firefox":
        options_obj = webdriver.FirefoxOptions()
        #certfication error handling, maximizing screen, making browser headless
        options_obj.add_argument("--ignore-certification-errors")
        service_obj = FirefoxService("/Users/bavi/Downloads/geckodriver 3")
        driver = webdriver.Firefox(service=service_obj, options=options_obj)
    elif browserName == "edge":
        options_obj = webdriver.EdgeOptions()
        options_obj.add_argument("--ignore-certificate-errors")
        options_obj.add_argument("--guest")
        service_obj = EdgeService("/Users/bavi/Downloads/msedgedriver")
        driver = webdriver.Edge(service=service_obj, options=options_obj)        
    elif browserName == "chrome":
        chromedriver_path = "/Users/bavi/Downloads/chromedriver"
        options_obj = webdriver.ChromeOptions()
        options_obj.add_argument("--ignore-certificate-errors")
        options_obj.add_argument("--guest")
        service = ChromeService(chromedriver_path)
        driver = webdriver.Chrome(service=service, options=options_obj)
    if request.cls:  # Skip for testcase which is not a class
        request.cls.driver = driver
    driver.maximize_window()
    yield driver
    # Cleanup
    driver.quit()