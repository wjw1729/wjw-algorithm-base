

t=int(input())
for _ in range(t):
    n=int(input())
    lx,rx=0,0
    ly,ry=0,0
    for i in range(n):
        x0,y0=[int(x) for x  in input().split()]

        lx=min(lx,x0)
        rx=max(rx,x0)
        ly=min(ly,y0)
        ry=max(ry,y0)


    print(2*(rx-lx+ry-ly))

