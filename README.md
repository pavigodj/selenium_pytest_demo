# selenium_test
Demo project to show case expertise in web UI selenium test automation using pytest framework

# Summary
* The frameworks follows POM for webpages as it makes the code modular and easy to read
* The Tests focuses on performaing end to end ecommerce webpage scenario and validating the same

# Demo Website
http://opencart.abstracta.us/

# Test scenario
* verify actions, web elements, fill and validate forms in checkout page
* e2e scenario comprising [ (repeat [ product search -> add cart ] ) --> check_cart --> check_checkout_page]
* landing page elements validations

# Key functionalities
* parameterization of test scenarios
* dynamic code path for handling guest and returning users
* Fixtures and POM implementation with scale and growth
* Explicit waits to make tests more consistent
* args to switch between firefox and chrome

# Directory Structure
```
├── ecommerce
│   ├── Utility
│   │   ├── Baseclass.py
│   ├── conftest.py
│   ├── page_objects
│   │   ├── checkout
│   │   │   ├── checkoutPage.py
│   │   │   └── checkoutPagelocators.py
│   │   ├── homePage.py
│   │   ├── productDetailsPage.py
│   │   ├── productPage.py
│   │   └── shoppingCart.py
│   ├── test_data
│   │   ├── order_data.yaml
│   │   └── placeOrderData.py
│   └── tests
│       ├── test_checkout_page.py
│       ├── test_home_page.py
│       └── test_place_order.py
```

# Result
```
ecommerce/tests/test_3_place_order.py::Test_PlaceOrder::test_e2e_flow[placeOrderData0] [find_product_and_add_to_cart] SUBPASS
ecommerce/tests/test_3_place_order.py::Test_PlaceOrder::test_e2e_flow[placeOrderData0] [verify_cart] SUBPASS
ecommerce/tests/test_3_place_order.py::Test_PlaceOrder::test_e2e_flow[placeOrderData0] [checkout step1] SUBPASS
ecommerce/tests/test_3_place_order.py::Test_PlaceOrder::test_e2e_flow[placeOrderData0] [checkout step2] SUBPASS
ecommerce/tests/test_3_place_order.py::Test_PlaceOrder::test_e2e_flow[placeOrderData0] [checkout step3] SUBPASS
ecommerce/tests/test_3_place_order.py::Test_PlaceOrder::test_e2e_flow[placeOrderData0] [checkout step4] SUBPASS
ecommerce/tests/test_3_place_order.py::Test_PlaceOrder::test_e2e_flow[placeOrderData0] [checkout step5] SUBPASS
ecommerce/tests/test_3_place_order.py::Test_PlaceOrder::test_e2e_flow[placeOrderData0] [checkout step6] SUBPASS
***	Your order has been placed!	***
ecommerce/tests/test_3_place_order.py::Test_PlaceOrder::test_e2e_flow[placeOrderData0] [cart_checkout] SUBPASS
ecommerce/tests/test_3_place_order.py::Test_PlaceOrder::test_e2e_flow[placeOrderData0] PASSED
ecommerce/tests/test_3_place_order.py::Test_PlaceOrder::test_e2e_flow[placeOrderData1] [find_product_and_add_to_cart] SUBPASS
ecommerce/tests/test_3_place_order.py::Test_PlaceOrder::test_e2e_flow[placeOrderData1] [verify_cart] SUBPASS
ecommerce/tests/test_3_place_order.py::Test_PlaceOrder::test_e2e_flow[placeOrderData1] [checkout step1] SUBPASS
ecommerce/tests/test_3_place_order.py::Test_PlaceOrder::test_e2e_flow[placeOrderData1] [checkout step2] SUBPASS
ecommerce/tests/test_3_place_order.py::Test_PlaceOrder::test_e2e_flow[placeOrderData1] [checkout step3] SUBPASS
ecommerce/tests/test_3_place_order.py::Test_PlaceOrder::test_e2e_flow[placeOrderData1] [checkout step4] SUBPASS
ecommerce/tests/test_3_place_order.py::Test_PlaceOrder::test_e2e_flow[placeOrderData1] [checkout step5] SUBPASS
ecommerce/tests/test_3_place_order.py::Test_PlaceOrder::test_e2e_flow[placeOrderData1] [checkout step6] SUBPASS
***	Your order has been placed!	***
ecommerce/tests/test_3_place_order.py::Test_PlaceOrder::test_e2e_flow[placeOrderData1] [cart_checkout] SUBPASS
ecommerce/tests/test_3_place_order.py::Test_PlaceOrder::test_e2e_flow[placeOrderData1] PASSED
```
