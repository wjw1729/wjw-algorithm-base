from collections import defaultdict


n=int(input())
nodes=set()
g=defaultdict(list)
indeg=defaultdict(int)
for _ in range(n):
    ipls=[int(x) for x in input().split()]
    m,u=ipls[0],ipls[1]
    g[u]=ipls[2:]
    nodes|=set(ipls[1:])



def solve():

    vis = {}
    for c in nodes:
        vis[c]=False
    ans = []
    check=False

    def dfs(u, path):
        nonlocal check
        nonlocal ans
        if check:
            return
        if vis[u]:
            return

        for v in g[u]:
            if v in path:
                idx = path.index(v)
                ans=path[idx:]
                check=True
                return
            path.append(v)
            dfs(v, path)
            path.pop()

        vis[u] = True

    for i in nodes:
        dfs(i, [])

    return ans

ans=solve()

minidx=min(range(len(ans)),key=lambda x:ans[x])
ans=ans[minidx:]+ans[:minidx+1]
print(*ans)








