"""
    PokemonType:
        Contains the relation between the objects of the classes Pokemon and Type.
"""

class PokemonType:
    def __init__ (self, id, id_pokemon, id_type):
        """
            Attribute:  what is that?  (type).

            id: Id of the PokemonType (integer).
            id_pokemon: Id of an object of the class Pokemon (integer).
            id_type: Id of an object of the class Type (integer).
            relation: type of the relation between the Pokemon and the Type (integer, 0 = Egg_Group, 1 = Type).
        """
        self.id = id
        self.id_pokemon = id_pokemon
        id.id_type = id_type
        id.relation = relation
