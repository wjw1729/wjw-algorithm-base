class Solution:
    def maxStarSum(self, vals, edges, k: int) -> int:

        n=len(vals)
        g=[[] for _ in range(n)]

        for u,v in edges:
            if vals[v]>0:
                g[u].append(vals[v])
            if vals[u]>0:
                g[v].append(vals[u])

        ans=max(vals)
        for i in range(n):

            g[i].sort(reverse=True)
            ans=max(ans,sum(g[i][:k])+vals[i])

        return ans

vals = [1,2,3,4,10,-10,-20]
edges = [[0,1],[1,2],[1,3],[3,4],[3,5],[3,6]]
k = 2
vals = [-5]
edges = []
k = 0
res=Solution().maxStarSum(vals,edges,k)
print(res)