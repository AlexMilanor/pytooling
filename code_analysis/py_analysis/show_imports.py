import ast

"""
https://stackoverflow.com/questions/44698193/how-to-get-a-list-of-classes-and-functions-from-a-python-file-without-importing
https://stackoverflow.com/questions/9008451/python-easy-way-to-read-all-import-statements-from-py-module
"""

def show_import_info(importNode):
    if isinstance(importNode, ast.Import):
        module = None
    elif isinstance(importNode, ast.ImportFrom):  
        module = importNode.module
    else:
        raise ValueError("Non import node.")

    print("Module: ", module)
    namespaces = []
    for n in importNode.names:
        namespaces.append(tuple([n.name, n.asname]))
    
    print("(Names, Alias): ", namespaces)
    print("")


def show_imports(filepath):
    with open(filepath) as file:
        root = ast.parse(file.read())
    
    imports = [n for n in root.body 
     if isinstance(n, ast.Import) or isinstance(n, ast.ImportFrom)]

    for import_ in imports:
        show_import_info(import_)
