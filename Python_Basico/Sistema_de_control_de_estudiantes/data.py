import csv

def save_students(file_path, data):

    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        headers = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)


def read_students(file_path):
    list_student = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for studens in reader:
                list_student.append(studens)
        
    except FileNotFoundError:
        print("No previoous records found")
    return list_student
