import time
from Utility.Baseclass import BaseClass
from page_objects.HomePage import HomePage
from page_objects.productDetailsPage import ProductDetails
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest 
# from selenium.webdriver.support.select import Select

class Test_CameraPage(BaseClass):
    '''Testing to place an order on canon Camera'''

    @pytest.fixture(autouse=True)
    def setUp(self):
        self.homePage = HomePage(self.driver)
        # self.prodObj = self.homePage.productClick("camera")
    
    # @pytest.fixture(autouse=True)
    # def setUp_prodPage(self):
    #     self.prodDetailsObj = ProductDetails(self.driver)
        
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
        # import pdb
        # pdb.set_trace()
        self.verifyElementPresence(self.prodDetailsObj.alert_locator)
        alert_msg = self.prodDetailsObj.alertmsg().text
        assert "Success" in alert_msg

    def test_view_cart(self):
        self.prodDetailsObj = ProductDetails(self.driver)
        self.homePage.cartButton().click()
        
        




