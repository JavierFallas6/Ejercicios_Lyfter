list_number = [9, 4, 7, 3, 5]

minor_number = list_number[0]

for num in list_number:
    if num < minor_number:
        minor_number = num
print(f"El numero menor es: {minor_number}")