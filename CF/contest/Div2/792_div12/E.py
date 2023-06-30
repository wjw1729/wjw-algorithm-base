
def mincost(a):
    a.sort()
    



t=int(input())
for _ in range(t):
    n,q=[int(x) for x  in input().split()]
    a=[int(x) for  x in input().split()]


    res=mincost(a)
    print(res)