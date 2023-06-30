
from collections import deque

n,m=[int(x) for x  in input().split()]
g=[[] for _ in range(n)]
indeg=[0]*n
outdeg=[0]*n
tpdeg=[0]*n
for _ in range(m):
    v,u=[int(x) for x  in input().split()]
    v-=1
    u-=1
    g[v].append(u)
    outdeg[v]+=1
    indeg[u]+=1
    tpdeg[u]+=1


q=deque(i for i in range(n) if indeg[i]==0)
f=[1]*n

while q:
    u=q.popleft()

    for v in g[u]:
        if indeg[v]>1 and outdeg[u]>1:
            f[v]=max(f[v],f[u]+1)
        tpdeg[v] -= 1
        if tpdeg[v]==0:
            q.append(v)


print(max(f))



