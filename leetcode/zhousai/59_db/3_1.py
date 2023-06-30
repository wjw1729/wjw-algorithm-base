"""
author:wjw
分析：先通过无向图求取最短路劲长度。再建立有向无环图。
在利用动态规划。
整个问题的求解分为三个步骤。第一步根据无向图求解最短路径。第二步无向图以及求出的最短路径构建有向图。第三步根据有向图求取最短路径的数目。（拓扑排序，记忆化搜索）。
时间复杂度:O(E+V)
"""

from collections import deque,defaultdict
class Solution:
    def countPaths(self,n,roads):
        if not roads:
            return 1
        MOD=10**9+7
        times=[float('inf')]*n
        times[0]=0
        queue=deque()
        queue.append(0)


        adj=defaultdict(list)

        for u,v,cost in roads:
            adj[u].append((v,cost))
            adj[v].append((u,cost))


        while queue:
            u=queue.popleft()

            for v,cost in adj[u]:
                if times[u]+cost<times[v]:
                    times[v]=times[u]+cost
                    queue.append(v)

        dag=defaultdict(list)
        for u,v ,cost in roads:
            if times[u]-times[v]==cost:
                dag[v].append(u)
            if times[v]-times[u]==cost:
                dag[u].append(v)

        f=[float('inf')]*n
        f[n-1]=1

        ###不在目标路径上的点的值为0，不影响。
        def update(u):

            res=0
            for v in dag[u]:
                if f[v]==float("inf"):
                    update(v)
                res+=f[v]
            f[u]=res%(MOD)
            return

        update(0)

        return f[0]%MOD

n = 7
roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]
res = Solution().countPaths(n, roads)
print(res)