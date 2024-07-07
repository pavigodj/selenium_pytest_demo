import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("driverSetUp")
class BaseClass():
    
    def verifyLinkPresence(self, value):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(By.LINK_TEXT,value))
    
    def selectOptionByText(self,locator, text):
        print(locator)
        sel = Select(locator)
        sel.select_by_visible_text(text)
        # print(sel)
        return sel.first_selected_option.text
    
    def verifyElementPresence(self,value):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(value))


        

