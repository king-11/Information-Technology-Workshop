x = open('myfile.txt', 'a+')

x.write("This is ITW1 class.")

x.seek(0)

print("".join(x.readlines()))

x.close()
