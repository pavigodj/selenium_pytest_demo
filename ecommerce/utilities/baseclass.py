# import backoff
# import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class BaseClass():
    
    def verifyLinkPresence(self, value):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(By.LINK_TEXT,value))
    
    def selectOptionByText(self,locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
        return sel.first_selected_option.text
    
    def verifyElementVisiblity(self,locator, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))
         
    def verifyElementPresence(self,locator):
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(locator))
        
    def verifyElementClickable(self,locator):
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(locator))






        

