import re

x = open('test.txt', 'r')

z = x.readlines()
for i in z:
    j = [x for x in re.split('[^a-zA-Z-]', i) if x != '']
    print(j)

x.close()
