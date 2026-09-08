
def convertir_a_entero(my_list1): 
    for item in my_list1: 
        try: 
            if not int(item):
                raise ValueError()
            print(f"{item} convertido a {int(item)}")
        except ValueError as error:
            print(f"No se pudo convertir el elemento: {item}")

def main():
    my_list = ['4', 'hola', '10', '5.2']
    convertir_a_entero(my_list)

if __name__ == '__main__':  
    main()