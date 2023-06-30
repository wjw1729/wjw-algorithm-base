
def solve(d):
    res=0
    for i in range(n):
        if d>w[i]:
            res+=w[i]+int(0.5*(d-w[i]))
        else:
            res+=d

    return res>=m



t=int(input())

for _ in range(t):
    n,m=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]

    w=[0]*n
    for i in a:
        w[i-1]+=1


    l=(m-1)//n+1
    r=2*l

    while l<=r:
        mid=(l+r+1)//2
        if solve(mid):
            ans=mid
            r=mid-1
        else:
            l=mid+1


    print(ans)





