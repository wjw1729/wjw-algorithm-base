


t=int(input())
for _ in range(t):
    a,b,c=[int(x) for x  in input().split()]

    z=c
    y=c+b
    x=c+b+a
    assert  x%y==a
    assert y%z==b
    assert z%x==c
    print(x,y,z)
