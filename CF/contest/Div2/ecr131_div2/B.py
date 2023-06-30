import math
t=int(input())
for _ in range(t):
    n=int(input())

    print(2)

    ans=[]
    vis=set()
    for i in range(1,n+1):
        if i in vis:
            continue
        j=i
        ans.append(i)
        vis.add(i)
        while j*2<=n:
            ans.append(2*j)
            vis.add(2*j)
            j=2*j

    print(*ans)