from sys import stdin

s, w = input("S:"), input("W:")

i, l = 0, len(s)

while True:
    try:
        j = min(l, i+4)
        r = j-1
        print(f'{s[i:j]}\t{s[i]}{s[r]}')
        i += 4
    except IndexError:
        break
