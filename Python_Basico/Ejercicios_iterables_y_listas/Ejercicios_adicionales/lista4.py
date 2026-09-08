list_numbers = [10, 20, 30, 40, 50]

sum_numbers = 0
counter = 0

for num in list_numbers:
    sum_numbers += num
    counter += 1

average = sum_numbers / counter
higher_numbers = []

for num in list_numbers:
    if num > average:
        higher_numbers.append(num)

print(f"Promedio: {average} ")
print(f"Nueva lista: {higher_numbers}")
