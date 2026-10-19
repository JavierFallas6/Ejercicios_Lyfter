class Movement:
    def __init__(self, description, category, expense_type, expense_amount):
        self.description = description
        self.category = category
        self.expense_type = expense_type
        self.expense_amount = expense_amount

class Category:
    def __init__(self, new_category):
        self.new_category = new_category


class PersonalFinancialManager:
    def __init__(self):
        self.movement_record = []
        self.categories_record = []

    def final_movements(self, description, category, expense_type, expense_amount):
        movement = Movement(description, category, expense_type, expense_amount)
        self.movement_record.append(movement)

    def add_category(self, new_category):
        category = Category(new_category)
        self.categories_record.append(category)