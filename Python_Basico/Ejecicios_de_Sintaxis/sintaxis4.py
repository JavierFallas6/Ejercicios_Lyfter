import random

random_number = random.randint(1, 10)
secret_number = int(input("Ingresa tu numero secreto "))

while secret_number != random_number:
    secret_number = int(input("Ingresa otro numero secreto "))

    if secret_number < random_number:
        print("Intentalo otra vez")
    elif secret_number > random_number:
        print(print("esta cerca, sigue intentando"))
    else:
        print("Correcto, lo adivinaste")

