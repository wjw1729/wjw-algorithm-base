


t=int(input())

for _ in range(t):
    n=int(input())
    a=[int(x) for x  in input().split()]
    m=int(input())
    b = [int(x) for x in input().split()]

    tmpa=max(a)
    tmpb=max(b)

    if tmpa>tmpb:
        print('Alice')
        print('Alice')
    elif tmpa<tmpb:
        print('Bob')
        print('Bob')
    else:
        print('Alice')
        print('Bob')
