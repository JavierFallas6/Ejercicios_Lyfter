time_limit = 600

time = int(input("Inserta minutos en segundos "))

if (time < time_limit):
    missing_seconds = time_limit - time
    print(f"faltan {missing_seconds} segundos")
else:
    if (time > time_limit):
        print("Mayor")
    else:
        if (time == time_limit):
            print("Igual")


