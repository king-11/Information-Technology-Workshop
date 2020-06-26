# function takes two list as arguments
# iterating over both list till max one finished


def fun9(m: list, n: list):
    final = list()
    x = y = 0
    a = max(len(m), len(n))
    for i in range(a):
        if m[x] < m[y]:
            final.append(m[x])
            x += 1
        else:
            final.append(n[y])
            y += 1
    return final
