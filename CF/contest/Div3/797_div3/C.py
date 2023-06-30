

t=int(input())
for _ in range(t):
    n=int(input())
    s=[int(x) for x  in input().split()]
    f=[int(x) for x  in input().split()]


    ans=[0]*n
    t=0
    for i in range(n):
       t=max(t,s[i])
       ans[i]=max(0,f[i]-t)
       t=max(t,f[i])

    print(*ans)