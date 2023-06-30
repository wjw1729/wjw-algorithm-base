"""
author:wjw
分析；树状dp+乘法逆元。

"""

from collections import defaultdict


class Solution:
    def waysToBuildRooms(self, prevRoom):

        MOD = 10 ** 9 + 7

        tree = defaultdict(list)

        n = len(prevRoom)

        for u, v in enumerate(prevRoom):
            tree[v].append(u)

        frac = [1] * n
        inv = [1] * n
        for i in range(1, n):
            frac[i] = frac[i - 1] * i % MOD
            inv[i] = pow(frac[i], MOD - 2, MOD)

        f = [1] * n

        cnt = [0] * n

        def dfs(u):
            f[u] = 1

            for v in tree[u]:
                dfs(v)
                f[u] = f[u] * f[v] * inv[cnt[v]] % MOD
                cnt[u] += cnt[v]
            f[u] = f[u] * frac[cnt[u]] % MOD
            cnt[u] += 1

        dfs(0)
        return f[0]


prevRoom = [-1, 0, 1]
prevRoom = [-1, 0, 0, 1, 2]
res = Solution().waysToBuildRooms(prevRoom)
print(res)
