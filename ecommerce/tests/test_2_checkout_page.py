# import time
import pytest
from ecommerce.Utility.Baseclass import BaseClass
from selenium.webdriver.common.by import By
import random
from ecommerce.page_objects.checkout.checkoutPage import CheckOutPage, AddressSubPage
import logging
logger = logging.getLogger(__name__)


@pytest.fixture(autouse=True)
def checkout_setup(driverSetUp):
    # prerequisite done using UI ( generally it can also be done using Backend API or mock data)
    driverSetUp.get("http://opencart.abstracta.us/index.php?route=product/category&path=24")
    driverSetUp.find_element(By.XPATH,"//div[@id='content']//div[1]//div[1]//div[2]//div[2]//button[1]").click()
    driverSetUp.get("https://opencart.abstracta.us/index.php?route=checkout/checkout")
    yield driverSetUp
    #TODO perform logout if needed

# parametrized user type
@pytest.mark.parametrize("user_type", ['guest', 'registered'])
def test_checkout_page(checkout_setup, subtests, user_type):
    ''' Parametrized Test Checkout Page to cover Guest User and Returning User'''
    mngr_obj = CheckOutPage_Manager(checkout_setup)
    mngr_obj.perform_checkout_process(subtests, user_type)

class CheckOutPage_Manager(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    def perform_checkout_process(self, subtests, user_type):
        '''To test complete flow of checkout of a product selected '''
        with subtests.test(msg='step1'):
            ''' To select the user type (guest/returning users) '''
            self.perform_checkout_option(user_type)  # step1

        for id, addr_type in enumerate(['billing', 'delivery']):  # step 2 and 3
            with subtests.test(msg=f'step{id+2}'):
                ''' For verifying billing details and delivery details '''
                self.perform_checkout_address_details(addr_type, user_type)

        with subtests.test(msg='step4'):
            ''' For verifying Delivery method selection'''
            self.checkOutPageObj.continueClick(self.checkOutPageObj.delivery_method.continue_bttn_locator).click()

        with subtests.test(msg='step5'):
            ''' For verifying Payment method selection '''
            self.checkOutPageObj.agree_terms().click()
            self.checkOutPageObj.continueClick(self.checkOutPageObj.payment_method.continue_bttn_locator).click()
        with subtests.test(msg='step6'):
            ''' '''
            self.verifyElementClickable(self.checkOutPageObj.confirm_order.confirm_bttn_locator)
            import pdb
            pdb.set_trace()
            self.checkOutPageObj.continueClick(self.checkOutPageObj.confirm_order.confirm_bttn_locator).click()

        self.verifyElementPresence(self.checkOutPageObj.confirm_order.confirm_order_locator)
        orderTxt = self.checkOutPageObj.confirm_order_txt().text
        logger.info(orderTxt)
        print(f'\n***\t{orderTxt}\t***')
        assert orderTxt == "Your order has been placed!"

    def perform_checkout_option(self, user_type):
        '''To select the user type button, if guest click 
        continue else fill in details for returning user and continue '''
        self.checkOutPageObj = CheckOutPage(self.driver)
        self.verifyElementPresence(self.checkOutPageObj.checkout_options.account_radio_locator)
        titleName = self.checkOutPageObj.checkoutName().text
        assert titleName == "Checkout", "Incorrect link"
        if user_type == "guest":
            checkout_options_str = 'Guest Checkout'
            account = self.checkOutPageObj.selectAccount(user_type)
            assert account.is_enabled(), "Expected Account type is not selected in checkout" 
            assert account.text == checkout_options_str, "Unexpected checkout options selected"
            self.checkOutPageObj.continueClick().click()            
        else:  # for returning account
            self.checkOutPageObj.loginUserName = 'bavi@y.com'
            assert self.checkOutPageObj.loginUserName == 'bavi@y.com'
            self.checkOutPageObj.loginUserPass = '123456'
            assert self.checkOutPageObj.loginUserPass == '123456'
            self.checkOutPageObj.loginButton().click()

    def perform_checkout_address_details(self, addr_type, user_type):
        ''' To fill in the Address form for returning or guest user by calling fill_addr_details function '''
        self.checkoutaddrSubPage = AddressSubPage(self.driver, addr_type)
        if user_type == 'registered':  # Returning User
            self.verifyElementClickable(self.checkoutaddrSubPage.locators.continue_bttn_locator_registered)
            self.checkoutaddrSubPage.continueClick(self.checkoutaddrSubPage.locators.continue_bttn_locator_registered).click()  # Move to next step
        else:  # Guest User
            if addr_type == 'billing':
                if random.randint(0,100) > 50:  # Randomly decides billing and delivery addr same or not
                    logger.info(f'Un-selecting same billing and delivery address checkbox')
                    self.checkoutaddrSubPage.billing_delivery_address_checkbox().click()
            else:
                if self.checkoutaddrSubPage.billing_delivery_address_checkbox().is_selected():
                    logger.info('Delivery address is same as Billing address. Skipping the checks')
                    return # Early return
                    #pytest.skip('Delivery address is same as Billing address. Skipping the checks')
            self.verifyElementPresence(self.checkoutaddrSubPage.locators.firstName_locator)
            self.fill_addr_details(addr_type,"mockData")  # TODO parameterizing data
            self.check_addr_details(addr_type,"mockData") # TODO parameterizing data
            self.verifyElementClickable(self.checkoutaddrSubPage.locators.continue_bttn_locator)
            self.checkoutaddrSubPage.continueClick().click()

    def fill_addr_details(self, addr_type, data=None):
        '''Data set up in the address fields'''
        self.checkoutaddrSubPage.firstNameEntry = 'Pavi'
        self.checkoutaddrSubPage.lastNameEntry = 'Bavi'
        if addr_type == 'billing':    
            self.checkoutaddrSubPage.emailEntry = 'BaviPavi@email.com'
            self.checkoutaddrSubPage.telephoneEntry = '8780001234'
        self.checkoutaddrSubPage.address1Entry = '456 N First St'
        self.checkoutaddrSubPage.cityEntry = 'Freemont'
        self.checkoutaddrSubPage.postalcodeEntry = '97631'
        self.checkoutaddrSubPage.countryEntry = 'United States'
        self.checkoutaddrSubPage.stateEntry = 'California'

    def check_addr_details(self, addr_type, data=None):
        '''Data assertion for address fields'''
        assert self.checkoutaddrSubPage.firstNameEntry == 'Pavi'
        assert self.checkoutaddrSubPage.lastNameEntry == 'Bavi'
        if addr_type == 'billing':    
            assert self.checkoutaddrSubPage.emailEntry == 'BaviPavi@email.com'
            assert self.checkoutaddrSubPage.telephoneEntry == '8780001234'
        assert self.checkoutaddrSubPage.address1Entry == '456 N First St'
        assert self.checkoutaddrSubPage.cityEntry == 'Freemont'                                                             
        assert self.checkoutaddrSubPage.postalcodeEntry == '97631'
        assert self.checkoutaddrSubPage.countryEntry == 'United States'  
        assert self.checkoutaddrSubPage.stateEntry == 'California'
