def bin_search(a: list, b):
    x, y = 0, len(a) - 1
    while x <= y:
        mid = int((x + y) / 2)
        if a[mid] == b:
            return mid
        elif a[mid] < b:
            x = mid + 1
        else:
            y = mid - 1
    return -1


class dwi:
    def __init__(self, a: list):
        self.samagri = sorted(a)

    def search(self, a: int):
        q = list()
        for i in range(0, len(self.samagri)):
            z = bin_search(self.samagri, a-self.samagri[i])
            if z != -1:
                le = [i + 1, z + 1]
                le.sort()
                if le not in q:
                    q.append(le)
        print(q)


namaste = dwi([10, 20, 10, 40, 50, 60, 70])
print(namaste.search(50))
