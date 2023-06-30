from collections import deque
class Solution:
    def mostProfitablePath(self, edges, bob: int, amount) -> int:

        n=len(edges)+1
        g=[[] for _ in range(n)]
        deg=[0]*n
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
            deg[x]+=1
            deg[y]+=1

        scorea=[0]*(n)

        opent=[float('inf')]*n
        bobp=[]

        def dfs(node,path):
            nonlocal bobp
            if node==bob:
                bobp=path[:]
                return


            for  v in g[node]:
                if (len(path)>=2 and v !=path[-2]) or len(path)<2:
                    path.append(v)
                    dfs(v,path)
                    path.pop()


        dfs(0,[0])
        i=0
        for c in bobp[::-1]:
            opent[c]=i
            i+=1

        ans=float('-inf')
        q=deque()
        q.append((0,amount[0],0,-1))

        while q:
            u,score,t,pre=q.popleft()
            if deg[u]==1 and u!=0:
                ans=max(ans,score)

            for v in g[u]:
                if v!=pre:
                    if t+1>opent[v]:
                        q.append((v,score,t+1,u))
                    elif t+1==opent[v]:
                        q.append((v,score+amount[v]/2,t+1,u))
                    else:
                        q.append((v,score+amount[v],t+1,u))

        return ans
edges = [[0,1],[1,2],[1,3],[3,4]]
bob = 3
amount = [-2,4,2,-4,6]
res=Solution().mostProfitablePath(edges,bob,amount)
print(res)