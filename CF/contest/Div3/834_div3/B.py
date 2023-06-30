
t=int(input())
for _ in range(t):
    m,s=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]

    tt=sum(b)+s
    maxb=max(b)
    check=False
    for i in range(maxb,100):
        if (i*(i+1))//2==tt:
            check=True
            break

    if check:
        print('YES')
    else:
        print('NO')
