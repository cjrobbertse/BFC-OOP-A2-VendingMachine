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


# create a product_catalogue with products and prices
# so that when a new instance of a product is created


class StockItem:
    count = 0

    def __init__(self, name, price):
        # set id to the increment of new Products
        Product.count += 1
        self.id = Product.count
        self.name = name
        self.price = price
        self.quantity = 1

    def __repr__(self):
        return f'{{id: {self.id}, name: {self.name}, price: {self.price}, quantity: {self.quantity}}}'


coke = StockItem('coke', 1.50)
print(coke)



