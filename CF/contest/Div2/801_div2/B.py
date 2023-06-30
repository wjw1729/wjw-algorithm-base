

t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x  in input().split()]

    if n%2==1:
        print('Mike')
    else:
        minx=min(a)
        idx=a.index(minx)
        if idx%2==0:
            print('Joe')
        else:
            print('Mike')