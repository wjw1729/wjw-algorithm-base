
t=int(input())
for _ in range(t):
    n=int(input())

    if 3**(n-1)>10**9:
        print('NO')
    else:
        print('YES')
        ans=[3**i for i in range(n)]
        print(*ans)