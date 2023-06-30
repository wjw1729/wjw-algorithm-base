"""
树上不相邻节点和最大。

递归.树上dp。
每个节点存储两种情况下的目标值，（选择该点、不选该点）
"""

from collections import defaultdict
class Solution:
    def maxsumTree(self,values,edges):

        values=[0]+values
        g=defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)

        chose=dict()#(maxsum,minnum)
        nch=dict()

        def dfs(pre,node):
            if node in chose and node in nch:
                return

            chres=[values[node],values[node]]
            nchres=[0,float('inf')]

            for v in g[node]:
                if v!=pre:
                    if v not in chose:
                        dfs(node,v)
                    chres[0]+=nch[v][0]
                    chres[1]=min(nch[v][1],chres[1])

                    nchres[0]+=chose[v][0]
                    nchres[1]=min(nchres[1],chose[v][1])

            chose[node]=tuple(chres)
            nch[node]=tuple(nchres)

        dfs(0,1)#0节点不存在，所以也不会有影响(将1视为根节点)

        if chose[1][0]>nch[1][0]:
            ans=chose[1]
        elif chose[1][0]<nch[1][0]:
            ans=nch[1]
        else:
            if chose[1][1]<nch[1][0]:
                ans=chose[1]
            else:
                ans=nch[1]

        return ans

nm=input().strip().split()
n,m=[int(x) for x in nm]
values=[int(x) for x in input().strip().split()]
edges=[]

for i in range(m):
    edges.append(int(x) for x  in input().strip().split())

print(Solution().maxsumTree(values,edges))














