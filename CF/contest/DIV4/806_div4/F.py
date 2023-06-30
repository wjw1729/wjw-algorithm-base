t=int(input())

for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]


    vis=[False]*n
    for i in range(n):
        if a[i]<i+1:
            vis[i]=True

    presum=[0]*(n+1)
    for i in range(1,n+1):
        presum[i]=presum[i-1]+int(vis[i-1])

    ans=0
    for i in range(n):
        if vis[i] and a[i]>=1:
            ans+=presum[a[i]-1]

    print(ans)

