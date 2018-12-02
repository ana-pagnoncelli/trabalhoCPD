"""
    PokemonType:
        Contains the relation between the objects of the classes Pokemon and Type.
"""

class PokemonType:
    def __init__ (self, id, id_pokemon, id_type, relation):
        """
            Attribute:  what is that?  (type).

            id: Id of the PokemonType (integer).
            id_pokemon: Id of an object of the class Pokemon (integer).
            id_type: Id of an object of the class Type (integer).
            relation: type of the relation between the Pokemon and the Type (integer, 0 = Egg_Group, 1 = Type).
        """
        self.id = id
        self.id_pokemon = id_pokemon
        self.id_type = id_type
        self.relation = relation

    def __repr__(self):
        return " /id: " + str(self.id) + " /id poke: " + str(self.id_pokemon) + " /id type: " + str(self.id_type) + " /relation: " + self.relation + "\n"
