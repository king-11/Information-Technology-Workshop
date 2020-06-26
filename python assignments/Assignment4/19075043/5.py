class rectangle():
    def __init__(self, height, width):
        self.h = height
        self.w = width

    def area(self):
        return self.h*self.w


naya = rectangle(10, 20)

print(naya.area())
