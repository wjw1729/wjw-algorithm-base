
t=int(input())

for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    for i in range(n):
        k,b=input().split()
        k=int(k)
        m=b.count('U')
        a[i]+=(k-2*m)
        a[i]%=10

    print(*a)
