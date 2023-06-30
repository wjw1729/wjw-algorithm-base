"""
author:wjw
分析：
    时光倒流+并查集。时间复杂度：O(m*n*alpha(m*n))
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

    def unionset(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return
        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx
        self.rank[fx] += self.rank[fy]
        self.parent[fy] = fx


class Solution:
    def latestDayToCross(self, row, col, cells):

        dsu = DisjointSetUnion(row * col + 2)

        land = set()
        for t in range(row * col - 1, -1, -1):
            r, c = cells[t][0] - 1, cells[t][1] - 1
            land.add((r, c))

            if r == 0:
                dsu.unionset(c, row * col)
            if r == row - 1:
                dsu.unionset(r * col + c, row * col + 1)

            for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if (x, y) in land:
                    dsu.unionset(r * col + c, x * col + y)

            if dsu.find(row * col) == dsu.find(row * col + 1):
                return t


row = 3
col = 3
cells = [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]
res = Solution().latestDayToCross(row, col, cells)
print(res)
