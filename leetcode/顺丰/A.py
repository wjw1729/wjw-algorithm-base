from collections import  defaultdict,deque
class Solution:
    def hasCycle(self, graph: str) -> bool:
        g=defaultdict(list)
        rg=defaultdict(list)
        vis={}

        sls=graph.split(',')
        for s in sls:
            s0,s1=[int(x) for  x in s.split('->')]
            g[s0].append(s1)
            rg[s1].append(s0)
            vis[s0]=False
            vis[s1]=False

        ans = []

        def dfs(u, path):
            if vis[u]:
                return

            for v in rg[u]:
                if v in path:
                    idx = path.index(v)
                    ans.append(path[idx:])
                    continue
                path.append(v)
                dfs(v, path)
                path.pop()

            vis[u] = True

        for i in vis:
            dfs(i, [])

        return ans!=[]





graph=input()
res=Solution().hasCycle(graph)
print(res)






