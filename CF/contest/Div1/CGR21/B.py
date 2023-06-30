

t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x  in input().split()]

    ans=2

    cnt=0
    pre=None
    for c in a+[0]:
        if c==0 and pre and pre!=0:
            cnt+=1
        pre=c

    ans=min(ans,cnt)

    print(ans)