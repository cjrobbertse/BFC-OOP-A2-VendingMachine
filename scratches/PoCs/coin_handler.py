from dataclasses import dataclass


@dataclass
class Coin:
    name: str
    value: float


coins = [
    Coin('One Penny',       0.01),
    Coin('Two Pence',       0.02),
    Coin('Five Pence',      0.05),
    Coin('Ten Pence',       0.10),
    Coin('Twenty Pence',    0.20),
    Coin('Fifty Pence',     0.50),
    Coin('One Pound',       1.00),
    Coin('One Two Pound',   2.00),
]


class CoinHandler:
    def __init__(self):
        self.inserted_coins = []

    def input_coin(self):
        """
        Append a user defined coin-value to self.inserted_coins, if valid input.

        The user will be asked, "Enter coin value: £", to enter a coin-value. The input value is then validated against
        all the coin values. Only if the input matches the value of a possible coin will the value be converted to a
        float and appended to the self.inserted_coins list.
        """
        while True:
            input_coin_value = input('Enter coin value: £')
            # the coin value input must match one of the predefined coin values (in string form and 2DP) to be accepted
            if input_coin_value not in [f'{coin.value:.2f}' for coin in coins]:
                print('Invalid input. Please refer to the guidance above and try again.')
                continue
            else:
                self.inserted_coins.append(float(input_coin_value))
                break


coin_handler = CoinHandler()

print('To insert a coin, please enter the value of the pound sterling coin to 2 decimal places. '
      'For example, 0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1.00 or 2.00')
coin_handler.input_coin()
