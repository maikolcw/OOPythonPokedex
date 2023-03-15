A python project that fetches Pokemon data for the user similar to a pokedex in the anime and game. AsyncIO library is used to write asynchronous code for HTTP client sessions and to create queries to an endpoint with GET HTTP Requests. Asyncio.gather() is used to run multiple queries concurrently. Similar modules are put into packages. Pokeretriever package contain all the modules and code required to create an aiohttp session and execute requests, parse the JSON and instantiate the appropriate object, and the Pokemon, Ability, Move, and Stat Classes. The facade class helps simplify the interface. The API used is the PokeAPI, a RESTful API at https://pokeapi.co/

Users will be able to make input from the terminal and the output data will either be on console or printed to a file specified by the user.

Argparse module will be used to facilitate command line arguments implementation.
python3 driver.py {"pokemon" | "ability" | "move"} {--inputfile "filename.txt" |--inputdata "name or id'} [--expanded] [--output "f]

Go to root folder of project and either use python3 or python depending on your system. Driver class and main method will be the driver.py module.

{"pokemon" | "ability" | "move"}
Pick one of the mutually exclusive argument. This argument specifies the mode that the application will be opened in. It can either be Pokemon, Ability, or Move.

●	In the pokemon mode, the input will be an id or the name of a pokemon. The pokedex will query pokemon information.
●	In the ability mode, the input will be an id or the name of a ability. These are certain effects that pokemon can enable. The pokedex will query the ability information.
●	In the move mode, the input will be an id or the name of a pokemon move. These are the attacks and actions pokemon can take. The pokedex will query the move information.

{--inputfile "filename.txt" |--inputdata "name or id'}
The user must pass in one of these arguments. They cannot pass in both. As input, the application can take in either a file name (Text file), or a name/id. When providing a file name, the --inputfile flag must be provided. The file name must end with a .txt extension. If providing just the name or id , then the –inputdata flag must be provided. The id must be a digit and the name a string. This is the second positional argument. Filenames allow the user to do bulk queries.

[--expanded]

When this optional flag is provided, certain attributes are expanded, that is the pokedex will do sub-queries to get more information about a particular attribute.  If this flag is not provided, the app will not get the extra information and just print what's provided.
For this prototype, only pokemon queries support the expanded mode. Refer to the pokemon query details below in the document for more information.

[--output "filename.txt"]

If provided, a filename (with a .txt extension) must also be provided. and the query result should be printed to the specified text file.  If this flag is not provided, then print the result to the console. Be sure to print the file in a nicely formatted, readable manner.