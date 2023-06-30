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


class Solution:
    def countPairs(self, n: int, edges) -> int:
        dsu = DisJoinUnoin(n)

        for a,b in edges:
            dsu.union(a,b)

        ans=(n-1)*n//2

        g=[[] for _ in range(n)]
        for i in range(n):
            g[dsu.find(i)].append(i)

        for v in g:
            ans-=len(v)*(len(v)-1)//2

        return ans

