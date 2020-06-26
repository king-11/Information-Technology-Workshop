def func7(a: list):
    count = 0
    for x in a:
        if type(x) != tuple:
            count += 1
        else:
            break
    print(count)

a = [10,20,30,(10,20),40]
func7(a)