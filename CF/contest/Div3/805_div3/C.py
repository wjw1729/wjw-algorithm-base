from collections import defaultdict
import random

t=int(input())
for _ in range(t):

    input()
    n,k=[int(x) for x  in input().split()]
    delta = random.randint(1, n)
    u=[int(x)+delta for x  in input().split()]


    li={}
    ri= {}

    for i in range(n):
        if u[i] in li:
            li[u[i]]=min(i,li[u[i]])
            ri[u[i]] = max(i, ri[u[i]])
        else:
            li[u[i]]=i
            ri[u[i]] = i




    for _ in range(k):
        a,b=[int(x) for x  in input().split()]
        a+=delta
        b+=delta
        if b not in ri or a not in li or li[a]>ri[b]:
            print('NO')
        else:
            print('YES')