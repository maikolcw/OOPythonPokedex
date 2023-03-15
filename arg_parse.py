import argparse
import os

from request import Request


class ArgParse:
    @staticmethod
    def parse_terminal_arguments():
        parser = argparse.ArgumentParser(description="Search pokemon api for pokemon data")
        group = parser.add_mutually_exclusive_group(required=True)
        parser.add_argument("mode", help="select search mode", choices=["pokemon", "ability", "move"])
        group.add_argument("--inputfile", help="use input file for parameters")
        group.add_argument("--inputdata", help="use terminal input for parameters (id or name)")
        parser.add_argument("-e", "--expanded", help="enable expanded search results", action="store_true")
        parser.add_argument("-o", "--output", help="select output to specified 'filename.txt'", default="console")
        args = parser.parse_args()
        try:
            request_object = Request(mode=args.mode, input_type=None, input_value=None, expanded=False,
                                     output_type=args.output)
            if args.inputfile:
                if ArgParse.check_file_is_text_file(args.inputfile):
                    request_object.set_input_type("file")
                    request_object.set_input_value(args.inputfile)
                else:
                    raise ValueError
            elif args.inputdata:
                request_object.set_input_type("console")
                request_object.set_input_value(args.inputdata)
            if args.expanded:
                request_object.set_expanded(True)
            if args.output != "console":
                if ArgParse.check_file_is_text_file(args.output):
                    request_object.set_output_type(args.output)
                else:
                    raise ValueError
            return request_object
        except ValueError:
            print("Invalid values, please check -h for more help")
            quit()

    @staticmethod
    def check_file_is_text_file(inputfile):
        return os.path.splitext(inputfile)[1] == ".txt"
