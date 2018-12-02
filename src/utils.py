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

def print_string(string):
    print(string.rstrip())