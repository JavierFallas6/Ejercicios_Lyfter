import actions as actions_module
import data as data_module

def menu_principal():
    file_path = "Students.csv"
    print("1. Add and Save new student")
    print("2. Top 3 students by Average")
    print("3. Students averages")
    print("4. list of Students")
    print("5. Exit")
    menu_selection = int(input("Select an option from Menu: "))

    match menu_selection:
        case 1:
            actions_module.asking_for_n_students(file_path)       
        case 2: 
            grades_array = data_module.read_students(file_path)
            actions_module.sort_top_averages(grades_array)
        case 3: 
            grades_array = data_module.read_students(file_path)
            actions_module.get_average(grades_array)
        case 4:
            list_of_student = data_module.read_students(file_path)
            actions_module.list_of_students(list_of_student)
        case 5:
            print("Chao")
            SystemExit()
        case _:
            print("Invalid Selection")
