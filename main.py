from distutils.dir_util import copy_tree

namen = """Dagobert Duck
Donald Duck
Daisy Duck"""

namen = [f'{name.split(" ")[-1]}, {" ".join(name.split(" ")[:-1])}' for name in namen.split("\n")]

for name in namen:
    copy_tree("__Aufgabe__", name)
