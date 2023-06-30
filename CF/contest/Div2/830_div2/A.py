import  math
t=int(input())

for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    check=False
    g=0
    for i in range(n):
        g=math.gcd(g,a[i])
        if g==1:
            check=True
            break
    if check:
        print(0)
    elif math.gcd(math.gcd(a[n-1],n),g)==1:
        print(1)
    elif math.gcd(math.gcd(n-1,a[n-2]),g)==1:
        print(2)
    else:
        print(3)
