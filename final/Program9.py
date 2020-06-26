from sys import stdin, stdout


class target_x():
    def __init__(self, n: str):
        self.x = n.lower().strip("\n")

    def solution(self):
        y = self.x[::-1]
        return y == self.x


if __name__ == "__main__":
    x = stdin.readline()
    program = target_x(x)
    print(program.solution())
