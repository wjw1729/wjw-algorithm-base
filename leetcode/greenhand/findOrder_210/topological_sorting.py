"""
author：wjw
分析：拓扑排序。
O(m+n)
"""

from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCoureses, prerequisites):

        adj = defaultdict(list)
        indeg = [0] * numCoureses
        for u, v in prerequisites:
            adj[v].append(u)
            indeg[u] += 1

        L = []
        S = deque(u for u in range(numCoureses) if indeg[u] == 0)

        while S:
            u = S.popleft()
            L.append(u)

            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    S.append(v)

        return L


numCourses = 2
prerequisites = [[1, 0]]
numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
res = Solution().findOrder(numCourses, prerequisites)
print(res)
