
from sqlglot import exp


def node_exists(node, tree):
    qt_nodes = len(tree.get_node(node))
    return qt_nodes > 0


def edge_exists(src, dest, tree):
    qt_edges = len(tree.get_edge(src, dest))
    return qt_edges


def get_tablename(tablenode):
    table = ""
    if tablenode.catalog != "":
        table += f"{tablenode.catalog}."
    if tablenode.db != "":
        table += f"{tablenode.db}."

    table += f"{tablenode.name}"

    return table


def get_sources(source):

    sources = {}
    if isinstance(source.expression, exp.SetOperation):
        new_scopes = source.union_scopes
        for scope in new_scopes:
            sources.update(get_sources(scope))

    else:
        sources.update(source.selected_sources)

    return sources