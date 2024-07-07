from selenium.webdriver.common.by import By
from PageObjects.cameraPage import CameraPage

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    homePage = (By.XPATH, "//a[text()='Your Store']")
    camera = (By.XPATH,"//a[text()='Cameras']")
    searchbar = (By.XPATH,"//div[@class= 'col-sm-5']")
    menuBar_locator = (By.XPATH,"//ul[@class= 'nav navbar-nav']/li")
    featuredLocator = (By.XPATH,"//h3")
    containerTab = (By.XPATH,"//div[@id ='top-links']/ul/li")
    cartButtonLocator = (By.XPATH,"//button[@class='btn btn-inverse btn-block btn-lg dropdown-toggle']")
    emptycartClickLocator = (By.XPATH,'//ul[@class="dropdown-menu pull-right"]/li')

    def homePageTitle(self):
        return self.driver.find_element(*HomePage.homePage)
    
    def search(self):
        return self.driver.find_element(*HomePage.searchbar)
    
    def containers(self):
        return self.driver.find_elements(*HomePage.containerTab)
    
    def menubar(self):
        return self.driver.find_elements(*HomePage.menuBar_locator)
    
    def feature(self):
        return self.driver.find_element(*HomePage.featuredLocator)
    
    def cameraClick(self):
        self.driver.find_element(*HomePage.camera).click()
        return CameraPage(self.driver)
    
    def cartButton(self):
        return self.driver.find_element(*HomePage.cartButtonLocator)





