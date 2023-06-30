from collections import deque,defaultdict


class DisJoinUnion:
    def __init__(self,n):
        self.parent=list(range(n+1))
        self.rank=[1]*(n+1)

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



t=int(input())

for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]


    q=deque(i for i in range(1,n+1))

    dsu=DisJoinUnion(n)
    for u,v in zip(a,b):
        dsu.union(u,v)

    pnum=defaultdict(int)
    for i in range(1,n+1):
        pnum[dsu.find(i)]+=1

    ans=0
    for k,v in sorted(pnum.items(),key=lambda x:x[1]):
        if v==1:
            continue

        m=v-1 if v%2==0 else v-2
        s=q.popleft()
        pre=s
        for i in range(m):
            if i%2==0:
                t=q.pop()
            else:
                t=q.popleft()

            ans+=abs(t-pre)
            pre=t
        ans+=abs(pre-s)

    print(ans)





