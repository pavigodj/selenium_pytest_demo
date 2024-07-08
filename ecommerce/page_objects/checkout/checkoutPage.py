import ecommerce.page_objects.checkout.checkoutPagelocators as checkoutPagelocators
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_options = checkoutPagelocators.CheckoutOptionsLocators()
        self.delivery_method = checkoutPagelocators.DeliveryMethodLocators()
        self.payment_method = checkoutPagelocators.PaymentMethodLocators()
        self.confirm_order = checkoutPagelocators.ConfirmOrderLocators()

    def checkoutName(self):
        return self.driver.find_element(*self.checkout_options.checkoutName_locator)
    
    def droplink(self):
        return self.driver.find_element(*self.checkout_options.checkoutlink_locator)
    
    def selectAccount(self, checkout_option):
        accounts = self.driver.find_elements(*self.checkout_options.account_radio_locator)
        for account in accounts:
            if checkout_option in account.text.lower():  # match the correct account
                if checkout_option == 'guest':
                    account.find_element(By.XPATH,"input[@value='guest']").click()
                else:
                    account.find_element(By.XPATH,"input[@value='register']").click()
                break
        return account

    def findAccount(self):
        accounts = self.driver.find_elements(*self.checkout_options.account_radio_locator)
        for account in accounts:
            if account.find_element(By.XPATH,"input[@value=account_name]").is_selected():
                break
        return account  
    
    def agree_terms(self):
        return self.driver.find_element(*self.payment_method.agree_checkbox_locator)
    
    @property
    def loginUserName(self):
        return self.driver.find_element(*self.checkout_options.input_email_locator).get_attribute('value')
    
    @loginUserName.setter
    def loginUserName(self, value):
        self.driver.find_element(*self.checkout_options.input_email_locator).send_keys(value)
        
    @property
    def loginUserPass(self):
        return self.driver.find_element(*self.checkout_options.input_passwd_locator).get_attribute('value')

    @loginUserPass.setter
    def loginUserPass(self, value):
        self.driver.find_element(*self.checkout_options.input_passwd_locator).send_keys(value)
        
    def loginButton(self, locator=None):
        return self.driver.find_element(*self.checkout_options.login_bttn_locator)

    def continueClick(self, locator=None):
        if locator:
            return self.driver.find_element(*locator)
        else:
            return self.driver.find_element(*self.checkout_options.continue_bttn_locator)

        

class AddressSubPage:
    def __init__(self, driver, addr_type):
        self.driver = driver
        if addr_type == 'billing':
            self.locators = checkoutPagelocators.BillingDetailsLocators()
        else:
            self.locators = checkoutPagelocators.DeliveryDetailsLocators()

    @property
    def firstNameEntry(self):
        return self.driver.find_element(*self.locators.firstName_locator).get_attribute('value')
    
    @firstNameEntry.setter
    def firstNameEntry(self, value):
        self.driver.find_element(*self.locators.firstName_locator).clear()
        self.driver.find_element(*self.locators.firstName_locator).send_keys(value)

    @property
    def lastNameEntry(self):
        return self.driver.find_element(*self.locators.lastName_locator).get_attribute('value')
    
    @lastNameEntry.setter
    def lastNameEntry(self, value):
        self.driver.find_element(*self.locators.lastName_locator).clear()
        self.driver.find_element(*self.locators.lastName_locator).send_keys(value)

    @property
    def emailEntry(self):
        return self.driver.find_element(*self.locators.email_locator).get_attribute('value')
    
    @emailEntry.setter
    def emailEntry(self, value):
        self.driver.find_element(*self.locators.email_locator).clear()
        self.driver.find_element(*self.locators.email_locator).send_keys(value)

    @property
    def telephoneEntry(self):
        return self.driver.find_element(*self.locators.telephone_locator).get_attribute('value')
    
    @telephoneEntry.setter
    def telephoneEntry(self, value):
        self.driver.find_element(*self.locators.telephone_locator).clear()
        self.driver.find_element(*self.locators.telephone_locator).send_keys(value)

    @property
    def address1Entry(self):
        return self.driver.find_element(*self.locators.address1_locator).get_attribute('value')
    
    @address1Entry.setter
    def address1Entry(self, value):
        self.driver.find_element(*self.locators.address1_locator).clear()
        self.driver.find_element(*self.locators.address1_locator).send_keys(value)

    @property
    def address2Entry(self):
        return self.driver.find_element(*self.locators.address2_locator).get_attribute('value')

    @address2Entry.setter
    def address2Entry(self, value):
        self.driver.find_element(*self.locators.address2_locator).clear()
        self.driver.find_element(*self.locators.address2_locator).send_keys(value)

    @property
    def cityEntry(self):
        return self.driver.find_element(*self.locators.city_locator).get_attribute('value')

    @cityEntry.setter
    def cityEntry(self, value):
        self.driver.find_element(*self.locators.city_locator).clear()
        self.driver.find_element(*self.locators.city_locator).send_keys(value)

    @property
    def postalcodeEntry(self):
        return self.driver.find_element(*self.locators.postalCode_locator).get_attribute('value')
    
    @postalcodeEntry.setter
    def postalcodeEntry(self, value):
        self.driver.find_element(*self.locators.postalCode_locator).clear()
        self.driver.find_element(*self.locators.postalCode_locator).send_keys(value)

    @property        
    def countryEntry(self):
        web_obj = self.driver.find_element(*self.locators.country_locator)
        sel_obj = Select(web_obj)
        return sel_obj.first_selected_option.text

    @countryEntry.setter        
    def countryEntry(self, value):
        web_obj = self.driver.find_element(*self.locators.country_locator)
        sel_obj = Select(web_obj)
        sel_obj.select_by_visible_text(value)

    @property        
    def stateEntry(self):
        web_obj = self.driver.find_element(*self.locators.region_locator)
        sel_obj = Select(web_obj)
        return sel_obj.first_selected_option.text

    @stateEntry.setter        
    def stateEntry(self, value):
        web_obj = self.driver.find_element(*self.locators.region_locator)
        sel_obj = Select(web_obj)
        sel_obj.select_by_visible_text(value)

    @property
    def passwordEntry(self):
        return self.driver.find_element(*self.locators.password_locator).get_attribute('value')
    
    @passwordEntry.setter
    def passwordEntry(self, value):
        self.driver.find_element(*self.locators.password_locator).clear()
        self.driver.find_element(*self.locators.password_locator).send_keys(value)

    @property
    def confirmPassEntry(self):
        return self.driver.find_element(*self.locators.password_confirm_locator).get_attribute('value')
    
    @confirmPassEntry.setter
    def confirmPassEntry(self, value):
        self.driver.find_element(*self.locators.password_confirm_locator).clear()
        self.driver.find_element(*self.locators.password_confirm_locator).send_keys(value)

    def billing_delivery_address_checkbox(self):
        return self.driver.find_element(*self.locators.delivery_address_checkbox_locator)

    def terms_agree_checkbox(self):
        return self.driver.find_element(*self.locators.terms_agree_checkbox_locator)
        
    def continueClick(self, locator=None):
        if locator:
            return self.driver.find_element(*locator)
        else:
            return self.driver.find_element(*self.locators.continue_bttn_locator)
    






    
