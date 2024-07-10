from selenium.webdriver.common.by import By
# changes CameraPage to ProductPage
class ProductPage:

    def __init__(self,driver):
        self.driver = driver
    
    title = (By.XPATH,"//div[@id='content']/h2")
    NamesLocator = (By.XPATH,"//div[@class='caption']/h4/a")
    selectColor = (By.XPATH,"//select[@id='input-option226']")
    product_title ={"camera":'Cameras',
                    "desktop":'Desktops',
                    "tablet": 'Tablets',
                    "laptop":'Laptops & Notebooks',
                    "phone":'Phones & PDAs'}
    def productName(self):
        return self.driver.find_elements(*ProductPage.NamesLocator)
    
    def productTitle(self):
        return self.driver.find_element(*ProductPage.title)
    
    def colordropdown(self):
        return self.driver.find_element(*ProductPage.selectColor)
    
    def quantity(self):
        pass

    def click_product_by_Name(self, name):
        ret_flag = False
        for product in self.productName():
            if product.text == name:
                product.click()
                ret_flag = True
                break
        return ret_flag
    
    



    
