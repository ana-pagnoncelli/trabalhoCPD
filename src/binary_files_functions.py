import re
import pickle
from src.classes import *
import sys
import os
import struct
import encodings, os
from encodings import aliases
import base64
from src.utils import *

def creating_arqs(list_objs_pokemon_type, list_objs_type, list_objs_pokemon, list_objs_has_gender, 
                list_objs_is_legendary, list_objs_has_mega_evolution):

    with open("data/list_objs_pokemon.bin","wb") as file:
        file.write(struct.pack("i", len(list_objs_pokemon)+1)) #cabeçalho, mostra quantos pokemons vao ter
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

    with open("data/list_objs_has_gender.bin","wb") as file:
        for has_gender in list_objs_has_gender:
            file.write(struct.pack("i", int(has_gender.id_pokemon)))
            file.write(has_gender.pokemon_name.encode("utf-8"))
        file.close()


    with open("data/list_objs_has_mega_evolution.bin", "wb") as file:
        for has_mega_evolution in list_objs_has_mega_evolution:
            file.write(struct.pack("i", has_mega_evolution.id_pokemon))
            file.write(has_mega_evolution.pokemon_name.encode("utf-8"))
        file.close()

    
    with open("data/list_objs_is_legendary.bin", "wb") as file:
        for is_legendary in list_objs_is_legendary:
            file.write(struct.pack("i", is_legendary.id_pokemon))
            file.write(is_legendary.pokemon_name.encode("utf-8"))
        file.close()


    with open("data/list_objs_pokemon_type.bin", "wb") as file:
        for pokemon_type in list_objs_pokemon_type:
            file.write(struct.pack("i", pokemon_type.id))
            file.write(struct.pack("i", pokemon_type.id_pokemon))
            file.write(struct.pack("i", pokemon_type.id_type))
            file.write(struct.pack("i", pokemon_type.relation))
        file.close()


    with open("data/list_objs_type.bin", "wb") as file:
        for type in list_objs_type:
            file.write(struct.pack("i", type.id))
            file.write(type.name.encode("utf-8"))
            for id_pokemon_type in type.id_pokemon_type:
                file.write(struct.pack("i", id_pokemon_type))
        file.close()

def read_booleans_arqs(arq):
    with open (arq, 'rb') as file:
        list_of_pokemons_names = []
        while True:
            try:
                id = struct.unpack('i', file.read(4))[0]
                pokemon_name = ''
                i = 0
                while i < 50:
                    temp = struct.unpack('c', file.read(1))[0]
                    temp = temp.decode('utf-8')
                    pokemon_name = pokemon_name + temp
                    i += 1
                list_of_pokemons_names.append(pokemon_name)
            except:
                break
        return list_of_pokemons_names

def read_arq_pokemons(id):
    with open ('data/list_objs_pokemon.bin', 'rb') as file:
        file.seek((230*(id-1)) + 4)
        try:
            id = struct.unpack('i', file.read(4))[0]
            name = ''
            print(name)
            i = 0
            while i < 50:
                temp = struct.unpack('c', file.read(1))[0]
                temp = temp.decode('utf-8')
                name = name + temp
                i += 1
            total = struct.unpack('i', file.read(4))[0]        
            hp = struct.unpack('i', file.read(4))[0] 
            defense = struct.unpack('i', file.read(4))[0] 
            attack = struct.unpack('i', file.read(4))[0] 
            sp_defense = struct.unpack('i', file.read(4))[0] 
            sp_attack = struct.unpack('i', file.read(4))[0] 
            speed = struct.unpack('i', file.read(4))[0] 
            generation = struct.unpack('i', file.read(4))[0] 
            is_legendary = struct.unpack('i', file.read(4))[0] 
            color = ''
            i = 0
            while i < 50:
                temp = struct.unpack('c', file.read(1))[0]
                temp = temp.decode('utf-8')
                color = color + temp
                i += 1
            has_gender = struct.unpack('i', file.read(4))[0] 
            pr_male = struct.unpack('f', file.read(4))[0] 
            has_mega_evolution = struct.unpack('i', file.read(4))[0] 
            height = struct.unpack('f', file.read(4))[0] 
            weight = struct.unpack('f', file.read(4))[0] 
            catch_rate = struct.unpack('f', file.read(4))[0] 
            body_style = ''
            i = 0
            while i < 50:
                temp = struct.unpack('c', file.read(1))[0]
                temp = temp.decode('utf-8')
                body_style = body_style + temp
                i += 1
            i = 0
            list_of_ids_pokemon_type = []
            while i < 4:
                id_pokemon_type = struct.unpack('i', file.read(4))[0]
                list_of_ids_pokemon_type.append(id_pokemon_type)
                i = i+1

            pokemon = Pokemon(id, name, total, hp, attack, defense, sp_attack, sp_defense,
                                speed, generation, is_legendary, color, has_gender, pr_male,
                                has_mega_evolution, height, weight, catch_rate, body_style, 
                                list_of_ids_pokemon_type)
            return pokemon
        except:
            return -1      

def read_arq_pokemon_types(id):
    with open ('data/list_objs_pokemon_type.bin', 'rb') as file:
        file.seek(16*(id-1))
        id = struct.unpack('i', file.read(4))[0]
        id_pokemon = struct.unpack('i', file.read(4))[0]
        id_type = struct.unpack('i', file.read(4))[0]
        relation = struct.unpack('i', file.read(4))[0]
        pokemon_type = PokemonType(id, id_pokemon, id_type, relation)
        return pokemon_type

def read_arq_types(id):
    with open ('data/list_objs_type.bin', 'rb') as file:
        file.seek(1054*(id-1))
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
        
        type = Type(id, name, list_ids_pokemon_type)
        return type

def find_type_by_name(type_name):
    with open ('data/list_objs_type.bin', 'rb') as file:
        name = ''
        fail = 0
        while(remove_spaces(name) != remove_spaces(type_name)):
            try:
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
            except:
                fail = 1
                break
        if fail:
            return 0
        else:
            return Type(id, name, list_ids_pokemon_type)
        