import datetime

import aiohttp

from pokeretriever.pokemonapicalls import PokemonApiCalls
from request import Request


class PokedexFacade:
    """
    This class obfuscates the complexity of the modules in the poketriever package
    """
    @staticmethod
    async def execute_request(request: Request):
        """
        Executes async requests to the pokemon api with information from a Request object and prints
        out the information into a file or console
        :param request: Request
        """
        pokemon_api_call = PokemonApiCalls()
        async with aiohttp.ClientSession():
            if request.get_mode() == "pokemon":
                api_call_method = pokemon_api_call.get_pokemon
            elif request.get_mode() == "ability":
                api_call_method = pokemon_api_call.get_ability
            else:
                api_call_method = pokemon_api_call.get_move
            if request.get_expanded() is False:
                if request.get_input_type() == "console":
                    pokedex_object = await api_call_method(parameter=request.get_input_value())
                    if request.get_output_type() == "console":
                        PokedexFacade.print_pokedex_object_to_console(pokedex_object)
                    else:
                        PokedexFacade.print_to_file(pokedex_object, request.get_output_type())
                else:
                    query_list = PokedexFacade.read_file_and_return_list_of_elements(request.get_input_value())
                    pokedex_objects = await pokemon_api_call.get_multiple_poke_requests(query_list,
                                                                                        api_call_method, False)
                    if request.get_output_type() == "console":
                        PokedexFacade.print_pokedex_objects_to_console(pokedex_objects)
                    else:
                        PokedexFacade.print_list_to_file(pokedex_objects, request.get_output_type())
            else:
                if request.get_input_type() == "console":
                    pokedex_object = await api_call_method(parameter=request.get_input_value(), expanded="")
                    if request.get_output_type() == "console":
                        PokedexFacade.print_pokedex_object_to_console(pokedex_object)
                    else:
                        PokedexFacade.print_to_file(pokedex_object, request.get_output_type())
                else:
                    query_list = PokedexFacade.read_file_and_return_list_of_elements(request.get_input_value())
                    pokedex_objects = await pokemon_api_call.get_multiple_poke_requests(query_list,
                                                                                        api_call_method, True)
                    if request.get_output_type() == "console":
                        PokedexFacade.print_pokedex_objects_to_console(pokedex_objects)
                    else:
                        PokedexFacade.print_list_to_file(pokedex_objects, request.get_output_type())

    @staticmethod
    def print_pokedex_object_to_console(pokdex_object):
        """
        Helper function to print a pokedex object to console
        :param pokdex_object: PokedexObject
        """
        date_time = datetime.datetime.now()
        print(f"Timestamp: {date_time.year}/{date_time.day}/{date_time.month} {date_time.hour}:"
              f"{date_time.minute}")
        print(pokdex_object)

    @staticmethod
    def print_pokedex_objects_to_console(pokedex_objects):
        """
        Helper function to print multiple pokdex objects to console
        :param pokedex_objects: list PokedexObject
        """
        date_time = datetime.datetime.now()
        number_of_requests = len(pokedex_objects)
        print(f"Timestamp: {date_time.year}/{date_time.day}/{date_time.month} {date_time.hour}:"
              f"{date_time.minute}")
        print(f"Number of requests: {number_of_requests}")
        for pokedex_object in pokedex_objects:
            print(pokedex_object)

    @staticmethod
    def print_to_file(pokedex_object, text_file):
        """
        Helper function to print a pokedex object into a file
        :param pokedex_object: PokedexObject
        :param text_file:
        :return:
        """
        date_time = datetime.datetime.now()
        with open(text_file, mode='w', encoding="utf-8") as text_file:
            text_file.write(f"Timestamp: {date_time.year}/{date_time.day}/{date_time.month} {date_time.hour}:"
                            f"{date_time.minute}\n")
            text_file.write(str(pokedex_object))

    @staticmethod
    def print_list_to_file(pokedex_objects, text_file):
        """
        Helper function to print a list of PokedexObject to a file
        :param pokedex_objects: list PokedexObject
        :param text_file: path
        """
        date_time = datetime.datetime.now()
        number_of_requests = len(pokedex_objects)
        with open(text_file, mode='w', encoding="utf-8") as text_file:
            text_file.write(f"Timestamp: {date_time.year}/{date_time.day}/{date_time.month} {date_time.hour}:"
                            f"{date_time.minute}\n")
            text_file.write(f"Number of requests: {number_of_requests}\n")
            for pokedex_object in pokedex_objects:
                text_file.write(str(pokedex_object))

    @staticmethod
    def read_file_and_return_list_of_elements(text_file):
        """
        Helper function to read a file of search parameters for poke queries and return them as a list
        :param text_file: path
        :return: list
        """
        query_list = []
        with open(text_file, mode='r', encoding="utf-8") as data_file:
            for line in data_file:
                line = line.strip()
                query_list.append(line)
        return query_list
