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

n=int(input())
pls=[int(x) for  x in input().split()]

dsu=DisJoinUnoin(n+1)
for i in range(n):
    dsu.union(i+1,pls[i])

ans=0
vis=set()
for i in range(1,n+1):
    fi=dsu.find(i)
    if fi not in vis:
        ans+=1
        vis.add(fi)

print(ans)



