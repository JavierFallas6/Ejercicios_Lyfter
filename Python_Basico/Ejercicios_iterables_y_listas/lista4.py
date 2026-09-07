my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

list_2 = 0

while list_2 < len(my_list):
    if my_list[list_2] % 2 != 0:
        my_list.pop(list_2)
    else:
        list_2 += 1

print(my_list)