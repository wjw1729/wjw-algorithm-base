from collections import deque
# 基环树:遍历基环+链
class Solution:
    def maximumInvitations(self, favorite) -> int:
        n = len(favorite)
        g = [[] for _ in range(n)]
        rg = [[] for _ in range(n)]
        indeg = [0] * n

        for u, v in enumerate(favorite):
            g[u].append(v)
            rg[v].append(u)
            indeg[v] += 1

        # 拓扑排序
        queue = deque(i for i, d in enumerate(indeg) if d == 0)

        while queue:
            u = queue.popleft()
            for v in g[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    queue.append(v)

        # 找基环
        ring = []
        vis = [False] * n

        def dfs(u):
            vis[u] = True
            ring.append(u)
            for v in g[u]:
                if not vis[v]:
                    dfs(v)

        # 找单边最长链
        maxdepth = 0

        def rdfs(u, fa, depth):
            nonlocal maxdepth
            maxdepth = max(maxdepth, depth)

            for v in rg[u]:
                if v != fa:
                    rdfs(v, u, depth + 1)

        max_ringsize = 0
        max_chainsize = 0

        for i, d in enumerate(indeg):
            if d > 0 and vis[i] == False:
                ring = []
                dfs(i)

                if len(ring) == 2:

                    u, v = ring
                    maxdepth = 0
                    rdfs(u, v, 1)
                    max_chainsize += maxdepth
                    maxdepth = 0
                    rdfs(v, u, 1)
                    max_chainsize += maxdepth


                else:
                    max_ringsize = max(max_ringsize, len(ring))

        return max(max_chainsize, max_ringsize)

favorite=[2,2,1,2]
res=Solution().maximumInvitations(favorite)
print(res)
