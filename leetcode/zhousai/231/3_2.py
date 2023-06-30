# bfs+拓扑排序
from collections import deque,defaultdict
class Solution:
    def countRestrictedPaths(self, n: int, edges) -> int:

        MOD = 10 ** 9 + 7
        adjacent = defaultdict(list)

        for u, v, w in edges:
            adjacent[u].append((v, w))
            adjacent[v].append((u, w))

        shortestvalue = [float('inf')] * (n + 1)
        shortestvalue[n] = 0

        queue = deque()
        queue.append(n)

        optimalmap = defaultdict(list)

        while queue:
            u = queue.popleft()

            for v, w in adjacent[u]:
                if shortestvalue[u] + w < shortestvalue[v]:
                    shortestvalue[v] = shortestvalue[u] + w
                    queue.append(v)
                    optimalmap[u].append(v)

        dp = [0] * (n + 1)

        dp[n] = 1

        indeg = [0] * (n + 1)

        for u in range(1, n + 1):
            for v in optimalmap[u]:
                if shortestvalue[v] > shortestvalue[u]:
                    indeg[v] += 1

        queue = deque()
        queue.append(n)

        while queue:
            u = queue.popleft()

            for v in optimalmap[u]:
                if shortestvalue[v] > shortestvalue[u]:
                    dp[v] += dp[u]
                    dp[v] %= MOD
                    indeg[v] -= 1
                    if indeg[v] == 0:
                        queue.append(v)

        return dp[1]

n = 5
edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
res=Solution().countRestrictedPaths(n,edges)
print(res)