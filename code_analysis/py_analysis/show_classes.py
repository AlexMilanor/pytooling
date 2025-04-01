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


def show_class(filepath):
    with open(filepath) as file:
        node = ast.parse(file.read())
           
    classes = [n for n in node.body if isinstance(n, ast.ClassDef)]
    for class_ in classes:
        print("Class name:", class_.name)
        methods = [n for n in class_.body if isinstance(n, ast.FunctionDef)]
        for method in methods:
            show_info(method)
