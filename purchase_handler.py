from coins import CoinFactory  # import the coin factory module :)


class PurchaseHandler:
    """PurchaseHandler handles the purchase of products"""
    def __init__(self, product):
        """Constructor takes a product as input"""
        self.product = product
        # and creates new money pot, for the user to add money to.
        self.coin_pot = CoinPot()

    @property  # property attribute is dynamically generated each time it is accessed.
    def remaining_to_pay(self):
        """Returns the value left to pay for the purchase's product"""
        # price of product minus the amount of money in the coin pot
        return self.product.price - self.coin_pot.sum
        # note the use of no parenthesis the sum function because it is a property

    def purchase(self):
        # loop until enough money is paid
        while self.remaining_to_pay > 0:  # remaining_to_pay is also a property, so no parenthesis needed :)
            # collect coins and add them to the pot until it is enough.
            self.coin_pot.add_coin(self.get_coin_value_from_customer())
        # confirm the payment is complete
        print('Purchase Complete!')
        # if the remaining is not 0
        if self.remaining_to_pay:
            # display the amount of change to be returned.
            print(f'You are due £{abs(self.remaining_to_pay):.2f} change.')

    def get_coin_value_from_customer(self):
        """Handles the request and input of coins entered by the customer"""
        while True:  # always loop, until break ;) (successfully)
            # display to the user how much money they still need to pay. So the first iteration will be the full
            # price of the product.
            print(f'Price to pay: £{self.remaining_to_pay:.2f}')  # formatting to 2 dp ;)
            # check if valid coin
            raw_coin_value_input = input('\nEnter Coin Value: £')  # new line before, just for formatting.
            try:
                # test if convertable to float
                coin_value_input = float(raw_coin_value_input)
                # is the coin value inputted in the list of coin values?
                if coin_value_input not in CoinFactory.COIN_VALUES:
                    # if not...
                    # display message that it is not and request re-try
                    print('The coin value entered was not a value coin value. Please try again, using only valid coin '
                          'values.')
                    continue  # repeat loop
                else:
                    # found value successfully
                    return coin_value_input
            except ValueError:
                # catch if not convertable to float
                print('The input was not a float. Please try again, only inputting a float value.')
                continue  # repeat loop


class CoinPot:
    """CoinPot is the controller for money storage within the vending machine.

    Specifically for the customers coins being added, the CoinPot will add coins to a dictionary and is able to
    calculate the sum of coins in the pot at any given time."""
    # NOTE: This class could act as a parent class in the future. There could be 2 separate pots, one for the customer
    #       and one for the machine. They could have different functionality and could interact with each other.
    #       This functionality could be implemented in the next iteration of the system with the business
    #       requirements.
    def __init__(self):
        # set up empty coin dictionary.
        self.coins = {}

    # Debugging output for MoneyPot class is the coins dictionary
    def __repr__(self):
        # returns the string format of the coins dictionary
        return str(self.coins)

    def add_coin(self, coin_value):
        """Adds a new coin to the 'coins' dictionary dependent on the inputted coin value"""

        # check if any other coins of that type has already been added, so we can use the append function on an
        # existing array, yet also, not have to create empty array values to append to, and then have to iterate
        # through them to see if they are empty before summing them ;)
        if coin_value in self.coins:
            # Then use the CoinFactory to create a new coin of that value and add it to the CoinPot's 'coins'
            # dictionary
            self.coins[coin_value].append(CoinFactory.create_coin_class(coin_value))
        else:
            # this one it is created for the first time when it does not already exist.
            self.coins[coin_value] = [CoinFactory.create_coin_class(coin_value)]

    @property  # another dynamic class property attribute that is generated every time it is called.
    def sum(self):
        """This property calculates and returns the sum of all the coins (values) that have been added to the
        CoinPot's 'coins' dictionary.

        Or in laymen terms, it calculates the amount of money the user has added to the machine."""
        total = 0  # total keeps track of the total as it loops
        # Iteration over the 'coins' dictionary items. Taking 'key' and 'value' variables into the loop for the key
        # and value of the item within the dictionary :)
        for key, value in self.coins.items():
            # the value of the coin is the key, so we can just multiply the key by the amount of objects (coins) in
            # the dictionary item list. (I know, it makes the value attribute of the coin classes redundant ;) shhh)
            total += key * len(value)
        return total
