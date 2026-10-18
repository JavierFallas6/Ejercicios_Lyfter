import data as dt
import movements as move


def import_existing_data():
    existing_data = dt.read_final_table()
    load_data_to_movements = move.PersonalFinancialManager()

    for items in existing_data:
        load_data_to_movements.final_movements(items[0], items[1], items[2], items[3])

def import_existing_categories():
    existing_data_categories = dt.read_final_table()
    load_categories_to_movement = move.PersonalFinancialManager()

    for movement in existing_data_categories:
        category = movement[1]

        if category not in load_categories_to_movement.categories_record:
            load_categories_to_movement.categories_record.append(category)
