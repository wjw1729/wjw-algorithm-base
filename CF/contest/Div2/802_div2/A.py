

t=int(input())
for _ in range(t):
    n,m=[int(x) for x  in input().split()]
    ans=(1+m)*m//2
    for i in range(m,n*m+1,m):
        ans+=i

    print(ans-m)