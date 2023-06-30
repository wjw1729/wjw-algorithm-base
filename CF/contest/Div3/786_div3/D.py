


t=int(input())

for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]

    for i in range(n-1,0,-2):
        if i-1<0:
            break
        if a[i]>=a[i-1]:
            continue
        else:
            a[i],a[i-1]=a[i-1],a[i]


    if a==sorted(a):
        print('YES')
    else:
        print('NO')


