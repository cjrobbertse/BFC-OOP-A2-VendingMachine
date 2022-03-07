from abc import ABC, abstractmethod
# abstract method for explicit abstract method Coin


class CoinFactory:
    """CoinFactory creates coin class instances, from a given coin_value input"""

    # constant list containing all the possible UK coin values.
    # also, a class attribute, so it is accessible from all instances of the class.
    COIN_VALUES = [
        0.01,
        0.02,
        0.05,
        0.10,
        0.20,
        0.50,
        1.00,
        2.00,
    ]

    # Needs to be static because it doesn't include self and doesn't need an instance.
    @staticmethod
    def create_coin_class(coin_value):
        """Returns a new instance of a Coin subclass, depending on the coin value argument"""
        if coin_value == 0.01:
            return OnePenny()
        if coin_value == 0.02:
            return TwoPence()
        if coin_value == 0.05:
            return FivePence()
        if coin_value == 0.10:
            return TenPence()
        if coin_value == 0.20:
            return TwentyPence()
        if coin_value == 0.50:
            return FiftyPence()
        if coin_value == 1.00:
            return OnePound()
        if coin_value == 2.00:
            return TwoPounds()


class Coin(ABC):
    """Parent Coin class is an abstract class that defines the attribute structure of all coins."""
    @abstractmethod
    def __init__(self, value=None):  # default value of None.
        self.value = value


class OnePenny(Coin):
    """OnePenny class represents a one penny coin"""
    def __init__(self):
        """Overloads parent method with specific value for coin"""
        super().__init__(0.01)


class TwoPence(Coin):
    """TwoPence class represents a one penny coin"""

    def __init__(self):
        """Overloads parent method with specific value for coin"""
        super().__init__(0.02)


class FivePence(Coin):
    """FivePence class represents a one penny coin"""

    def __init__(self):
        """Overloads parent method with specific value for coin"""
        super().__init__(0.05)


class TenPence(Coin):
    """TenPence class represents a one penny coin"""

    def __init__(self):
        """Overloads parent method with specific value for coin"""
        super().__init__(0.10)


class TwentyPence(Coin):
    """TwentyPence class represents a one penny coin"""

    def __init__(self):
        """Overloads parent method with specific value for coin"""
        super().__init__(0.20)


class FiftyPence(Coin):
    """FiftyPence class represents a one penny coin"""

    def __init__(self):
        """Overloads parent method with specific value for coin"""
        super().__init__(0.50)


class OnePound(Coin):
    """OnePound class represents a one penny coin"""

    def __init__(self):
        """Overloads parent method with specific value for coin"""
        super().__init__(1.00)


class TwoPounds(Coin):
    """TwoPounds class represents a one penny coin"""

    def __init__(self):
        """Overloads parent method with specific value for coin"""
        super().__init__(2.00)
