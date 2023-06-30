from collections import Counter

def tandemrep(a):
    conuter=Counter(a)
    for k,v  in conuter.items():
        if v%2==1:
            return -1




t=int(input())

for _ in range(t):
    n=int(input())
    a=[int(x) for x  in input().split()]
