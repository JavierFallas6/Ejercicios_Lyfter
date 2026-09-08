sum = 0
count = 1

number = int(input("Inserta un numero "))

while count <= number:
    sum = sum + count
    count = count + 1

print(f"La suma total es {sum}")