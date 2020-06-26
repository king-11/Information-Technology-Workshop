import itertools as it

# takes list as argument and prints a list
# where duplicates are removed
# itertools groupby function used


def fun17(a: list):
    a.sort()
    print(list(a for a, _ in it.groupby(a)))
