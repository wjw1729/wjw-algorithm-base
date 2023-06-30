import math

t=int(input())
for _ in range(t):
    n,m,k=[int(x) for  x in input().split()]
    a=[int(x) for  x in input().split()]

    maxa=max(a)

    if k!=1 and math.ceil(maxa/(k-1))>n-maxa+1:
        print('NO')
    else:
        print('YES')
