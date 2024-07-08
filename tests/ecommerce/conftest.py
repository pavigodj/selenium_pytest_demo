import pytest
from tests.ecommerce.page_objects.checkout.checkoutPage import CheckOutPage
from tests.ecommerce.page_objects.homePage import HomePage

@pytest.fixture(scope="class")
def checkoutPage(driverSetUp):
    # TODO do UI / Backend Setup for checkout page
    yield CheckOutPage(driverSetUp)



