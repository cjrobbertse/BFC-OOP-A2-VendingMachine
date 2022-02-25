from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float


products = {
    1: Product('Coke', 1.50),
}


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

selected_product = products[1]  # products[int(input('Enter product id: '))]
print(f'You have selected the {selected_product.name}, which costs £{selected_product.price:.2f}.\n')

print('To insert a coin, please enter the value of the pound sterling coin to 2 decimal places.\n'
      'For example, [0.01, 0.02. 0.05, 0.10, 0.20, 0.50, 1.00, 2.00]')

print('Please begin inserting coins...')

# print message to user:
# 'That coin value is invalid. The input must be a value representing a valid Sterling coin denomination and to 2DP.
# For example, 1.00'

# Please enter the value of Sterling coin denomination to 2 decimal places. For example, [0.01, 0.02. 0.05, 0.10, 0.20,
# 0.50, 1.00, 2.00]


def input_coin():
    # float(input('Coin value: '))
    while True:
        input_coin_value = input('\nCoin value: ')
        # could replace with
        if input_coin_value not in [f'{coin.value:.2f}' for coin in coins]:
            print('invalid entry')  # TODO: polite helpful correction message
            continue
        else:
            return float(input_coin_value)


def get_change(amount_over):
    # return a list of coins as change
    change_to_return = []
    while sum(change_to_return) < amount_over:
        if amount_over - sum(change_to_return) >= 2.00:
            change_to_return.append(2.00)
        elif amount_over - sum(change_to_return) >= 1.00:
            change_to_return.append(1.00)
        elif amount_over - sum(change_to_return) >= 0.50:
            change_to_return.append(0.50)
        elif amount_over - sum(change_to_return) >= 0.20:
            change_to_return.append(0.20)
        elif amount_over - sum(change_to_return) >= 0.10:
            change_to_return.append(0.10)
        elif amount_over - sum(change_to_return) >= 0.05:
            change_to_return.append(0.05)
        elif amount_over - sum(change_to_return) >= 0.02:
            change_to_return.append(0.02)
        elif amount_over - sum(change_to_return) >= 0.01:
            change_to_return.append(0.01)
        else:
            # float types don't always stick to 2 decimal places, so when there is a difference of 0.00000002, we can
            # just break the loop.
            break

    return change_to_return


inserted_coins = []  # [0.2, 0.2, 0.5, 0.1, 0.2, 1.0]

while sum(inserted_coins) < selected_product.price:  # total value of coins inserted < price of product
    inserted_coins.append(input_coin())
    print(inserted_coins)
    print(f'Sum of inserted coins: £{sum(inserted_coins):.2f}')
    print(f'Sum cost remaining: £{selected_product.price - sum(inserted_coins):.2f}')

if selected_product.price - sum(inserted_coins) < 0:
    # return change
    change = get_change(abs(selected_product.price - sum(inserted_coins)))
    print(f'return change: {change}')

print(f'\nHere is your {selected_product.name}.')
print('\nThank you for your business. See you soon!')
