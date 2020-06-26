x = open('test.txt', 'r')

n = int(input("Enter number of last lines to print "))
n *= -1

y = x.readlines()


for i in y[n:]:
    print(i, end="")


x.close()
