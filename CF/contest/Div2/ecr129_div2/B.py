

t=int(input())

for _ in range(t):
    n=int(input())
    a=[int(x) for  x in input().split()]
    m=int(input())
    b=[int(x) for x  in input().split()]

    bs=sum(b)

    print(a[bs%n])