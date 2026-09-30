from Ejercicio_1 import bubble_sort
import pytest
import random

def test_shot_list():

    short_list_input = [5,110,2,3,50]

    result_short_list = bubble_sort(short_list_input)

    assert result_short_list == [2, 3, 5, 50, 110]



def test_long_list():

    long_list_input = [random.randint(0, 300) for _ in range(125)]

    result_long_list_input = bubble_sort(long_list_input)

    assert result_long_list_input == sorted(long_list_input)



def test_empty_list():

    empty_list = []

    result_empty_list = bubble_sort(empty_list)

    assert result_empty_list == []



def test_not_list():

    input_value = 10

    with pytest.raises(TypeError):
        bubble_sort(input_value)    