def validate_prime(list_prime):
    new_list = []
    for index in range(0,len(list_prime)):
        count = 0
        record = list_prime[index]
        if record == 1 or record == 0:
            False
        elif record == 2:
            new_list.append(record)
        elif record > 2:
            for index_1 in range(1, record+1, 1):
                if record % index_1 == 0:
                    count = count + 1
            if count ==2:
                new_list.append(record)


    print(new_list)


def prime_request():
    prime_number_list = [1,2,3,4,5,6,7,8,9,10,11]
    validate_prime(prime_number_list)
    

prime_request()

