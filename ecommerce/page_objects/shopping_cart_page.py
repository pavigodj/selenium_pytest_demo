from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import re
import logging
from tabulate import tabulate
from collections import defaultdict
logger = logging.getLogger(__name__)
class ShoppingCart:
    
    def __init__(self, driver):
        self.driver = driver
    
    table_locator = (By.XPATH, "//tr")
    productNames_locator = (By.XPATH,".//td[@class='text-left']/a")
    productquantity_locator = (By.XPATH,".//td[@class='text-right'][1]")

    def product_quantity_details(self):
        tableStruct = self.driver.find_elements(*ShoppingCart.table_locator)
        prodQuantDict = defaultdict(int)
        for row in tableStruct:
            try:
                prod = row.find_element(*ShoppingCart.productNames_locator).text
                quantstr = row.find_element(*ShoppingCart.productquantity_locator).text
                quant = re.findall(r'\d+', quantstr)
                prodQuantDict[prod] += int(quant[0])
            except NoSuchElementException as e:
                logger.info('Fetched all the Product details')
                break
        return prodQuantDict
    
