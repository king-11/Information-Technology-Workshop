from sys import stdin, stdout

n, k = [int(x) for x in stdin.readline().split()]
arr = [int(x) for x in stdin.readline().split()]


def validSubArrLength(a: list, n: int, k: int):
    pos, ans, mx, pre = [0]*4
    q, dp = list(), [None]*(n+1)

    for i in range(n):
        x = len(q)
        try:
            while x != 0 and a[q[x-1]] < a[i]:
                q.pop()
                x = len(q)
            q.append(i)
        except IndexError:
            print(len(q))

        if i == 0:
            mx = a[i]
            dp[i] = a[i]
        elif mx <= a[i]:
            dp[i] = dp[i-1] + a[i]
            mx = a[i]
        else:
            dp[i] = dp[i-1]+a[i]

        if pre == 0:
            pos = 0
        else:
            pos = pre - 1

        while ((i-pre+1)*mx - (dp[i] - dp[pos]) > k) and pre < i:
            pos = pre
            pre += 1

            while x != 0 and q[0] < pre and pre < i:
                q.pop(0)
                mx = a[q[0]]
        ans = max(ans, i-pre+1)

    return ans


a = validSubArrLength(arr, n, k)
print(a)
