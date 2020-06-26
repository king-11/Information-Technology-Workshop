# input string
# convert into list
# stores set of list having all distinct characters
# prints count if each element in set

s = input()
a = list(s)
b = set(a)
for x in b:
    print(x, s.count(x))
