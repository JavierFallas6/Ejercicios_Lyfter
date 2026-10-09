def sum_numbers(list):
    result = 0
    for items in list: 
        result += items
    return result


def reverse_string(text):
    return text[::-1]


def sorted_words(chain):
    list_words = chain.split("-")
    sorted_word = sorted(list_words)
    return "-".join(sorted_word)


def count_upper_lower_case(text):

    upper_case = 0
    lower_case = 0

    for letters in text:
        if letters.isupper():
            upper_case += 1
        elif letters.islower():
            lower_case += 1
    
    return upper_case, lower_case


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


    result = sorted_words("python-variable-funcion-computadora-monitor")
    print(result)

    up_case, low_case = count_upper_lower_case("I love Nacion Sushi")
    print(f"There are: {up_case} upper cases and {low_case} lower case")