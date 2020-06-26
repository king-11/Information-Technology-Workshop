class shabadkosh():
    def __init__(self, vakya: str):
        self.vakya = vakya.split()

    def ulta(self):
        a = [x[::-1] for x in self.vakya]
        return " ".join(a)


namaste = shabadkosh("nar sanghari manush")

print(namaste.ulta())
