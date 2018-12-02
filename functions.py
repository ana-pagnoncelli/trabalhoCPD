import re
import pickle
from classes import *
import sys
import os
import struct
import encodings, os
from encodings import aliases
import base64

def format_string(string):
    last_caractere = ord(string[-1:])
    if last_caractere == 9792:
        string = string[:-1]
        string =  string + 'A'
    if last_caractere == 9794:
        string = string[:-1]
        string = string + 'O'
    return "{:<50}".format(string.lower())
#returns the list_objs_type atualized and the obj_type
def create_type(type_name, list_objs_type):
    id = 1 #save the id number
    #serch in the saved objects if this type_name is already registered
    for obj_type in list_objs_type:
        #if it finds a record with the same name, then it's registred and only takes the existent id
        if type_name == obj_type.name:
            return obj_type, list_objs_type
        id = id + 1
    #else a new obj is created with the type_name and added to the list.
    list_of_ids = [0] * 250 
    type = Type(id, type_name, list_of_ids)
    list_objs_type.append(type)

    return type, list_objs_type

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
    if is_legendary == 'True':
        is_legendary = 1
    else:
        is_legendary = 0
    color = format_string(wordList[13])
    has_gender = wordList[14]
    if has_gender == 'True':
        has_gender = 1
    else:
        has_gender = 0

    if wordList[15]:
        pr_male = float(wordList[15])
    else:
        pr_male = float(0)
    if wordList[16] and wordList[16] != 'Undiscovered':
        egg_group_1 = format_string(wordList[16])
    else:
        egg_group_1 = None

    if wordList[17] and wordList[17] != 'Undiscovered':
        egg_group_2 = format_string(wordList[17])
    else:
        egg_group_2 = None

    has_mega_evolution = wordList[18]
    if has_mega_evolution == 'True':
        has_mega_evolution = 1
    else:
        has_mega_evolution = 0
    height = float(wordList[19])
    weight = float(wordList[20])
    catch_rate = float(wordList[21])

    body_style = format_string(wordList[22])

    aux_class = AuxiliarClass(id, name, type_1, type_2, total, hp, attack, defense,
                            sp_attack, sp_defense, speed, generation, is_legendary,
                            color, has_gender, pr_male, egg_group_1, egg_group_2,
                            has_mega_evolution, height, weight, catch_rate, body_style)

    return aux_class

def create_pokemon(aux_class, list_objs_pokemon):
    type_array = [0]*4
    pokemon = Pokemon(aux_class.id, aux_class.name, aux_class.total, aux_class.hp,
                        aux_class.attack, aux_class.defense, aux_class.sp_attack,
                        aux_class.sp_defense, aux_class.speed, aux_class.generation,
                        aux_class.is_legendary, aux_class.color, aux_class.has_gender,
                        aux_class.pr_male, aux_class.has_mega_evolution, aux_class.height,
                        aux_class.weight, aux_class.catch_rate, aux_class.body_style, type_array)

    return pokemon, list_objs_pokemon

def create_pokemon_type(id_pokemon_type, pokemon_id, type_id, list_objs_pokemon_type,
                        list_objs_type, relation):
    pokemon_type = PokemonType(id_pokemon_type, pokemon_id, type_id, relation)
    list_objs_pokemon_type.append(pokemon_type)
    return pokemon_type, list_objs_pokemon_type

