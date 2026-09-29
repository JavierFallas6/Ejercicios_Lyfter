def print_numbers_times_2(numbers_list):
	for number in numbers_list:
		print(number * 2)

# print_numbers_times_2 es O(n), tine solo un ciclo que va a ejecutarse siempre n cantidad de veces de acuerdo a su entrada.



def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a: 
		for element_b in list_b:
			if element_a == element_b:
				return True
				
	return False



# check_if_lists_have_an_equal es O(n^2), por tener 2 ciclos donde: for element_a in list_a: y for element_b in list_b:


def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print)
	for index in range(min(list_len, 10)):
		print(list_to_print[index])




# print_10_or_less_elements es O(1) el rango es de 10 iteraciones


def generate_list_trios(list_a, list_b, list_c):
	result_list = []
	for element_a in list_a:
		for element_b in list_b:
			for element_c in list_c:
				result_list.append(f'{element_a} {element_b} {element_c}')
				
	return result_list 

# en esta no estoy tan seguro me voy por la logica de que como tiene varios for anidados seria O(n^3) a la potencia 3 por ser 3 for anidados.