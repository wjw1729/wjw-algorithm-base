
from itertools import permutations
from collections import defaultdict
def minops(pls):

    f=[0]*2
    l0,l1=0,0

    for i in range(n):
        g=[float('inf')]*2
        minl=min(pls[i])
        maxl=max(pls[i])

        g[0]=min(f[0]+abs(l0-minl)+maxl-minl,f[1]+abs(l1-minl)+maxl-minl)
        g[1]=min(f[0]+abs(l0-maxl)+maxl-minl,f[1]+abs(l1-maxl)+maxl-minl)

        l0=maxl
        l1=minl
        f=g[:]

    return min(f)

t=int(input())

for i in range(t):
    n,p=[int(x) for x in input().split()]
    pls=[]
    for _ in range(n):
        pls.append([int(x) for x  in input().split()])

    res=minops(pls)
    print('Case #%d: %d'%(i+1,res))