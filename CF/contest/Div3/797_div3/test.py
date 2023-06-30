

t=int(input())

for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for x  in input().split()]

    gap=-1
    zerogap=-1
    check=True
    for x,y in zip(a,b):
        if x<y:
            check=False
            break
        if y==0:
            zerogap=max(zerogap,x-y)
        else:
            if gap>=0:
                if gap!=x-y:
                    check=False
                    break
            else:
                gap=x-y
        if gap >= 0 and gap < zerogap:
            check = False
            break

    if check:
        print('YES')
    else:
        print('NO')





