import re
from collections import Counter

x = open('test.txt', 'r')

y = [j for i in x.readlines() for j in re.split('[^a-zA-Z-]', i) if j != '']

print("Number of words", Counter(y))

# for i in x.readlines():
#     for j in re.split('[^a-zA-Z-]', i):
#         if j in y:
#             y[j] += 1
#         else:
#             y[j] = 1

# print(y)
x.close()
