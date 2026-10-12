
class Expenses:
    def __init__(self, profits, losses):
        self.profits = profits
        self.losses = losses


class Categories:
    def __init__(self, category):
        self.category = category


class FinalMovements(Expenses, Categories):
    def __init__(self, profits, losses, category, movement_description):
        Expenses.__init__(self, profits, losses)
        Categories.__init__(self, category)
        self.movement_description = movement_description


