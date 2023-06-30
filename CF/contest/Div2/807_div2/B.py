
t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x  in input().split()]


    ans=0
    pre=0
    check=False
    for i in range(n-1):
        if check and  a[i]==0 and (a[i+1]>0 or i==n-2):
            ans+=i-pre
        elif a[i]>0:
            ans+=a[i]
            pre=i
            check=True

    print(ans)
