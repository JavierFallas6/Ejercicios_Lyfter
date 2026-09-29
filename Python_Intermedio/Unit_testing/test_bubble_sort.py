from Ejercicio_1 import bubble_sort
import pytest

def test_shot_list():

    input = [5,110,2,3,50]

    result = bubble_sort(input)

    assert result == [2, 3, 5, 50, 110]



def test_long_list():

    input = list(range(0,100,1))

    result = bubble_sort(input)

    assert result == list(range(0,100))



def test_empty_list():

    input = []

    result = bubble_sort(input)

    assert result == []



def test_not_list():

    input_value = 10

    with pytest.raises(TypeError):
        bubble_sort(input_value)    