class something:
    name = "critical"


wander = something()

print(wander.name)


class empty:
    def __init__(self):
        return


print(type(empty))
