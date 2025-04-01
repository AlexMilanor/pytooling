from .traverse_sql_graph import query_tree


def analyze_query(path:str, dialect:str="bigquery"):
    print("Analyzing {path}...")
    with open(path, 'r') as fp:
        query = fp.read()

    all_queries = query_tree(query, dialect)

    for q in all_queries:
        name = q.get_name()
        q.write_png(f"./{name}.png")

