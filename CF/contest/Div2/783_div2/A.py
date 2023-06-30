

def directionc(n,m):

    d=n-1
    r=m-1
    l=min(d,r)
    h=max(d,r)

    if h>l+1:
        if l==0:
            return -1
        ans=2*l+1+((h-l-1)*2 if (h-l-1)%2==0 else (h-l-1)*2+1)
    else:
        ans=h+l

    return ans

t=int(input())
for _ in range(t):
    n,m=[int(x) for x in input().split()]
    print(directionc(n,m))

