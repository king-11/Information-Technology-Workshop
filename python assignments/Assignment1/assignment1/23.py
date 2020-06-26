# function arguments two lists
# iterates over both simulatenously
# print both list until least lenght one exhusted


def fun23(a: list, b: list):
    for x, y in zip(a, b):
        print(x, y)
