from Ejercicio_2 import sum
from Ejercicio_2 import reverse_string
from Ejercicio_2 import get_primes



def test_result_sum_list():
    list_to_sum_input = [1,2,3,4,5]

    result_list_to_sum_input = sum(list_to_sum_input)

    assert result_list_to_sum_input == 15


def test_reverse_string():

    input_string ="Hello" 

    result_input_string = reverse_string(input_string)

    assert result_input_string == "olleH"


def test_prime_numbers():

    prime_numbers_input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result_prime_numbers = get_primes(prime_numbers_input_list)

    assert result_prime_numbers == [2, 3, 5, 7]
