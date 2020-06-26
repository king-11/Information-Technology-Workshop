from sys import stdin, stdout

n = int(stdin.readline())

for i in range(1, n):
    for j in range(i):
        print(i, end=' ')
    stdout.write('\n')
