def sum(list):
    result = 0
    for items in list: 
        result += items
    return result


def reverse_string(text):
    return text[::-1]


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

if __name__ == "__main__":

    list_to_sum = [1,2,3,4,5] 
    final_sum_result = sum(list_to_sum)  
    print(final_sum_result) 

    reverse_result = reverse_string("Hello")
    print(reverse_result)

    list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(get_primes(list_numbers))