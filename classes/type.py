"""
    Type:
        Contains the pokemons types, like water, fire, air...
"""

class Type:
    def __init__ (self, id, type, id_pokemon_type):
        """
            Attribute: what is that? (type).

            id: Type id (integer).
            type: Name of the Type (string).
            id_pokemon_type: Like the class Pokemon, this field has an array with ids.
            This ids come from objects of the class id_pokemon_type (array of integers).
        """
        self.id = id
        self.type = type
        self.id_pokemon_type = id_pokemon_type
