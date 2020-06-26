# takes a list of elements as input
# takes string to be added before
# print new list

print("Enter elements of list")
a = [int(x) for x in input().split()]
b = input("Enter term to add")
print([b+str(x) for x in a])
