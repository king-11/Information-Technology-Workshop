def fun14(a: list):
    count = -1
    n = len(a)
    for x in range(n-1):
        if count == 0:
            break
                
        count = 0
        for y in range(0,n-x-1):
            if a[y] > a[y+1]:
                a[y], a[y+1] = a[y+1], a[y]
                count += 1
    print(a)

    

a = [int(x) for x in input("Enter list of numbers ").split()]
fun14(a)
    


    

        


