t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]

    b=[i+1-a[i] for i in range(n)]


    preb=[0]*n

    for i in range(1,n):
        preb[i]=max(preb[i-1],b[i])


    ans=(n+1)*n//2-sum(preb)
    print(ans)