import menu as menu_module
import data as data_module
import sys


class Student():
    def __init__(self, student_name, student_section , spanish_grade, english_grade, socials_grade, science_grade ):
        self.student_name = student_name
        self.student_section = student_section
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.socials_grade = socials_grade
        self.science_grade = science_grade

def asking_for_n_students(list_of_students):


    name = input(f"Full Student name: ")
    section = input(f"Section of {name}: ")
    score_1 = validations(name,"Spanish")
    score_2 = validations(name,"English")
    score_3 = validations(name,"Socials")
    score_4 = validations(name,"Science")

    
    list_of_students.append(Student(name, section,score_1,score_2,score_3,score_4))

        
    return list_of_students


def validations(student, subject):
    while True:
        try:
            grade = float(input(f"Type grade for {student}, assigment {subject}: "))
            while not 0 <= grade <= 100:
                grade = float(input(f"Grade out of range, Type grade for {student}, assigment {subject}: "))
            return grade
        except ValueError:
            print("Invalid number")


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

def return_to_menu(final_list):
    print("¿Would you like to return to menu?")
    print("Type 1 for YES or 2 for EXIT")
    while True:
        try:
            selection = int(input("Your Answer "))
            while not 1 <= selection <= 2:
                selection = int(input("Your Answer: "))
            seleccion_final(selection,final_list)
        except ValueError:
            print("Invalid Selection")
        else:
            break

def seleccion_final(seleccion_final,final_list):
    
    match int(seleccion_final):
        case 1: 
            menu_module.menu_principal(final_list)
        case 2:
            sys.exit("Chao")

def validate_selection():
    while True:
        try:
            validation = int(input("Select an option from Menu: "))
            while not 1 <= validation <= 7:
                validation = int(input("Select an option from Menu: "))
            return validation
        except ValueError:
            print("Invalid option from Menu")
        else:
            break

def save_records(file_path, data):
    data_module.save_students(file_path,data)

    print("Student Succesfully added")
