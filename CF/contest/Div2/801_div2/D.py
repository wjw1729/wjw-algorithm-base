from collections import defaultdict,deque


def bfs(node):

    q=deque()
    q.append((node,0))
    group=defaultdict(set)
    vis=set()
    vis.add(node)

    while q:
        u,l=q.popleft()

        for v in edegs[u]:
            if v not in vis:
                group[l+1].add(v)
                q.append((v,l+1))
                vis.add(v)

    return max(len(v) for k,v in group.items())




t=int(input())
for _ in range(t):
    n=int(input())
    if n==1:
        print(0)
        continue
    edegs = defaultdict(list)
    deg=[0]*(n+1)
    for _ in range(n-1):
        x,y=[int(x) for x in input().split()]
        edegs[x].append(y)
        edegs[y].append(x)
        deg[x]+=1
        deg[y]+=1

    ans=n
    for i in range(1,n+1):
        if deg[i]==1:
            ans=min(ans,bfs(i))

    print(ans)




