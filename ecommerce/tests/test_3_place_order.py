import backoff
from selenium.common.exceptions import TimeoutException
from ecommerce.Utility.Baseclass import BaseClass
from ecommerce.page_objects.homePage import HomePage
from ecommerce.page_objects.productDetailsPage import ProductDetails
from ecommerce.page_objects.productPage import ProductPage
from ecommerce.tests.test_2_checkout_page import CheckOutPage_Manager
from ecommerce.test_data.placeOrderData import PlaceOrderParamData
import pytest
import logging
logger = logging.getLogger(__name__)

@pytest.fixture(scope="class", autouse=True)
def landingPageSetUp(request,driverSetUp):
    '''Setting up HomePage'''
    driverSetUp.get("https://opencart.abstracta.us/")
    request.cls.homePage = HomePage(driverSetUp)
    request.cls.prodObj = ProductPage(driverSetUp)
    request.cls.prodDetailsObj = ProductDetails(driverSetUp)

@pytest.fixture(params=PlaceOrderParamData.order_data)
def placeOrderData(request):
    ''' parameterize end to end test flow with order data'''
    return request.param

class Test_PlaceOrder(BaseClass):
    '''Testing End to End Scenario : place an order on canon Camera'''
    CHECKOUT_OPTION = 'guest'

    def test_e2e_flow(self, subtests, placeOrderData):
        with subtests.test(msg='find_product_and_add_to_cart'):
            for category, products in placeOrderData.items():
                for prod_data in products:
                    self.select_and_add_product_to_cart(category, prod_data)
        with subtests.test(msg='verify_cart'):
            logger.info('Attempting to click and wait for checkout page')
            # click_cart(self)
            self.homePage.cartButton().click()
            self.verifyElementPresence(self.homePage.checkout_locator)
            self.verifyElementClickable(self.homePage.checkout_locator)
            assert self.homePage.checkoutButton()
            self.checkoutObj = self.homePage.doCheckout()  # Goto checkout page
        with subtests.test(msg='cart_checkout'):
            page_obj = CheckOutPage_Manager(self.driver)
            page_obj.perform_checkout_process(subtests, user_type=self.CHECKOUT_OPTION)

    # Helper functions
    def select_and_add_product_to_cart(self, category, prod_data):
        self.click_and_check_product_category(category)
        assert self.prodObj.click_product_by_Name(prod_data['name']), 'product OOS or unable to select requested product'
        self.fine_tune_product_attributes(prod_data)
        self.add_to_cart_click()
        self.homePage.goHome()

    def fine_tune_product_attributes(self, prod_data):
        if prod_data.get('color', None):
            dropdown_element = self.prodDetailsObj.availableOptions()
            selected_text = self.selectOptionByText(dropdown_element, prod_data['color'])
            assert selected_text == prod_data['color'], "Color selection didn't match for product {prod_data['name']"
        if prod_data.get('quantity', None):
            self.prodDetailsObj.quantity().clear()
            self.prodDetailsObj.quantity().send_keys(prod_data['quantity'])
            quantity = self.prodDetailsObj.quantity().get_attribute('value')
            assert quantity.isdigit()
            assert prod_data['quantity'] == int(quantity), f"Quantity dont match for product {prod_data['name']}"        

    def click_and_check_product_category(self, category):
        self.homePage.productClick(category)
        title = self.driver.title
        assert title == self.prodObj.product_title[category], f"Window Title doesnt match for {self.prodObj.product_title[category]} product category"
        actualText = self.prodObj.productTitle().text
        assert actualText == self.prodObj.product_title[category], f"Not a {self.prodObj.product_title[category]} page"

    def add_to_cart_click(self):
        self.verifyElementPresence(self.prodDetailsObj.addTocart_locator)
        self.prodDetailsObj.addtoCart()
        # TODO fix this
        # self.verifyElementVisiblity(self.prodDetailsObj.alert_locator)
        # alert_msg = self.prodDetailsObj.alertmsg().text
        # assert "Success" in alert_msg

@backoff.on_exception(backoff.expo, TimeoutException, max_tries=5)
def click_cart(obj: Test_PlaceOrder):  # Retry mechanism
    logger.info('Attempting to click and wait for checkout page')
    obj.homePage.cartButton().click()
    obj.verifyElementPresence(obj.homePage.checkout_locator)