
class Expenses:
    def __init__(self, expense_amount):
        self.expense_amount = expense_amount


class Categories:
    def __init__(self, category):
        self.category = category


class FinalMovements(Expenses, Categories):
    def __init__(self, expense_amount, category, movement_description,expense):
        Expenses.__init__(self, expense_amount)
        Categories.__init__(self, category)
        self.movement_description = movement_description
        self.expense = expense



