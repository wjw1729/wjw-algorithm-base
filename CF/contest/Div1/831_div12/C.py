
t=int(input())

for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]

    a.sort()


    ans=0
    for i in range(n-1):
        ans=max(ans,a[-1]-a[i]+a[i+1]-a[i])
        ans=max(ans,a[i+1]-a[i]+a[i+1]-a[0])

    print(ans)