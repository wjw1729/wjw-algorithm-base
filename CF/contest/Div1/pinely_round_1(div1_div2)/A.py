t=int(input())
for _ in range(t):
    n,a,b=[int(x) for x  in input().split()]
    if a==b==n:
        print('Yes')
    elif a+b>=n-1:
        print('No')
    else:
        print('Yes')
