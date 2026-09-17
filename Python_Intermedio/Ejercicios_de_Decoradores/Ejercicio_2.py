def validate_number(func):
    def validate(*args):
        for index, arg in enumerate(args):
            if not isinstance(arg, (int, float)):
                raise ValueError(f"{arg} No es un número")
                continue
        
        func(*args)

    return validate



@validate_number
def print_number(*args):
    print(f"{args} es un numero")




print_number(10,5,"hola")
