import backoff
from selenium.common.exceptions import TimeoutException
from ecommerce.Utility.Baseclass import BaseClass
from ecommerce.page_objects.homePage import HomePage
from ecommerce.page_objects.productDetailsPage import ProductDetails
from ecommerce.page_objects.checkout.checkoutPage import CheckOutPage, AddressSubPage
import random
import pytest
import logging
logger = logging.getLogger(__name__)

class Test_PlaceOrder(BaseClass):
    '''Testing End to End Scenario : place an order on canon Camera'''
    CHECKOUT_OPTION = 'guest'
    @pytest.fixture(autouse=True)
    def setUp(self):
        self.homePage = HomePage(self.driver)
        
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
        self.prodDetailsObj = ProductDetails(self.driver)
        dropdown_element = self.prodDetailsObj.availableOptions()
        selected_text = self.selectOptionByText(dropdown_element, "Red")
        assert selected_text == "Red", "Color selection didn't match"
    
    def test_quantity(self):
        self.prodDetailsObj = ProductDetails(self.driver)
        self.prodDetailsObj.quantity().clear()
        self.prodDetailsObj.quantity().send_keys(2)
        quantity = self.prodDetailsObj.quantity().get_attribute('value')
        assert quantity.isdigit()
        assert 2 == int(quantity), "Quantity dont match"

    def test_add_to_cart_click(self):
        self.prodDetailsObj = ProductDetails(self.driver)
        self.prodDetailsObj.addtoCart()
        self.verifyElementPresence(self.prodDetailsObj.alert_locator)
        alert_msg = self.prodDetailsObj.alertmsg().text
        assert "Success" in alert_msg

    def test_view_cart(self):
        self.prodDetailsObj = ProductDetails(self.driver)
        logger.info('Attempting to click and wait for checkout page')
        # click_cart(self)
        self.homePage.cartButton().click()
        self.verifyElementPresence(self.homePage.checkout_locator)
        assert self.homePage.checkoutButton()
        self.checkoutObj = self.homePage.doCheckout()  # Goto checkout page

    def test_checkout_option(self):
        self.checkOutPageObj = CheckOutPage(self.driver)
        self.verifyElementPresence(self.checkOutPageObj.checkout_options.account_radio_locator)
        titleName = self.checkOutPageObj.checkoutName().text
        assert titleName == "Checkout", "Incorrect link"
        checkout_options_str = 'Guest Checkout'
        account = self.checkOutPageObj.selectAccount('guest')
        assert account.is_enabled(), "Expected Account type is not selected in checkout" 
        assert account.text == checkout_options_str, "Unexpected checkout options selected"
        self.checkOutPageObj.continueClick().click()

    @pytest.mark.parametrize("addr_type", ['billing', 'delivery'])
    def test_checkout_address_details(self, subtests, addr_type):
        if addr_type == 'billing':
            self.checkoutaddrSubPage = AddressSubPage(self.driver, addr_type)
            if random.randint(0,100) > 50:  # Randomly decides billing and delivery addr same or not
                logger.info(f'Un-selecting same billing and delivery address checkbox')
                self.checkoutaddrSubPage.billing_delivery_address_checkbox().click()
        else:
            self.checkoutaddrSubPage = AddressSubPage(self.driver, addr_type)
            if self.checkoutaddrSubPage.billing_delivery_address_checkbox().is_selected():
                pytest.skip('Delivery address is same as Billing address. Skipping the checks')
        with subtests.test(msg="FirstName"):
            self.checkoutaddrSubPage.firstNameEntry = 'Pavi'
            assert self.checkoutaddrSubPage.firstNameEntry == 'Pavi'
        with subtests.test(msg="LastName"):
            self.checkoutaddrSubPage.lastNameEntry = 'Bavi'
            assert self.checkoutaddrSubPage.lastNameEntry == 'Bavi'
        if addr_type == 'billing':    
            with subtests.test(msg="Email"):
                self.checkoutaddrSubPage.emailEntry = 'BaviPavi@email.com'
                assert self.checkoutaddrSubPage.emailEntry == 'BaviPavi@email.com'
            with subtests.test(msg="Telephone"):
                self.checkoutaddrSubPage.telephoneEntry = '8780001234'
                assert self.checkoutaddrSubPage.telephoneEntry == '8780001234'
        with subtests.test(msg="Address"):
            self.checkoutaddrSubPage.address1Entry = '456 N First St'
            assert self.checkoutaddrSubPage.address1Entry == '456 N First St'
        with subtests.test(msg="City"):
            self.checkoutaddrSubPage.cityEntry = 'Freemont'
            assert self.checkoutaddrSubPage.cityEntry == 'Freemont'                                                             
        with subtests.test(msg="Zip"):
            self.checkoutaddrSubPage.postalcodeEntry = '97631'
            assert self.checkoutaddrSubPage.postalcodeEntry == '97631'
        with subtests.test(msg="Country"):
            self.checkoutaddrSubPage.countryEntry = 'United States'
            assert self.checkoutaddrSubPage.countryEntry == 'United States'  
        with subtests.test(msg="State"):
            self.checkoutaddrSubPage.stateEntry = 'California'
            assert self.checkoutaddrSubPage.stateEntry == 'California'
        if addr_type == 'billing' and Test_PlaceOrder.CHECKOUT_OPTION == 'register':
            with subtests.test(msg="Password"):
                self.checkoutaddrSubPage.passwordEntry = '12345678'
                assert self.checkoutaddrSubPage.passwordEntry == '12345678'
            with subtests.test(msg="ConfirmPass"):
                self.checkoutaddrSubPage.confirmPassEntry = '12345678'
                assert self.checkoutaddrSubPage.confirmPassEntry == '12345678' 
            self.checkoutaddrSubPage.terms_agree_checkbox().click()
            self.checkoutaddrSubPage.continueClick(self.checkoutaddrSubPage.locators.continue_bttn_locator_register).click()
        else:                                                     
            self.checkoutaddrSubPage.continueClick().click()


@backoff.on_exception(backoff.expo, TimeoutException, max_tries=1)
def click_cart(obj: Test_PlaceOrder):  # Retry mechanism
    logger.info('Attempting to click and wait for checkout page')
    obj.homePage.cartButton().click()
    obj.verifyElementPresence(obj.homePage.checkout_locator)

@pytest.fixture(scope="class", autouse=True)
def getUrl(driverSetUp):
    driverSetUp.get("https://opencart.abstracta.us/")
