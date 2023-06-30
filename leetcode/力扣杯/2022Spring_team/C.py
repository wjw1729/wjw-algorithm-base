from collections import defaultdict
class Solution:
    def getMaximumNumber(self, moles) -> int:



        d=defaultdict(set)
        timels=set()
        for t,x,y in moles:
            d[t].add(x*3+y)
            timels.add(t)

        timels=list(timels)
        timels.sort()

        adj=[[] for _ in range(9)]
        adj[0]=[0,1,3]
        adj[1]=[0,1,2,4]
        adj[2]=[1,2,5]
        adj[3]=[0,6,4,3]
        adj[4]=[1,3,5,7,4]
        adj[5]=[2,4,8,5]
        adj[6]=[3,7,6]
        adj[7]=[4,6,8,7]
        adj[8]=[5,7,8]


        f = [-float('inf')] * 9
        f[4]=0 if 4 not in d[0] else 1

        for i,k in enumerate(timels):
            if k==0:
                continue

            ttt=k-timels[i-1] if i>0 else k
            if ttt-1>=4:
                f=[max(f)]*9
            for tt in range(ttt-1):
                g=[x for x in f]
                for j in range(9):
                    for nx in adj[j]:
                        g[j] = max(g[j], f[nx])
                if f==g:
                    break
                f=[x for x in g]

            g=[x for x in f]
            for j in range(9):
                if j in d[k]:
                    for nx in adj[j]:
                        g[j] = max(f[nx] + 1, g[j])
                else:
                    for nx in adj[j]:
                        g[j] = max(g[j], f[nx])
            f=[x for x in g]

        return max(f)

import random
import time
moles = [[1,1,0],[2,0,1],[4,2,2]]
moles = [[2,0,2],[5,2,0],[4,1,0],[1,2,1],[3,0,2]]
#moles = [[0,1,0],[0,0,1]]

moles=[[0,0,0] for _ in range(10**5)]
for i in range(10**5):
    moles[i][0]=random.randint(1,10**9)
    moles[i][1]=random.randint(0,2)
    moles[i][2] = random.randint(0, 2)

t1=time.time()
res=Solution().getMaximumNumber(moles)
print(res)
print(time.time()-t1)
