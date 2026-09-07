hotel_dictionary = {
    'hotel_name': 'Nombre del Hotel',
    'star_number': 'Numero de estellas',
    'rooms' : [
        {'room_number': 16,
         'floor': 50, 
         'night_price': 150},
        {'room_number': 20,
         'floor': 51, 
         'night_price': 130},
       {'room_number': 26,
         'floor': 50, 
         'night_price': 150}
    ]
}
print(hotel_dictionary['rooms'])

for room in hotel_dictionary.keys():
    print(room)

