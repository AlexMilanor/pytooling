import argparse
from os import readv

from code_analysis.show_files import traverse_files
from code_analysis.show_variables import show_vars
from code_analysis.show_functions import show_fun
from code_analysis.show_classes import show_class
from code_analysis.show_imports import show_imports


def main(options):
    if options.command == "show_files":
        print(options.src_path)
        traverse_files(options.src_path)
    if options.command == "show_vars":
        traverse_files(options.src_path, fun=show_vars)
    if options.command == "show_functions":
        traverse_files(options.src_path, fun=show_fun)
    if options.command == "show_classes":
        traverse_files(options.src_path, fun=show_class)
    if options.command == "show_imports":
        traverse_files(options.src_path, fun=show_imports)


def set_commands():
    main_parser = argparse.ArgumentParser(
        prog='PyCodeAnalysis',
        description=("CLI used for running a suite of tools to help "
                     "understand a python codebase.")
    )

    main_parser.add_argument(
        'src_path', 
        type=str, 
        help='Path of the codebase to be analyzed.'
    )


    subparsers = main_parser.add_subparsers(
        help="Available tools.",
        dest="command"
    )


    parser_files = subparsers.add_parser(
        name="show_files", 
        help="Show all files inside the codebase."
    )

    parser_var = subparsers.add_parser(
        name="show_vars", 
        help=("Show all variables defined in the codebase,"
              " outside of functions and classes.")
    )

    parser_fun = subparsers.add_parser(
        name="show_functions", 
        help=("Show all functions defined in the codebase,"
              "outside of classes")
    )

    parser_class = subparsers.add_parser(
        name="show_classes", 
        help="Show all classes defined in the codebase."
    )

    parser_import = subparsers.add_parser(
        name="show_imports", 
        help="Show which modules are imported by which modules in the codebase."
    )

    return main_parser


