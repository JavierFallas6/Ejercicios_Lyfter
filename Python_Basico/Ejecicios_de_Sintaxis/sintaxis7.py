number = int(input("Ingrese un número del 1 al 10: "))

print(f"Tabla de multiplicar del {number}")

for i in range(1, 13):
    print(f"{number} x {i} = {number * i}")
