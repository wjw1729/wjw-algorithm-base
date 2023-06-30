import math

mod = 998244353

n, k = [int(x) for x in input().split()]

tmp = 0

for i in range(n):
    tmp += k + i
    if tmp >= n:
        N = i + 1
        break

f = [[0] * (n + 1) for _ in range(N + 1)]
f[0][0] = 1

for i in range(1, N + 1):
    for j in range(1, n + 1):
        for jj in range(k + i - 1, j + 1, k + i - 1):
            f[i][j] += f[i - 1][j - jj]
            f[i][j] %= mod
ans = []
for j in range(1, n + 1):
    ans.append(sum(f[i][j] for i in range(N + 1)) % mod)

print(*ans)