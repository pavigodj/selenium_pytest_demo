# selenium_test
Demo project to show case expertise in web UI selenium test automation using pytest framework

# Summary
* The frameworks follows POM for webpages as it makes the code modular and easy to read
* The Tests focuses on performaing end to end ecommerce webpage scenario and validating the same

# Demo Website
http://opencart.abstracta.us/

# Test scenario
* Landing Page validation
* Check out Page Testing: verify actions, web elements, fill and validate forms in checkout page
* Product Order Testing: e2e scenario comprising [ (repeat [ product search -> add cart ] ) --> check_cart --> check_checkout_page]  

# Key functionalities
* Parameterization of test scenarios(various Products along with other attributes for placing order)
* Dynamic code path for handling guest and returning users in checkout page
* Fixtures and POM implementation with scale and growth
* Explicit waits to make tests more consistent (Base class in utility)
* args to switch between firefox and chrome (in CLI)

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
+----------------+------------------+-----------------+---------+
| Product Name   |   Order Quantity |   Cart Quantity | Check   |
+================+==================+=================+=========+
| Canon EOS 5D   |                1 |               1 | True    |
+----------------+------------------+-----------------+---------+
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
+-------------------------+------------------+-----------------+---------+
| Product Name            |   Order Quantity |   Cart Quantity | Check   |
+=========================+==================+=================+=========+
| Canon EOS 5D            |                7 |               7 | True    |
+-------------------------+------------------+-----------------+---------+
| Nikon D300              |                7 |               7 | True    |
+-------------------------+------------------+-----------------+---------+
| iPhone                  |                2 |               2 | True    |
+-------------------------+------------------+-----------------+---------+
| HTC Touch HD            |                6 |               6 | True    |
+-------------------------+------------------+-----------------+---------+
| Samsung Galaxy Tab 10.1 |                9 |               9 | True    |
+-------------------------+------------------+-----------------+---------+
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
