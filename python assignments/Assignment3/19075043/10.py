x = open('file1')
y = open('file2')
z = open('combine', '+w')

for i, j in zip(x.readlines(), y.readlines()):
    z.write(i)
    z.write(j)

z.seek(0)
print("".join(z.readlines()))
