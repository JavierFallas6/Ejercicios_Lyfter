import FreeSimpleGUI as sg
import data as dt
import Movements as move
import Validations as validator

def Movements_table():
    final_table_movements = dt.read_final_table()

    headers = [ "Description","Category", "Expense","Expense Amount"]

    rows = [
        [            
            movement["Description"],
            movement["Category"],
            movement["Expense"],
            movement["Expense Amount"]
        ]
        for movement in final_table_movements
    ]

    layout = [[sg.Table(values=rows,headings=headers,
            key="table",auto_size_columns=True,justification="center",
            expand_x=True,expand_y=True
        )]
    ]

    window = sg.Window(
        "Movements Table",
        layout,
        resizable=True
    )

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

    window.close()

def new_movement_window():
    category_options = dt.read_categories()
    layout = [[sg.Text("Description:")],[sg.Input(key="Description")],
            [sg.Text("Type of Expense:")],[sg.Combo(values= ["Profit", "Loss"],key="expense_combo")],[sg.Text("Amount $:")],[sg.Input(default_text=0, key="expense_value")],
            [sg.Text("Select a Category:")],[sg.Combo(values= category_options,key="Combo_category")],
            [sg.Button("Save")]
    ]

    window = sg.Window("New Movement" , layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        if event == "Save":
            try:
                category_value = validator.category_empty(values["Combo_category"])
                description_value = values["Description"]
                expense_value = float(values["expense_value"])
                type_value = values["expense_combo"]


                movements = move.FinalMovements(expense_value,category_value,description_value,type_value)
                dt.save_final_table([movements])

                sg.popup(
                    "Successfully Added!"
                )

                window["Description"].update("")
                window["Combo_category"].update("")
                window["expense_value"].update(0) 
                window["expense_combo"].update("")                 

            except ValueError as error:
                sg.popup_error(str(error))
            

    window.close()

def new_category_window():
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

                category_value = validator.category_validation(category_value)
                category_to_add = move.Categories(category_value)
                dt.save_categories([category_to_add])

                sg.popup(
                    "Category successfully Added!"
                )

                window["new_category"].update("")


            except ValueError as error:
                sg.popup_error(str(error))            

    window.close()

def gui_principal():
    layout = [[sg.Button("See Movements")],
            [sg.Button("Add New Movement")],
            [sg.Button("Add New Category")]
    ]


    window = sg.Window("Finances" , layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == "See Movements":
            Movements_table()
        elif event == "Add New Movement":
            new_movement_window()
        elif event == "Add New Category":
            new_category_window()                        

    window.close()



if __name__ == "__main__":
    gui_principal()