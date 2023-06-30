
t=int(input())
for _ in range(t):
    n=int(input())
    if n%2==0:
        ans=list(range(1,n-1))[::-1]+[n-1,n]
        print(*ans)

    else:
        ans=[1]+list(range(2,n-1))[::-1]+[n-1,n]
        print(*ans)