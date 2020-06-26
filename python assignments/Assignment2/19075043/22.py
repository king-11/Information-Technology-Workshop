import random, string

def randstring():
    charas = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(charas) for i in range(10))

print ("First Random String ", randstring() )
print ("Second Random String", randstring() )
print ("Third Random String", randstring() )