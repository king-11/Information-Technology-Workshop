class converter:
    def __init__(self, hex):
        self.dec = int(hex, 16)

    def convert(self):
        print(self.dec)


value = converter("C77")
value.convert()
