import argparse
from os import readv

from code_analysis.py_analysis import (
    traverse_files,
    show_vars,
    show_fun,
    show_class,
    show_imports
)

from code_analysis.sql_analysis import (
    analyze_query
)


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
    if options.command == "analyze_sql":
        analyze_query(options.src_path)


def set_commands():
    main_parser = argparse.ArgumentParser(
        prog='Code Analysis',
        description=("CLI used for running a suite of tools to help "
                     "understand a data science codebase (python and SQL).")
    )


    subparsers = main_parser.add_subparsers(
        help="Available tools.",
        dest="command"
    )

    parse_py_analysis(subparsers)
    parse_sql_analysis(subparsers)

    return main_parser



def parse_py_analysis(subparsers):

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


    for parser in [parser_files, parser_var, parser_fun, parser_class, parser_import]:
        parser.add_argument(
        'src_path', 
        type=str, 
        help='Path of the codebase to be analyzed.'
    )


def parse_sql_analysis(subparsers):

    parser = subparsers.add_parser(
        name="analyze_sql",
        help="Transform sql query to png flowchart."
    )

    parser.add_argument(
        'src_path', 
        type=str, 
        help='Path of the codebase to be analyzed.'
    )

    parser.add_argument(
        "--dialect",
        type=str,
        choices=["bigquery", "duckdb", "mysql", "postgres", "redshift", "tsql", "sqlite"],
        default=None,
        help="Define a SQL dialect to use."
    )
