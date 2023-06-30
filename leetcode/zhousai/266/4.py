"""
author:wjw
ref:pku_erutan
分析：dfs+剪枝+优先队列(优先队列存放的是一个四元组(cost,value,node,visited))

"""

from collections import defaultdict
import heapq

class Solution:
    def maximalPathQuality(self,values,edges,maxTime):

        n=len(values)

        adjacent=defaultdict(dict)

        for u,v,w in edges:
            adjacent[u][v]=w
            adjacent[v][u]=w


        maxv=[-1]*(n)#这个仅仅是用来进行第一次剪枝的（在满足time<maxTime内到每个点的最大价值）
        minc=[float('inf')]*n#当前结点回0点的最短路径


        heap=[(0,values[0],0,{0})]

        ans=0

        while heap:
            cost,value,node,visited=heapq.heappop(heap)

            if value<=maxv[node]:
                continue

            maxv[node]=value
            minc[node]=min(cost,minc[node])

            if node==0:
                ans=max(value,ans)

            for nxt in adjacent[node]:
                nc=cost+adjacent[node][nxt]
                if nc+minc[nxt]>maxTime and 2*nc>maxTime:
                    continue

                nv=value
                nxtv=visited

                if nxt not in visited:
                    nv=value+values[nxt]
                    nxtv=visited|{nxt}

                heapq.heappush(heap,(nc,nv,nxt,nxtv))

        return ans



values = [0,32,10,43]
edges = [[0,1,10],[1,2,15],[0,3,10]]
maxTime = 49
values = [5,10,15,20]
edges = [[0,1,10],[1,2,10],[0,3,10]]
maxTime = 30
values=[61,11,18,43,81]
edges=[[0,3,45],[0,2,16],[0,1,36],[3,4,38],[2,3,29]]
maxTime=88
res=Solution().maximalPathQuality(values,edges,maxTime)
print(res)




