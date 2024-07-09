import yaml

class PlaceOrderParamData:
    @classmethod
    def fetch_order_data():
        try:
            with open('order_data.yaml') as fp:
                PlaceOrderParamData.order_data = yaml.load(fp)
        except:
            PlaceOrderParamData.order_data
        return PlaceOrderParamData.order_data

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

