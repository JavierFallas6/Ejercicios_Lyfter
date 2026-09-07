number1 = int(input("Ingresa el primer numero "))
number2 = int(input("Ingresa el seguido numero "))
number3 = int(input("Ingresa el tercer numero "))

if number1 == 30 or number2 == 30 or number3 == 30 or (number1 + number2 + number3) == 30:
    print("Correcto")
else:
    print("Incorrecto")