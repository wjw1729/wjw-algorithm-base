
from collections import defaultdict,deque
class Solution:
    def networkBecomesIdle(self, edges, patience) -> int:

        n = len(patience)
        minpaths = [float('inf')] * n

        adjacent = defaultdict(list)

        for u, v in edges:
            adjacent[u].append(v)
            adjacent[v].append(u)

        minpaths[0] = 0
        queue = deque()
        queue.append(0)

        while queue:
            u = queue.popleft()

            for v in adjacent[u]:
                if minpaths[u] + 1 < minpaths[v]:
                    minpaths[v] = minpaths[u] + 1
                    queue.append(v)

        last = [(2*minpaths[i] - 1) // patience[i] * patience[i] + 2*minpaths[i] for i in range(1, n)]

        return max(last) + 1


edges = [[0,1],[1,2]]
patience = [0,2,1]
edges = [[0,1],[0,2],[1,2]]
patience = [0,10,10]
res=Solution().networkBecomesIdle(edges,patience)
print(res)