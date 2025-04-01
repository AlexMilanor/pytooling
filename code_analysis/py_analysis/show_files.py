import os
from pathlib import Path

IGNORE_DIR = ["__pycache__", ".ipynb_checkpoints", "tests"]

def traverse_files(codename, fun=None):
    src_path = Path(codename)
    queue = [(src_path, str(src_path).rsplit(os.sep, 1)[-1])]

    while len(queue) > 0:
        case, name = queue.pop(0)
        if os.path.isdir(case):
            queue.extend([(case / x, f"{name}/{x}")
                 for x in os.listdir(case) if x not in IGNORE_DIR])
        else:
            print(f"{'===== ':<5}{name+' ':=<35}")
            if fun is not None:
                fun(case)
            print("")
