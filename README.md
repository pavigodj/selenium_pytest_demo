# selenium_test
web UI selenium test automation using pytest framework

# Directory Structure

├── Pipfile
├── README.md
├── ecommerce
│   ├── Utility
│   │   ├── Baseclass.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── conftest.py
│   ├── page_objects
│   │   ├── __init__.py
│   │   ├── checkout
│   │   │   ├── __init__.py
│   │   │   ├── checkoutPage.py
│   │   │   └── checkoutPagelocators.py
│   │   ├── homePage.py
│   │   ├── productDetailsPage.py
│   │   ├── productPage.py
│   │   └── shoppingCart.py
│   └── tests
│       ├── test_checkout_page.py
│       ├── test_home_page.py
│       └── test_place_order.py
└── pytest.ini
