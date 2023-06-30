def getmap(x, y):
    return (y, n - 1 - x), (n - 1 - x, n - 1 - y), (n - 1 - y, x), (x, y)


t = int(input())

for _ in range(t):
    n = int(input())
    mat = []
    for _ in range(n):
        mat.append([int(x) for x in input()])

    ans = 0

    for i in range(n // 2):
        for j in range(i, n - 1 - i):
            tmp = sum(mat[x][y] == 0 for x, y in getmap(i, j))
            ans += min(tmp, 4 - tmp)


    print(ans)
