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


class MoneyPot:
    # list of coin names, used to populate the keys for the coins dictionary
    coin_names = {
        'One Penny',
        'Two Pence',
        'Five Pence',
        'Ten Pence',
        'Twenty Pence',
        'Fifty Pence',
        'One Pound',
        'Two Pounds',
    }

    def __init__(self):
        # Initialise 'coins' dictionary with coin name keys and empty array values.
        self.coins = {key: [] for key in self.coin_names}

    # Debugging output for MoneyPot class is the coins dictionary
    def __repr__(self):
        return str(self.coins)


class CustomerMoneyPot(MoneyPot):
    def reset(self):
        # reset the pot to its original state using its parent's init method
        super().__init__()

    def sum(self):
        total = 0
        # value of coin time stack count = total of stack.
        for stack in self.coins.values():
            pass


class MachineMoneyPot(MoneyPot):
    # create iadd function to handle += command onto the money pot.
    def __iadd__(self, other):
        # loop the other coin dictionary with the key and value (coin, stack)
        for coin, stack in other.coins.items():
            # add the items from the other stack into the self stack.
            self.coins[coin] = self.coins[coin] + stack
        return self


machine_money_pot = MachineMoneyPot()
customer_money_pot = CustomerMoneyPot()
print('mch', machine_money_pot)
print('cst', customer_money_pot)

customer_money_pot.coins['One Penny'].append(OnePenny())
print('cst', customer_money_pot)

machine_money_pot += customer_money_pot
print('mch', machine_money_pot)

customer_money_pot.reset()
print('cst', customer_money_pot)

print(type(machine_money_pot.coins))





purchase_pot = MoneyPot()
#
while True:
    print(purchase_pot.coins)

    coin_value_text = input("Enter the value of your coin: ")

    if coin_value_text == '0.01':
        purchase_pot.coins['One Penny'].append(OnePenny())
    elif coin_value_text == '0.02':
        purchase_pot.coins['Two Pence'].append(TwoPence())
    elif coin_value_text == '0.05':
        purchase_pot.coins['Five Pence'].append(FivePence())
    elif coin_value_text == '0.10':
        purchase_pot.coins['Ten Pence'].append(TenPence())
    elif coin_value_text == '0.20':
        purchase_pot.coins['Twenty Pence'].append(TwentyPence())
    elif coin_value_text == '0.50':
        purchase_pot.coins['Fifty Pence'].append(FiftyPence())
    elif coin_value_text == '1.00':
        purchase_pot.coins['One Pound'].append(OnePound())
    elif coin_value_text == '2.00':
        purchase_pot.coins['Two Pounds'].append(TwoPounds())
    elif coin_value_text == 'q':
        break
    else:
        print("Invalid Input")
