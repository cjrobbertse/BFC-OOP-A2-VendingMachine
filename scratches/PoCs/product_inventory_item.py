from dataclasses import dataclass


@dataclass
class ProductInventoryItem:
    name: str
    price: float
    quantity: int = 0


class ProductInventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.apppend(item)

    def get_item_index(self, item_name):


    def decrease_item_quantity(self, item_name, quantity):
        self.items


# input_product_id = input('Enter product id: ')
# print(product_inventory[])

products = {
    1: {'name': 'coke', 'price': 1.50},
}

selected_product = products[input('Enter product id: ')]

class Purchase:
    def select_product(self, input_product_id):
        # TODO: validate
        self.selected_product = products[input_product_id]


purchase = Purchase

purchase.select_product(input('Enter product id:'))
