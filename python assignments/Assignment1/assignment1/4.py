# function takes needs two list string input


def fun4(a: str, b: str) -> str:
    # returns required string using string slicing at middle
    x = int(len(a) / 2)
    return a[:x]+b+a[x:]
