import backoff
from selenium.common.exceptions import TimeoutException
from ecommerce.Utility.Baseclass import BaseClass
from ecommerce.page_objects.homePage import HomePage
from ecommerce.page_objects.productDetailsPage import ProductDetails
from ecommerce.page_objects.checkout.checkoutPage import CheckOutPage, AddressSubPage
from ecommerce.tests.test_2_checkout_page import CheckOutPage_Manager
import random
import pytest
import logging
logger = logging.getLogger(__name__)

@pytest.fixture(scope="class", autouse=True)
def landingPageSetUp(request,driverSetUp):
    '''Setting up HomePage'''
    driverSetUp.get("https://opencart.abstracta.us/")
    request.cls.homePage = HomePage(driverSetUp)
    request.cls.prodDetailsObj = ProductDetails(driverSetUp)

class Test_PlaceOrder(BaseClass):
    '''Testing End to End Scenario : place an order on canon Camera'''
    CHECKOUT_OPTION = 'guest'

    def test_titleName(self):
        self.prodObj = self.homePage.productClick("camera")
        title = self.driver.title
        assert title == "Cameras", "Window Title doesnt match"
    

    def test_headerName(self):
        self.prodObj = self.homePage.productClick("camera")
        actualText = self.prodObj.productTitle().text
        assert actualText == "Cameras", "Not a camera page"

    def test_cameraContent(self):
        self.prodObj = self.homePage.productClick("camera")
        cameras = self.prodObj.productName()
        for camera in cameras:
            if camera.text == "Canon EOS 5D":
                camera.click()
                break
        assert "Canon EOS 5D" in self.driver.title, "Title doesnt match"

    def test_addingCamera(self):
        dropdown_element = self.prodDetailsObj.availableOptions()
        selected_text = self.selectOptionByText(dropdown_element, "Red")
        assert selected_text == "Red", "Color selection didn't match"
    
    def test_quantity(self):
        self.prodDetailsObj.quantity().clear()
        self.prodDetailsObj.quantity().send_keys(2)
        quantity = self.prodDetailsObj.quantity().get_attribute('value')
        assert quantity.isdigit()
        assert 2 == int(quantity), "Quantity dont match"

    def test_add_to_cart_click(self):
        self.verifyElementPresence(self.prodDetailsObj.addTocart_locator)
        self.prodDetailsObj.addtoCart()
        self.verifyElementVisiblity(self.prodDetailsObj.alert_locator)
        alert_msg = self.prodDetailsObj.alertmsg().text
        assert "Success" in alert_msg

    def test_view_cart(self):
        logger.info('Attempting to click and wait for checkout page')
        # click_cart(self)
        self.homePage.cartButton().click()
        self.verifyElementPresence(self.homePage.checkout_locator)
        self.verifyElementClickable(self.homePage.checkout_locator)
        assert self.homePage.checkoutButton()
        self.checkoutObj = self.homePage.doCheckout()  # Goto checkout page

    def test_product_checkout(self, subtests):
        page_obj = CheckOutPage_Manager(self.driver)
        page_obj.perform_checkout_process(subtests, user_type='guest')

@backoff.on_exception(backoff.expo, TimeoutException, max_tries=5)
def click_cart(obj: Test_PlaceOrder):  # Retry mechanism
    logger.info('Attempting to click and wait for checkout page')
    obj.homePage.cartButton().click()
    obj.verifyElementPresence(obj.homePage.checkout_locator)