


t=int(input())
for _ in range(t):
    n,m=[int(x) for x  in input().split()]
    a=[int(x) for x  in input().split()]

    tt=sum(a)

    if m>=tt:
        print(0)
    else:
        print(tt-m)
