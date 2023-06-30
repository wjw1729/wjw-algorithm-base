"""
拓扑排序法。
"""
from collections import deque

class Solution:
    def deleteTreeNodes(self,nodes,parent,value):

        childrennum=[0]*nodes

        for u,v in enumerate(parent):
            if v!=-1:
                childrennum[v]+=1

        subnum=[1]*nodes
        queue=deque(x for x in range(nodes) if childrennum[x]==0)


        while queue:
            node=queue.popleft()

            if value[node]==0:
                subnum[node]=0

            childrennum[parent[node]]-=1
            value[parent[node]]+=value[node]
            subnum[parent[node]]+=subnum[node]
            if childrennum[parent[node]]==0:
                queue.append(parent[node])


        return subnum[0]

nodes=7
parent=[-1,0,0,1,2,2,2]
value=[1,-2,4,0,-2,-1,-1]


nodes=7
parent=[-1,0,0,1,2,2,2]
value=[1,-2,4,0,-2,-1,-2]

nodes=5
parent=[-1,0,1,0,0]
value=[-672,441,18,728,378]

nodes=5
parent=[-1,0,0,1,1]
value=[-686,-842,616,-739,-746]


res=Solution().deleteTreeNodes(nodes,parent,value)
print(res)