def assing_all_types(pokemon_type_id, pokemon, aux_class, list_objs_pokemon_type, list_objs_type):
    new_type, list_objs_type = create_type(aux_class.type_1, list_objs_type)
    new_pokemon_type, list_objs_pokemon_type = create_pokemon_type(pokemon_type_id,
                                                                    pokemon.id,
                                                                    new_type.id,
                                                                    list_objs_pokemon_type,
                                                                    list_objs_type,
                                                                    1)
    pokemon.id_pokemon_type[0] = int(new_pokemon_type.id)
    pokemon_type_id = pokemon_type_id + 1
    list_objs_type[new_type.id-1].id_pokemon_type.append(new_pokemon_type.id)
    list_objs_type[new_type.id-1].id_pokemon_type.pop(0)

    if aux_class.type_2:
        new_type, list_objs_type = create_type(aux_class.type_2, list_objs_type)
        new_pokemon_type, list_objs_pokemon_type = create_pokemon_type(pokemon_type_id,
                                                                        pokemon.id,
                                                                        new_type.id,
                                                                        list_objs_pokemon_type,
                                                                        list_objs_type,
                                                                        1)
        pokemon.id_pokemon_type[1] = int(new_pokemon_type.id)
        list_objs_type[new_type.id-1].id_pokemon_type.append(new_pokemon_type.id)
        list_objs_type[new_type.id-1].id_pokemon_type.pop(0)
        pokemon_type_id = pokemon_type_id + 1
    if aux_class.egg_group_1:
        new_type, list_objs_type = create_type(aux_class.egg_group_1, list_objs_type)
        new_pokemon_type, list_objs_pokemon_type = create_pokemon_type(pokemon_type_id,
                                                                        pokemon.id,
                                                                        new_type.id,
                                                                        list_objs_pokemon_type,
                                                                        list_objs_type,
                                                                        0)
        pokemon.id_pokemon_type[2] = int(new_pokemon_type.id)
        list_objs_type[new_type.id-1].id_pokemon_type.append(new_pokemon_type.id)
        list_objs_type[new_type.id-1].id_pokemon_type.pop(0)
        pokemon_type_id = pokemon_type_id + 1
    if aux_class.egg_group_2:
        new_type, list_objs_type = create_type(aux_class.egg_group_2, list_objs_type)
        new_pokemon_type, list_objs_pokemon_type = create_pokemon_type(pokemon_type_id,
                                                                        pokemon.id,
                                                                        new_type.id,
                                                                        list_objs_pokemon_type,
                                                                        list_objs_type,
                                                                        0)
        pokemon.id_pokemon_type[3] = int(new_pokemon_type.id)
        list_objs_type[new_type.id-1].id_pokemon_type.append(new_pokemon_type.id)
        list_objs_type[new_type.id-1].id_pokemon_type.pop(0)
        pokemon_type_id = pokemon_type_id + 1

    return pokemon, list_objs_pokemon_type, list_objs_type, pokemon_type_id

def create_has_gender(pokemon_id, pokemon_name, list_objs_has_gender):
    new_has_gender = HasGender(pokemon_id, pokemon_name)
    list_objs_has_gender.append(new_has_gender)
    return list_objs_has_gender

def create_has_mega_evolution(pokemon_id, pokemon_name, list_objs_has_mega_evolution):
    new_has_mega_evolution = HasMegaEvolution(pokemon_id, pokemon_name)
    list_objs_has_mega_evolution.append(new_has_mega_evolution)
    return list_objs_has_mega_evolution

def create_is_legendary(pokemon_id, pokemon_name, list_objs_is_legendary):
    new_is_legendary = IsLgendary(pokemon_id, pokemon_name)
    list_objs_is_legendary.append(new_is_legendary)
    return list_objs_is_legendary

def assing_all_boolean_tables(aux_class, list_objs_has_gender, list_objs_is_legendary, 
                              list_objs_has_mega_evolution):
    if aux_class.has_gender == 1:
        list_objs_has_gender = create_has_gender(aux_class.id, aux_class.name, list_objs_has_gender)
    if aux_class.is_legendary == 1:
        list_objs_is_legendary = create_is_legendary(aux_class.id, aux_class.name, list_objs_is_legendary)
    if aux_class.has_mega_evolution == 1:
        list_objs_has_mega_evolution = create_has_mega_evolution(aux_class.id, aux_class.name, list_objs_has_mega_evolution)
    return list_objs_has_gender, list_objs_is_legendary, list_objs_has_mega_evolution

