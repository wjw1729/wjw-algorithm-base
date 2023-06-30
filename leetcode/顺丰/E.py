class DisJoinUnion:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[1]*n

    def find(self,x):
        if self.parent[x]==x:
            return x
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
    def isCompliance(self, distance, n: int) -> bool:

        m=len(distance)

        dsu=DisJoinUnion(m)
        for i in range(m):
            for j in range(i+1,m):
                if distance[i][j]<=2:
                    dsu.union(i,j)

        ans=0
        vis=set()
        for i in range(m):
            fi=dsu.find(i)
            if fi in vis:
                continue
            ans+=1
            vis.add(fi)

        return ans<=n
