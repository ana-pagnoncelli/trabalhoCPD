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
        if self.relation == 0:
            relation_name = 'Egg Group'
        else:
            relation_name = 'Type'
        return "\nPokemon Type \n\nid: {id} \nId pokemon: {id_pokemon} \nId type: {id_type}\
                \nRelation: {relation}\n".format(id=self.id, id_pokemon=self.id_pokemon,
                id_type=self.id_type, relation=relation_name)
