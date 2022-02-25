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

print('1.00' == f'{coins.value:.2f}')

# print the name of a coin from its given value.

value = 1.00

relevant_coin = None

for coin in coins:
    if coin.value != value:
        continue
    else:
        relevant_coin = coin
        break


name = relevant_coin.name

print(name)
