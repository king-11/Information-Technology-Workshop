# takes input of list
# takes input of frequency to split at
# print splitted list

print('Enter elements of list')
a = list(input().split())
n = int(input('Enter number to split at'))
print([a[x:x+n] for x in range(0, len(a), n)])
