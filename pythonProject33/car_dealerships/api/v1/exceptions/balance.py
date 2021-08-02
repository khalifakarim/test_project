class BalanceError(Exception):
    def __init__(self, showroom_name):
        self.showroom_name = showroom_name

    def __str__(self):
        return f"{self.showroom_name} does not have enough money on the balance"
