
t=int(input())
for _ in range(t):
    n=int(input())
    if n%2==1:
        ans=list(range(1,n+1))
        for i in range(1,n,2):
            ans[i],ans[i+1]=ans[i+1],ans[i]
        print(*ans)
    else:
        ans = list(range(1, n + 1))
        for i in range(0, n, 2):
            ans[i], ans[i + 1] = ans[i + 1], ans[i]
        print(*ans)
