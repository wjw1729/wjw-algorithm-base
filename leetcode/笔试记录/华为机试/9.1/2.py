"""
author:wjw
分析：知识图谱

    建图+BFS就好
"""

from collections import  defaultdict,deque
class Solution:
    def Instances(self,n,connections,target):

        instances=defaultdict(list)
        subclass=defaultdict(list)

        for connection in connections:
            v,link,u=connection.split()
            if link=='subClassOf':
                subclass[u].append(v)
            if link=='instanceOf':
                instances[u].append(v)

        ans=[]
        queue=deque()
        queue.append(target)
        bin={target}

        while queue:
            u=queue.popleft()
            if u in instances:
                ans+=instances[u]

            for v in subclass[u]:
                if v not in bin:
                    queue.append(v)
                    bin.add(v)
        ans.sort()
        if not ans:
            return 'empty'

        return ' '.join(ans)


n=int(input().strip())
connections=[]
for i in range(n):
    connections.append(input().strip())
target=input().strip()

res=Solution().Instances(n,connections,target)
print(res)