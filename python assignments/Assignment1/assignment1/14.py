# function takes argument as list and element
# count its frequency in list
# return integer count


def fun14(a: list, b):
    count = 0
    for x in a:
        if x == b:
            count += 1

    return count