def save_data_file():
    list_objs_type = []
    list_objs_pokemon = []
    list_objs_pokemon_type = []
    list_objs_has_gender = []
    list_objs_is_legendary = []
    list_objs_has_mega_evolution = []
    pokemon_type_id = 1
    with open("data/pokemons.csv") as file:
        for line in file:
            wordList = line.split(',')
            if wordList[0] != 'Number':
                auxiliar_class = assing_attributes_auxiliar_class(wordList)

                new_pokemon, list_objs_pokemon = create_pokemon(auxiliar_class, list_objs_pokemon)
                pokemon, list_objs_pokemon_type, list_objs_type, pokemon_type_id = assing_all_types(pokemon_type_id,
                                                                                                            new_pokemon,
                                                                                                            auxiliar_class,
                                                                                                            list_objs_pokemon_type,
                                                                                                            list_objs_type)

                list_objs_has_gender, list_objs_is_legendary, list_objs_has_mega_evolution = assing_all_boolean_tables(auxiliar_class,
                                                                                                                        list_objs_has_gender,
                                                                                                                        list_objs_is_legendary,
                                                                                                                        list_objs_has_mega_evolution)
                list_objs_pokemon.append(pokemon)
    return list_objs_pokemon_type, list_objs_type, list_objs_pokemon, list_objs_has_gender, list_objs_is_legendary, list_objs_has_mega_evolution
 
def creating_arqs(list_objs_pokemon_type, list_objs_type, list_objs_pokemon, list_objs_has_gender, 
                list_objs_is_legendary, list_objs_has_mega_evolution):

    with open("data/list_objs_pokemon.bin","ab") as file:
        for pokemon in list_objs_pokemon:
            file.write(struct.pack("i", pokemon.id))
            file.write(pokemon.name.encode("utf-8"))
            file.write(struct.pack("i", pokemon.total))
            file.write(struct.pack("i", pokemon.hp))
            file.write(struct.pack("i", pokemon.defense))
            file.write(struct.pack("i", pokemon.attack))
            file.write(struct.pack("i", pokemon.sp_attack))
            file.write(struct.pack("i", pokemon.sp_defense))
            file.write(struct.pack("i", pokemon.speed))
            file.write(struct.pack("i", pokemon.generation))
            file.write(struct.pack("i", pokemon.is_legendary))
            file.write(pokemon.color.encode("utf-8"))
            file.write(struct.pack("i", pokemon.has_gender))
            file.write(struct.pack("f", pokemon.pr_male))
            file.write(struct.pack("i", pokemon.has_mega_evolution))
            file.write(struct.pack("f", pokemon.height))
            file.write(struct.pack("f", pokemon.weight))
            file.write(struct.pack("f", pokemon.catch_rate))
            file.write(pokemon.body_style.encode("utf-8"))
            for id_pokemon_type in pokemon.id_pokemon_type:
                file.write(struct.pack("i", id_pokemon_type))
        file.close()

    with open("data/list_objs_has_gender.bin","ab") as file:
        for has_gender in list_objs_has_gender:
            file.write(struct.pack("i", int(has_gender.id_pokemon)))
            file.write(has_gender.pokemon_name.encode("utf-8"))
        file.close()


    with open("data/list_objs_has_mega_evolution.bin", "ab") as file:
        for has_mega_evolution in list_objs_has_mega_evolution:
            file.write(struct.pack("i", has_mega_evolution.id_pokemon))
            file.write(has_mega_evolution.pokemon_name.encode("utf-8"))
        file.close()

    
    with open("data/list_objs_is_legendary.bin", "ab") as file:
        for is_legendary in list_objs_is_legendary:
            file.write(struct.pack("i", is_legendary.id_pokemon))
            file.write(is_legendary.pokemon_name.encode("utf-8"))
        file.close()


    with open("data/list_objs_pokemon_type.bin", "ab") as file:
        for pokemon_type in list_objs_pokemon_type:
            file.write(struct.pack("i", pokemon_type.id))
            file.write(struct.pack("i", pokemon_type.id_pokemon))
            file.write(struct.pack("i", pokemon_type.id_type))
            file.write(struct.pack("i", pokemon_type.relation))
        file.close()


    with open("data/list_objs_type.bin", "ab") as file:
        for type in list_objs_type:
            file.write(struct.pack("i", type.id))
            file.write(type.name.encode("utf-8"))
            for id_pokemon_type in type.id_pokemon_type:
                file.write(struct.pack("i", id_pokemon_type))
        file.close()


