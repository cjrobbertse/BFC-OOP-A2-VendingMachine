COIN_NAMES = {
    'One Penny',
    'Two Pence',
    'Five Pence',
    'Ten Pence',
    'Twenty Pence',
    'Fifty Pence',
    'One Pound',
    'Two Pounds',
}

from abc import ABC, abstractmethod


class Coin(ABC):
    @abstractmethod
    def __init__(self, value=None):
        self.value = value


class OnePenny(Coin):
    def __init__(self):
        super().__init__(0.01)


class TwoPence(Coin):
    def __init__(self):
        super().__init__(0.02)


class FivePence(Coin):
    def __init__(self):
        super().__init__(0.05)


class TenPence(Coin):
    def __init__(self):
        super().__init__(0.10)


class TwentyPence(Coin):
    def __init__(self):
        super().__init__(0.20)


class FiftyPence(Coin):
    def __init__(self):
        super().__init__(0.50)


class OnePound(Coin):
    def __init__(self):
        super().__init__(1.00)


class TwoPounds(Coin):
    def __init__(self):
        super().__init__(2.00)


class Product:
    count = 0

    def __init__(self, name, price):
        # set id to the increment of new Products
        Product.count += 1
        self.id = Product.count
        self.name = name
        self.price = price

    def __repr__(self):
        return f'{{id: {self.id}, name: {self.name}, price: {self.price}}}'


class VendingMachine:
    def __init__(self, products, coin_inventory):
        # insert products and coin inventory as technician might do.
        self.product_inventory = products
        self.coin_inventory = coin_inventory

    @staticmethod
    def display_welcome_message():
        print("Hello and welcome to Christopher J. Robbertse's vending machine.")

    def display_menu(self):
        self.product_inventory


input_products = {}  # TODO: populate with 10 of each product
input_coin_inventory = {key: [] for key in COIN_NAMES}  # TODO: populate with 100 of each coin

vending_machine = VendingMachine(input_products, input_coin_inventory)

vending_machine.display_welcome_message()
vending_machine.display_menu()

