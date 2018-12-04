from src.binary_files_functions import *
from src.reading_data import *
from src.ui import *
from src.trie import *
from src.utils import *
from src.radix import *
import os


if __name__ == "__main__":
    operacao = menu_de_criacao_arquivos()
    list_objs_pokemon = []
    flag = 0
    if operacao == 1:
        flag = 1
        list_objs_pokemon_type, list_objs_type, list_objs_pokemon, list_objs_has_gender, list_objs_is_legendary, list_objs_has_mega_evolution = save_data_file()
        creating_arqs(list_objs_pokemon_type, list_objs_type, list_objs_pokemon, list_objs_has_gender, list_objs_is_legendary, list_objs_has_mega_evolution)
    raiz_trie = runTrie(list_objs_pokemon, flag)
    operacao = 1
    while(operacao == 1):
        operacao = menu_de_operacoes()
        if operacao == 1:
            clear()
            pokemon_name = input("Informe o nome do pokemon:")
            id = buscaTrie(raiz_trie, pokemon_name)
            if id != -1:
                pokemon = read_arq_pokemons(id)
                print(pokemon)
            operacao = menu_nova_operacao()

        if operacao == 2:
            clear()
            type_name = input("Informe o nome do tipo:")
            type = find_type_by_name(type_name)
            x = 0
            list_pokemons = []
            if type:
                list_ids_pokemon_type = remove_zeros_from_array(type.id_pokemon_type)
                for id_pokemon_type in list_ids_pokemon_type:
                    pokemon_type = read_arq_pokemon_types(id_pokemon_type)
                    pokemon = read_arq_pokemons(pokemon_type.id_pokemon)
                    list_pokemons.append(remove_spaces(pokemon.name))
                    x = x + 1
            else:
                print('Tipo inválido!')
            ordenated_list = radix_sort(list_pokemons)
            for pokemon in ordenated_list:
                print(pokemon)
            print("\nExistem " + str(x) + " pokemons de " + type_name + "\n")
            operacao = menu_nova_operacao()

        if operacao == 3:
            clear()
            list_of_pokemons_names = read_booleans_arqs("data/list_objs_is_legendary.bin")
            ordenated_list = radix_sort(list_of_pokemons_names)
            x = 0
            for pokemon_name in ordenated_list:
                print(pokemon_name)
                x = x + 1
            print("\nExistem " + str(x) + " pokemons lendários.\n")
            operacao = menu_nova_operacao()

        if operacao == 5:
            clear()
            list_of_pokemons_names = read_booleans_arqs("data/list_objs_has_gender.bin")
            ordenated_list = radix_sort(list_of_pokemons_names)
            x = 0
            for pokemon_name in ordenated_list:
                print(pokemon_name)
                x = x + 1
            print("\nExistem " + str(x) + " pokemons que tem genero.\n")
            operacao = menu_nova_operacao()
        
        if operacao == 4:
            clear()
            list_of_pokemons_names = read_booleans_arqs("data/list_objs_has_mega_evolution.bin")
            ordenated_list = radix_sort(list_of_pokemons_names)
            x = 0
            for pokemon_name in list_of_pokemons_names:
                print(pokemon_name)
                x = x + 1
            print("\nExistem " + str(x) + " pokemons que tem mega evolução.\n")
            operacao = menu_nova_operacao()

        
        if operacao == 6:
            clear()
            has_pokemon = 1
            pokemon = 1
            x = 1
            while has_pokemon:
                if pokemon != -1:
                    pokemon = read_arq_pokemons(x)
                    if pokemon != -1:
                        print(pokemon)
                else:
                    has_pokemon = 0
                x = x + 1
            operacao = menu_nova_operacao()


        if operacao == 7:
            clear()
            try:
                with open("data/list_objs_pokemon.bin","rb") as file:
                    numero_pokemon = struct.unpack('i', file.read(4))[0]
                    print(numero_pokemon)
                file.close()
                pokemon = 1
                while numero_pokemon>0:
                    if pokemon != -1:
                        pokemon = read_arq_pokemons(numero_pokemon)
                        if pokemon != -1:
                            print(pokemon)
                    else:
                        numero_pokemon = 0
                    numero_pokemon = numero_pokemon - 1
            except:
                print("\nOperação Inválida!\n")
            operacao = menu_nova_operacao()            



        

