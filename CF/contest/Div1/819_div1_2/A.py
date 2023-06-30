


t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]


    ans=a[-1]-a[0]
    for i in range(n-1):
        ans=max(ans,a[i]-a[i+1])

    mina=[0]*n

    mina[0]=a[0]
    for i in range(1,n):
        mina[i]=min(mina[i-1],a[i])


    for i in range(n):
        ans=max(a[-1]-mina[i],ans)

    maxa=[0]*n
    maxa[n-1]=a[-1]
    for i in range(n-2,-1,-1):
        maxa[i]=max(maxa[i+1],a[i])

    for i in range(n):
        ans=max(ans,maxa[i]-a[0])


    print(ans)


