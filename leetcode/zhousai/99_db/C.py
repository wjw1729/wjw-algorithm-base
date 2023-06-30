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
    def countWays(self, ranges) -> int:
        mod=10**9+7

        n=len(ranges)
        ranges.sort()
        dsu=DisJoinUnoin(n)

        pret=ranges[0][1]
        pre=0
        for i,(s,t) in enumerate(ranges):
            if i==0:
                continue
            if s<=pret:
                dsu.union(pre,i)
                pret=max(pret,t)
            else:
                pre=i
                pret=t


        vis=set()
        for i in range(n):
            vis.add(dsu.find(i))

        return pow(2,len(vis),mod)

ranges=[[34,56],[28,29],[12,16],[11,48],[28,54],[22,55],[28,41],[41,44]]
res=Solution().countWays(ranges)
print(res)



