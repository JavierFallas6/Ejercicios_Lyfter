import csv

def save_games(file_path, data):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        headers = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

def request_games():
    counter = 1
    list_games = []
    number_of_games = int(input("Ingrese el numero de juegos que desea agregar: "))
    while counter <= number_of_games:
        name = input(f"Ingrese el nombre del juego {counter}: ")
        genre = input(f"Ingrese el genero del juego {counter}: ")
        developer = input(f"Ingrese el desarrollador del juego {counter}: ")
        esrb_rating = input(f"Ingrese el clasificacion ESRB del juego {counter}: ")

        game_data = {"Nombre":name,"Genero":genre,"Desarrollador":developer,"Clasificacion ESRB":esrb_rating}
        list_games.append(game_data)

        counter += 1
    return list_games

def main():
    games = request_games()
    save_games('games_classification.csv', games)
    print("Done")

if __name__ == '__main__':  
    main()