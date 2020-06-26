import sys

x = input("Enter objects ").split()

for a in x:
    print(f"Memory size of \'{a}\' is {sys.getsizeof(a)}")
