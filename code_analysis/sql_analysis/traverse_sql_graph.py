import sys
import json


import pydot
import sqlglot
from sqlglot import parse, exp
from sqlglot.optimizer.scope import build_scope

from .utils import (
    node_exists,
    edge_exists,
    get_tablename,
    get_sources
)


def traverse_tree(root, rootname, tree):

    for alias, (node, source) in get_sources(root).items():

        if isinstance(source, exp.Table):
            tablename = get_tablename(source)
            traverse = False

        elif isinstance(node, exp.Unnest):
            tablename = f"UNNEST({node.args.get('expressions')[0]})"
            traverse = False

        else:
            if source.is_cte:
                tablename = f"CTE({node.args.get('this')})"
                traverse = True

            elif source.is_derived_table:
                tablename = f"SUB({alias})"
                traverse = True

            else:
                raise ValueError("Erro")


        if not node_exists(tablename, tree):
            tree.add_node(pydot.Node(tablename, label=tablename))

        if not edge_exists(tablename, rootname, tree):
            tree.add_edge(pydot.Edge(tablename, rootname))

        if traverse:
            traverse_tree(source, tablename, tree)


def query_tree(query, dialect="bigquery"):
    all_trees = []
    n = 1
    for expression in parse(query, dialect, error_level=None):
        name = f"sql_graph_{n}"
        print(f"Running {name}...")

        root = build_scope(expression)
        tree = pydot.Dot(name, graph_type="digraph")
        traverse_tree(root, "root", tree)
        
        all_trees.append(tree)

    return all_trees