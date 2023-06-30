
t=int(input())
for _ in range(t):
    n,x=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]

    ans=0
    l=a[0]-x
    r=a[0]+x
    for c in a[1:]:
        ll=c-x
        rr=c+x

        if ll>r or rr<l:
            l=ll
            r=rr
            ans+=1
        else:
            l=max(ll,l)
            r=min(rr,r)

    print(ans)


