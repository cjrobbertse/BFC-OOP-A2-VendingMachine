# Magical Virtual Vending Machine

## About

- **College**: Blackpool and the Flyde College
- **Subject**: Object-Oriented Programming
- **Assessment Number**: 2
- **Author**: Christopher Robbertse

## Program Requirements

- `Python3`: The program WILL NOT WORK with older versions of Python.

## UML

### Use Case Diagrams

 - [`UML/Use Case Diagrams/VendingMachine Simplified.png`](UML/Use Case Diagrams/VendingMachine Simplified.png)

### Activity Diagrams

 - [`UML/Activity Diagram/Welcome.png`](UML/Activity Diagram/Welcome.png)
 - [`UML/Activity Diagram/DisplayProducts.png`](UML/Activity Diagram/DisplayProducts.png)
 - [`UML/Activity Diagram/SelectProduct.png`](UML/Activity Diagram/SelectProduct.png)
 - [`UML/Activity Diagram/PayForProduct.png`](UML/Activity Diagram/PayForProduct.png)

### Class Diagrams

 - [`UML/Class Diagrams/Coins.png`](UML/Class Diagrams/Coins.png)
 - [`UML/Class Diagrams/Classes.png`](UML/Class Diagrams/Classes.png)
 
## Assessment Technical Requirements

 - Abstract parent class: `Coin`
 - Child classes: `OnePenny`, `TwoPenny`, etc.
 - Abstract method: `Coin.__init__`.
 - Static method: `Coin.create_coin_class`.
 - Property methods:
   - `PurchaseHandler.remaining_to_pay`
   - `PurchaseHandler.sum`
 - Class methods: `VendingMachine.display_menu` and more.
 - Class attribute: `CoinFactory.COIN_VALUES`.
 - Instance attributes: `product.name`
   - `product.price`
   - `product_inventory.products`
   - and more
 - Polymorphism: `Coin`'s child classes override the value in its constructor.
 - Dictionaries: `ProductInventory.products` and `CoinPot.coins`
 - List: `CoinPot.coins[coin_value]`
 - Importation of modules: 
   - `import ABC (abstract class) and abstractmethod` in `coins.py`
   - `import CoinFactory` in `purchase_handler.py`
   - `import Product and ProductInventory` in `main.py`
   - `import PurchaseHandler` in `main.py`
 - Constructors: 
   - `VendingMachine.__init__(self, welcome_message, product_inventory)`
   - `PurchaseHandler.__init__(self, product)`
   - `CoinPot.__init__(self)`
   - `Product.__init__(self, name, price)`
   - `ProductInvetory.__init__(self, products)`
   - and more
 - Super Constructors:
   - `FivePence, super().__init__(0.05)`
   - `TenPence, super().__init__(0.10)`
   - etc.
 - Doc strings used under every class, and comments general comments throughout.
 - Validation and error checking:
   - `VendingMachine.get_product_id_from_customer`
   - `PurchaseHandler.get_coin_value_from_customer`
