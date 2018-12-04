from src.utils import remove_spaces

"""
Pokemon:
    Contains all the details of a pokemon.
"""


class Pokemon:
    def __init__(self, id, name, total, hp, attack, defense, sp_attack, sp_defense, speed,
                generation, is_legendary, color, has_gender, pr_male, has_mega_evolution,
                height, weight, catch_rate, body_style, id_pokemon_type):
        """
            Attribute: what is that? (type).

            id: Id of the Pokemon (Integer).
            name: Name of the Pokemon (string).
            total: Total points of the Pokemon (Integer).
            hp: Total life of the Pokemon (Integer).
            attack: Total attack of the Pokemon (Integer).
            defense: Total defense of the Pokemon (Integer).
            sp_attack: Attack speed (Integer).
            sp_defense: Defense speed (Integer).
            spped: Total speed (Integer).
            generation: Generation of the Pokemon (Integer).
            is_legendary: Is lengendary or not(boolean).
            color: The color of the Pokemon (string).
            has_gender: Has gender or not (boolean).
            pr_male: Percentege of being male (float).
            has_mega_evolution: Has mega evolution or not (boolean).
            height: The height of the Pokemon (float).
            weight: The weight of the Pokemon (float).
            catch_rate: The catch rate of the Pokemon (float).
            body_style: The body_style of the Pokemon (string).

            id_pokemon_type: Representing the fields Egg_Group_1, Egg_Group_2, Type_1 and Type_2,
            this field has an array with ids. This ids come from objects of the class pokemon_type,
            that makes a relation between the objects of the class Pokemon and objects of the class type.
            (array of integers).
        """
        self.id = id
        self.name = name
        self.total = total
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed
        self.generation = generation
        self.is_legendary = is_legendary
        self.color = color
        self.has_gender = has_gender
        self.pr_male = pr_male
        self.has_mega_evolution = has_mega_evolution
        self.height = height
        self.weight = weight
        self.catch_rate = catch_rate
        self.body_style = body_style
        self.id_pokemon_type = id_pokemon_type

        #prints the class
    def __repr__(self):
        
        if self.is_legendary == 1:
            is_leg_name = 'True'
        else:
            is_leg_name = 'False'
        if self.has_gender == 1:
            has_gender_name = 'True'
        else:
            has_gender_name = 'False'
        if self.has_mega_evolution == 1:
            mega_evolution_name = 'True'
        else:
            mega_evolution_name = 'False'

        return "Pokemon\n\nId: {id}  \nName: {name} \nTotal: {total} \nHp: {hp} \nAttack: {attack} \
                \nDefense: {defense} \nAttack Speed: {sp_attack} \nDefense Speed:{sp_defense}\
                \nSpeed: {speed} \nGeneration: {generation} \nLegendary: {is_legendary}\
                \nColor: {color} \nHas Gender: {has_gender} \nPercentage of being male: {pr_male}\
                \nHas mega evolution: {has_mega_evolution} \nHeight: {height}\
                \nWeight: {weight} \nCatch Rate: {catch_rate} \nBody Style: {body_style}\
                \nId Pokemon Type: {id_pokemon_type}"\
                .format(id=self.id, name=self.name, total=self.total, hp=self.hp,
                attack=self.attack, defense=self.defense, sp_attack=self.sp_attack,
                sp_defense=self.sp_defense, speed=self.speed, generation=self.generation,
                is_legendary=is_leg_name, color=self.color, has_gender=has_gender_name,
                pr_male=self.pr_male, has_mega_evolution=mega_evolution_name,
                height=self.height, weight=self.weight, catch_rate=self.catch_rate,
                body_style=remove_spaces(self.body_style), id_pokemon_type=self.id_pokemon_type)
