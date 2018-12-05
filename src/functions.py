from src.utils import clear
import struct
from src.reading_data import *
from src.binary_files_functions import *
from src.classes.type import Type
import os
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
    with open("data/list_objs_pokemon.bin","r+b") as file:
        file.write(struct.pack("i", numero_pokemon+1))
        print(numero_pokemon+1)
    file.close()
    word_list = [numero_pokemon+1, name, type_1, type_2, total, hp, attack,
                defense, sp_attack, sp_defense, speed, generation, is_legendary,
                color, has_gender, pr_male, egg_group_1, egg_group_2, has_mega_evolution,
                height, weight, cath_rate, body_style]
    aux_class = assing_attributes_auxiliar_class(word_list)

    newType = find_type_by_name(aux_class.type_1)
    size = os.path.getsize("data/list_objs_pokemon_type.bin")
    newPokeTypeId = int(size/16)
    if (not newType):
        size = os.path.getsize("data/list_objs_type.bin")
        with open ('data/list_objs_type.bin', 'ab') as file:
            newId = int(size/1054)
            newType = Type(newId, aux_class.type_1, [0] *249 + [newPokeTypeId])
            file.write(struct.pack("i", int(newType.id)))
            file.write(newType.name.encode("utf-8"))
            for id_pokemon_type in newType.id_pokemon_type:
                file.write(struct.pack("i", int(id_pokemon_type)))
            file.close()
    else:
        with open ('data/list_objs_type.bin', 'r+b') as file:
            file.seek((newType.id-1) * 1054)
            newType.id_pokemon_type.pop(0)
            newType.id_pokemon_type.append(newPokeTypeId)
            file.write(struct.pack("i", int(newType.id)))
            file.write(newType.name.encode("utf-8"))
            for id_pokemon_type in newType.id_pokemon_type:
                file.write(struct.pack("i", int(id_pokemon_type)))
            file.close()
    with open ('data/list_objs_pokemon_type.bin', 'ab') as file:
        file.write(struct.pack("i", newPokeTypeId))
        file.write(struct.pack("i", aux_class.id))
        file.write(struct.pack("i", newType.id))
        file.write(struct.pack("i", 0))
        file.close()
    newType = find_type_by_name(aux_class.type_2)
    oldPokeType = newPokeTypeId
    newPokeTypeId += 1
    if (not newType):
        size = os.path.getsize("data/list_objs_type.bin")
        with open ('data/list_objs_type.bin', 'ab') as file:
            newId = int(size/1054)
            newType = Type(newId, aux_class.type_2, [0] *249 + [newPokeTypeId])
            file.write(struct.pack("i", int(newType.id)))
            file.write(newType.name.encode("utf-8"))
            for id_pokemon_type in newType.id_pokemon_type:
                file.write(struct.pack("i", int(id_pokemon_type)))
            file.close()
    else:
        with open ('data/list_objs_type.bin', 'r+b') as file:
            file.seek((newType.id-1) * 1054)
            newType.id_pokemon_type.pop(0)
            newType.id_pokemon_type.append(newPokeTypeId)
            file.write(struct.pack("i", int(newType.id)))
            file.write(newType.name.encode("utf-8"))
            for id_pokemon_type in newType.id_pokemon_type:
                file.write(struct.pack("i", int(id_pokemon_type)))
            file.close()
    with open ('data/list_objs_pokemon_type.bin', 'ab') as file:
        file.write(struct.pack("i", newPokeTypeId))
        file.write(struct.pack("i", aux_class.id))
        file.write(struct.pack("i", newType.id))
        file.write(struct.pack("i", 0))
        file.close()
    if (not aux_class.has_gender):
        size = os.path.getsize("data/list_objs_has_gender.bin")
        with open ('data/list_objs_type.bin', 'ab') as file:
            file.write(struct.pack("i", int(aux_class.id)))
            file.write(aux_class.name.encode("utf-8"))
            file.close()
    if (not aux_class.has_mega_evolution):
        size = os.path.getsize("data/list_objs_has_mega_evolution.bin")
        with open ('data/list_objs_type.bin', 'ab') as file:
            file.write(struct.pack("i", aux_class.id))
            file.write(aux_class.name.encode("utf-8"))
            file.close()
    if (not aux_class.is_legendary):
        size = os.path.getsize("data/list_objs_is_legendary.bin")
        with open ('data/list_objs_type.bin', 'ab') as file:
            file.write(struct.pack("i", aux_class.id))
            file.write(aux_class.name.encode("utf-8"))
            file.close()
    aux_class.id_pokemon_type = [oldPokeType, newPokeTypeId]
    with open("data/list_objs_pokemon.bin","ab") as file:
        file.write(struct.pack("i", aux_class.id))
        file.write(aux_class.name.encode("utf-8"))
        file.write(struct.pack("i", aux_class.total))
        file.write(struct.pack("i", aux_class.hp))
        file.write(struct.pack("i", aux_class.defense))
        file.write(struct.pack("i", aux_class.attack))
        file.write(struct.pack("i", aux_class.sp_attack))
        file.write(struct.pack("i", aux_class.sp_defense))
        file.write(struct.pack("i", aux_class.speed))
        file.write(struct.pack("i", aux_class.generation))
        file.write(struct.pack("i", aux_class.is_legendary))
        file.write(aux_class.color.encode("utf-8"))
        file.write(struct.pack("i", aux_class.has_gender))
        file.write(struct.pack("f", aux_class.pr_male))
        file.write(struct.pack("i", aux_class.has_mega_evolution))
        file.write(struct.pack("f", aux_class.height))
        file.write(struct.pack("f", aux_class.weight))
        file.write(struct.pack("f", aux_class.catch_rate))
        file.write(aux_class.body_style.encode("utf-8"))
        for id_pokemon_type in aux_class.id_pokemon_type:
            file.write(struct.pack("i", id_pokemon_type))
        file.close()
    return aux_class.name, aux_class.id