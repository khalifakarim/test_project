class SaleHistoryError(Exception):
    def __init__(self, showroom_name):
        self.showroom_name = showroom_name

    def __str__(self):
        return f"{self.showroom_name} has no sales history"
