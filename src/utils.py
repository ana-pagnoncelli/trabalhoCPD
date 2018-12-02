import os

def format_string(string):
    last_caractere = ord(string[-1:])
    if last_caractere == 9792:
        string = string[:-1]
        string =  string + 'A'
    if last_caractere == 9794:
        string = string[:-1]
        string = string + 'O'
    new_string = ''
    for caractere in string:
        if caractere == 'é':
            new_string = new_string + 'e'
        else:
            new_string = new_string + caractere
    return "{:<50}".format(new_string.lower())
#returns the list_objs_type atualized and the obj_type

def print_string(string):
    print(string.rstrip())

def remove_spaces(string):
    return string.rstrip()

def clear():
    return os.system('clear')

def remove_zeros_from_array(list_of_ids_pokemon_type):
    new_list_of_ids = []
    for i in range(len(list_of_ids_pokemon_type)):
        if list_of_ids_pokemon_type[i] != 0:
            new_list_of_ids.append(list_of_ids_pokemon_type[i])
    return new_list_of_ids
