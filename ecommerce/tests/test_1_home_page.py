from ecommerce.utilities.baseclass import BaseClass
from selenium.webdriver.common.by import By
from ecommerce.page_objects.home_page import HomePage
import pytest
import re
import logging
logger = logging.getLogger(__name__)


@pytest.fixture(scope="class", autouse=True)
def homePageSetUp(request,driverSetUp):
    '''Setting up HomePage'''
    driverSetUp.get("https://opencart.abstracta.us/")
    request.cls.homePage = HomePage(driverSetUp)

class Test_HomePage(BaseClass):
    '''To test HomePage attributes'''
    
    @pytest.mark.smoke
    def test_windowTitleName(self):
        '''To validate the title of window'''
        actualTitle = self.driver.title
        logger.info("'Your Store' as")
        assert actualTitle == "Your Store", "Title doesnt match"

    def test_PageTitle(self):
        '''To vadidate page header'''
        result_txt = self.homePage.homePageTitle().text
        logger.info("Title displayed on Home Page ")
        assert result_txt == "Your Store", "Home Page Headline not matching"

    def test_verify_search(self):
        '''To validate if search button is displayed and enabled for use'''
        searchlink = self.homePage.search()
        assert searchlink.is_displayed()
        assert searchlink.is_enabled()

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_verify_containers(self):
        '''To test the presence of all the containers in the menu tab'''
        self.homePage.containers()
        logger.info(f"container num = {len(self.homePage.containers())}")
        assert len(self.homePage.containers()) == 5

    @pytest.mark.smoke
    def test_validate_containers(self):
        '''To test the values of all the containers in the menu tab'''
        lst = []
        for val in self.homePage.containers():
            lst.append(val.text)
        expectedlstVal = ["My Account", "Wish List (0)" ,"Shopping Cart" , "Checkout" ]
        assert expectedlstVal.sort() == lst.sort()

    @pytest.mark.smoke
    def test_verify_CartButton(self):
        '''To validate if cart button is displayed and enabled for use'''
        assert self.homePage.cartButton().is_displayed()
        assert self.homePage.cartButton().is_enabled()

    def test_zeroItemcheckout(self):
        '''To check if alert is thrown when the cart is empty'''
        itemVal = self.homePage.cartButton().text
        item_pattern = r'(\d+)\s*item\(s\)'
        item_match = re.search(item_pattern, itemVal)
        if item_match:
            items = item_match.group(1)
        if items == 0:
            self.homePage.cartButton().click()
            actualOutput = self.driver.find_element(By.XPATH,'//ul[@class="dropdown-menu pull-right"]/li').text
            assert "Your shopping cart is empty!" == actualOutput, "Wrong response since cart is empty"

