import actions as actions_module
import data as data_module
import sys
final_list = []

def menu_principal():
    global final_list
    file_path = "Students.csv"
    print("1. Type information from students")
    print("2. Review information from students")
    print("3. Top 3 students by Average")
    print("4. Students average")
    print("5. Export Students to CSV")
    print("6. Import Students from CSV")
    print("7. Exit")
    
    menu_selection = actions_module.validate_selection()
    match menu_selection:      
        case 1:
            final_list = actions_module.asking_for_n_students()
            actions_module.return_to_menu () 
        case 2:
            actions_module.list_of_students(final_list)
        case 3:
            actions_module.sort_top_3_averages(final_list)
        case 4: 
            actions_module.get_average(final_list)
        case 5:
            exported_student = data_module.read_students(file_path)
            exported_student.extend(final_list)
            actions_module.save_records(file_path, exported_student)
        case 6:
            exported_student = data_module.read_students(file_path)
            actions_module.list_of_students(exported_student)
        case 7:
            sys.exit("Chao")


