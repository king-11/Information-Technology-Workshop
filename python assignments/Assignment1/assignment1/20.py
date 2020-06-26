# takes two list as input
# iterate over both list
# print output lists

print("Enter elements of first list")
a = list(input().split())
print('Enter elements of second list')
b = list(input().split())
a1 = list()
for x in a:
    if x not in b:
        a1.append(x)
b1 = list()
for x in b:
    if x not in a:
        b1.append(x)
print(a1)
print(b1)
