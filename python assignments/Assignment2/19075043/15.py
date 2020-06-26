def fun15(a: list):
    n = len(a)
    for x in range(n):
        mini = x
        for y in range(x,n):
            if a[y] < a[mini]:
                mini = y
        a[x], a[mini] = a[mini], a[x]    
    print(a)

    

a = [int(x) for x in input("Enter list of numbers ").split()]
fun15(a)
    


    

        


