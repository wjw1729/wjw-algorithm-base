import math
t=int(input())

for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]


    def lcm(a,b):
        return a*b//math.gcd(a,b)

    def solve():
        b=[0]*(n+1)
        b[n]=a[n-1]
        for i in range(n-1,-1,-1):

            b[i]=lcm(a[i],a[i-1] if i>0 else 1)
            if math.gcd(b[i],b[i+1])!=a[i]:
                print('NO')
                return

        print('YES')


    solve()


