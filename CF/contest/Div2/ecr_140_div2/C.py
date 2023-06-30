n = int(input())

mod = 998244353
cls = []


def solve():
    g = [[-1] * n for _ in range(n)]

    for i in range(n):
        cls.append([int(x) for x in input().split()])
        if cls[i][0] == 2:
            return 0
        is2 = False
        for x in cls[i]:
            if x == 2:
                is2 = True
            if x == 1 and is2 == True:
                return 0

        g[i][i:] = cls[i]

    for i in range(n):
        for j in range(i, n):
            if g[i][j] == 2:
                if any(x == 1 for x in [g[ii][jj] for ii in range(i + 1) for jj in range(j, n)]):
                    return 0

    # print(g)

    l = list(range(n))
    for i in range(n):
        for j in range(n - i):
            if cls[i][j] == 1:
                r = i + j + 1
                l[i:r] = [l[i]] * (r - i)

    a0 = 1  # 纯
    a1 = 0  # 不纯
    if l[n-1]==0:
        return 2
    i = l[l[n-1]-1]


    j=l[n-1]
    while i >= 0:

        if g[i][j] == 2:
            a1 = (a0 + a1 * 2) % mod
            a0 = 0

        elif g[i][j] == 0:
            a0 = a0
            a1 = (a0 + a1 * 2) % mod
        j=i
        if i==0:
            break
        i=l[i-1]
    return (a0 + a1) * 2 % mod


print(solve())
