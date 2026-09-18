def print_parameters(func):
    def wrapper(*args):
        print("Parameters:", args)

        result = func(*args)

        print("Return:", result)

    return wrapper


@print_parameters
def sumar(a, b):
    return a + b


sumar(5, 3)
