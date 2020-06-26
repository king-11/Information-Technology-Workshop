x = open('test.txt')
n = int(input("Number of lines to read : "))


for i in range(n):
    print(x.readline(), end="")
