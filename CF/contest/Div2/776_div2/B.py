


t=int(input())
for _ in range(t):
    l,r,a=[int(x) for x   in input().split()]

    d=r//a
    res=r%a
    if res==a-1:
        print(res+d)
    else:
        if (d-1)*a+a-1>=l:
            print(d-1+a-1)
        else:
            print(d+res)
