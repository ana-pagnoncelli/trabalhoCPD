"""
AuxiliarClass:
    The only objective of this class is to contain all the attributes that are read
    in the file, to clean the code. (Really looks like the class Pokemon, but without
    the many to many relation).
"""


class AuxiliarClass:
    def __init__(self, id, name, type_1, type_2, total, hp, attack, defense, sp_attack,
                sp_defense, speed, generation, is_legendary, color, has_gender, pr_male,
                egg_group_1, egg_group_2, has_mega_evolution, height, weight, catch_rate,
                body_style):
        """
            Attribute: what is that? (type).

            id: Id of the Pokemon (Integer).
            name: Name of the Pokemon (string).
            type_1:
            type_2:
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
            egg_group_1:
            egg_group_2:
            has_mega_evolution: Has mega evolution or not (boolean).
            height: The height of the Pokemon (float).
            weight: The weight of the Pokemon (float).
            catch_rate: The catch rate of the Pokemon (float).
            body_style: The body_style of the Pokemon (string).
        """
        self.id = id
        self.name = name
        self.type_1 = type_1
        self.type_2 = type_2
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
        self.egg_group_1 = egg_group_1
        self.egg_group_2 = egg_group_2
        self.has_mega_evolution = has_mega_evolution
        self.height = height
        self.weight = weight
        self.catch_rate = catch_rate
        self.body_style = body_style

    def __repr__(self):
        return "\nId: {id}  \nName: {name} \nTotal: {total} \nHp: {hp} \nAttack: {attack} \
                \nDefense: {defense} \nAttack Speed: {sp_attack} \nDefense Speed:{sp_defense}\
                \nSpeed: {speed} \nGeneration: {generation} \nLegendary: {is_legendary}\
                \nColor: {color} \nHas Gender: {has_gender} \nPercentage of being male: {pr_male}\
                \nHas mega evolution: {has_mega_evolution} \nHeight: {height}\
                \nWeight: {weight} \nCatch Rate: {catch_rate} \nBody Style: {body_style}"\
                .format(id=self.id, name=self.name, total=self.total, hp=self.hp,
                attack=self.attack, defense=self.defense, sp_attack=self.sp_attack,
                sp_defense=self.sp_defense, speed=self.speed, generation=self.generation,
                is_legendary=self.is_legendary, color=self.color, has_gender=self.has_gender,
                pr_male=self.pr_male, has_mega_evolution=self.has_mega_evolution,
                height=self.height, weight=self.weight, catch_rate=self.catch_rate,
                body_style=self.body_style)
