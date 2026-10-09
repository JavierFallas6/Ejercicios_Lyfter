from Ejercicio_2 import sum_numbers
from Ejercicio_2 import reverse_string
from Ejercicio_2 import get_primes
from Ejercicio_2 import sorted_words
from Ejercicio_2 import count_upper_lower_case
import pytest

# Ejercicio sum_numbers

def test_result_sum_numbers():
    list_to_sum_input = [1,2,3,4,5]

    result_list_to_sum_input = sum_numbers(list_to_sum_input)

    assert result_list_to_sum_input == 15

def test_result_sum_numbers_empty():
    list_to_sum_input = []

    result_list_to_sum_input = sum_numbers(list_to_sum_input)

    assert result_list_to_sum_input == 0

def test_not_a_number():

    input_value = "not a number"

    with pytest.raises(TypeError):
        sum_numbers(input_value)   

############################


# Ejercicio reverse_string
def test_reverse_string():

    input_string ="Hello" 

    result_input_string = reverse_string(input_string)

    assert result_input_string == "olleH"

def test_reverse_string_empty():

    input_string = "" 

    result_input_string = reverse_string(input_string)

    assert result_input_string == ""

def test_not_a_string():

    input_value = 100

    with pytest.raises(TypeError):
        reverse_string(input_value)  

#############################

# ejercicio_sorted_words

def test_sorted_words():
    sorted_word_input = "python-variable-funcion-computadora-monitor"

    result_sorted_word_input = sorted_words(sorted_word_input)

    assert result_sorted_word_input == "computadora-funcion-monitor-python-variable"


def test_sorted_words_is_empty():
    sorted_word_input_empty = ""

    result_sorted_word_input_empty = sorted_words(sorted_word_input_empty)

    assert result_sorted_word_input_empty == ""



def test_words_already_sorted():
    word_input_already_sorted = "apple-tree-word"

    result_word_input_already_sorted = sorted_words(word_input_already_sorted)

    assert result_word_input_already_sorted == "apple-tree-word"

##############################

def test_count_upper_lower_case():
    up_low_case_input = "Hello Word"
    result_up_low_case = count_upper_lower_case(up_low_case_input)
    assert result_up_low_case == (2, 7)


def test_only_upper_case():
    uppercase_input = "HELLO"
    result_uppercase = count_upper_lower_case(uppercase_input)
    assert result_uppercase == (5, 0)


def test_only_lower_case():
    lowercase_input = "hello"
    result_lowercase = count_upper_lower_case(lowercase_input)
    assert result_lowercase == (0, 5)


##############################

#Ejercicio numeros primos
def test_prime_numbers():

    prime_numbers_input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result_prime_numbers = get_primes(prime_numbers_input_list)

    assert result_prime_numbers == [2, 3, 5, 7]


def test_prime_numbers_empty():

    prime_numbers_input_list = []

    result_prime_numbers = get_primes(prime_numbers_input_list)

    assert result_prime_numbers == []    


def test_prime_numbers_empty():

    prime_numbers_input_list = [1,2,3,"hola"]

    with pytest.raises(TypeError):
        get_primes(prime_numbers_input_list)  
