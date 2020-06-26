def func1(a:dict, b:dict):
    for x in a:
        if b.get(x) != None and b[x] == a[x]:
            print(x,a[x])

a = {'key1': 1, 'key2': 3, 'key3': 2}
b = {'key1': 1, 'key2': 2}

func1(a,b)