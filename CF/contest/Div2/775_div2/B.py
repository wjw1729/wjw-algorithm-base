

t=int(input())
for _ in range(t):
    n=int(input())

    a=[int(x) for  x in input().split()]

    tt=sum(a)
    if tt==0:
        print(0)
    else:
        ans=1
        for c  in a:
            if c<=tt-c+1:
                ans=max(ans,1)
            else:
                ans=max(ans,c-(tt-c))

        print(ans)