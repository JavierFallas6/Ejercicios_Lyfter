my_list = [3, 6, 8, 2, 4]

positive_numbers = True

for num in my_list:
    if num <= 0:
        positive_numbers = False
        break
                  
if positive_numbers: 
    print("Todos los numeros son positivos")
else:
    print("Hay al menos un numero negativo o cero")