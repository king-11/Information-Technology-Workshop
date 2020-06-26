x = open('ninth.txt', '+w')

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

x.write("\n".join(color))
x.seek(0)

print("".join(x.readlines()))
x.close()
