def func4(a: list):
    n = len(a)
    for x in range(1,n):
        for y in range(x,0,-1):
            if a[y][1] > a[y-1][1]:
                a[y], a[y-1] = a[y-1], a[y]
            else:
                break
    print(a)        

            

    

a = [ ('item2', '15.10'), ('item1', '12.20'), ('item3', '24.5')]
func4(a)