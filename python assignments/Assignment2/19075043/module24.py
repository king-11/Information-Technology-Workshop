def lottey():
    import random, string

    def randstring():
        charas = string.digits
        return "".join(random.choice(charas) for x in range(10))

    lottu = set()

    while len(lottu) != 100:
        lottu.add(randstring())

    x, y = random.randint(1,100), random.randint(1,100)

    while(x == y):
        y = random.randint(1,100)

    arr = list()

    i = 1
    for z in lottu:
        if i==x or i==y:
            arr.append(z)
        i += 1
    return arr


