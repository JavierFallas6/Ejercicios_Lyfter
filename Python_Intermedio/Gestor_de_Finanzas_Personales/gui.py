import FreeSimpleGUI as sg
import movements as move
import validations as validator
import data as dt
import import_data as id



def new_movement_window():
    financial_record = move.PersonalFinancialManager()
    category_options = financial_record.categories_record

    layout = [[sg.Text("Description:")],[sg.Input(key="Description")],
            [sg.Text("Type of Expense:")],[sg.Combo(default_value="Profit", values= ["Profit", "Loss"],key="expense_combo", readonly=True)],[sg.Text("Amount $:")],[sg.Input(default_text=0, key="expense_value")],
            [sg.Text("Select a Category:")],[sg.Combo(values= category_options,key="Combo_category", readonly=True)],
            [sg.Button("Save")]
    ]

    window = sg.Window("New Movement" , layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        if event == "Save":
            try:
                
                

                description_value = values["Description"]
                description_value = validator.validate_description_empty(description_value)

                category_value = validator.validate_category_empty(values["Combo_category"])

                type_value = values["expense_combo"]

                expense_value = values["expense_value"]
                expense_value = validator.validate_amount(expense_value)
                expense_value = validator.validate_amount_not_less_than_zero(expense_value)
                
                financial_record.final_movements(description_value,category_value,type_value,expense_value)                

                sg.popup(
                    "Successfully Added!"
                )

                window["Description"].update("")
                window["Combo_category"].update("Profit")
                window["expense_value"].update(0) 
                window["expense_combo"].update("")                   

            except ValueError as error:
                sg.popup_error(str(error))
            

    window.close()

def new_category_window():
    financial_record_category = move.PersonalFinancialManager()

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
                category_value = validator.validate_category(category_value)
                financial_record_category.categories_list(category_value)

                sg.popup(
                    "Category successfully Added!"
                )

                window["new_category"].update("")


            except ValueError as error:
                sg.popup_error(str(error))            

    window.close()

def gui_principal():
    id.import_existing_categories()
    id.import_existing_data()
    final_table_movements = move.PersonalFinancialManager()
    final_table_movements = final_table_movements.movement_record

    headers = [ "Description","Category", "Expense Type","Expense Amount"]

    rows = [
        [            
            movement[0],
            movement[1],
            movement[2],
            movement[3]
        ]
        for movement in final_table_movements
    ]

    layout = [[sg.Table(values=rows,headings=headers,key="table",auto_size_columns=True,justification="center",expand_x=True,expand_y=True)],
            [sg.Button("Add New Movement")],[sg.Button("Add New Category")],[sg.Button("Export to CSV")]
    ]

    
    window = sg.Window("Finances" , layout,resizable = True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Add New Movement":
            new_movement_window()

            final_table_movements = move.PersonalFinancialManager()
            final_table_movements = final_table_movements.movement_record

            rows = [
                [
                movement[0],
                movement[1],
                movement[2],
                movement[3]
                ]
                for movement in final_table_movements
            ]

            window["table"].update(values=rows)
        
        elif event == "Add New Category":
            new_category_window()           

        elif event == "Export to CSV":

            dt.save_final_table(rows)
            sg.popup("Data Exported")



    window.close()



if __name__ == "__main__":
    gui_principal()