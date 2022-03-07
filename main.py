# custom modules
from product import Product, ProductInventory
from purchase_handler import PurchaseHandler


class VendingMachine:
    """Controls the vending machine process"""
    def __init__(self, welcome_message, product_inventory):
        """Constructor, takes in a custom welcome message and product inventory for the machine"""
        self.welcome_message = welcome_message
        self.product_inventory = product_inventory
        self.selected_product = None

    def new_customer(self):
        """Runs the entire use journey script and manages flow"""
        self.display_welcome_message()
        self.display_menu()
        # set the selected product
        self.selected_product = self.select_product()
        self.confirm_product_selection()
        self.pay_for_product()

    def display_welcome_message(self):
        """displays the specific vending machines welcome message"""
        print(self.welcome_message)
        print('\n')

    def display_menu(self):
        """Displays the menu of products from the vending machine's product inventory"""
        print('Below is the menu of products:\n')
        print(f"{'ID':2} {'Name':10} Price")  # spacing and justification.
        print('--------------------')
        # loop over items in dictionary of product items
        for product_id, product in self.product_inventory.products.items():
            # spacing for id, name, and rounding to 2 decimal places in f string below.
            print(f'{product_id:>2} {product.name:<10} £{product.price:.2f}')
        print()  # new line

    def select_product(self):
        """Method manages the product selection process"""
        # get id from user
        selected_product_id = self.get_product_id_from_customer()
        # return product found with id
        return self.product_inventory.products[selected_product_id]

    def get_product_id_from_customer(self):
        """Get the product id from the user, only accepting valid input"""
        # loop user input to validate for error
        while True:
            # temporary variable to check validity
            raw_product_selection_input = input('\nPlease enter the ID of the product you wish to purchase: ')
            try:
                # convert to int
                product_selection_input = int(raw_product_selection_input)
                # check value is a valid product ID
                if product_selection_input not in self.product_inventory.products:
                    # retry and hint message
                    print('The integer you have entered is not in the product ID list. '
                          'Please try again, using a valid product ID.')
                    continue  # repeat loop
                else:
                    # found value successfully
                    return product_selection_input
            except ValueError:  # catch exception ;)
                # not an int
                print('The input was not an int. Please try again, only inputting an int value.')
                continue  # repeat loop

    def confirm_product_selection(self):
        """Display confirmation of selected product to the user"""
        print(f"You have selected {self.selected_product.name}.")

    def pay_for_product(self):
        """Manages the payment of a product"""
        # creates new purchase handler instance using the product;imported from local custom module purchase_handler.py
        purchase_handler = PurchaseHandler(self.selected_product)
        # activates the purchase procedure.
        purchase_handler.purchase()


def main():
    """runs the application"""
    # set up Vending Machine
    vending_machine_welcome_message = "Welcome to this MAGICAL virtual vending machine.\n\n" \
                                      "You may be wondering, 'What makes this virtual vending machine MAGICAL?',\n" \
                                      "and that would be completely normal. However, do not fret because I, your\n" \
                                      "friendly *evil laugh* virtual vending machine assistant, will elevate any\n" \
                                      "qualms you may have.\n\n" \
                                      "This virtual vending machine is MAGICAL because it has unlimited products\n" \
                                      "and coins. That means you, our precious little customer, can spend to\n" \
                                      "your little (or big) heart's content. £££ MWAHAHAHA £££\n\n" \
                                      "Enjoy!"
    # set product menu
    # products are created using the Product class found in imported module.
    product_dict = {
        1: Product('Coke', 1.50),
        2: Product('Fanta', 1.37),
        3: Product('Water', 0.60),
        4: Product('Crisps', 0.86),
        5: Product('Mars Bar', 0.55),
        6: Product('Nuts', 0.22),
    }

    # instantiate vending machine class object by passing in welcome message and product dict.
    vending_machine = VendingMachine(
        vending_machine_welcome_message,
        ProductInventory(product_dict))

    # run the vending machine customer journey process
    vending_machine.new_customer()


if __name__ == '__main__':
    # run run run
    main()
