class Coin:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


coins = {
    'One Penny': 0.01,
    'Two Pence': 0.02,
}

coin_quantity = 100

one_penny = Coin('One Penny', 0.01)
two_pence = Coin('Two Pence', 0.02)

coin_inventory = {
    1: {'coin': one_penny, 'quantity': 100},
    2: {'coin': two_pence, 'quantity': 100},
}

coke = Product('Coke', 1.50)
mars_bar = Product('Mars Bar', 2.00)

product_inventory = {
    1: {'product': coke, 'quantity': 10},
    2: {'product': mars_bar, 'quantity': 10}
}


class ProductInventory:
    def __init__(self):
        self.products = [
            []
        ]

    def add_product(self, product):
        self.products.a


pi = ProductInventory()
