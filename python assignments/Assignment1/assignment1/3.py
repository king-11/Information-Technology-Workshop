# takes input of string

s = input()

# find 'not' and 'poor' substring using find function and prints required string
a = s.find("not")
if a != -1:
    b = s.find('poor', a)

    if (b != -1):
        b += 4
        print(s[:a] + 'good' + s[b:])
    else:
        print(s)
else:
    print(s)
