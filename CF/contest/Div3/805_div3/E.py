t=int(input())


class DisJoinUnion():
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[1]*n

    def find(self,x):
        if self.parent[x]==x:
            return x
        return self.find(self.parent[x])

    def union(self,x,y):
        fx,fy=self.find(x),self.find(y)

        if self.rank[fx]<self.rank[fy]:
            fx,fy=fy,fx

        self.parent[fy]=fx
        self.rank[fx]+=self.rank[fy]


for _ in range(t):
    n=int(input())

    check=True
    dsu=DisJoinUnion(n+1)
    ct=[0]*(n+1)
    for _ in range(n):
        a,b=[int(x) for x in input().split()]
        dsu.union(a,b)
        ct[a]+=1
        ct[b]+=1
        if ct[a]>2 or ct[b]>2:
            check=False

    if check:
        cnt=[0]*(n+1)
        for i in range(1,n+1):
            cnt[dsu.find(i)]+=1

        check=all(cnt[x]%2==0 for x in range(1,n+1))
    if check:
        print('YES')
    else:
        print('NO')




