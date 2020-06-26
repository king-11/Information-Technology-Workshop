# enter list of numbers
# convert each to string
# join list

print('Enter elements of list')
a = list(map(int, input().split()))
b = list(map(str, a))
print("".join(b))
