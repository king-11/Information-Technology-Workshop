import string
import sys

bets = string.ascii_lowercase

n = int(sys.stdin.readline())
L = []
for i in range(n):
    s = " ".join(bets[i:n])
    L.append((s[::-1]+s[1:]).center(4*n-3, " "))
sys.stdout.write('\n'.join(L[:0:-1]+L))
