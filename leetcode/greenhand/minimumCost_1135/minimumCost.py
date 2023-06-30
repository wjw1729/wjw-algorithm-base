"""
来源：尊贵的会员题
author:wjw
分析：kruskal算法。时间复杂度O(nlogn)，n为边数。
稀疏图？
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
    def minimumCost(self, n, connections):
        if len(connections) < n - 1:
            return -1

        dsu = DisjointSetUnion(n)
        connections.sort(key=lambda x: x[2])
        ans = 0
        num = 0

        for x, y, cost in connections:
            x -= 1
            y -= 1
            if dsu.find(x) != dsu.find(y):
                ans += cost
                dsu.unionSet(x, y)
                num += 1
                if num == n - 1:
                    break

        return ans if num == n - 1 else -1


n = 3
connections = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]
n = 4
connections = [[1, 2, 3], [3, 4, 4]]
res = Solution().minimumCost(n, connections)
print(res)
