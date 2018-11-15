import re
from classes import Pokemon

def save_data_file():
    with open("data/pokemons.csv") as file:
        for line in file:
            wordList = re.sub("[^\w]", " ",  line).split()

        name = wordList[1].lower()
        type1 = wordList[2].lower()
        type2 = wordList[3].lower()
        total = int(wordList[4])
        hp = int(wordList[5])
        attack = int(wordList[6])
        defense = int(wordList[7])
        sp_attack = int(wordList[8])
        sp_defense = int(wordList[9])
        speed = int(wordList[10])
        generation = int(wordList[11])
        is_legendary = wordList[12]
        color = wordList[13].lower()
        has_gender = wordList[14]

        if wordList[15] == 'Undiscovered':
            pr_male = 0
        else:
            pr_male = wordList[15]
            
        egg_group_1 = wordList[16].lower()
        egg_group_2 = wordList[17].lower()
        has_mega_evolution = wordList[18]
        height = float(wordList[19])
        weight = float(wordList[20])
        catch_rate = float(wordList[21])
        body_style = wordList[22].lower()


        print(wordList)
        pokemon = Pokemon(id, name, total, hp, attack, defense, sp_attack, sp_defense,
                            speed, generation, is_legendary, color, has_gender, pr_male,
                            has_mega_evolution, height, weight, catch_rate, body_style, 1)
        print(pokemon)
