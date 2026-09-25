def bubble_sort(list_sort):
    for items in range(0, len(list_sort)-1):
        has_changed = False
        for items_2 in range(0, len(list_sort)- 1):
            current_number = list_sort[items_2]
            next_number = list_sort[items_2 + 1]
            print(f'-- Iteracion {items}, {items_2}. Elemento actual: {current_number}, Siguiente elemento: {next_number}')

            if current_number > next_number:
                print('El elemento actual es mayor al siguiente. Intercambiandolos...')
                list_sort[items_2 + 1] = current_number
                list_sort[items_2] = next_number
                has_changed = True

        if not has_changed:
            return       

list_to_sort = [5,110,2,3,50,4,9,-2,7]
bubble_sort(list_to_sort)
print(list_to_sort)