class trishukl():
    def __init__(self, vakya: list):
        z = []
        for i, x in enumerate(vakya):
            for j, y in enumerate(vakya[x+1:]):
                if j != i and - (x + y) in vakya:
                    a = [x, y, -(x+y)]
                    a.sort()
                    if a not in z:
                        z.append(a)

        print(z)


namaste = trishukl([-25, -10, -7, -3, 2, 4, 8, 10])
