import csv
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FINAL_TABLE_FILE = os.path.join(BASE_DIR, "Final_Table.csv")


def read_final_table():
    final_table = []

    if not os.path.exists(FINAL_TABLE_FILE):
        return final_table

    with open(FINAL_TABLE_FILE, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)

        for data in reader:
            final_table.append(data)

    return final_table


def save_final_table(data):
    file_exists = os.path.exists(FINAL_TABLE_FILE)
    file_is_empty = (not file_exists or os.path.getsize(FINAL_TABLE_FILE) == 0)

    headers = ["Description", "Category","Expense Type","Expense Amount"]

    with open(FINAL_TABLE_FILE, "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)

        if file_is_empty:
            writer.writerow(headers)

        writer.writerows(data)
