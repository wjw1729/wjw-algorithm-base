"""

"""

from collections import defaultdict


class Solution:
    def domino(self, n: int, m: int, broken) -> int:

        hashmap = defaultdict(list)
        broken = {(x, y) for x, y in broken}
        Match = {}

        for i in range(n):
            for j in range(m):
                if (i, j) in broken:
                    continue
                for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= x < n and 0 <= y < m and (x, y) not in broken:
                        hashmap[(i, j)].append((x, y))
                Match[(i, j)] = None

        n = len(hashmap)

        def dfs(u):
            for v in hashmap[u]:
                if vis[v]:
                    continue
                vis[v] = True
                if Match[v] == None or dfs(v):
                    Match[u] = v
                    Match[v] = u
                    return True
            return False

        ans = 0

        for i, j in hashmap.keys():
            vis = {k: False for k, v in hashmap.items()}
            if Match[(i, j)] == None:
                if dfs((i, j)):
                    ans += 1

        return ans


n = 3
m = 3
broken = []
res = Solution().domino(n, m, broken)
print(res)
