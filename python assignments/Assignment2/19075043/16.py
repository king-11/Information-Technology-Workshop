def merge(a: list, b: list):
    x,y = 0,0
    z = list()
    while x < len(a) and y < len(b):
        if a[x] < b[y]:
            z.append(a[x])
            x += 1
        else :
            z.append(b[y])
            y += 1
    else:
        if x < len(a):
            for i in range(x,len(a)):
                z.append(a[i])
        else :
            for i in range(y,len(b)):
                z.append(b[i])
    return z


def mergeSort(a:list,start:int,stop:int):
    n = int((start+stop)/2)
    if(start != stop):
        x = mergeSort(a,start,n)
        y = mergeSort(a,n+1,stop)
        return merge(x,y)
    else:
        return a[start:stop+1]




    
a = [int(x) for x in input("Enter numbers: ").split()]
print(mergeSort(a,0,len(a)-1))

    

        


