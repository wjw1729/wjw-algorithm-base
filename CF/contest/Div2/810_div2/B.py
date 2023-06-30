

t=int(input())

for _ in range(t):
    n,m=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]

    g=[[] for _ in range(n)]
    indeg=[0]*n

    for _ in range(m):
        x,y=[int(x) for x in input().split()]
        x-=1
        y-=1
        g[x].append(y)
        g[y].append(x)
        indeg[x]+=1
        indeg[y]+=1

    if m%2==0:
        print(0)
    else:
        ols=[i for i in range(n) if indeg[i]%2==1]

        ans=min([a[i] for i in ols] ,default=float('inf'))

        for i in range(n):

            if not g[i] or indeg[i]%2==1 :
                continue
            ans=min(ans,a[i]+min([a[j] for j in g[i] if indeg[j]%2==0],default=float('inf') ))

        print(ans)


