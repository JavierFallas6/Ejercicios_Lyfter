def validar(my_list1):
    list_sumar = []
    for item in my_list1: 
        try: 
            if not float(item):
                raise ValueError()
            print(f"{item} Sumado Correctamente")
            list_sumar.append(item)
        except ValueError as error:
            print(f"Elemento Invalido: {item}")
    return list_sumar


def sumar_valores(list):
    suma = 0
    for item in list:
        suma = float(item) + suma

    print(f"Total de la suma: {suma}")


def main():
    my_list = ['10', 'manzana', '5.5', '3', 'n/a']
    lista_sumable = validar(my_list)
    sumar_valores(lista_sumable)

if __name__ == '__main__':  
    main()