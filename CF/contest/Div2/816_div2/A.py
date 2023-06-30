

t=int(input())
for _ in range(t):
    n,m=[int(x) for x in input().split()]
    if n==1 and m==1:
        print(0)
    else:
        print(min(n+2*m-2,2*n+m-2))

