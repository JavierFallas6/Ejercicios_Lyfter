import json

def read_json(path):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data   

def request_pokemon_data():

    print("Type following information to add a new pokemon")
    pokemon_name = input("name of pokemon: ")
    pokemon_type = input("type of pokemon: ")
    pokemon_level = input("level of pokemon: ")
    pokemon_weight = input("weight in kg of pokemon: ")
    is_shiny_value = input("is shiny, true or false: ")
    held_item_value = input("held item: ")
    pokemon_skills = skills_values_funtion()
    pokemon_stats = stats_values_funtion()
    
    new_pokemon =    {
      "name": pokemon_name,
      "type":pokemon_type,
      "level":int(pokemon_level),
      "weight_kg":float(pokemon_weight),
      "is_shiny":bool(is_shiny_value),
      "held_item":held_item_value,
      "skills":pokemon_skills,
      "stats":pokemon_stats}

    return new_pokemon

def skills_values_funtion():
    counter = 1
    list_skills = []
    number_of_skills = int(input("how many skill do you need to add: "))

    while counter <= number_of_skills:
        new_skill = input(f"pokemon skill number {counter}: ")
        list_skills.append(new_skill)

        counter += 1
    return list_skills

def stats_values_funtion():
    print("Please type following stats")
    hp_value = input("hp value: ")
    attack_value = input("attack value: ")
    defense_value = input("defense value: ")
    sp_attack_value = input("sp attack value: ")
    sp_defense_value = input("sp defense value: ")
    speed = input("speed value: ")

    new_pokemon_stats =    {
      "hp": float(hp_value),
      "attack":float(attack_value),
      "defense":int(defense_value),
      "sp_attack":float(sp_attack_value),
      "sp_defense":float(sp_defense_value),
      "speed":float(speed)}

    return new_pokemon_stats

def number_of_pokemons():
    counter = 0
    counter_for_pokemons = int(input("Number of pokemons to add: "))
    while counter < counter_for_pokemons:
        existing_pokemons = read_json("pokemones.json")
        new_pokemon_information = request_pokemon_data()
        existing_pokemons.append(new_pokemon_information)

        save_new_pokemon("pokemones.json",existing_pokemons)
        counter +=1

def save_new_pokemon(path,data_pokemon):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data_pokemon, file, indent=4, ensure_ascii=False)

def main():
    number_of_pokemons()

if __name__ == '__main__':  
    main()
    
