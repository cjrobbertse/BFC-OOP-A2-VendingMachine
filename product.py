class Product:
    """Product class contains name and value of product as attributes"""
    def __init__(self, name, price):
        """constructor takes name and price of product"""
        self.name = name
        self.price = price


class ProductInventory:
    """ProductInventory is a management of products."""
    # NOTE: could be used to handle stock or other product inventory functions in the future with more business
    #       use cases.
    def __init__(self, products):
        self.products = products
