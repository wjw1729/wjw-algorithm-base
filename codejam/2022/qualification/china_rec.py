



import heapq
from collections import defaultdict,deque
def maxscore(scorels,edges):

    n=len(scorels)
    level=[0]*n
    heap=[]
    tree=defaultdict(list)

    edges=[x-1 for x  in edges]
    queue = deque()

    for i in range(n):
        if edges[i]!=-1:
            tree[edges[i]].append(i)
        else:
            queue.append(i)

    while queue:
        node=queue.popleft()

        for v in tree[node]:
            level[v]=level[node]+1
            queue.append(v)


    ns=set(x for x in edges if x>=0)

    for i in range(n):
        if i not in ns:
            heapq.heappush(heap,(level[i],scorels[i],i))

    ans=0
    vis=set()
    while heap:
        lev,score,node=heapq.heappop(heap)

        while edges[node]>=0:
            node=edges[node]
            if node in vis:
                break
            vis.add(node)
            score=max(score,scorels[node])

        ans+=score
    return ans

n=int(input())
for i in range(n):
    m=input()
    socrels=[int(x) for x in input().strip().split()]
    edges=[int(x) for x in input().strip().split()]
    res=maxscore(socrels,edges)
    print('Case #%d: %d'%(i+1,res))













