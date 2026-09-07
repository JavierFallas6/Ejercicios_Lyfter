
def Suma(numero_actual1):
    Result = 0 
    try:
        try:
            number_1 = float(input("Ingrese un Numero "))
        except:
            print(f"Valor Invalido")
            number_1 = float(input("Ingrese un Numero "))

        Result = numero_actual1 + number_1 
        print(f"Su resultado es: {Result}")
        return Result
    except ValueError as error:
        print(error)
        return numero_actual1

def Resta(numero_actual1):
    Result = 0    
    try:
        try:
            number_1 = float(input("Ingrese un Numero "))
        except:
            print(f"Valor Invalido")
            number_1 = float(input("Ingrese un Numero "))

        Result = numero_actual1 - number_1
        print(f"Su resultado es: {Result}")
        return Result
    except ValueError as error:
        print(error)
        return numero_actual1

def Division(numero_actual1):
    Result = 0 
    try:
        try:
            number_1 = float(input("Ingrese un Numero "))
        except:
            print(f"Valor Invalido")
            number_1 = float(input("Ingrese un Numero "))

        Result = numero_actual1 / number_1 
        print(f"Su resultado es: {Result}")
        return Result
    except ValueError as error:
        print(error)
        return numero_actual1
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return numero_actual1
    
def Multiplicacion(numero_actual1):
    Result = 0 
    try:
        try:
            number_1 = float(input("Ingrese un Numero "))
        except:
            print(f"Valor Invalido")
            number_1 = float(input("Ingrese un Numero "))     

        Result = numero_actual1 * number_1
        print(f"Su resultado es: {Result}")
        return Result
    except ValueError as error:
        print(error)
        return numero_actual1


def main():
    try:

        print("Seleccion: 1.Suma 2.Resta 3.Division 4.Multiplicacion 5.Borrar Resultado 6.Salir" )
        Selector = int(input("Su Seleccion: " ))
        numero_actual = 0

        while Selector <= 7:
            match Selector:
                case 1:
                    numero_actual = Suma(numero_actual)
                case 2:
                    numero_actual = Resta(numero_actual)
                case 3:
                    numero_actual = Division(numero_actual)
                case 4:
                    numero_actual = Multiplicacion(numero_actual)
                case 5:
                    numero_actual = 0
                case 6:
                    break
                case _:
                    print("Valor Incorrecto")

            print("Seleccion: 1.Suma 2.Resta 3.Division 4.Multiplicacion 5.Borrar Resultado 6.Salir " )
            Selector = int(input("Su Seleccion: " ))                        
    except ValueError:
        print("Calculadora Cerrada, debido a que no se ingreso un numero")

if __name__ == '__main__':
	main()   