"""
author:wjw
分析：先通过无向图求取最短路劲长度。再建立有向无环图。
在利用动态规划。
"""
from collections import defaultdict, deque


class Solution:
    def countPaths(self, n: int, roads) -> int:
        MOD = 10 ** 9 + 7
        time = [float('inf')] * n
        nums = [0] * n
        time[0] = 0
        nums[0] = 1

        adj = defaultdict(list)
        for u, v, cost in roads:
            adj[u].append((v, cost))
            adj[v].append((u, cost))

        queue = deque()
        queue.append((0, time[0]))

        while queue:
            u, t = queue.popleft()
            for v, cost in adj[u]:
                if t + cost <= time[v]:
                    if time[v] == t + cost:
                        nums[v] += 1  # nums
                    else:
                        nums[v] = 1
                    time[v] = t + cost
                    queue.append((v, time[v]))

        return nums[n - 1] % MOD


n = 7
roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]
res = Solution().countPaths(n, roads)
print(res)
