def get_name():
    name = input(f"Ingrese su nombre: ")
    if name.isdigit():
        raise ValueError("El nombre no puede ser un número")
    return name

def get_age():    
    Age = None
    try:
        Age = int(input(f"Ingrese su edad: "))
    except:
        print("Numero no valido")
    return Age

def main():
    try:
        Nombre = get_name()
        Edad = get_age()
        print(f"Hola {Nombre}, su edad es: {Edad}")
    except ValueError as ex:
        print(ex)
    
if __name__ == '__main__':  
    main()