from sys import stdin, stdout
from itertools import permutations


class target_x():
    def __init__(self, n: str):
        self.x = n.strip("\n")

    def solution(self):
        l = set()
        for p in permutations(self.x):
            l.add("".join(p))
        return l


if __name__ == "__main__":
    x = stdin.readline()
    program = target_x(x)
    for i, x in enumerate(program.solution()):
        print(i, x)
