import ast

"""
https://stackoverflow.com/questions/69807005/how-do-i-use-python-ast-module-to-obtain-all-targets-and-value-for-assignment-no
https://realpython.com/python-variables/#getting-to-know-variables-in-python
"""

def get_id(Node):
    """
    Get the relevant node id to be able to parse what 
    is written as the LHS of an assignment operator.

    The ids of each node type is as follows:
    - ast.Name: {Node.id}
    - ast.Attribute: {id(Node.value)}.{Node.attr}
    - ast.Subscript: {id(Node.value)}[id(Node.slice)]
    - ast.Constant: {Node.value}
    - ast.Slice: {id(Node.lower)}:{id(Node.upper)}:{id(Node.step)}
    - ast.Tuple: {id(Node.elts[0]), ..., id(Node.elts[-1])}
    """

    name: str
    if isinstance(Node, ast.Name):
        name = f"{Node.id}"

    elif isinstance(Node, ast.Constant):
        if type(Node.value) == str:
            name = f"'{Node.value}'"
        else:
            name = f"{Node.value}"

    elif isinstance(Node, ast.Attribute):
        name = f"{get_id(Node.value)}.{Node.attr}"

    elif isinstance(Node, ast.Subscript):
        name = f"{get_id(Node.value)}[{get_id(Node.slice)}]"

    elif isinstance(Node, ast.Slice):
        name = f"{get_id(Node.lower)}:"
        if Node.upper is not None:
            name += f"{get_id(Node.upper)}"
        if Node.step is not None:
            name += f":{get_id(Node.step)}"

    elif isinstance(Node, ast.Tuple):
        name = ",".join([f"{get_id(elt)}" for elt in Node.elts])

    else:
        raise ValueError(f"Invalid variable writing node type"
                         f" {type(subNode)}")

    return name


def show_assign_info(assignNode):
    if isinstance(assignNode, ast.Assign):
        all_vars = assignNode.targets
        out = "{name}"
    else:
        all_vars = [assignNode.target]
        out = "{name} (Annotation)"

    for tgt in all_vars:

        if isinstance(tgt, ast.Tuple):
            for elt in tgt.elts:
                print(out.format(name=get_id(elt)))
                
        else:
            print(out.format(name=get_id(tgt)))


def show_vars(filepath):
    with open(filepath) as file:
        root = ast.parse(file.read())
    
    assigns = [n for n in root.body 
               if isinstance(n, ast.Assign) 
               or isinstance(n, ast.AnnAssign)]

    for assign_ in assigns:
        show_assign_info(assign_)
