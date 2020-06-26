from sys import stdin, stdout
import numpy as np


class target_x():
    a = np.arange(10, 34).reshape(8, 3)
    b = np.split(a, 4)


if __name__ == "__main__":
    program = target_x()
    print("Creating 8x3 array\n", program.a)
    print("Dividing 8x3 array into 4 sub array\n", program.b)
