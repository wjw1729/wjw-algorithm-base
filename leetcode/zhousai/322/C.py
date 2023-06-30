class DisJoinUnoin:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[1]*n


    def find(self,x):
        if self.parent[x]==x:
            return x
        else:
            return self.find(self.parent[x])


    def union(self,x,y):
        fx,fy=self.find(x),self.find(y)

        if fx==fy:
            return

        if self.rank[fx]<self.rank[fy]:
            fx,fy=fy,fx

        self.parent[fy]=fx
        self.rank[fx]+=self.rank[fy]

class Solution:
    def minScore(self, n: int, roads) -> int:

        dsu=DisJoinUnoin(n)

        g=[float('inf')]*n
        for u,v,w in roads:
            u-=1
            v-=1

            dsu.union(u,v)
            g[u]=min(g[u],w)
            g[v]=min(g[v],w)

        ans=float('inf')
        for i in range(n):
            if dsu.find(0)==dsu.find(i):
                ans=min(ans,g[i])

        return ans

