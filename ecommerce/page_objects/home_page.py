from selenium.webdriver.common.by import By
from ecommerce.page_objects.product_category_page import ProductPage
from ecommerce.page_objects.checkout.checkout_page import CheckOutPage

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    homePage = (By.XPATH, "//a[text()='Your Store']")
    camera = (By.XPATH,"//a[text()='Cameras']")
    # statically defined
    product_xpath ={"camera":(By.XPATH,"//a[text()='Cameras']"),
                    "desktop":(By.XPATH,"//a[text()='Desktops']"),
                    "tablet":(By.XPATH,"//a[text()='Tablets']"),
                    "laptop":(By.XPATH,"//a[text()='Laptops & Notebooks']"),
                    "phone":(By.XPATH,"//a[text()='Phones & PDAs']")}
    
    searchbar = (By.XPATH,"//div[@class= 'col-sm-5']")
    menuBar_locator = (By.XPATH,"//ul[@class= 'nav navbar-nav']/li")
    featuredLocator = (By.XPATH,"//h3")
    containerTab = (By.XPATH,"//div[@id ='top-links']/ul/li")
    cartButtonLocator = (By.XPATH,"//button[@class='btn btn-inverse btn-block btn-lg dropdown-toggle']")
    emptycartClickLocator = (By.XPATH,'//ul[@class="dropdown-menu pull-right"]/li')
    checkout_locator = (By.XPATH, "//strong/i[@class='fa fa-share']")
    home_locator = (By.XPATH,"//div[@class= 'col-sm-4']")

    def goHome(self):
        self.driver.get("http://opencart.abstracta.us:80/index.php?route=common/home")
        # self.driver.find_element(*HomePage.homePage.home_locator).click() TODO

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
    
    def productClick(self,prodName):
        self.driver.find_element(*HomePage.product_xpath[prodName]).click()
        return ProductPage(self.driver)
    
    def cartButton(self):
        return self.driver.find_element(*HomePage.cartButtonLocator)

    def checkoutButton(self):
        return self.driver.find_element(*HomePage.checkout_locator)
        
    def doCheckout(self):
        self.checkoutButton().click()
        return CheckOutPage(self.driver)








