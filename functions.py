import re
from classes import *

def format_string(string):
    return "{:<50}".format(string.lower())

#returns the list_objs_type atualized and the obj_type
def assing_type(type_name, list_objs_type):
    id = 1 #save the id number
    #serch in the saved objects if this type_name is already registered
    for obj_type in list_objs_type:
        print(obj_type)
        #if it finds a record with the same name, then it's registred and only takes the existent id
        if type_name == obj_type.name:
            return obj_type.id, list_objs_type
        id = id + 1
    #else a new obj is created with the type_name and added to the list.
    list_of_ids = [0] * 200
    type = Type(id, type_name, list_of_ids)
    list_objs_type.append(type)

    return type.id, list_objs_type

def assing_attributes_auxiliar_class(wordList):
    id = int(wordList[0])
    name = format_string(wordList[1])
    type_1 = format_string(wordList[2])

    if wordList[3]:
        type_2 = format_string(wordList[3])
    else:
        type_2 = None

    total = int(wordList[4])
    hp = int(wordList[5])
    attack = int(wordList[6])
    defense = int(wordList[7])
    sp_attack = int(wordList[8])
    sp_defense = int(wordList[9])
    speed = int(wordList[10])
    generation = int(wordList[11])
    is_legendary = wordList[12]
    color = format_string(wordList[13])
    has_gender = wordList[14]

    if wordList[15]:
        pr_male = wordList[15]
    else:
        pr_male = 0
    if wordList[16]:
        egg_group_1 = format_string(wordList[16])
    else:
        egg_group_1 = None

    if wordList[17]:
        egg_group_2 = format_string(wordList[17])
    else:
        egg_group_2 = None

    has_mega_evolution = wordList[18]
    height = float(wordList[19])
    weight = float(wordList[20])
    catch_rate = float(wordList[21])

    body_style = format_string(wordList[22])

    aux_class = AuxiliarClass(id, name, type_1, type_2, total, hp, attack, defense,
                            sp_attack, sp_defense, speed, generation, is_legendary,
                            color, has_gender, pr_male, egg_group_1, egg_group_2,
                            has_mega_evolution, height, weight, catch_rate, body_style)

    return aux_class

def assing_pokemon(aux_class, list_objs_pokemon):
    type_array = [0]*4
    pokemon = Pokemon(aux_class.id, aux_class.name, aux_class.total, aux_class.hp,
                        aux_class.attack, aux_class.defense, aux_class.sp_attack,
                        aux_class.sp_defense, aux_class.speed, aux_class.generation,
                        aux_class.is_legendary, aux_class.color, aux_class.has_gender,
                        aux_class.pr_male, aux_class.has_mega_evolution, aux_class.height,
                        aux_class.weight, aux_class.catch_rate, aux_class.body_style, type_array)

    print(pokemon)
    list_objs_pokemon.append(pokemon)
    return pokemon.id, list_objs_pokemon

def assing_pokemon_type(id_pokemon_type, pokemon_id, type_id, list_objs_pokemon_type, relation):
    pokemon_type = PokemonType(id_pokemon_type, pokemon_id, type_id, relation)
    list_objs_pokemon_type.append(pokemon_type)
    # print(pokemon_type)
    return pokemon_type, list_objs_pokemon_type

def save_data_file():
    list_objs_type = []
    list_objs_pokemon = []
    list_objs_pokemon_type = []
    pokemon_type_id = 1
    with open("data/pokemons.csv") as file:
        for line in file:
            wordList = line.split(',')
            if wordList[0] != 'Number':
                auxiliar_class = assing_attributes_auxiliar_class(wordList)
                type_id, list_objs_type = assing_type(auxiliar_class.type_1, list_objs_type)
                pokemon_id, list_objs_pokemon = assing_pokemon(auxiliar_class, list_objs_pokemon)
                new_pokemon_type, list_objs_pokemon_type = assing_pokemon_type(pokemon_type_id,
                                                                                pokemon_id,
                                                                                type_id,
                                                                                list_objs_pokemon_type,
                                                                                'type')
                pokemon_type_id = pokemon_type_id + 1
                # print(list_objs_pokemon_type)
        print(list_objs_pokemon_type)
        print(list_objs_type)
