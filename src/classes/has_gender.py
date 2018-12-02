"""
    HasGender:
        The only objective of this class is being an easy way to know if a pokemon has gender or not.
"""
class HasGender:
    def __init__ (self, id_pokemon, pokemon_name):
        """
            Attribute:  what is that?  (type).

            id_pokemon: Id of the HasGender, but at the same time of an object of the class Pokemon.
            pokemon_name: The name of an object Pokemon, represented for id_pokemon.
        """
        self.id_pokemon = id_pokemon
        self.pokemon_name = pokemon_name

    def __repr__(self):
        return " /id: " + str(self.id_pokemon) + " /id poke: " + self.pokemon_name + "\n"
