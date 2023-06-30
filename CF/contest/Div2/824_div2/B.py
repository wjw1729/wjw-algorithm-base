import math
t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    mina=min(a)
    res=0
    for c in a:
        res+=math.ceil(c/(2*mina-1))-1

    print(res)
