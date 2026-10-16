
class PersonalFinancialManager:
    movement_record = []
    categories_record = []

    def categories_list(self, category_to_create):
        self.categories_record.append(category_to_create)

    def final_movements(self,movement_description,category,expense_type,expense_amount):
        final_movement_list = [movement_description,category,expense_type,expense_amount]

        self.movement_record.append(final_movement_list)



