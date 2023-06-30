
t=int(input())
for _ in range(t):
    n=int(input())


    if n==3:
        print(-1)
    elif n%2==0:
        print(*list(range(1,n+1))[::-1])

    else:
        ans=list(range(1,n+1))
        print(*(ans[-2:][::-1]+ans[0:-2]))