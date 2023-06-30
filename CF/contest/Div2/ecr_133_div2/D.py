
from collections import defaultdict

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

d = [defaultdict(int) for _ in range(N + 1)]
d[0][0] = 1
for j in range(1, n + 1):
    for i in range(1, N + 1):
        f[i][j] += d[i - 1][j % (k + i - 1)]
        f[i][j] %= mod

    for i in range(1, N + 1):
        d[i][j % (k + i)] += f[i][j]
        d[i][j % (k + i)] %= mod


ans = []
for j in range(1, n + 1):
    ans.append(sum(f[i][j] for i in range(N + 1)) % mod)

print(*ans)
