
from collections import defaultdict
import random
t=int(input())


def q(i,j):
    print('? '+str(i+1)+' '+str(j+1),flush=True)
    return int(input())
for _ in range(t):
    n=int(input())


    def solve():
        pls=list(range(n))
        random.shuffle(pls)
        while len(pls)>2:
            a=pls[0]
            pi=0
            d=defaultdict(list)
            for j in pls[1:]:
                tmp=q(a,j)
                pi=max(pi,tmp)
                d[tmp].append(j)
            if len(d)==len(pls)-1:
                return a,a

            pls=d[pi]
        if len(pls)==1:
            return pls[0],pls[0]
        return pls

    res=solve()
    print('! '+' '.join(str(x+1) for x in res),flush=True)
    input()






