# split input numbers using split function
#  convert binary to decimal anf then check
# print answers

nums = input().split(',')
a = list()
for x in nums:
    if int(x, 2) % 5 == 0:
        a.append(x)
print(a)
