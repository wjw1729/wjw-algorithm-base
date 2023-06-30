"""
author:wjw
分析：并查集。
时间复杂度:O(mnlogmn)
"""


class DisjointSetUnion:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])

    def unionSet(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return

        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx

        self.rank[fx] += self.rank[fy]
        self.parent[fy] = fx


class Solution:
    def minimumEffortPath(self, heights):
        m = len(heights)
        n = len(heights[0])

        edges = []

        for i in range(m):
            for j in range(n):

                for x, y in [(i + 1, j), (i, j + 1)]:
                    if 0 <= x < m and 0 <= y < n:
                        dis = abs(heights[x][y] - heights[i][j])
                        edges.append((dis, i * n + j, x * n + y))

        edges.sort(key=lambda x: x[0])

        dsu = DisjointSetUnion(m * n)

        for edge in edges:
            dis, x, y = edge

            dsu.unionSet(x, y)
            if dsu.find(0) == dsu.find(m * n - 1):
                return dis


heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
heights = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
heights=[[3]]
res = Solution().minimumEffortPath(heights)
print(res)

