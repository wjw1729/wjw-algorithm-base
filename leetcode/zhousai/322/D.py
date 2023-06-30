class DisJoinUnoin:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])

    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)

        if fx == fy:
            return

        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx

        self.parent[fy] = fx
        self.rank[fx] += self.rank[fy]


from collections import deque, defaultdict


class Solution:
    def magnificentSets(self, n: int, edges) -> int:

        dsu = DisJoinUnoin(n)

        g = [[] for _ in range(n)]
        for u, v in edges:
            u -= 1
            v -= 1
            g[u].append(v)
            g[v].append(u)
            dsu.union(u, v)

        def getnum(u):
            q = deque()
            q.append((u, 0))
            ans = 0
            vis = set()
            vis.add(u)

            while q:
                u, l = q.popleft()
                ans = max(ans, l + 1)

                for v in g[u]:
                    if v in vis:
                        continue
                    q.append((v, l + 1))
                    vis.add(v)

            return ans

        color = [-1] * n

        q = deque([0])
        color[0] = 0
        while q:
            u = q.popleft()

            for v in g[u]:
                if color[v] == -1:
                    q.append(v)
                    color[v] = 1 - color[u]
                else:
                    if color[v] + color[u] != 1:
                        return -1

        gls = defaultdict(int)

        for i in range(n):
            tmp = getnum(i)
            gls[dsu.find(i)] = max(gls[dsu.find(i)], tmp)

        return sum(gls.values())


n = 6
edges = [[1, 2], [1, 4], [1, 5], [2, 6], [2, 3], [4, 6]]
n = 92
edges = [[67, 29], [13, 29], [77, 29], [36, 29], [82, 29], [54, 29], [57, 29], [53, 29], [68, 29], [26, 29], [21, 29],
         [46, 29], [41, 29], [45, 29], [56, 29], [88, 29], [2, 29], [7, 29], [5, 29], [16, 29], [37, 29], [50, 29],
         [79, 29], [91, 29], [48, 29], [87, 29], [25, 29], [80, 29], [71, 29], [9, 29], [78, 29], [33, 29], [4, 29],
         [44, 29], [72, 29], [65, 29], [61, 29]]
n = 26
edges = [[9, 16], [8, 3], [20, 21], [12, 16], [14, 3], [7, 21], [22, 3], [22, 18], [11, 16], [25, 4], [2, 4], [14, 21],
         [23, 3], [17, 3], [2, 16], [24, 16], [13, 4], [10, 21], [7, 4], [9, 18], [14, 18], [14, 4], [14, 16], [1, 3],
         [25, 18], [17, 4], [1, 16], [23, 4], [2, 21], [5, 16], [24, 18], [20, 18], [19, 16], [24, 21], [9, 3], [24, 3],
         [19, 18], [25, 16], [19, 21], [6, 3], [26, 18], [5, 21], [20, 16], [2, 3], [10, 18], [26, 16], [8, 4],
         [11, 21], [23, 16], [13, 16], [25, 3], [7, 18], [19, 3], [20, 4], [26, 3], [23, 18], [15, 18], [17, 18],
         [10, 16], [26, 21], [23, 21], [7, 16], [8, 18], [10, 4], [24, 4], [7, 3], [11, 18], [9, 4], [26, 4], [13, 21],
         [22, 16], [22, 21], [20, 3], [6, 18], [9, 21], [10, 3], [22, 4], [1, 18], [25, 21], [11, 4], [1, 21], [15, 3],
         [1, 4], [15, 16], [2, 18], [13, 3], [8, 21], [13, 18], [11, 3], [15, 21], [8, 16], [17, 16], [15, 4], [12, 3],
         [6, 4], [17, 21], [5, 18], [6, 16], [6, 21], [12, 4], [19, 4], [5, 3], [12, 21], [5, 4]]

res = Solution().magnificentSets(n, edges)
print(res)
