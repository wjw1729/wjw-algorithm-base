mod=998244353
"""
t=int(input())

for _ in range(t):
    n=int(input())
    for _ in range(n-1):
        u,v=[int(x) for x in input().split()]
"""
def compute(a,b):

    return a*(pow(b,mod-2,mod))%mod

print(compute(14,9))
