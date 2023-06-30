

t=int(input())
for _ in range(t):
    n=int(input())
    p=[int(x) for x  in input().split()]


    chs=False
    ans=0
    for i in range(1,n):
        if not chs and  p[i]<p[i-1]:
            ans+=1
            chs=True
        else:
            chs=False

    print(ans)

