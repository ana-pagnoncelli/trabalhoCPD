from src.utils import clear
import struct
from src.binary_files_functions import *
from src.reading_data import *

def informacoes_novo_pokemon():
    clear()
    print("Insira os dados do seu pokemon!")
    print("\nNome: ")
    name = str(input())
    print("\nType 1: ")
    type_1 = str(input())
    print("\nType_2: ")
    type_2 = str(input())
    print("\nPontos totais: ")
    total = int(input())
    print("\nVida: ")
    hp = int(input())
    print("\nAtaque: ")
    attack = int(input())
    print("\nDefesa: ")
    defense = int(input())
    print("\nVelocidade de ataque: ")
    sp_attack = int(input())
    print("\nVelocidade de defesa: ")
    sp_defense = int(input())
    print("\nVelocidade: ")
    speed = int(input())
    print("\nGeração: ")
    generation = int(input())
    print("\nÉ lendário? True ou False")
    is_legendary = str(input())
    print("\nCor: ")
    color = str(input())
    print("\nTem genero? True ou False")
    has_gender = str(input())
    print("\nPorcentagem de ser macho: ")
    pr_male = float(input())
    print("\nTipo de ovo 1: ")
    egg_group_1 = str(input())
    print("\nTipo de ovo 2: ")
    egg_group_2 = str(input())
    print("\nTem mega evolução? True ou False ")
    has_mega_evolution = str(input())
    print("\nAltura: ")
    height = float(input())
    print("\nPeso:")
    weight = float(input())
    print("\nPorcentagem de pegar: ")
    cath_rate = float(input())
    print("\nComo é o corpo dele: ")
    body_style = str(input())

    with open("data/list_objs_pokemon.bin","rb") as file:
        numero_pokemon = struct.unpack('i', file.read(4))[0]
    file.close()
    with open("data/list_objs_pokemon.bin","wb") as file:
        file.write(struct.pack("i", numero_pokemon+1))
        print(numero_pokemon+1)
    file.close()
    word_list = [numero_pokemon+1, name, type_1, type_2, total, hp, attack,
                defense, sp_attack, sp_defense, speed, generation, is_legendary,
                color, has_gender, pr_male, egg_group_1, egg_group_2, has_mega_evolution,
                height, weight, cath_rate, body_style]
    aux_class = assing_attributes_auxiliar_class(word_list)

    print(aux_class)


def remove_pokemon(pokemon_id):
    with open("data/list_objs_pokemon.bin","rb") as file:
        numero_pokemon = struct.unpack('i', file.read(4))[0]
    file.close()
    with open("data/list_objs_pokemon.bin","r+b") as file:
        file.seek(0)
        file.write(struct.pack("i", numero_pokemon-1))
    file.close()
    pokemon = read_arq_pokemons(numero_pokemon-1)
    print("pokemon_substituto")
    print(pokemon)

    pokemon_anterior = read_arq_pokemons(pokemon_id)
    print("pokemon_anterior")
    print(pokemon_anterior)
    
    with open("data/list_objs_pokemon.bin","r+b") as file:
        file.seek(0)
        file.seek((230*(pokemon_id-1)) + 4)
        file.write(struct.pack("i", pokemon_id))
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

    return pokemon.name
