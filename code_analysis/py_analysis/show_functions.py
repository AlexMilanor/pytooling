import ast

"""
https://stackoverflow.com/questions/44698193/how-to-get-a-list-of-classes-and-functions-from-a-python-file-without-importing
https://stackoverflow.com/questions/9008451/python-easy-way-to-read-all-import-statements-from-py-module
"""

def show_info(functionNode):
    print("Function name:", functionNode.name)
    print("Args:")
    for arg in functionNode.args.args:
        print("\tParameter name:", arg.arg)
    print("")

def show_fun(filepath):
    with open(filepath) as file:
        node = ast.parse(file.read())

    functions = [n for n in node.body if isinstance(n, ast.FunctionDef)]
    for function in functions:
        show_info(function)
