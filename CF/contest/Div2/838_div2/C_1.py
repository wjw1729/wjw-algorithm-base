n = int(input())

mod = 998244353
cls = []


def solve():
    g = [[-1] * n for _ in range(n)]

    for i in range(n):
        cls.append([int(x) for x in input().split()])
        g[i][i:] = cls[i]

    for i in range(n):
        for j in range(i, n):
            if g[i][j] == 1:
                for ii in range(i,j+1):
                    for jj in range(ii,j+1):
                        if g[ii][jj]==2:
                            return 0


