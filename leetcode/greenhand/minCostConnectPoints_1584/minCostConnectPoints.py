"""
author:wjw
分析：kruskal 算法生成最小生成树。加并查集维护连通关系。
时间复杂度：O（n**2logn）。

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
    def minCostConnectPoints(self, points):

        n = len(points)
        dsu = DisjointSetUnion(n)

        edges = []

        for i in range(n):
            for j in range(i + 1, n):
                dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dis, i, j))

        edges.sort(key=lambda x: x[0])

        ans = 0
        for i in range(len(edges)):
            dis, x, y = edges[i]

            if dsu.find(x) != dsu.find(y):
                ans += dis
                dsu.unionSet(x, y)

        return ans


points = [[3, 12], [-2, 5], [-4, 1]]
points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
points = [[0, 0], [1, 1], [1, 0], [-1, 1]]
points = [[-1000000, -1000000], [1000000, 1000000]]
points = [[0, 0]]
res = Solution().minCostConnectPoints(points)
print(res)
