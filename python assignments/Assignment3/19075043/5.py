import re

x = open('test.txt', 'r')

j = list()

for i in x.readlines():
    j += [x for x in re.split('[^a-zA-Z-]', i) if x != '']

print(j)
x.close()
