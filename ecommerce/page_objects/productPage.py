from selenium.webdriver.common.by import By
# changes CameraPage to ProductPage
class ProductPage:

    def __init__(self,driver):
        self.driver = driver
    
    title = (By.XPATH,"//div[@id='content']/h2")
    NamesLocator = (By.XPATH,"//div[@class='caption']/h4/a")
    selectColor = (By.XPATH,"//select[@id='input-option226']")
    
    def productName(self):
        return self.driver.find_elements(*ProductPage.NamesLocator)
    
    def productTitle(self):
        return self.driver.find_element(*ProductPage.title)
    
    def colordropdown(self):
        return self.driver.find_element(*ProductPage.selectColor)
    
    def quantity(self):
        pass
    
