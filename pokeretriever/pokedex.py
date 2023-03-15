import abc


class PokedexObject(abc.ABC):
    def __init__(self, **kwargs):
        self._name = kwargs["name"]
        self._id = kwargs["id"]

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id


class Pokemon(PokedexObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._height = kwargs["height"]
        self._weight = kwargs["weight"]
        self._stats = kwargs["stats"]
        self._types = kwargs["types"]
        self._abilities = kwargs["abilities"]
        self._moves = kwargs["moves"]

    def __str__(self):
        """
        :return: a string representation of a pokemon object
        """
        return f"Name: {self.name}\n" \
               f"ID: {self._id}\n" \
               f"Height: {self._height} decimetres\n" \
               f"Weight: {self._weight} hectograms\n" \
               f"Types: {', '.join(repr(single_type) for single_type in self._types)}\n\n" \
               f"Stats:  \n" \
               f"-------\n\n" \
               f"{''.join(repr(stat) for stat in self._stats)}" \
               f"Abilities: \n" \
               f"----------\n\n" \
               f"{''.join(repr(ability) for ability in self._abilities)}" \
               f"Moves: \n" \
               f"-------\n\n" \
               f"{''.join(repr(move) for move in self._moves)}"


class Ability(PokedexObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._generation = kwargs["generation"]
        self._effect = kwargs["effect"]
        self._effect_short = kwargs["effect_short"]
        self._pokemon = kwargs["pokemons"]

    def __repr__(self):
        if self._id is None:
            return f"{self.name}\n\n"
        else:
            return f"Name: {self.name}\n" \
                   f"ID: {self._id}\n" \
                   f"Generation: {self._generation}\n" \
                   f"Effect: {self._effect}\n" \
                   f"Effect (Short): {self._effect_short}\n" \
                   f"Pokemon: {', '.join(repr(single_pokemon) for single_pokemon in self._pokemon)}\n\n"

    def __str__(self):
        """
        :return: a string representation of a pokemon ability object
        """
        if self._id is None:
            return f"Name: {self.name}\n"
        else:
            return f"Name: {self.name}\n" \
                   f"ID: {self._id}\n" \
                   f"Generation: {self._generation}\n" \
                   f"Effect: {self._effect}\n" \
                   f"Effect (Short): {self._effect_short}\n" \
                   f"Pokemon: {', '.join(repr(single_pokemon) for single_pokemon in self._pokemon)}\n"


class Stat(PokedexObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._base_value = kwargs["base_value"]
        self._is_battle_only = kwargs["is_battle_only"]

    def __repr__(self):
        if self._is_battle_only is None:
            return f"('{self.name}', {self._base_value})\n"
        else:
            return f"Name: {self.name}\n" \
                   f"ID: {self._id}\n" \
                   f"Base Value: {self._base_value}\n" \
                   f"Battle Only: {self._is_battle_only}\n\n"

    def __str__(self):
        """
        :return: a string representation of one stat type of a pokemon
        """
        if self._is_battle_only is None:
            return f"Name: {self.name}\n" \
                   f"Base Value: {self._base_value}\n"
        else:
            return f"Name: {self.name}\n" \
                   f"Id: {self._id}\n" \
                   f"Base Value: {self._base_value}\n" \
                   f"Battle Only: {self._is_battle_only}\n"


class Move(PokedexObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._generation = kwargs["generation"]
        self._accuracy = kwargs["accuracy"]
        self._pp = kwargs["pp"]
        self._power = kwargs["power"]
        self._type = kwargs["type"]
        self._damage_class = kwargs["damage_class"]
        self._effect = kwargs["effect"]
        self._level_learned = kwargs["level_learned"]

    def __repr__(self):
        if self._id is None:
            return f"('Move name: {self.name}', 'Level acquired: {self._level_learned}')\n"
        else:
            return f"Name: {self.name}\n" \
                   f"ID: {self._id}\n" \
                   f"Generation: {self._generation}\n" \
                   f"Accuracy: {self._accuracy}\n" \
                   f"PP: {self._pp}\n" \
                   f"Power: {self._power}\n" \
                   f"Type: {self._type}\n" \
                   f"Damage class: {self._damage_class}\n" \
                   f"Effect (Short): {self._effect}\n\n"

    def __str__(self):
        """
        :return: a string representation of a pokemon move object
        """
        if self._id is None:
            return f"Name: {self.name}\n" \
                   f"Level learned at: {self._level_learned}\n"
        else:
            return f"Name: {self.name}\n" \
                   f"ID: {self._id}\n" \
                   f"Generation: {self._generation}\n" \
                   f"Accuracy: {self._accuracy}\n" \
                   f"PP: {self._pp}\n" \
                   f"Power: {self._power}\n" \
                   f"Type: {self._type}\n" \
                   f"Damage class: {self._damage_class}\n" \
                   f"Effect (Short): {self._effect}\n"
