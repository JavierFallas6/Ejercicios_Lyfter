import data as dt


def import_existing_data(manager):
    existing_data = dt.read_final_table()

    for movement in existing_data:
        manager.final_movements(
            movement[0],
            movement[1],
            movement[2],
            movement[3]
        )

def import_existing_categories(manager):
    existing_categories = dt.read_categories()

    for category in existing_categories:
        manager.add_category(category)