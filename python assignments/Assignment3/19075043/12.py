# to end input press ctrl+d

from sys import stdin

read = stdin.readlines()

for x in read:
    print(x.upper(), end="")
