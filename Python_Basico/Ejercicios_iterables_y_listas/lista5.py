number = []
for i in range(10):
    num = float(input(f"Introduce el número {i+1}: "))
    number.append(num)

higher_number = max(number)

print("Los números ingresados son:", number, f'El numero mayor es: {higher_number}')