from Utility.Baseclass import BaseClass
from selenium.webdriver.common.by import By
from PageObjects.HomePage import HomePage
import pytest
import re
import logging
logger = logging.getLogger(__name__)

class Test_HomePage(BaseClass):
#creating homePage object once for each testcases in setUp method
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.homePage = HomePage(self.driver)
    
    @pytest.mark.smoke
    def test_windowTitleName(self):
        actualTitle = self.driver.title
        logger.info("test_windowtitleName")
        assert actualTitle == "Your Store", "Title doesnt match"

    def test_PageTitle(self):
        result_txt = self.homePage.homePageTitle().text
        logger.info("test_PageTitle")
        assert result_txt == "Your Store", "Home Page Headline not matching"

    def test_verify_search(self):
        searchlink = self.homePage.search()
        assert searchlink.is_displayed()
        assert searchlink.is_enabled()


    @pytest.mark.smoke
    def test_verify_containers(self):
        self.homePage.containers()
        logger.info(f"container num = {len(self.homePage.containers())}")
        assert len(self.homePage.containers()) == 5

    @pytest.mark.smoke
    def test_validate_containers(self):
        lst = []
        for val in self.homePage.containers():
            lst.append(val.text)
        expectedlstVal = ["My Account", "Wish List (0)" ,"Shopping Cart" , "Checkout" ]
        assert expectedlstVal.sort() == lst.sort()

    @pytest.mark.smoke
    def test_verify_CartButton(self):
        assert self.homePage.cartButton().is_displayed()
        assert self.homePage.cartButton().is_enabled()

    def test_zeroItemcheckout(self):
        itemVal = self.homePage.cartButton().text
        item_pattern = r'(\d+)\s*item\(s\)'
        item_match = re.search(item_pattern, itemVal)
        if item_match:
            items = item_match.group(1)
        if items == 0:
            self.homePage.cartButton().click()
            actualOutput = self.driver.find_element(By.XPATH,'//ul[@class="dropdown-menu pull-right"]/li').text
            assert "Your shopping cart is empty!" == actualOutput, "Wrong response since cart is empty"

    
    # testing by directly selecting the Product from HomePage
    # def test_SelectCamera(self):
    #     self.driver.find_element(By.XPATH, "//div[4]//div[1]//div[3]//button[1]//span[1]").click()
    #     actualTitle = self.driver.title
    #     assert "OpenCart" in actualTitle, "Title doesnt match"

