def sum(list):
    result = 0
    for items in list: 
        result += items
    print(result)
    return result

list_to_sum = [1,2,3,4,5] 
sum(list_to_sum)   


def reverse_string(text):
    return text[::-1]

resultado = reverse_string("Hola")
print(resultado)



def get_primes(numbers):
    primes = []

    for number in numbers:
        if number < 2:
            continue

        is_prime = True

        for divisor in range(2, number):
            if number % divisor == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(number)

    return primes


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(get_primes(numeros))