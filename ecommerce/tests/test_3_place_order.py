import backoff
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from ecommerce.utilities.baseclass import BaseClass
from ecommerce.page_objects.home_page import HomePage
from ecommerce.page_objects.product_page import ProductDetails
from ecommerce.page_objects.product_category_page import ProductPage
from ecommerce.tests.test_2_checkout_page import CheckOutPage_Manager
from ecommerce.test_data.place_order_data import PlaceOrderParamData
from ecommerce.page_objects.shopping_cart_page import ShoppingCart
from tabulate import tabulate
import itertools
from collections import defaultdict
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
    request.cls.shoppingCartObj = ShoppingCart(driverSetUp)

@pytest.fixture(params=PlaceOrderParamData.fetch_order_data())
def placeOrderData(request):
    ''' parameterize end to end test flow with order data'''
    return request.param

class Test_PlaceOrder(BaseClass):
    '''Testing End to End Scenario : place an order for various Products'''
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
            self.verify_cart_table(placeOrderData)

        with subtests.test(msg='cart_checkout'):
            self.verifyElementPresence(self.homePage.checkout_locator)
            self.verifyElementClickable(self.homePage.checkout_locator)            
            assert self.homePage.checkoutButton()
            self.checkoutObj = self.homePage.doCheckout()  # Goto checkout page            
            page_obj = CheckOutPage_Manager(self.driver)
            page_obj.perform_checkout_process(subtests, user_type=self.CHECKOUT_OPTION)

    # Helper functions
    def select_and_add_product_to_cart(self, category, prod_data):
        ''' To select the Category of the product by click_and_check_product_category
        and selecting specific Product '''
        self.click_and_check_product_category(category)
        assert self.prodObj.click_product_by_Name(prod_data['name']), 'product OOS or unable to select requested product'
        self.fine_tune_product_attributes(prod_data)
        self.add_to_cart_click()
        self.homePage.goHome()

    
    def click_and_check_product_category(self, category):
        '''Select Product category and verifcation'''
        self.homePage.productClick(category)
        title = self.driver.title
        assert title == self.prodObj.product_title[category], f"Window Title doesnt match for {self.prodObj.product_title[category]} product category"
        actualText = self.prodObj.productTitle().text
        assert actualText == self.prodObj.product_title[category], f"Not a {self.prodObj.product_title[category]} page"

    def fine_tune_product_attributes(self, prod_data):
        '''Selecting the color and quantity of the product'''
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


    def add_to_cart_click(self):
        '''Add selected product to cart and verify alert msg'''
        self.verifyElementPresence(self.prodDetailsObj.addTocart_locator)
        self.prodDetailsObj.addtoCart()
        try:
            self.verifyElementVisiblity(self.prodDetailsObj.alert_locator, timeout=1)
        except (TimeoutException, NoSuchElementException):
            logger.warning('Alert message not displayed!')
            # pytest.xfail('looks to be bug in the web page')
        else:
            self.verifyElementVisiblity(self.prodDetailsObj.alert_locator)
            alert_msg = self.prodDetailsObj.alertmsg().text
            assert "Success" in alert_msg

        # try: # TODO
        #     self.verifyElementVisiblity(self.prodDetailsObj.alert_locator)
        #     alert_msg = self.prodDetailsObj.alertmsg().text
        #     assert "Success" in alert_msg
        # except TimeoutException:
        #     logger.warn('Alert message not displayed!')

    @staticmethod
    def parse_expected_data(placeOrderData):
        """ Parse input order data to match expected data """
        parsed_expected_data = defaultdict(int)
        for item_data in list(itertools.chain(*placeOrderData.values())):  # Flatten the input order data
             parsed_expected_data[item_data['name']] += item_data['quantity']
        return parsed_expected_data

    def verify_cart_table(self, placeOrderData):
        '''Validate product quantity in cart'''
        self.verifyElementVisiblity(self.shoppingCartObj.table_locator)
        actual_data = self.shoppingCartObj.product_quantity_details()
        expected_data = self.parse_expected_data(placeOrderData)
        table_data = []
        # [(actual_data.get(e_prod) == e_quantity) for e_prod, e_quantity in expected_data.items()]
        for e_prod, e_quantity in expected_data.items():
            a_quantity = 0  # Table defaults
            is_product_quantity_correct = False
            is_product_in_cart = e_prod in actual_data.keys() # Check expected product in Actual Cart
            assert is_product_in_cart, f'Product {e_prod} missing in cart'
            if is_product_in_cart:
                a_quantity = actual_data[e_prod]
                is_product_quantity_correct = (e_quantity == a_quantity)
                assert is_product_quantity_correct, f'Cart Quantity mismatch for Product {e_prod} Actual: {a_quantity} , expected: {e_quantity}'
            table_data.append([e_prod, e_quantity, a_quantity, is_product_quantity_correct])
        headers = ["Product Name", "Order Quantity", "Cart Quantity", "Check"]
        print("\n" + tabulate(table_data, headers, tablefmt="grid"), end='')
        logger.info(f'Cart Details: {tabulate(table_data, headers, tablefmt="grid")}')
    

@backoff.on_exception(backoff.expo, TimeoutException, max_tries=5)
def click_cart(obj: Test_PlaceOrder):  # Retry mechanism
    logger.info('Attempting to click and wait for checkout page')
    obj.homePage.cartButton().click()
    obj.verifyElementPresence(obj.homePage.checkout_locator)
