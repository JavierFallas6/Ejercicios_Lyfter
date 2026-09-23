def bubble_sort(list_sort):
    for items in range(0, len(list_sort)-1):
        has_changed = False
        for items_2 in range(0, len(list_sort)- 1 - items):
            current_number = list_sort[items_2]
            next_number = list_sort[items_2 + 1]

            if current_number > next_number:
                list_sort[items_2 + 1] = current_number
                list_sort[items_2] = next_number
                has_changed = True

        if not has_changed:
            return       

list_to_sort = [5,2,3,4,9,-2]
bubble_sort(list_to_sort)
print(list_to_sort)