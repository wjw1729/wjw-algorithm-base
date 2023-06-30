from collections import defaultdict,deque
from functools import lru_cache


def solve(i):

    ans=[-1]*(n+1)

    @lru_cache(None)
    def dfs(pre,node):

        res=max(0,len(edegs[node])-2)
        for v in edegs[node]:
            if v==pre:
                continue
            if ans[v]==-1:
                dfs(node, v)
            res+=ans[v]

        ans[node]=res


    dfs(None,i)

    return  ans[i]+1



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

    res=float('inf')
    for i in range(1,n+1):

        tmp=solve(i)
        res=min(res,solve(i))

    print(res)