def read_booleans_arqs(arq):
    with open (arq, 'rb') as file:
        file.seek(54*5)
        id = struct.unpack('i', file.read(4))[0]
        print(id)
        pokemon_name = ''
        i = 0
        while i < 50:
            temp = struct.unpack('c', file.read(1))[0]
            temp = temp.decode('utf-8')
            pokemon_name = pokemon_name + temp
            i += 1
        print(pokemon_name)


def read_arq_pokemons():
    with open ('data/list_objs_pokemon.bin', 'rb') as file:
        file.seek(230*633)

        id = struct.unpack('i', file.read(4))[0]
        print(id)
        name = ''
        i = 0
        while i < 50:
            temp = struct.unpack('c', file.read(1))[0]
            temp = temp.decode('utf-8')
            name = name + temp
            i += 1
        print(name)
        total = struct.unpack('i', file.read(4))[0]        
        print(total)
        hp = struct.unpack('i', file.read(4))[0] 
        print(hp)
        defense = struct.unpack('i', file.read(4))[0] 
        print(defense)
        attack = struct.unpack('i', file.read(4))[0] 
        print(attack)
        sp_defense = struct.unpack('i', file.read(4))[0] 
        print(sp_defense)
        sp_attack = struct.unpack('i', file.read(4))[0] 
        print(sp_attack)
        speed = struct.unpack('i', file.read(4))[0] 
        print(speed)
        generation = struct.unpack('i', file.read(4))[0] 
        print(generation)
        is_legendary = struct.unpack('i', file.read(4))[0] 
        print(is_legendary)
        color = ''
        i = 0
        while i < 50:
            temp = struct.unpack('c', file.read(1))[0]
            temp = temp.decode('utf-8')
            color = color + temp
            i += 1
        print(color)
        has_gender = struct.unpack('i', file.read(4))[0] 
        print(has_gender)
        pr_male = struct.unpack('f', file.read(4))[0] 
        print(pr_male)
        has_mega_evolution = struct.unpack('i', file.read(4))[0] 
        print(has_mega_evolution)
        height = struct.unpack('f', file.read(4))[0] 
        print(height)
        weight = struct.unpack('f', file.read(4))[0] 
        print(weight)
        catch_rate = struct.unpack('f', file.read(4))[0] 
        print(catch_rate)
        body_style = ''
        i = 0
        while i < 50:
            temp = struct.unpack('c', file.read(1))[0]
            temp = temp.decode('utf-8')
            body_style = body_style + temp
            i += 1
        print(body_style)
        i = 0
        list_of_ids_pokemon_type = []
        while i < 4:
            id_pokemon_type = struct.unpack('i', file.read(4))[0]
            list_of_ids_pokemon_type.append(id_pokemon_type)
            i = i+1
        print(list_of_ids_pokemon_type)

def read_arq_pokemon_types():
    with open ('data/list_objs_pokemon_type.bin', 'rb') as file:
        file.seek(16*1000)
        id = struct.unpack('i', file.read(4))[0]
        id_pokemon = struct.unpack('i', file.read(4))[0]
        id_type = struct.unpack('i', file.read(4))[0]
        relation = struct.unpack('i', file.read(4))[0]
        print(id, id_pokemon, id_type, relation)

def read_arq_types():
    with open ('data/list_objs_type.bin', 'rb') as file:
        file.seek(1054*21)
        id = struct.unpack('i', file.read(4))[0]
        name = ''
        i = 0
        while i < 50:
            temp = struct.unpack('c', file.read(1))[0]
            temp = temp.decode('utf-8')
            name = name + temp
            i += 1
        i = 0
        list_ids_pokemon_type = []
        while i < 250:
            id_pokemon_type = struct.unpack('i', file.read(4))[0]
            list_ids_pokemon_type.append(id_pokemon_type)
            i = i + 1
        
        print(id, name, list_ids_pokemon_type)