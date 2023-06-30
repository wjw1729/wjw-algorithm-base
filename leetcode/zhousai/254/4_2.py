"""
author:wjw
分析：时光倒流+并查集。O(m*n*alpha(m*n))
    会超时。O（m*n**3）。
    所以要引入两个超级结点。
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
    def latestDayToCross(self, row, col, cells):
        dsu = DisjointSetUnion(row * col)

        land = set()
        for k in range(row * col - 1, -1, -1):
            r, c = cells[k]
            r -= 1
            c -= 1
            land.add((r, c))

            for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= x < row and 0 <= y < col and (x, y) in land:
                    dsu.unionSet(r * col + c, x * col + y)

            for i in range(col):
                for j in range((row - 1) * col, row * col):
                    if dsu.find(i) == dsu.find(j):
                        return k


row = 2
col = 2
cells = [[1, 1], [2, 1], [1, 2], [2, 2]]
row = 2
col = 2
cells = [[1, 1], [1, 2], [2, 1], [2, 2]]
row = 3
col = 3
cells = [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]

res = Solution().latestDayToCross(row, col, cells)
print(res)
