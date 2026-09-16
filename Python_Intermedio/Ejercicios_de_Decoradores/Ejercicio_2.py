class Number:
    def __init__(self, number):
        self.number = number


def validate_number(func):
    def validate(number):
        if not isinstance(number.number, (int, float)):
            raise ValueError("No es un número")
        
        func(number)

    return validate



@validate_number
def print_number(number):
    print(f"el {number.number} es un numero")




my_number = Number(10)
print_number(my_number)

my_number = Number("Hola")
print_number(my_number)
