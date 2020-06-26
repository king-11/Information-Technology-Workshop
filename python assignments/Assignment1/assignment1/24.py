# function argument list containing two lists and number to iterate till
# returns required list


def fun24(a: list, n: int):
    z = list()
    for x, y in zip(a[0][:n+1], a[1][:n+1]):      
	z.append(x)
        z.append(y)
    return z
