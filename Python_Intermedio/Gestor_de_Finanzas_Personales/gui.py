import FreeSimpleGUI as sg
import movements as move
import validations as validator
import data as dt
import import_data as impdat



def new_movement_window(type_of_expense,manager):
    if not manager.categories_record:
        sg.popup_error("Please create a category first!")
        return

    category_options = [category.new_category for category in manager.categories_record]

    layout = [[sg.Text("Description:")],[sg.Input(key="Description")],
            [sg.Text("Type of Expense:")],[sg.Input(default_text=type_of_expense, key="expense_type", readonly= True)],[sg.Text("Amount $:")],[sg.Input(default_text=0, key="expense_value")],
            [sg.Text("Select a Category:")],[sg.Combo(values= category_options,key="Combo_category", readonly=True)],
            [sg.Button("Save")]
    ]

    window = sg.Window("New Movement (Profit/Loss)" , layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        if event == "Save":
            try:
                
                description_value = values["Description"]
                description_value = validator.validate_description_empty(description_value)

                category_value = validator.validate_category_empty(values["Combo_category"])

                type_value = values["expense_type"]

                expense_value = values["expense_value"]
                expense_value = validator.validate_amount(expense_value)
                expense_value = validator.validate_amount_not_less_than_zero(expense_value)
                
                manager.final_movements(description_value,category_value,type_value,expense_value)                

                sg.popup(
                    "Successfully Added!"
                )

                window["Description"].update("")
                window["Combo_category"].update("")
                window["expense_value"].update(0) 
                window["expense_type"].update(type_of_expense)                   

            except ValueError as error:
                sg.popup_error(str(error))
            

    window.close()

def new_category_window(manager):
    layout = [[sg.Text("Type Category:")],[sg.Input(key="new_category")],
            [sg.Button("Save")]
    ]

    window = sg.Window("Create New Category" , layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == "Save":
            try:
                
                category_value = values["new_category"]
                category_value = validator.validate_category_empty(category_value)
                category_value = validator.validate_category(category_value,manager)
                manager.add_category(category_value)
                dt.save_categories(category_value)
                sg.popup(
                    "Category successfully Added!"
                )

                window["new_category"].update("")


            except ValueError as error:
                sg.popup_error(str(error))            

    window.close()

def open_movement_window(expense_type_value,manager):
    new_movement_window(expense_type_value,manager)

    rows = [
        [
            movement.description,
            movement.category,
            movement.expense_type,
            movement.expense_amount,
        ]
        for movement in manager.movement_record
    ]

    return rows 

def gui_principal():
    manager = move.PersonalFinancialManager()
    impdat.import_existing_categories(manager)
    impdat.import_existing_data(manager)
    headers = [ "Description","Category", "Expense Type","Expense Amount"]

    rows = [
        [
            movement.description,
            movement.category,
            movement.expense_type,
            movement.expense_amount,
        ]
        for movement in manager.movement_record
    ]

    layout = [[sg.Table(values=rows,headings=headers,key="table",auto_size_columns=True,justification="center",expand_x=True,expand_y=True)],
            [sg.Button("Add New Category")],[sg.Button("New Profit")],[sg.Button("New Loss")]
    ]

    
    window = sg.Window("Finances" , layout,resizable = True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:

            rows = [
                [
                    movement.description,
                    movement.category,
                    movement.expense_type,
                    movement.expense_amount,
                ]
                for movement in manager.movement_record
            ]  
            dt.save_final_table(manager.movement_record)
            break

        elif event == "New Profit":
                expense_type_value = "Profit"
                rows_from_movement = open_movement_window(expense_type_value,manager)    
                window["table"].update(values=rows_from_movement)

        elif event == "New Loss":
            expense_type_value = "Loss"
            rows_from_movement = open_movement_window(expense_type_value,manager)    
            window["table"].update(values=rows_from_movement)


        elif event == "Add New Category":
            new_category_window(manager)           


    window.close()



if __name__ == "__main__":
    gui_principal()