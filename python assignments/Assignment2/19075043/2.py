def func2(a:list, b:list):
    z = {}
    for x, y in zip(a,b):
        z[x] = y
    print(z)

a = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
b = [1, 2, 2, 3]
    
func2(a,b)