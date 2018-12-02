from src.binary_files_functions import *
from src.reading_data import *

if __name__ == "__main__":
    list_objs_pokemon_type, list_objs_type, list_objs_pokemon, list_objs_has_gender, list_objs_is_legendary, list_objs_has_mega_evolution = save_data_file()
    creating_arqs(list_objs_pokemon_type, list_objs_type, list_objs_pokemon, list_objs_has_gender, list_objs_is_legendary, list_objs_has_mega_evolution)
    list_of_pokemons_names = read_booleans_arqs("data/list_objs_has_mega_evolution.bin")
    for name in list_of_pokemons_names:
        print_string(name)
    # pokemon = read_arq_pokemons(8)
    # pokemon_type = read_arq_pokemon_types(8)
    # type = read_arq_types(2)