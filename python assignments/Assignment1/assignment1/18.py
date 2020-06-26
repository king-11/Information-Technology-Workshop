# function argument is a list
# sum each list in given list
# returns element with max sum


def fun18(a: list):
    x = max([sum(x) for x in a])
    for i in a:
        if sum(i) == x:
            return i
