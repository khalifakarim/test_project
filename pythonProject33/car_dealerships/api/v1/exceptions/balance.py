class BalanceError(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} does not have enough money on the balance"
