"""https://codeforces.com/contest/175/problem/C"""

n = int(input())
gls = []
for _ in range(n):
    m, sc = [int(x) for x in input().split()]
    gls.append([m, sc])

t = int(input())
p = [int(x) for x in input().split()]
for i in range(t - 1, 0, -1):
    p[i] = p[i] - p[i - 1]
p += [float('inf')]


def solve():
    gls.sort(key=lambda x: x[1])
    ans = 0

    j = 0
    for i in range(t + 1):
        while j < n and gls[j][0] <= p[i]:
            ans += gls[j][1] * (i + 1) * gls[j][0]

            p[i] -= gls[j][0]
            gls[j][0] = 0
            j += 1

        if j >= n:
            return ans

        gls[j][0] -= p[i]
        ans += gls[j][1] * (i + 1) * p[i]
        p[i] = 0

    return ans


print(solve())
