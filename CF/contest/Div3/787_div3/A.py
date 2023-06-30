

t=int(input())
for _ in range(t):
    a,b,c,x,y=[int(x0) for x0 in input().split()]

    x-=a
    y-=b

    res=0
    if x>0:
        res+=x
    if y>0:
        res+=y

    if res<=c:
        print('YES')
    else:
        print('NO')
