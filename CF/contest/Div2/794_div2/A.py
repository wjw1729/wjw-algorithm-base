

t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x  in input().split()]

    tt=sum(a)
    check=False
    for i in a:
        if i*n==tt:
            check=True
            break

    if check:
        print('YES')
    else:
        print('NO')
