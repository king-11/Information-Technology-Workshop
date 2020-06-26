def func5(a: list):
    x = 0
    while x < len(a):
        if not a[x]:
            a.pop(x)
        else:
            x += 1

a = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
func5(a)
print(a)