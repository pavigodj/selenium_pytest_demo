from selenium.webdriver.common.by import By

class ProductDetails:

    def __init__(self,driver):
        self.driver = driver
    
    optionsDropdown = (By.XPATH, "//select[@id='input-option226']")
    quantity_locator = (By.XPATH,"//input[@id='input-quantity']")
    addTocart_locator = (By.XPATH,"//button[@id='button-cart']")
    alert_locator = (By.XPATH,"//div[@class='alert alert-success alert-dismissible']")

    def availableOptions(self):
        # self.driver.find_element(By.XPATH, "//select[@id='input-option226']")
        return self.driver.find_element(*ProductDetails.optionsDropdown)
    
    def quantity(self):
        return self.driver.find_element(*ProductDetails.quantity_locator)

    def addtoCartButton(self):
        return self.driver.find_element(*ProductDetails.addTocart_locator)

    def addtoCart(self):
        self.driver.find_element(*ProductDetails.addTocart_locator).click()

    def alertmsg(self):
        return self.driver.find_element(*ProductDetails.alert_locator)
        

    

    