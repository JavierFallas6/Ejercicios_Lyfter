approved_grades = 0
failed_grades = 0
average_approved_grades = 0
average_failed_grades = 0
average_total_grades = 0
actual_grades = 0
contador = 0
sum_grades_fail = 0
sum_grades_approved = 0

total_grades = int(input("Ingrese la cantidad de notas: "))

while contador < total_grades:
    actual_grades = float(input("Ingrese la nota: "))


    if (actual_grades  >= 0 and actual_grades <= 100):

        contador += 1
        if (actual_grades < 70):
            failed_grades = failed_grades + 1
            sum_grades_fail = sum_grades_fail + actual_grades
        else:
            approved_grades = approved_grades + 1
            sum_grades_approved = sum_grades_approved + actual_grades
    else:
        print("Inserte un numero valido")

if failed_grades == 0:
    print("Paso")
else:
    average_failed_grades = sum_grades_fail / failed_grades

if approved_grades == 0:
    print("No Paso")
else:
    average_approved_grades = sum_grades_approved / approved_grades

average_total_grades = (sum_grades_fail + sum_grades_approved) / total_grades

print(f"El estudiante tiene esta cantidad de notas aprobadas, {approved_grades}")
print(f"Este es el promedio de notas aprobadas, {average_approved_grades}")
print(f"El estudiante tiene esta cantidad de notas desaprobadas, {failed_grades}")
print(f"Este es el promedio de notas desaprobadas, {average_failed_grades}")
print(f"Este es el promedio total de notas, {average_total_grades}")



