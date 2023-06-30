
t=int(input())
for _ in range(t):
    n=int(input())
    if n%2==1 or n==2:
        print(-1)
    else:

        n4=n//4
        if n%4==2:
            maxx=n4
            minx=1+(n4-1)//3*2+(n4-1)%3


        else:
            minx=n4//3*2+n4%3
            maxx=n4




        print(minx,maxx)