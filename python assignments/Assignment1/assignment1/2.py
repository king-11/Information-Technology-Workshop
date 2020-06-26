# takes input of string
# converts into a list then loops through list
s = list(input())
for i, x in enumerate(s[1:]):
    if x == s[0]:
        s[i+1] = '$'
print("".join(s))
