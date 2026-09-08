employee = {
    'name': 'John',
    'email': 'jonh@ecorp.com',
    'access_level': 5,
    'age': 28
}


list_of_keys = ['access_level', 'age']
for key in list_of_keys:
    employee.pop(key)

print(employee)
