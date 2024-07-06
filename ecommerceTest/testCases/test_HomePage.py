from Utility.Baseclass import BaseClass
from selenium.webdriver.common.by import By

class Test_HomePage(BaseClass):

    def test_titleName(self):
        actualTitle = self.driver.title
        assert actualTitle == "Your Store", "Title doesnt match"
    
    def test_SelectCamera(self):
        self.driver.find_element(By.XPATH, "//div[4]//div[1]//div[3]//button[1]//span[1]").click()
        actualTitle = self.driver.title
        assert "OpenCart" in actualTitle, "Title doesnt match"

