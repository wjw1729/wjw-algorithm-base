
t=int(input())

for _ in range(t):
    n=int(input())
    m=len(str(n))
    ans=0
    ans+=9*(m-1)
    ans+=int(str(n)[0])

    print(ans)