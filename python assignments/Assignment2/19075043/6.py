def func6(a: tuple):
    n = len(a)
    s = {}
    for x in range(n):
        s[a[x][1]] = a[x][0]
    print(s)

a = ((2, "w"),(3, "r"))
func6(a)