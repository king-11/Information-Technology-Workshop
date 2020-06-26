def user_input():
    while True:
        s = input()
        if not s:
            return
        yield s


class target_x:
    lines = []

    def solution(self):
        for line in map(str.upper, user_input()):
            self.lines.append(line)
        print("\n".join(self.lines))


if __name__ == "__main__":
    program = target_x()
    program.solution()
