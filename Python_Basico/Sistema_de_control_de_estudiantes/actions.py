import menu as menu_module
import data as data_module
import sys


def asking_for_n_students():
    list_of_students = []
    counter = 1
    n_students = input("Type number of students to enter: ")

    while not n_students.isdigit():
        n_students = input("Type number of students to enter: ")

    while counter <= int(n_students):
        student_name = input(f"Full Student name {counter}: ")
        student_section = input(f"Section of {student_name}: ")
        spanish_grade = validations(student_name,"Spanish")
        english_grade = validations(student_name,"English")
        socials_grade = validations(student_name,"Socials")
        science_grade = validations(student_name,"Science")

        student = {"Student Name": student_name, 
                   "Section": student_section,
                   "Spanish Grade":spanish_grade, 
                   "English Grade": english_grade,
                   "Socials Grade":socials_grade,
                   "Science Grade" : science_grade }
        list_of_students.append(student)
        counter += 1

        
    return list_of_students

def validations(student, subject):
    grade = 0
    try:
        grade = input(f"Type grade for {student}, assigment {subject}: ")
        while not grade.isdigit():
            grade = input(f"Type a valid grade for {student}, assignment {subject}: ")      
        while not (0 <= float(grade) <= 100):
            grade = float(input(f"Type a valid grade for {student}, assignment {subject}: "))
    except ValueError:
        grade = float(input(f"Type a valid grade for {student}, assignment {subject}: "))
    return float(grade)

def get_average(grades):
    average = 0
    top_average = []
    try:
        for grade in grades:
            average = (float(grade['Spanish Grade']) + float(grade['English Grade']) + float(grade['Socials Grade']) + float(grade['Science Grade']))/4
            print(f"The average grade of {grade['Student Name']} is: {average}")
            averages = {"Student Name" : grade['Student Name'], "Average": average}
            top_average.append(averages)

    except ValueError as error:
        print("No grades to average")
    return_to_menu()

def list_of_students(list):

    try:
        for students in list:
            print(f"Student Name: {students['Student Name']}")
            print(f"Section: {students['Section']}")
            print(f"Spanish Grade: {students['Spanish Grade']}")
            print(f"English Grade: {students['English Grade']}")
            print(f"Socials Grade: {students['Socials Grade']}")
            print(f"Science Grade: {students['Science Grade']}")
  
    except TypeError as error:
        print("There are no students to show")
    return_to_menu()

def sort_top_3_averages(grades):
    average = 0
    top_average = []
    try:
        for grade in grades:
            average = (float(grade['Spanish Grade']) + float(grade['English Grade']) + float(grade['Socials Grade']) + float(grade['Science Grade']))/4
            averages = {"Student Name" : grade['Student Name'], "Average": average}
            top_average.append(averages)

        sort_by_average = sorted(top_average, key= lambda x:x["Average"], reverse=True)[:3]

        print("Top 3 students with best average grade: ")
        for average in sort_by_average:
            print(f"Student name: {average['Student Name']}, average: {average['Average']}")
            print
    except ValueError as error:
        print("There is not data to show top 3 students with best average")
    return_to_menu()

def return_to_menu():
    print("¿Would you like to return to menu?")
    print("Type 1 for YES or 2 for EXIT")
    selection = input("your answer: ")
    while not selection.isdigit():
        selection = input("Enter a valid number: ")

    while not (1 <= int(selection) <= 2):
        selection = int(input("Select a valid option 1 or 2: "))

    seleccion_final(selection)

def seleccion_final(seleccion_final):
    
    match int(seleccion_final):
        case 1: 
            menu_module.menu_principal()
        case 2:
            sys.exit("Chao")

def validate_selection():
    validation = input("Select an option from Menu: ")
    while not validation.isdigit():
        validation = input("Select an option from Menu: ")

    while not (1 <= int(validation) <= 7):
        validation = int(input("Select a valid option from Menu from 1 to 7: "))

    return int(validation)

def save_records(file_path, data):
    data_module.save_students(file_path,data)

    print("Student Succesfully added")
    return_to_menu()
