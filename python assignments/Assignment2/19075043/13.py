def fun13(a: list, b: int):
    l,r = 0, len(a)-1
    while(l <= r):
        mid = int((l+r)/2)
        if(a[mid] < b):
            l = mid+1
        elif(a[mid]>b):
            r = mid-1
        else:
            print(f'{b} was found at index {mid}')
            break
    else:
        print(b,"is not in given list")

a = [int(x) for x in input("Enter list of sorted numbers ").split()]
b = int(input("Number to search for "))
fun13(a,b)
    


    

        


