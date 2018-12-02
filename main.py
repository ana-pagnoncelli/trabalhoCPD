from src.binary_files_functions import *
from src.reading_data import *
from src.ui import *
from src.trie import *
import os

if __name__ == "__main__":
    list_objs_pokemon_type, list_objs_type, list_objs_pokemon, list_objs_has_gender, list_objs_is_legendary, list_objs_has_mega_evolution = save_data_file()
    creating_arqs(list_objs_pokemon_type, list_objs_type, list_objs_pokemon, list_objs_has_gender, list_objs_is_legendary, list_objs_has_mega_evolution)
    raiz_trie = runTrie(list_objs_pokemon)
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
            if type:
                list_ids_pokemon_type = remove_zeros_from_array(type.id_pokemon_type)
                for id_pokemon_type in list_ids_pokemon_type:
                    pokemon_type = read_arq_pokemon_types(id_pokemon_type)
                    pokemon = read_arq_pokemons(pokemon_type.id_pokemon)
                    if pokemon_type.relation == 0:
                        print(pokemon.name, 'Egg Group')
                    else:
                        print(pokemon.name, 'Type')
            else:
                print('Tipo inválido!')
            operacao = menu_nova_operacao()
        
    
    # print(id)
    # list_of_pokemons_names = read_booleans_arqs("data/list_objs_has_mega_evolution.bin")
    # for name in list_of_pokemons_names:
    #     print_string(name)
    # pokemon = read_arq_pokemons(8)
    # pokemon_type = read_arq_pokemon_types(8)
    # type = read_arq_types(2)