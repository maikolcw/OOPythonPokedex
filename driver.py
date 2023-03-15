# Name: Maikol Chow Wang

import asyncio

from arg_parse import ArgParse
from pokedex_facade import PokedexFacade


def main():
    """
    Main, drives the program
    """
    loop = asyncio.get_event_loop()
    arg_parse = ArgParse()
    request = arg_parse.parse_terminal_arguments()
    pokedex_facade = PokedexFacade()
    loop.run_until_complete(pokedex_facade.execute_request(request))


if __name__ == '__main__':
    main()
