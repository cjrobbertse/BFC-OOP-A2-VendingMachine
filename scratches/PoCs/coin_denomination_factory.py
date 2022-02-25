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


coins = {
    'One Penny': [],
    'Two Pence': [],
    'Five Pence': [],
    'Ten Pence': [],
    'Twenty Pence': [],
    'Fifty Pence': [],
    'One Pound': [],
    'Two Pounds': [],
}

while True:
    print(coins)

    coin_value_text = input("Enter the value of your coin: ")

    if coin_value_text == '0.01':
        coins['One Penny'].append(OnePenny())
    elif coin_value_text == '0.02':
        coins['Two Pence'].append(TwoPence())
    elif coin_value_text == '0.05':
        coins['Five Pence'].append(FivePence())
    elif coin_value_text == '0.10':
        coins['Ten Pence'].append(TenPence())
    elif coin_value_text == '0.20':
        coins['Twenty Pence'].append(TwentyPence())
    elif coin_value_text == '0.50':
        coins['Fifty Pence'].append(FiftyPence())
    elif coin_value_text == '1.00':
        coins['One Pound'].append(OnePound())
    elif coin_value_text == '2.00':
        coins['Two Pounds'].append(TwoPounds())
    else:
        print("Invalid Input")
