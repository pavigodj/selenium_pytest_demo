from selenium.webdriver.common.by import By

class CheckoutOptionsLocators:
    checkoutName_locator = (By.XPATH, "//h1[contains(text(),'Checkout')]")
    account_radio_locator = (By.XPATH,"//div[@class='radio']/label")
    guest_acc_radio_locator = (By.XPATH,"//input[@value='guest']")
    register_acc_radio_locator = (By.XPATH,"//input[@value='register']")
    checkoutlink_locator = (By.XPATH,"//a[@class='accordion-toggle']")
    continue_bttn_locator = (By.XPATH,"//input[@id='button-account']")
    input_email_locator = (By.XPATH,"//*[@id='input-email']")
    input_passwd_locator = (By.XPATH,"//*[@id='input-password']")
    login_bttn_locator = (By.XPATH,"//*[@id='button-login']")

class BillingDetailsLocators:
    firstName_locator = (By.XPATH,"//input[@id='input-payment-firstname']")
    lastName_locator = (By.XPATH,"//input[@id='input-payment-lastname']")
    email_locator = (By.XPATH,"//input[@id='input-payment-email']")
    telephone_locator = (By.XPATH,"//input[@id='input-payment-telephone']")
    address1_locator = (By.XPATH,"//input[@id='input-payment-address-1']")
    address2_locator = (By.XPATH,"//input[@id='input-payment-address-2']")
    city_locator = (By.XPATH,"//input[@id='input-payment-city']")
    postalCode_locator = (By.XPATH,"//input[@id='input-payment-postcode']")
    country_locator = (By.XPATH,"//select[@id='input-payment-country']")
    region_locator = (By.XPATH,"//select[@id='input-payment-zone']")
    continue_bttn_locator = (By.XPATH,"//input[@id='button-guest']")
    continue_bttn_locator_registered = (By.XPATH,"//input[@id='button-payment-address']")
    password_locator = (By.XPATH,"//*[@id='input-payment-password']")
    password_confirm_locator = (By.XPATH,"//*[@id='input-payment-confirm']")
    terms_agree_checkbox_locator = (By.XPATH,"//input[@name ='agree']")
    delivery_address_checkbox_locator = (By.XPATH,"//input[@name ='shipping_address']")


class DeliveryDetailsLocators:
    firstName_locator = (By.XPATH,"//input[@id='input-shipping-firstname']")
    lastName_locator = (By.XPATH,"//input[@id='input-shipping-lastname']")
    address1_locator = (By.XPATH,"//input[@id='input-shipping-address-1']")
    address2_locator = (By.XPATH,"//input[@id='input-shipping-address-2']")
    city_locator = (By.XPATH,"//input[@id='input-shipping-city']")
    postalCode_locator = (By.XPATH,"//input[@id='input-shipping-postcode']")
    country_locator = (By.XPATH,"//select[@id='input-shipping-country']")
    region_locator = (By.XPATH,"//select[@id='input-shipping-zone']")
    continue_bttn_locator = (By.XPATH,"//input[@id='button-guest-shipping']")
    continue_bttn_locator_registered = (By.XPATH,"//input[@id='button-shipping-address']")    
    delivery_address_checkbox_locator = (By.XPATH,"//input[@name ='shipping_address']")

class DeliveryMethodLocators:
    continue_bttn_locator = (By.XPATH,"//input[@id='button-shipping-method']")
    # "//input[@name ='payment_method']"

class PaymentMethodLocators:
    paymentRadio_locator = (By.XPATH,"//input[@name ='payment_method']")
    agree_checkbox_locator = (By.XPATH,"//input[@name ='agree']")
    continue_bttn_locator = (By.XPATH,"//input[@id='button-payment-method']")


class ConfirmOrderLocators:
    confirm_bttn_locator = (By.XPATH,"//input[@id='button-confirm']")
    confirm_order_locator = (By.XPATH,"//div[@id='content']/h1")

    #table content locators



