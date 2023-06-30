

t=int(input())

for _ in range(t):
    n=int(input())
    a=[int(x) for x  in input().split()]

    vis=set()
    ans=-1
    for i in range(n-1,-1,-1):
        if a[i] in vis:
            ans=i
            break
        vis.add(a[i])

    print(ans+1)
