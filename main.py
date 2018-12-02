from functions import *

if __name__ == "__main__":
    list_objs_pokemon_type, list_objs_type, list_objs_pokemon, list_objs_has_gender, list_objs_is_legendary, list_objs_has_mega_evolution = save_data_file()
    creating_arqs(list_objs_pokemon_type, list_objs_type, list_objs_pokemon, list_objs_has_gender, list_objs_is_legendary, list_objs_has_mega_evolution)
    read_booleans_arqs("data/list_objs_has_mega_evolution.bin")
    # read_arq_pokemons()
    # read_arq_pokemon_types()
    # read_arq_types()