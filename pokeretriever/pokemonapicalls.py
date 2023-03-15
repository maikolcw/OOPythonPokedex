import asyncio

import aiohttp
from aiohttp import ContentTypeError

from pokeretriever.pokedex import Ability, Move, Stat, Pokemon


class PokemonApiCalls:
    @staticmethod
    async def get_multiple_poke_requests(list_of_queries, get_mode, is_expanded):
        async with aiohttp.ClientSession():
            if is_expanded:
                async_coroutines = [get_mode(parameter=query, expanded="") for query in list_of_queries]
                responses = await asyncio.gather(*async_coroutines)
                return responses
            else:
                async_coroutines = [get_mode(parameter=query) for query in list_of_queries]
                responses = await asyncio.gather(*async_coroutines)
                return responses


    @staticmethod
    async def get_ability(**kwargs):
        base = "https://pokeapi.co/api/v2/ability/{}"
        target_url = PokemonApiCalls.helper_return_api_url_with_parameters(base=base, **kwargs)
        try:
            async with aiohttp.ClientSession() as session:
                response = await session.request(method="GET", url=target_url)
                json_dict = await response.json()
                name = json_dict["name"]
                pokemon_id = json_dict["id"]
                generation = json_dict["generation"]["name"]
                effect = json_dict["effect_entries"][1]["effect"].replace("\n", " ")
                effect_short = json_dict["effect_entries"][1]["short_effect"]
                list_of_pokemons_that_have_this_ability = []
                for entry in json_dict["pokemon"]:
                    list_of_pokemons_that_have_this_ability.append(entry["pokemon"]["name"])
                ability = Ability(name=name, id=pokemon_id, generation=generation, effect=effect,
                                  effect_short=effect_short,
                                  pokemons=list_of_pokemons_that_have_this_ability)
                return ability
        except ContentTypeError:
            return "\nAn error occurred. Skipping this request\n"

    @staticmethod
    async def helper_get_abilities(ability_list, abilities_json, **kwargs):
        if "expanded" in kwargs:
            async with aiohttp.ClientSession():
                for ability in abilities_json:
                    ability_object = await PokemonApiCalls.get_ability(url=ability["ability"]["url"])
                    ability_list.append(ability_object)
        else:
            for ability in abilities_json:
                name = ability["ability"]["name"]
                ability_list.append(Ability(name=name, id=None, generation=None, effect=None, effect_short=None,
                                            pokemons=None))

    @staticmethod
    async def get_move(**kwargs):
        base = "https://pokeapi.co/api/v2/move/{}"
        target_url = PokemonApiCalls.helper_return_api_url_with_parameters(base=base, **kwargs)
        try:
            async with aiohttp.ClientSession() as session:
                response = await session.request(method="GET", url=target_url)
                json_dict = await response.json()
                name = json_dict["name"]
                pokemon_id = json_dict["id"]
                generation = json_dict["generation"]["name"]
                accuracy = json_dict["accuracy"]
                pp = json_dict["pp"]
                power = json_dict["power"]
                move_type = json_dict["type"]["name"]
                damage_class = json_dict["damage_class"]["name"]
                effect = json_dict["effect_entries"][0]["effect"].replace("\n", " ")
                move = Move(name=name, id=pokemon_id, generation=generation, accuracy=accuracy, pp=pp, power=power,
                            type=move_type, damage_class=damage_class, effect=effect, level_learned=None)
                return move
        except ContentTypeError:
            return "\nAn error occurred. Skipping this request\n"

    @staticmethod
    async def helper_get_moves(move_list, moves_json, **kwargs):
        if "expanded" in kwargs:
            async with aiohttp.ClientSession():
                for move in moves_json:
                    move_object = await PokemonApiCalls.get_move(url=move["move"]["url"])
                    move_list.append(move_object)
        else:
            for move in moves_json:
                name = move["move"]["name"]
                level_learned = move["version_group_details"][0]["level_learned_at"]
                move_list.append(Move(name=name, level_learned=level_learned, id=None, generation=None, accuracy=None,
                                      pp=None, power=None, type=None, damage_class=None, effect=None))

    @staticmethod
    async def get_stat(**kwargs):
        base = "https://pokeapi.co/api/v2/stat/{}"
        target_url = PokemonApiCalls.helper_return_api_url_with_parameters(base=base, **kwargs)
        async with aiohttp.ClientSession() as session:
            response = await session.request(method="GET", url=target_url)
            json_dict = await response.json()
            name = json_dict["name"]
            pokemon_id = json_dict["id"]
            is_battle_only = json_dict["is_battle_only"]
            stat = Stat(name=name, id=pokemon_id, base_value=kwargs["base_value"], is_battle_only=is_battle_only)
            return stat

    @staticmethod
    async def helper_get_stat(stat_list, stats_json, **kwargs):
        if "expanded" in kwargs:
            async with aiohttp.ClientSession():
                for stat in stats_json:
                    stat_object = await PokemonApiCalls.get_stat(url=stat["stat"]["url"], base_value=stat["base_stat"])
                    stat_list.append(stat_object)
        else:
            for stat in stats_json:
                name = stat["stat"]["name"]
                base_value = stat["base_stat"]
                stat_list.append(Stat(name=name, base_value=base_value, id=None,
                                      is_battle_only=None))

    @staticmethod
    async def get_pokemon(**kwargs):
        base = "https://pokeapi.co/api/v2/pokemon/{}"
        target_url = PokemonApiCalls.helper_return_api_url_with_parameters(base=base, **kwargs)
        try:
            async with aiohttp.ClientSession() as session:
                response = await session.request(method="GET", url=target_url)
                json_dict = await response.json()
                name = json_dict["name"]
                pokemon_id = json_dict["id"]
                height = json_dict["height"]
                weight = json_dict["weight"]
                type_list = []
                types_json = json_dict["types"]
                for type in types_json:
                    type_list.append(type["type"]["name"])
                # fills stat_list with stat objects
                stat_list = []
                stats_json = json_dict["stats"]
                await PokemonApiCalls.helper_get_stat(stat_list, stats_json, **kwargs)
                # fills ability_list with ability objects
                ability_list = []
                abilities_json = json_dict["abilities"]
                await PokemonApiCalls.helper_get_abilities(ability_list, abilities_json, **kwargs)
                move_list = []
                moves_json = json_dict["moves"]
                await PokemonApiCalls.helper_get_moves(move_list, moves_json, **kwargs)
                pokemon_object = Pokemon(name=name, id=pokemon_id, height=height, weight=weight, stats=stat_list,
                                         types=type_list, abilities=ability_list, moves=move_list)
                return pokemon_object
        except ContentTypeError:
            return "\nAn error occurred. Skipping this request\n"

    @staticmethod
    def helper_return_api_url_with_parameters(**kwargs):
        url = kwargs["base"]
        if "parameter" in kwargs:
            target_url = url.format(kwargs["parameter"])
        else:
            target_url = kwargs["url"]
        return target_url
