import csv
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FINAL_TABLE_FILE = os.path.join(BASE_DIR, "Final_Table.csv")
CATEGORIES_FILE = os.path.join(BASE_DIR, "Categories.csv")


def read_final_table():
    final_table = []

    if not os.path.exists(FINAL_TABLE_FILE):
        return final_table

    with open(FINAL_TABLE_FILE, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)

        for data in reader:
            if data:
                final_table.append(data)

    return final_table


def save_final_table(data):
    headers = ["Description", "Category", "Expense Type","Expense Amount"
]

    with open(FINAL_TABLE_FILE, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        for movement in data:
            if hasattr(movement, "description"):
                writer.writerow([
                    movement.description,
                    movement.category,
                    movement.expense_type,
                    movement.expense_amount
                ])
            else:
                writer.writerow(movement)


def save_categories(data):
    file_is_empty = (
        not os.path.exists(CATEGORIES_FILE)
        or os.path.getsize(CATEGORIES_FILE) == 0
    )

    with open(CATEGORIES_FILE, "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)

        if file_is_empty:
            writer.writerow(["Category"])

        if hasattr(data, "name"):
            writer.writerow([data.name])
        else:
            writer.writerow([data])


def read_categories():
    categories_table = []

    if not os.path.exists(CATEGORIES_FILE):
        return categories_table

    with open(CATEGORIES_FILE, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)

        for data in reader:
            if data:
                categories_table.append(data[0])

    return categories_table
