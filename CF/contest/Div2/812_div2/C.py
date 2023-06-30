import math
t=int(input())
for _ in range(t):
    n=int(input())

    a=[0]*n
    vis=set()
    for i in range(n-1,-1,-1):
        for j in range(math.floor(math.sqrt(n-1+i)),math.ceil(math.sqrt(i))-1,-1):
            if j**2-i in vis:
                continue
            a[i]=j**2-i
            vis.add(j**2-i)
            break

    print(*a)
