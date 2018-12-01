from functions import *

if __name__ == "__main__":
    list_objs_pokemon_type, list_objs_type, list_objs_pokemon, list_objs_has_gender, list_objs_is_legendary, list_objs_has_mega_evolution = save_data_file()
    opening_arqs(list_objs_pokemon_type, list_objs_type, list_objs_pokemon, list_objs_has_gender, list_objs_is_legendary, list_objs_has_mega_evolution)
    read_arq_has_gender('list_objs_has_gender.bin')