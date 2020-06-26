# converts string to list by spliting at '-'
# sort list
# join list

a = list(input().split('-'))
a.sort()
print("-".join(a))
