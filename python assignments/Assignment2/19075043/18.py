def reverse(x: str):
    new = ""
    n = len(x)-1
    for i in range(n,-1,-1):
        new += x[i]
    return(new)

a = input("Enter String to reverse ")

print(reverse(a))
    



