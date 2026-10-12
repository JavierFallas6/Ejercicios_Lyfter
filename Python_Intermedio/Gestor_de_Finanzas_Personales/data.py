import csv
import os

def read_categories():
    categories_list = []

    if not os.path.exists("Categories.csv"):
        return categories_list
    
    with open("Categories.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for categories in reader:
            categories_list.append(categories["Categories"])


    return categories_list

def read_final_table():
    final_table = []

    if not os.path.exists("Final_Table.csv"):
        return final_table

    with open("Final_Table.csv", "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for data in reader:
            final_table.append(data)

    return final_table

def save_categories(data):
    file_exists = os.path.exists("Categories.csv")
    file_is_empty = (not file_exists or os.path.getsize("Categories.csv") == 0)
    headers = ["Categories"]

    with open("Categories.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)

        if file_is_empty:
            writer.writeheader()        

        for categories in data:
            categories_dictionary = {
                "Categories": categories.category,
            }

            writer.writerow(categories_dictionary)

def save_final_table(data):
    file_exists = os.path.exists("Final_Table.csv")
    file_is_empty = (not file_exists or os.path.getsize("Final_Table.csv") == 0)

    headers = ["Profit", "Loss", "Category", "Description"]

    with open("Final_Table.csv", "a", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)

        if file_is_empty:
            writer.writeheader()

        for movement in data:
            movement_dictionary = {
                "Profit": movement.profits,
                "Loss": movement.losses,
                "Category": movement.category,
                "Description": movement.movement_description
            }

            writer.writerow(movement_dictionary)
