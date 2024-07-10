import yaml
from pathlib import Path
class PlaceOrderParamData:
    @classmethod
    def fetch_order_data(self):
        try:
            with open(Path('/Users/bavi/selenium_pytest_demo/selenium_pytest_demo/ecommerce/test_data/order_data.yaml')) as fp:
                PlaceOrderParamData.order_data = yaml.load(fp, Loader=yaml.FullLoader)
        except:
            PlaceOrderParamData.order_data
        return PlaceOrderParamData.order_data

    # Default value for exception handling
    order_data = [
        {
            'camera': [
                {'color': 'Blue', 'name': 'Canon EOS 5D', 'quantity': 1}
            ]
        },        
        {
            'camera': [
                {'color': 'Red', 'name': 'Canon EOS 5D', 'quantity': 2},
                {'color': 'Blue', 'name': 'Canon EOS 5D', 'quantity': 5},
                {'name': 'Nikon D300', 'quantity': 7}
            ],
            'phone': [
                {'name': 'iPhone', 'quantity': 2},
                {'name': 'HTC Touch HD', 'quantity': 6}
            ],
            'tablet': [
                {'name': 'Samsung Galaxy Tab 10.1', 'quantity': 9}
            ]
        }
    ]