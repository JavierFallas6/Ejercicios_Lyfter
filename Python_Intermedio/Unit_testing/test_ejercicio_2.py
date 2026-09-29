from Ejercicio_2 import sum
from Ejercicio_2 import reverse_string
from Ejercicio_2 import get_primes



def test_result_sum_list():
    input_list = [1,2,3,4,5]

    result = sum(input_list)

    assert result == 15


def test_reverse_string():

    input_string ="Hola" 

    result = reverse_string(input_string)

    assert result == "aloH"


def test_prime_numbers():

    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result = get_primes(input_list)

    assert result == [2, 3, 5, 7]
