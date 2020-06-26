from random import randint

x = open('test.txt', 'r')

z = x.readlines()
print(z[randint(0, len(z)-1)])
x.close()
